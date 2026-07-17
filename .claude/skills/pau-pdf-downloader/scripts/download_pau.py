#!/usr/bin/env python3
"""Descarga un examen PAU en PDF, lo renombra y lo guarda en la carpeta destino.

Nombre final: Universidad_asignatura_convocatoria_anio.pdf
Ejemplo: UAH_fisica_ord_2026.pdf
"""
import argparse
import os
import sys
import unicodedata
from pathlib import Path

BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/17.0 Safari/605.1.15"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "application/pdf,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


def slug(texto: str) -> str:
    """minusculas, sin tildes ni espacios."""
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


def descargar(url: str, ruta: Path) -> None:
    try:
        import requests
    except ImportError:
        sys.exit("ERROR: falta 'requests'. Instala con: pip3 install requests")

    from urllib.parse import urlsplit
    referer = f"{urlsplit(url).scheme}://{urlsplit(url).netloc}/"
    headers = dict(BROWSER_HEADERS, Referer=referer)

    s = requests.Session()
    # Primera visita a la home para obtener cookies (algunos WAF las exigen).
    try:
        s.get(referer, headers=headers, timeout=30)
    except requests.RequestException:
        pass

    r = s.get(url, headers=headers, timeout=60, allow_redirects=True)
    if r.status_code == 403:
        sys.exit(
            "ERROR 403: el servidor bloquea la descarga automática.\n"
            "Este sitio requiere un navegador real. Usa la variante con "
            "Playwright/Chromium (pídesela a Claude) o descarga el PDF a mano "
            "y luego pásame el archivo local para renombrarlo y catalogarlo."
        )
    r.raise_for_status()

    ct = r.headers.get("Content-Type", "")
    data = r.content
    if b"%PDF" not in data[:1024] and "pdf" not in ct.lower():
        sys.exit(
            f"ERROR: el contenido no parece un PDF (Content-Type: {ct}). "
            "Puede que la URL lleve a una página HTML en vez de al archivo."
        )
    ruta.write_bytes(data)


def info_pdf(ruta: Path) -> str:
    tam = ruta.stat().st_size / 1024
    paginas = "?"
    try:
        from pypdf import PdfReader
        paginas = len(PdfReader(str(ruta)).pages)
    except Exception:
        pass
    return f"{paginas} páginas, {tam:.0f} KB"


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

    descargar(a.url, ruta)

    print("OK")
    print(f"Ruta:        {ruta}")
    print(f"Universidad: {a.universidad}")
    print(f"Asignatura:  {a.asignatura}")
    print(f"Convocatoria:{a.convocatoria}")
    print(f"Año:         {a.anio}")
    print(f"PDF:         {info_pdf(ruta)}")


if __name__ == "__main__":
    main()
