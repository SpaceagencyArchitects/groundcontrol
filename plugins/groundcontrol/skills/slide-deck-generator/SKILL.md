---
name: slide-deck-generator
description: Generate a polished HTML slide deck from a topic, outline, or data. Outputs a self-contained .html file with keyboard/touch navigation, responsive typography, and the spaceagency design system — Helvetica, editorial layout, clean white backgrounds.
---

# Presentation Generator

## Conventions (spA)

Full detail in the plugin's `../../rules/` folder. If that folder is not present (the skill is running standalone, without the plugin), treat the conventions here as authoritative.

- **Metric & Australian English** by default; **WA** context unless stated otherwise.
- **AI-assisted output** supporting the architect's judgment — flag assumptions and anything unverified (`../../rules/professional-disclaimer.md`).

You generate self-contained HTML slide presentations using the spaceagency design system — editorial layout with Helvetica, left-aligned typography, generous whitespace, and a clean monochrome palette. The user provides a topic, outline, data, or document — you produce a complete `.html` file they can open in any browser.

## On Start

When invoked, list the available page types for the user before proceeding:

| # | Type | Layout | Background |
|---|------|--------|------------|
| 1 | Title (Image + Title) | Full bleed image, text overlay bottom-left | Image |
| 2 | Title (Text Only) | Left-aligned h1 + subtitle + credit | White |
| 3 | Heading + Body | Eyebrow + h2 + paragraph | White |
| 4 | Heading + List | Eyebrow + h2 + bullet list | White / Grey |
| 5 | Heading + Stats | Eyebrow + h2 + vertical stat lines | White |
| 6 | Stat Row | Large centered numbers in columns | White / Grey |
| 7 | Stat Comparison | Before/after with arrows | White / Grey |
| 8 | Heading + Stat Row | Eyebrow + h2 + stat columns (centered) | White / Grey |
| 9 | Statement (white) | Bold centered text | White |
| 10 | Statement (dark) | Bold centered text | Dark |
| 11 | Data Table | Eyebrow + h2 + table | Grey |
| 12 | Insight List | Eyebrow + h2 + numbered items | White |
| 13 | Bar Chart | Eyebrow + h2 + horizontal bars | White |
| 14 | Timeline | Eyebrow + h2 + phased dots (centered) | White |
| 15 | Two Column | Eyebrow + h2 + side-by-side text | White / Grey |
| 16 | Comparison | Eyebrow + h2 + before/after boxes (centered) | White |
| 17 | Image — Full Bleed | Single image, edge to edge | Image |
| 18 | Image — Full Bleed + Title | Full image with gradient + overlaid text | Image |
| 19 | Image — Split 2 | Two images side by side | White border |
| 20 | Image — Split 3 | Three images in a row | White border |
| 21 | Image — Split 4 | 2×2 grid | White border |
| 22 | Image — Split 6 | 3×2 grid | White border |

Any slide can include a **Callout** (footnote annotation) appended below the main content.

A sample deck demonstrating every type is at `references/sample-deck.html`.

## Workflow

1. **Understand the input.** The user may provide:
   - A topic or title (you research/generate content)
   - An outline or bullet points (you expand into slides)
   - A document or report (you distill into a deck)
   - Data or analysis results (you visualize as stats/tables/charts)
   - Local image files or a folder (use as image slides — see Image Handling below)

2. **Plan the deck.** Before writing HTML, decide:
   - How many slides (aim for 10-20, never fewer than 6)
   - Which slide type and components each slide uses
   - The narrative arc: setup -> insight -> evidence -> recommendation -> close

3. **Embed local images.** If the user provides local image paths, encode them as base64 before writing the HTML (see Image Handling below). This keeps the deck self-contained and portable.

4. **Write the HTML file.** Use the template in `templates/deck-template.html` as the foundation. Customize only the slide content inside `<body>`.

5. **Save the file.** Write to the path the user specifies, or default to `./presentation.html`. Tell the user the path so they can open it.

## Image Handling

The deck must be self-contained — local images must be embedded as base64 data URIs, not referenced by file path. A file path `src` breaks as soon as the HTML is moved or shared.

### Encoding local images

For every local image path the user provides, run this Python snippet via Bash to get the base64 data URI:

```python
import base64, sys, mimetypes
path = sys.argv[1]
mime = mimetypes.guess_type(path)[0] or "image/jpeg"
with open(path, "rb") as f:
    data = base64.b64encode(f.read()).decode()
print(f"data:{mime};base64,{data}")
```

Then use the output as the `src` value:

```html
<img src="data:image/jpeg;base64,/9j/4AAQ..." alt="Description" />
```

### Using pre-sized images

If the user has pre-sized images (e.g. a `resized-slides/` folder) already sized for the slide canvas:

- `*-slides-wide.jpg` — 1920×1080 (16:9) — use for full-bleed and image-grid slides
- `*-slides-standard.jpg` — 1024×768 (4:3) — use only if the user asked for a 4:3 deck

Prefer `slides-wide` images. Embed them as base64 (see above) so the deck stays portable.

### When no local images are provided

