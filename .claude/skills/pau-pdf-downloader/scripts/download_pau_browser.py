#!/usr/bin/env python3
"""Descarga un examen PAU usando un navegador real (Playwright/Chromium).

Úsalo cuando download_pau.py falla con 403 (WAF), como en la UCLM.
Requiere: pip3 install playwright && playwright install chromium

Mismos argumentos que download_pau.py.
"""
import argparse
import os
import sys
import unicodedata
from pathlib import Path


def slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return "".join(c for c in t.lower() if c.isalnum())


def nombre_unico(destino: Path, base: str) -> Path:
    ruta = destino / f"{base}.pdf"
    if not ruta.exists():
        return ruta
    i = 2
    while (destino / f"{base}_v{i}.pdf").exists():
        i += 1
    return destino / f"{base}_v{i}.pdf"


def info_pdf(ruta: Path) -> str:
    tam = ruta.stat().st_size / 1024
    paginas = "?"
    try:
        from pypdf import PdfReader
        paginas = len(PdfReader(str(ruta)).pages)
    except Exception:
        pass
    return f"{paginas} páginas, {tam:.0f} KB"


def descargar_playwright(url: str, ruta: Path) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit(
            "ERROR: falta Playwright. Instala con:\n"
            "  pip3 install playwright && playwright install chromium"
        )

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                "Version/17.0 Safari/605.1.15"
            ),
            accept_downloads=True,
            locale="es-ES",
        )
        page = ctx.new_page()
        # La respuesta directa suele ser el binario del PDF: la capturamos.
        resp = page.request.get(url)
        if not resp.ok:
            browser.close()
            sys.exit(f"ERROR {resp.status}: no se pudo descargar tras usar navegador.")
        data = resp.body()
        browser.close()

    if b"%PDF" not in data[:1024]:
        sys.exit("ERROR: el contenido descargado no es un PDF.")
    ruta.write_bytes(data)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True)
    p.add_argument("--universidad", required=True)
    p.add_argument("--asignatura", required=True)
    p.add_argument("--convocatoria", required=True, choices=["ord", "extr"])
    p.add_argument("--anio", required=True)
    p.add_argument("--dest", default="~/Downloads/PAU")
    a = p.parse_args()

    destino = Path(os.path.expanduser(a.dest))
    destino.mkdir(parents=True, exist_ok=True)
    base = f"{a.universidad}_{slug(a.asignatura)}_{a.convocatoria}_{a.anio}"
    ruta = nombre_unico(destino, base)

    descargar_playwright(a.url, ruta)

    print("OK (via Playwright)")
    print(f"Ruta:        {ruta}")
    print(f"Universidad: {a.universidad}")
    print(f"Asignatura:  {a.asignatura}")
    print(f"Convocatoria:{a.convocatoria}")
    print(f"Año:         {a.anio}")
    print(f"PDF:         {info_pdf(ruta)}")


if __name__ == "__main__":
    main()
