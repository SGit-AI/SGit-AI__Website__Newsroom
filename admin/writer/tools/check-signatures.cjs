#!/usr/bin/env node
// check-signatures.cjs: every writer commit since git_signing began is a git SSH signature by its registration's key,
// read from its parent's register, with the registration's Claude-Session (admin/build/writer_register.js,
// checkSignatures; admin/notes/2026-11-19__signed-commits/notes.md). Run by the deploy workflow's signatures job,
// whose failure refuses the release; validate.js runs the same check locally with full history. Exit 1 on any failure.
'use strict';
const path = require('path');
const { checkSignatures } = require('../../build/writer_register');
const { fails, warns } = checkSignatures(path.resolve(__dirname, '..', '..', '..'));
for (const w of warns) console.log('WARN ' + w);
for (const f of fails) console.log('FAIL ' + f);
console.log(fails.length ? `signatures: ${fails.length} failed` : `signatures: OK${warns.length ? ` (${warns.length} warnings)` : ''}`);
process.exit(fails.length ? 1 : 0);
