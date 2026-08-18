# Code & Standard Currency

Codes, standards, and rating tools are revised on their own cycles — the NCC on a roughly three-year cycle (adopted by WA with state variations and its own commencement dates), Australian Standards whenever revised, and rating tools (Green Star, NABERS) by version. **A cited edition is only correct if it is the edition in force for the project at the relevant date.** This rule applies to every output that relies on a code, standard, regulation, or rating-tool version. **Default jurisdiction: Western Australia.**

## Verify before you rely

Before relying on any code / standard / rating-tool edition in an output:

1. **Confirm the current in-force edition against the official source** (table below). Do not assume the edition named in this repo, in a bundled reference file, or in your own training is current — all three go stale.
2. **Check the WA position for the NCC.** The NCC is adopted by each state with variations and sometimes a delayed or staged commencement. Confirm both the current national edition *and* whether WA has adopted it, and from what date, via NCC Vol. 1 & 2 **Appendix WA**.
3. **State the check in the output.** Name the edition used and the date it was confirmed — e.g. "NCC edition confirmed current as at [date] via ncc.abcb.gov.au". If you could not verify (no web access), say so and treat the edition as **unconfirmed**.
4. **Cite the edition in force at the relevant date, not simply the newest.** For a DA that is usually the edition in force at lodgement; for construction, the edition under the building permit. State which date governs.

## Official sources — verify here first

| Instrument | Authoritative source |
|---|---|
| NCC (national edition + state adoption) | [ncc.abcb.gov.au](https://ncc.abcb.gov.au/) — current edition and each state's adoption / commencement |
| WA NCC variations | NCC Vol. 1 & 2 **Appendix WA**; Building and Energy, [wa.gov.au](https://www.wa.gov.au/) |
| R-Codes (SPP 7.3) | [WAPC — R-Codes](https://www.wa.gov.au/government/publications/state-planning-policy-73-residential-design-codes) |
| Australian Standards | [store.standards.org.au](https://store.standards.org.au/) — confirm current designation and year |
| Green Star | [GBCA](https://new.gbca.org.au/) — confirm the current rating-tool version |
| NABERS | [nabers.gov.au](https://www.nabers.gov.au/) — confirm the current tool / version |
| WA legislation (as in force) | [legislation.wa.gov.au](https://www.legislation.wa.gov.au/) — current consolidated version |
| Local Planning Schemes | the relevant LGA — the currently-gazetted consolidated Scheme text |

## Do not assert an edition as "current" in a fixed document

Reference material in this repo (rules, SKILLs, bundled files) must **not** state that a specific edition "is current" as a bare fact — that assertion rots. Write "cite the edition in force (verify — see code-currency)" and use specific edition years only as **illustrative citation examples**, marked as indicative. Bundled reference data (R-Codes, LPS extracts, NCC load-factor snapshots) is a dated snapshot: state which edition it represents and verify it against the gazetted source before relying on it.

## When verification isn't possible

If web access is unavailable, do not silently fall back to a hardcoded edition. State the edition assumed, flag it as **unverified**, and tell the user to confirm the current edition against the official source before the output is relied on.
