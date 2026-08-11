# GI · Sistema de Diseño de Documentos

Especificación para **documentos** de Growth Institute: reportes, propuestas, one-pagers, case studies. Usa **exclusivamente la marca maestra GI** (sin colores de cursos como SU, ImpactX u otros MBC, ni la semántica de las 4 Decisiones). Todo va sobre **fondo claro**; el color vive en los elementos.

> Este es un sistema **distinto** al de slides. Aquí prima la lectura: cuerpo más chico, más densidad de texto, encabezado/pie corridos y **folio de página** (permitido en documentos, a diferencia de las slides).

---

## 1. Principios

1. **Solo marca GI.** Nada de colores de cursos ni de framework (4 Decisiones, Etapas, Enfoques). Solo la paleta maestra.
2. **Claro por defecto.** El fondo de página es siempre claro. El color aparece en encabezados, acentos, datos y objetos — nunca como fondo.
3. **El texto siempre contrasta con su fondo.** Nunca texto claro sobre fondo claro.
4. **Isotipo en su tono original.** El logo/isotipo se usa tal cual (positivo negro, negativo blanco); no se retinta.
5. **Documento ≠ slide.** Jerarquía de lectura, folio de página y componentes editoriales.

---

## 2. Color (solo GI)

### Marca
| Token | Uso | HEX |
|---|---|---|
| `--primary` | Azul GI · encabezados H2, tabla, enlaces | `#1F4FD8` |
| `--secondary` | Azul secundario · degradados/hover | `#1A30D6` |
| `--accent` | **Acento en AZUL** · overlines, viñetas, reglas | `#1F4FD8` |
| `--accent-2` | Lavanda · acento terciario opcional | `#897AEB` |
| `--ink` | Tinta de marca (casi negro azulado) | `#081022` |

> El acento es **azul** (igual que el primario): el sistema es monocromático en azul. Si se necesita un segundo tono para jerarquía, usar la lavanda `--accent-2`.

### Neutros (tinte azul ~220°)
| Token | HEX | Uso típico |
|---|---|---|
| `--n0` | `#FFFFFF` | Fondo de página |
| `--n100` | `#EFF2F8` | Fondos de nota, filas alternas, divisores |
| `--n200` | `#DFE4EF` | Líneas, bordes |
| `--n300` | `#C6CFDE` | Bordes, marcadores tenues |
| `--n400` | `#9DA9BE` | Texto muy secundario, folios |
| `--n500` | `#7C89A2` | Pies de figura / captions |
| `--n600` | `#5B6986` | Texto secundario (AA) |
| `--n700` | `#414E68` | Entradilla |
| `--n800` | `#273146` | Cuerpo |
| `--n900` | `#141A2A` | Títulos, tinta principal |

### Datos / gráficos
| Token | HEX |
|---|---|
| `--data-1` | `#1F4FD8` |
| `--data-2` | `#4FC8DC` |
| `--data-3` | `#FFA500` |
| `--data-4` | `#897AEB` |
| `--data-positive` | `#8FC93A` |
| `--data-negative` | `#D64045` |
| `--data-neutral` | `#C6CFDE` |

> Regla de datos: nunca comunicar solo con color; acompañar con signo, flecha o etiqueta. (El naranja `#FFA500` sigue disponible **solo** como color de dato en gráficos, no como acento de marca.)

---

## 3. Tipografía

**Familia única: Plus Jakarta Sans** (títulos y cuerpo).

```
--font-display: "Plus Jakarta Sans", system-ui, sans-serif;
--font-body:    "Plus Jakarta Sans", system-ui, sans-serif;
```

Escala (px sobre página Carta @96dpi; equivalente en pt aprox.):

| Rol | Token | px | ~pt | Peso |
|---|---|---|---|---|
| Portada | `--t-cover` | 53 | 40 | 700 |
| Título H1 | `--t-h1` | 32 | 24 | 700 |
| Subtítulo H2 (azul) | `--t-h2` | 23 | 17 | 600 |
| Apartado H3 | `--t-h3` | 17 | 13 | 600 |
| Entradilla / lead | `--t-lead` | 17 | 13 | 400 |
| Cuerpo | `--t-body` | 14 | 10.5 | 400 |
| Secundario | `--t-small` | 12 | 9 | 400 |
| Caption / pie | `--t-caption` | 11 | 8.5 | 400 |
| Overline / eyebrow | `--t-eyebrow` | 12 | 9 | 600 · MAYÚS · tracking .14em · **azul** |
| Fuente / folio | `--t-source` | 11 | 8 | 400 |

