#!/usr/bin/env bash
# video-cut.sh <input video> <output folder>: make a video stream from a vault.
#
# A vault encrypts each file as one block, so a browser can only decrypt a file once all of it has arrived: a
# 24 MB film cannot start playing until 24 MB have downloaded, and the vault's read API refuses objects that
# large. Cut into 2-second pieces, each its own small encrypted object, the same film starts after the first
# half megabyte (measured 14 November 2026: about 4 s to the first frame at 20 Mbit/s, against about 11.5 s for
# the whole file through a temporary S3 link). See admin/notes/2026-11-14__vault-video/.
#
# Writes into <output folder>: init.mp4, seg-NNN.m4s (2-second fragmented-MP4 pieces, a keyframe at each),
# poster.jpg (a frame at 1.2 s, or at a tenth of the length if shorter) and manifest.json, which the page's
# player (assets/vault-video/vault-video.js) reads. Re-encodes with x264 at CRF 20 (High profile); keeps the
# audio as AAC if there is any. Then put the folder in the newsroom media vault (sgit commit, sgit push) and
# add a line to the article:  !video newsroom-media <folder path in the vault> | <caption>
set -euo pipefail
IN=$1; OUT=$2
command -v ffmpeg > /dev/null || { echo "ffmpeg is needed"; exit 1; }
mkdir -p "$OUT"
find "$OUT" -maxdepth 1 \( -name 'seg-*.m4s' -o -name 'init.mp4' -o -name 'index.m3u8' -o -name 'manifest.json' \) -delete
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
AUDIO=$(ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$IN" | head -1)
A=(-an); [ -n "$AUDIO" ] && A=(-c:a aac -b:a 128k)
( cd "$OUT" && ffmpeg -v error -i "$IN" -c:v libx264 -preset slow -crf 20 -profile:v high -pix_fmt yuv420p \
    -force_key_frames "expr:gte(t,n_forced*2)" "${A[@]}" -f hls -hls_time 2 -hls_playlist_type vod \
    -hls_segment_type fmp4 -hls_fmp4_init_filename init.mp4 -hls_segment_filename 'seg-%03d.m4s' index.m3u8 )
AT=$(python3 -c "d=float('$DUR'); print(1.2 if d > 3 else round(d/10, 2))")
ffmpeg -v error -y -ss "$AT" -i "$IN" -frames:v 1 -vf "scale='min(1280,iw)':-2" "$OUT/poster.jpg"
python3 - "$OUT" "$IN" <<'PY'
import json, os, re, subprocess, sys
out, src = sys.argv[1], sys.argv[2]
probe = lambda f, q: subprocess.run(['ffprobe', '-v', 'error', *q, '-of', 'json', f], capture_output=True, text=True).stdout
joined = os.path.join(out, '.probe.mp4')
segs = sorted(f for f in os.listdir(out) if re.fullmatch(r'seg-\d{3}\.m4s', f))
with open(joined, 'wb') as j:
    for f in ['init.mp4', segs[0]]: j.write(open(os.path.join(out, f), 'rb').read())
streams = json.loads(probe(joined, ['-show_entries', 'stream=codec_type,profile,level,width,height']))['streams']
os.remove(joined)
v = next(s for s in streams if s['codec_type'] == 'video')
prof = {'High': '6400', 'Main': '4d00', 'Baseline': '42e0', 'Constrained Baseline': '42e0'}.get(v.get('profile'), '6400')
codecs = ['avc1.%s%02x' % (prof, int(v.get('level') or 40))]
if any(s['codec_type'] == 'audio' for s in streams): codecs.append('mp4a.40.2')
durs = [float(x) for x in re.findall(r'#EXTINF:([\d.]+)', open(os.path.join(out, 'index.m3u8')).read())]
os.remove(os.path.join(out, 'index.m3u8'))
size = lambda f: os.path.getsize(os.path.join(out, f))
man = {"mime": 'video/mp4; codecs="%s"' % ','.join(codecs), "init": "init.mp4", "duration": round(sum(durs), 3),
       "width": v.get('width'), "height": v.get('height'),
       "segments": [{"file": f, "bytes": size(f), "seconds": d} for f, d in zip(segs, durs)],
       "total_bytes": size('init.mp4') + sum(size(f) for f in segs),
       "source": os.path.basename(src), "made_by": "admin/writer/tools/video-cut.sh"}
big = [s['file'] for s in man['segments'] if s['bytes'] > 4 * 1024 * 1024]
json.dump(man, open(os.path.join(out, 'manifest.json'), 'w'), indent=1)
print(f"{len(segs)} pieces, {man['duration']} s, {man['total_bytes'] / 1048576:.1f} MB, {man['mime']}")
if big: print('WARNING: over 4 MB, the vault may refuse them:', ', '.join(big))
PY
