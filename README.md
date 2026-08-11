# GI · Document Design System

Sistema de diseño oficial de Growth Institute para **documentos** (reportes, one-pagers, propuestas, case studies, memos, briefs). Empaquetado como skill de Claude e importable en Claude Design.

- Marca madre GI únicamente — sin colores de cursos/MBC ni paletas semánticas.
- Fondos siempre claros; el color vive en los elementos. Acento **azul** `#1F4FD8`.
- Tipografía: **Plus Jakarta Sans**.
- No aplica a slides (eso es un sistema aparte).

## Contenido

| Archivo | Qué es |
|---|---|
| [SKILL.md](SKILL.md) | Instrucciones del skill (workflow + reglas no negociables) |
| [references/design-system-docs-gi.md](references/design-system-docs-gi.md) | Especificación completa: tokens, escala tipográfica, componentes |
| [assets/tokens.css](assets/tokens.css) | Tokens de color, tipografía y métricas de página |
| [assets/base.css](assets/base.css) | Estructura de página + componentes de documento |
| [assets/GI_Icon_Positive.svg](assets/GI_Icon_Positive.svg) · [assets/GI_Logo_Positive.svg](assets/GI_Logo_Positive.svg) | Isotipo y logo |
| [scripts/render_pdf.py](scripts/render_pdf.py) | Render HTML → PDF Letter (requiere playwright + chromium) |
