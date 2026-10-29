/**
 * qr.js: QR codes for the public parts of the independent review section (reviews/vaults.html, card 093). Every
 * element with data-qr gets a QR code of its text, drawn here with the vendored qrcode-generator (through
 * assets/vault-pane/inbox.js), so a reviewer can scan a vault's read key or a key link from the screen. Only public
 * text is ever put in data-qr: the secrets are never on the site.
 *
 * @module review-qr
 */
import { qrSvg } from '../vault-pane/inbox.js'

for (const el of document.querySelectorAll('[data-qr]')) {
    qrSvg(el.getAttribute('data-qr'), { cell: 3, label: el.getAttribute('data-qr-label') || 'QR code' })
        .then(({ svg }) => { el.innerHTML = svg })
        .catch(() => { el.textContent = 'The QR code could not be drawn here; the text beside it is the same.' })
}
