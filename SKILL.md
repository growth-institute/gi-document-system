---
name: gi-document-system
description: >
  Create Growth Institute (GI) branded documents — reports, one-pagers, proposals, case
  studies, memos, briefs — using GI's official DOCUMENT design system: GI master brand only
  (no course/MBC colors, no 4-Decisiones semantics), always light backgrounds with color in
  the elements, Plus Jakarta Sans typography, and BLUE accents. Use this skill whenever the
  user asks for a GI document, a branded report / proposal / one-pager / case study / memo,
  or anything that should follow GI's document look and feel — even if they don't say
  "design system" or "brand" explicitly. Do NOT use it for slide decks (that's a separate
  slide system).
---

# GI · Document Design System

This skill produces on-brand Growth Institute documents. Backgrounds are always light; the
color lives in headings, accents, and data. It uses only the GI master brand.

## Workflow

1. **Read the spec first.** Open `references/design-system-docs-gi.md` for the full token
   values, type scale, components, and rules. Follow it exactly.
2. **Set up the working folder.** Copy `assets/tokens.css` and `assets/base.css` next to the
   HTML you will create (or link them by relative path). Copy `assets/GI_Icon_Positive.svg`
   (running-header isotipo) and `assets/GI_Logo_Positive.svg` (cover) as needed.
3. **Compose the document as HTML**, one `<section class="doc-page">` per page. Use the
   component classes from the spec: `.eyebrow`, `.d-h1`/`.d-h2`/`.d-h3`, `.d-lead`, `.d-body`,
   lists, `.d-callout`, `.d-pull`, `.d-stat`, `.d-table`, `.d-figure`, `.d-aside`, `.d-rule`,
   `.doc-cover`, `.doc-section`, `.doc-header`, `.doc-footer`. Load Plus Jakarta Sans:
   `<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">`
4. **Render to PDF** with `python3 scripts/render_pdf.py <input.html> <output.pdf>`
   (Letter 816×1056px, prints backgrounds, waits for fonts). Requires playwright + chromium.
5. **QA before delivering:** confirm every page is on a light background, no light-on-light
   text, headings/eyebrows/rules in blue, tables with blue header, and the isotipo in its
   original tone. Present the PDF to the user.

## Non-negotiable rules

- **GI master brand only.** Never use Scaling Up, ImpactX or other course/MBC colors, nor the
  4-Decisiones / Stages / Focuses semantic palettes.
- **Light backgrounds only.** Color appears in elements, never as a page background.
- **Accent is BLUE** (`--accent: #1F4FD8`). Orange exists only as a data color in charts.
- **Text always contrasts with its background** — never light on light.
- **Isotipo in its original tone** (positive black / negative white); never retint it.
- **Documents may show page folios** and running header/footer (unlike GI slides).
- **Typeface: Plus Jakarta Sans** for everything.

## Files

- `references/design-system-docs-gi.md` — full specification (read this).
- `assets/tokens.css` — GI-only tokens (color, type scale, page metrics).
- `assets/base.css` — page structure + all document components.
- `assets/GI_Icon_Positive.svg`, `assets/GI_Logo_Positive.svg` — logo/isotipo.
- `scripts/render_pdf.py` — HTML → Letter PDF renderer.

## Minimal page skeleton

```html
<!doctype html><html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="tokens.css"><link rel="stylesheet" href="base.css"></head><body>
  <section class="doc-page">
    <div class="doc-header"><span><!-- inline GI_Icon_Positive.svg here (class="ico") --></span><span>Título del documento</span></div>
    <p class="eyebrow">Sección</p>
    <h1 class="d-h1">Título</h1>
    <hr class="d-rule">
    <p class="d-lead">Entradilla…</p>
    <p class="d-body">Cuerpo…</p>
    <div class="doc-footer"><span>Growth Institute</span><span>01</span></div>
  </section>
</body></html>
```