Interlínea de cuerpo: **1.55**.

---

## 4. Página

Carta (US Letter) vertical.

```
--doc-w: 816px;  --doc-h: 1056px;   /* 8.5 × 11 in @96dpi */
--doc-mx: 84px;                      /* margen lateral */
--doc-mt: 110px;                     /* superior (aire para encabezado) */
--doc-mb: 92px;                      /* inferior (aire para pie) */
--col-gap: 32px;
```

- **Encabezado corrido** (`.doc-header`): isotipo (negro) + título de documento, con línea inferior.
- **Pie corrido** (`.doc-footer`): marca a la izquierda, **folio de página** a la derecha.
- Contenido a **1 o 2 columnas** (`.doc-cols`).
- Para A4, cambiar `--doc-w/--doc-h` a `794px × 1123px`.

---

## 5. Componentes

| Clase | Qué es | Notas de estilo |
|---|---|---|
| `.doc-page` | Página base | Carta, fondo `--n0`, padding de márgenes, salto de página |
| `.doc-cover` | Portada | Banda superior (`masthead`) en `--primary`; logo en `--ink`; palabra destacada en `--accent` (azul) |
| `.doc-section` | Portada de sección | Fondo `--n100`; número grande en acento; título en tinta |
| `.doc-header` / `.doc-footer` | Encabezado / pie corridos | Isotipo negro; folio en el pie |
| `.eyebrow` | Overline | Mayúsculas, tracking, **azul** |
| `.d-h1` | Título de sección | Display 32px, tinta |
| `.d-h2` | Subtítulo | Display 23px, **azul** `--primary` |
| `.d-h3` | Apartado | Display 17px, tinta |
| `.d-lead` | Entradilla | 17px, `--n700` |
| `.d-body` / `p` | Cuerpo | 14px, `--n800`, interlínea 1.55 |
| `.d-small` / `.d-caption` | Secundario / pie | `--n600` / `--n500` |
| `ul` / `ol` | Listas | Viñeta en acento (azul); numeración en `--primary` |
| `.d-callout` | Nota / aviso | Fondo `--n100`, filo izquierdo en acento; `.k` = título |
| `.d-pull` | Cita destacada | Display, texto en `--primary`, filo en acento; `.who` = autor |
| `.d-stat` | Dato clave | Número display 44px en `--primary`; `.pos` → verde, `.neg` → rojo |
| `.d-table` | Tabla | Cabecera `--primary` con texto blanco; filas alternas `--n100`; líneas `--n200` |
| `.d-figure` + `figcaption` | Figura con pie | Marco `--n100`; pie en `--n500` |
| `.d-aside` | Barra lateral | Fondo `--n100`; `.k` en `--primary` |
| `.d-rule` | Reglita de acento | Barra 56×3px en acento (azul) |
| `.c-1…4`, `.c-pos`, `.c-neg` | Helpers de color de datos | Para texto/íconos en gráficos |

---

## 6. Cómo aplicarlo

Enlazar los dos archivos del sistema y componer páginas con las clases:

```html
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="styles/base.css">

<section class="doc-page">
  <div class="doc-header"><span><svg class="ico">…isotipo…</svg></span><span>Título del documento</span></div>

  <p class="eyebrow">Sección</p>
  <h1 class="d-h1">Título</h1>
  <hr class="d-rule">
  <p class="d-lead">Entradilla del apartado…</p>
  <p class="d-body">Cuerpo de lectura…</p>

  <div class="d-callout"><p class="k">Nota</p><p class="d-body">…</p></div>

  <div class="doc-footer"><span>Growth Institute</span><span>02</span></div>
</section>
```

Renderizado a PDF (fiel a fuentes y variables CSS) con Chromium/Playwright a tamaño `816×1056px`, `printBackground`, `preferCSSPageSize`.

---

## 7. Reglas de oro (resumen)

- Solo marca GI; sin colores de cursos ni de las 4 Decisiones.
- Fondo siempre claro; el color va en los elementos.
- Acento en **azul**; naranja solo como color de dato en gráficos.
- Texto siempre en contraste con su fondo.
- Isotipo en su tono original (no retintar).
- Folio de página permitido; encabezado y pie corridos.
- Tipografía única: **Plus Jakarta Sans**.
