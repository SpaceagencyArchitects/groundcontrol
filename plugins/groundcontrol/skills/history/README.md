# /history

Neighbourhood context and history analysis for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Provide a Western Australian address and get development history, architectural character, heritage status, Traditional Owner context, landmarks, commercial activity, and planned development — sourced from inHerit, LGA Local Heritage Surveys, the State Library of WA, Trove, and other archives.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../../LICENSE)

## Install

```bash
# Via plugin system
claude plugin marketplace add SpaceagencyArchitects/groundcontrol
claude plugin install groundcontrol@groundcontrol

# Or symlink just this skill
git clone https://github.com/SpaceagencyArchitects/groundcontrol.git
ln -s $(pwd)/groundcontrol/plugins/groundcontrol/skills/history ~/.claude/skills/history
```

## Usage

```
/history 48 Swanbourne St, Fremantle WA 6160
```

Or start with no context:

```
/history
```

The skill researches:

- **Aboriginal context** — the relevant Noongar group / Traditional Owners; AHIS findings on or near the site, with the caveat that cultural significance may exist whether or not formally recorded
- **Development history** — how the area was built out, key subdivision and construction periods, major changes
- **Heritage context** — State Register (inHerit) listings, Local Heritage Survey listings, Heritage Area designations under the LPS
- **Adjacent land uses** — what's in every direction
- **Architectural character** — Australian styles and eras (Federation, Inter-War, Post-War, Contemporary), materials, streetscape
- **Landmarks & institutions** — notable buildings, parks, institutions within ~1 km
- **Commercial activity** — named retail / hospitality precincts and market character
- **Planned development** — major DAs and structure / activity centre plans nearby

Output is saved as a markdown file in the working directory (`./history-[location-slug].md`).

## Data Sources

Only governmental, university, museum, and non-profit sources are used. Commercial real estate sites and neighbourhood blogs are never used; Trove and the SLWA are the primary references for WA local history.

| Source | Data |
|--------|------|
| inHerit | State Register + Local Heritage Surveys |
| LGA Local Heritage Survey | Supplements inHerit |
| Heritage Council of WA | State Register administration, statements of significance |
| State Library of WA (SLWA) | Historical photographs, plans, manuscripts (Battye Library) |
| State Records Office of WA | Historical land and government records |
| Trove (NLA) | Historical newspapers, photos, books |
| Western Australian Museum | Cultural and natural history |
| LGA online maps + DA register | Heritage overlays, zoning, current development applications |
| AHIS | Registered Aboriginal Sites and Other Heritage Places |
| SWALSC | Native Title context for SW WA |

For overseas projects the skill falls back to international sources (UNESCO World Heritage, the relevant national heritage agency).

## What's Included

| File | Purpose |
|------|---------|
| `SKILL.md` | Research workflow, output template, preferred sources, guidelines |

## License

MIT
