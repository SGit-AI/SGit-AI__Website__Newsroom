# Odoo and our stack (16 November 2026)

Dinis asked for a strategy to integrate our workflows and stack with odoo.com, then for it as an article. Facts from
Odoo's 19 and 20 release notes (read via WebFetch; the pages were long and partly read) and integrators' summaries
(Carly, a vendor; Teqstars; Cybrosys; Apideck); claims from them are hedged in the text. Customer numbers are
third-party estimates. The ABP figure is an illustration, not a measured policy. Nothing built or sold.

## Update, later on 16 November
Dinis asked to add Odoo 19, 18 and older, and to try an ephemeral deployment. Done in this session with Docker (dockerd
started by hand) and the official odoo:12.0, 15.0, 18.0, 19.0 images and postgres:16 (postgres:12 for Odoo 12): scripts in
the writer's scratchpad (odoo/poc: run.sh, agent.py, down.sh). Timings: 19 44.9 s, 18 47.1 s, 15 36.4 s, 12 49.7 s from
start to agent done; teardown under 0.5 s. Odoo 12 and 15 needed l10n_generic_coa for a purchase journal. JSON-2 with an
API key tested on 19. Images removed afterwards for disk. Companion article: integrate-with-whatever-is-on-the-other-side
(the organisation from today's MVP is not named, at Dinis's word that they want to review the content first).

## The MVP on Odoo 20 (report from odoo@AgentiCCells.dinis, session_018yvwtR5QXpatuyNUw5q8jz)
Built end to end on odoo:20.0 in 98 s; simulated approval; abp_grant module; findings and corrections applied to odoo-and-our-stack (Enterprise-only agents and MCP, automatic triggers without approval, RPC removal Odoo 22 and Online 21.1, credits EUR 1, ir.access). Article: our-workflow-on-odoo-20. Screenshots stayed in that session; figures drawn from its data.
