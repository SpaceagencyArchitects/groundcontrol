# /zoning-envelope

Interactive 3D zoning envelope viewer as a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill. Generates a self-contained HTML file with Three.js that renders the buildable envelope for any lot — exact lot polygon from GIS data, setback zones, extruded volumes, height caps, and interactive orbit controls.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../../LICENSE)

## Install

```bash
# Via plugin system
claude plugin marketplace add SpaceagencyArchitects/groundcontrol
claude plugin install groundcontrol@groundcontrol

# Or symlink just this skill
git clone https://github.com/SpaceagencyArchitects/groundcontrol.git
ln -s $(pwd)/groundcontrol/plugins/groundcontrol/skills/zoning-envelope ~/.claude/skills/zoning-envelope
```

## Usage

First, run a planning analysis to generate a report:

```
/planning-analysis-wa 48 Swanbourne St, Fremantle WA 6160
```

Then generate the 3D viewer:

```
/zoning-envelope path/to/planning-analysis-48-swanbourne-st.md
```

Or search by keyword:

```
/zoning-envelope 48 swanbourne
```

Or auto-detect the most recent report:

```
/zoning-envelope
```

## What it renders

- **Exact lot polygon** from GIS data (Landgate for WA) — not a simplified rectangle
- **Setback zones** as coloured ground overlays with dashed inset boundaries
- **Buildable volumes** — base, tower, upper volume — extruded from the lot polygon at correct heights
- **Height cap** — amber plane at maximum building height
- **Edge-length labels** on lot boundary edges
- **Height labels** with dashed reference lines
- **Parameters panel** — plot ratio, max GFA, height limits, setbacks
- **Interactive controls** — orbit, zoom, pan (Three.js OrbitControls)

## How it works

The skill reads the `## Envelope Data` JSON block from a planning analysis report. This block contains:

```json
{
  "lot_poly": [[0.0, 40.2], [15.3, 40.2], [15.3, 0.0], [0.0, 0.0]],
  "unit": "m",
  "setbacks": { "front": 4, "rear": 3, "lateral1": 1.5, "lateral2": 1.5 },
  "volumes": [
    { "type": "base", "inset": 1.5, "h_bottom": 0, "h_top": 7, "label": "base" },
    { "type": "upper", "inset": 3, "h_bottom": 7, "h_top": 11, "label": "upper" }
  ],
  "height_cap": 11,
  "info": { "title": "48 Swanbourne St", "zone": "R-AC3", ... },
  "stats": { "Plot Ratio": "0.7", ... }
}
```

The skill then:

1. Parses the polygon and envelope parameters
2. Computes inset polygons for setback zones and building volumes
3. Triangulates the polygons (ear-clipping) for 3D extrusion
4. Generates a self-contained HTML file with embedded Three.js
5. Opens it in the browser

## Key features

- **Self-correcting polygon inset** — automatically detects and corrects for different polygon winding directions across data sources
- **Multi-volume envelopes** — base + upper volume for R-Code setback envelopes
- **Multi-scenario support** — toggle buttons for comparing development scenarios (individual, party-wall, unified)
- **Works with any polygon source** — Landgate or manual coordinates

## Dependency

This skill requires a planning analysis report as input. It does not perform planning calculations — run `/planning-analysis-wa` first.

## License

MIT
