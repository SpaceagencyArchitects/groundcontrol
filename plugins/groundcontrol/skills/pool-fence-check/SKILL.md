---
name: pool-fence-check
description: Check swimming pool and spa barrier design against Western Australian requirements. Use whenever an architect needs to assess pool fencing — barrier height, gap and opening dimensions, gate and latch specification, material choice, Non-Climbable Zones (NCZ), or barrier placement near columns/structures — during design review, documentation audit, or due diligence on a project with a pool or spa. Also use for direct technical questions about WA pool barrier rules (e.g. "how far does a fence need to be from a wall", "does this gap comply", "what height barrier do we need here").
allowed-tools:
  - Read
  - Write
  - Edit
  - WebFetch
  - AskUserQuestion
  - Bash
  - Glob
  - Grep
user-invocable: true
---

# /pool-fence-check — Pool & Spa Barrier Compliance Check (Western Australia)

## Conventions (spA)

Apply before producing output; full detail in the plugin's `../../rules/` folder. If that folder is not present (the skill is running standalone, without the plugin), treat the conventions here as authoritative.

- **Metric & WA default** — metric (SI), Australian English, Western Australia jurisdiction unless the user states otherwise.
- **Verify code currency** — never rely on a standard or requirements-guide edition without confirming it against the official source; state what was checked and when, or flag it as unverified (`../../rules/code-currency.md`).
- **Professional disclaimer** — AI-assisted output supporting a registered architect's judgment, not a substitute for it. Don't assert compliance outright ("appears consistent with… subject to verification"); flag where site inspection or certification is required (`../../rules/professional-disclaimer.md`).

Assess swimming pool and spa safety barrier designs against WA Building and Energy requirements and AS 1926.1 / AS 1926.2. Covers barrier height, gaps, gates, materials, Non-Climbable Zones (NCZ), and placement — for design review, documentation audit, and due diligence on any project with a pool or spa.

## Honest scope — verify live, every time

WA Building and Energy's pool barrier guide is Crown copyright and revisable — it cannot be bundled as a static copy without going stale, and a paraphrase can drift from the exact wording (an earlier draft of this skill described NCZ 3 as a straight vertical clearance; it is actually a curved quadrant sweeping outward *and* upward — a materially different shape once you check obstructions near a barrier). Treat `references/pool-barrier-requirements.md` as **orientation only** — it tells you what to check for and how to phrase a sharp WebFetch prompt. It is not the answer to give an architect on its own.

**Before answering anything dimensional, a zone definition, a gate/latch spec, a material rule, or anything that will end up on a drawing or in a client-facing answer:**

1. WebFetch the live source with a **targeted** prompt asking for the specific clause (e.g. "quote the exact definition of NCZ 3, including whether it extends outward as well as upward") — not a request to reproduce the whole document; the source declines full verbatim reproduction on copyright grounds, and a narrow prompt is faster and more reliable anyway.
   - Technical detail: `https://www.wa.gov.au/media/60087/download?inline` (Pool and Spa Safety Barrier Requirements Guide)
   - Regulatory/process overview: `https://www.wa.gov.au/organisation/building-and-energy/swimming-pool-and-spa-safety-barrier-requirements`
2. State the retrieval date (today, not a cached one) alongside anything sourced this way.
3. If WebFetch is unavailable or the page fails to load, say so explicitly, fall back to `references/pool-barrier-requirements.md`, and flag the answer as **unverified against the live source — confirm before relying on it**.
4. For standard-edition currency (has AS 1926.1-2012 / AS 1926.2-2007 been superseded?), use WebSearch rather than assuming the years cited anywhere in this skill are still current — see `../../rules/code-currency.md`.

## When to use

- Design review — an architect has a barrier design or client question and needs it checked
- Documentation audit — reviewing drawings/specs for barrier compliance detail
- Due diligence / site brief — assessing an existing pool's barrier status
- Direct technical questions — "how far does the fence need to be from the column", "does an 80 mm gap comply", "what's the latch height rule"

## Workflow

1. **Gather what's known.** Barrier type (solid, mesh, glass, combination), height and location (poolside vs non-poolside), material, gate design and latch height, any site-specific constraints (columns, walls, roof edges, level changes, adjoining use), new build vs retrofit. Don't block on missing info — answer what's asked and note what else would sharpen the assessment.
2. **Load `references/pool-barrier-requirements.md`** for orientation — it maps out height, gaps, gates, materials, and the five NCZ zones so you know exactly what clause to verify.
3. **Verify against the live source** per "Honest scope" above for any figure or clause the answer depends on.
4. **Answer in spA voice** — terse, direct, cite the clause and retrieval date. Use "appears consistent with [clause]" / "no inconsistencies identified", never "compliant" or "approved" outright, per `../../rules/professional-disclaimer.md`.
5. **Close with the disclaimer** required by `../../rules/professional-disclaimer.md` whenever the answer could inform a drawing, spec, or client-facing compliance statement.

## Reference

- `references/pool-barrier-requirements.md` — quick-reference technical detail (height, gaps, gates, materials, NCZ 1–5, placement, checklist). Orientation only; verify live before advising.
