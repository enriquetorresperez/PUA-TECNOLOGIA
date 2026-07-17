#!/usr/bin/env python3
"""
Extrae las figuras de un examen en PDF para poder inspeccionarlas visualmente
ANTES de reproducirlas como SVG. Es el primer paso para lograr diagramas fieles.

Produce, en la carpeta de salida:
  - pagina_NN.png        : cada página rasterizada a alta resolución (para leer y ver figuras).
  - imagen_NN_MM.png     : cada imagen incrustada extraída (curvas, fotos de circuitos, etc.).
  - figuras_report.txt   : inventario de imágenes por página con sus dimensiones.

Uso:
    python3 extract_figures.py examen.pdf carpeta_salida/

Requisitos: pymupdf (fitz). Si falta:  pip install pymupdf --break-system-packages
Tras ejecutarlo, USA la herramienta `view` sobre cada PNG para observar cada figura
y medir proporciones, posiciones de puntos, ejes y etiquetas antes de dibujar el SVG.
"""
import os
import sys


def main():
    if len(sys.argv) < 3:
        print("Uso: python3 extract_figures.py examen.pdf carpeta_salida/", file=sys.stderr)
        sys.exit(1)
    pdf_path, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)

    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("Falta PyMuPDF. Instala:  pip install pymupdf --break-system-packages", file=sys.stderr)
        sys.exit(2)

    doc = fitz.open(pdf_path)
    report = []
    # Rasteriza cada página a ~200 DPI para ver figuras con nitidez
    zoom = 200 / 72.0
    mat = fitz.Matrix(zoom, zoom)
    for pno in range(len(doc)):
        page = doc[pno]
        pix = page.get_pixmap(matrix=mat)
        pg_name = os.path.join(outdir, f"pagina_{pno+1:02d}.png")
        pix.save(pg_name)
        # Imágenes incrustadas (gráficas, fotos escaneadas de figuras)
        imgs = page.get_images(full=True)
        report.append(f"Página {pno+1}: {len(imgs)} imagen(es) incrustada(s)")
        for i, img in enumerate(imgs):
            xref = img[0]
            try:
                base = fitz.Pixmap(doc, xref)
                if base.n - base.alpha >= 4:  # CMYK u otros -> pasar a RGB
                    base = fitz.Pixmap(fitz.csRGB, base)
                im_name = os.path.join(outdir, f"imagen_{pno+1:02d}_{i+1:02d}.png")
                base.save(im_name)
                report.append(f"    - imagen_{pno+1:02d}_{i+1:02d}.png  ({base.width}x{base.height}px)")
                base = None
            except Exception as e:
                report.append(f"    - (no se pudo extraer imagen {i+1}: {e})")

    with open(os.path.join(outdir, "figuras_report.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(report))
    print("\n".join(report))
    print(f"\nRasterizadas {len(doc)} páginas en {outdir}")
    print("SIGUIENTE PASO: usa `view` sobre cada pagina_NN.png para observar las figuras "
          "y reproducirlas fielmente como SVG (proporciones, ejes, puntos, etiquetas).")
    doc.close()


if __name__ == "__main__":
    main()