Use `src=""` with a descriptive `alt` attribute as a placeholder. Note the placeholder in the output so the user knows which slides need images:

```html
<img src="" alt="[Insert: project exterior view]" />
```

### File size note

Base64-encoding large images increases HTML file size. If the user provides many high-res images, warn them: "Embedding N images will produce a large HTML file (~X MB). Consider resizing them (max ~2000px on the long edge) first to reduce file size before embedding."

## Design System

### Layout Philosophy
- **Left-aligned by default.** Content is flush-left with generous left padding. Only statement slides center text.
- **Massive whitespace.** Content should breathe. Never fill the slide — leave at least 40% empty.
- **Eyebrow top-left.** Small bold monospace text in the top-left corner identifies the section.
- **Brand mark bottom-right.** A small "spA" wordmark sits fixed in the bottom-right corner.
- **No decorative boxes or cards.** Stats, lists, and content stand on their own — no background panels or rounded containers.

### Slide Types (background classes on `.slide` div)
| Class | Background | Text | Use for |
|-------|-----------|------|---------|
| *(none)* | White (#ffffff) | Dark | Title, content, lists, tables — the default |
| `grey` | Light grey (#f5f5f3) | Dark | Tables, stat comparisons, alternating rhythm |
| `dark` | Dark (#1a1a1a) | White | Statement slides — bold centered declarations |

### Components

The full component pattern library — every slide component with ready-to-paste HTML — lives in [`references/component-patterns.md`](references/component-patterns.md). Read it when composing slides.

### Composition Rules
- Every content slide (not statements) should have a `eyebrow` top-left
- **Title slide**: full-bleed image with `.image-title-slide` — h1 + subtitle over gradient overlay. Falls back to white text-only title if no image is available.
- **Content slides**: white (default), left-aligned — `eyebrow` + `.content` with heading + body/list/stats
- **Statement slides**: centered text, no eyebrow — white bg for regular statements, `dark` for dramatic ones
- **Stat slides**: white or grey, centered stat-row or stat-comparison layout
- **Table slides**: white or grey, left-aligned heading + data-table
- **Dark slides**: use sparingly — at most 1-2 per deck for maximum emphasis
- **Closing slide**: white, left-aligned or centered — bold statement or summary
- Use `<span class="emphasis">` for bold inline text
- Never put more than one major component per slide (one table OR one stat-row OR one list)
- Alternate slide backgrounds for visual rhythm — never use the same type 3x in a row
- **Centered content**: Use `.slide.centered` (class on the slide div) for slides with a heading + grid, timeline, stat-row, or comparison below. These read better centered. Left-align is for heading + body text, lists, tables, and insight lists.
- Leave generous whitespace — content should occupy at most 60% of the slide

### Writing Style
- Headlines: short, declarative, opinionated. State the insight, not the topic.
  - Good: "We have 18 huddle rooms. At peak, 29 groups need one."
  - Bad: "Huddle Room Analysis"
- Subtitles and descriptions: lightweight, factual, no jargon
- Stats: pick the most dramatic number, give it context with the label
- Tables: 4-6 rows max. Use colored indicators for changes (red for negative, green for positive).
- Lists: lead with the bold action/finding, follow with the detail after an em dash

## HTML Template

The complete deck template — the self-contained HTML shell (head, CSS design system, navigation JS) you fill with slides — lives in [`templates/deck-template.html`](templates/deck-template.html). Start from that file, keep its head / CSS / scripts intact, and replace the slide content. A rendered example is in [`references/sample-deck.html`](references/sample-deck.html).


## Accent Color

The default accent is `--accent: #E8B517` (warm yellow — used only on the progress bar). The design is primarily monochrome — black, white, and greys. Change indicators use `--negative: #D92B2B` (red) and `--positive: #2563EB` (blue) for data.

If the presentation is for a different brand or context, change `--accent`. Common alternatives:
- Blue: `#2563EB`
- Teal: `#0D7377`
- Purple: `#6B21A8`
- Orange: `#C2410C`

Ask the user if they want a specific accent color. If the topic suggests a brand, try to match.

## Slide Structure Rules

1. **First slide**: Always `active` — use `.image-title-slide` with a relevant cover image, h1 + subtitle over gradient. If no image is available, fall back to white text-only title (h1 + `.subtitle` + credit).
2. **Second slide**: Context or framing question — what we need to answer, what this is about.
3. **Middle slides**: Alternate between white and grey backgrounds. Use statement slides (white or dark) to break rhythm and emphasize key points. Build the argument.
4. **Stat slides**: Use `<div class="slide centered">` to center the stat-row on the page. No eyebrow needed.
5. **Statement slides**: Center the `.statement` div. No eyebrow. Use dark bg sparingly (1-2 per deck).
6. **Penultimate slide**: The ask / recommendations / next steps
7. **Last slide**: White — closing statement or summary, left-aligned or centered.

## Output

Write the complete HTML file using the Write tool. The first slide must have class `active`. Every slide must be a direct child `<div class="slide ...">` inside body, before the `<nav>`. Add `<div class="brand-mark">spA</div>` to every slide.
