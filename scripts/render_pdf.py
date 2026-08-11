#!/usr/bin/env python3
"""Render a GI document HTML to a Letter-size PDF (faithful to CSS variables + fonts).

Usage:  python3 render_pdf.py <input.html> <output.pdf>

The HTML must link the bundled assets/tokens.css and assets/base.css and load
Plus Jakarta Sans from Google Fonts. Requires playwright + chromium in the env.
"""
import sys, pathlib
from playwright.sync_api import sync_playwright

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 render_pdf.py <input.html> <output.pdf>"); sys.exit(1)
    src = pathlib.Path(sys.argv[1]).resolve()
    out = sys.argv[2]
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto("file://" + str(src))
        pg.wait_for_timeout(2500)  # allow web fonts to load
        pg.pdf(path=out, width="816px", height="1056px",
               print_background=True, prefer_css_page_size=True)
        b.close()
    print("Wrote", out)

if __name__ == "__main__":
    main()
