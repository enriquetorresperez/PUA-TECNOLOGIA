# Esquema del JSON de entrada

`build_dashboard.py` recibe un JSON con esta forma. Los campos de texto admiten **HTML inline** (por ejemplo `<b>`, `<i>`, `<sub>`, `<ul><li>`) y **fórmulas KaTeX** con `\( ... \)` (en línea) o `$$ ... $$` (bloque). Las figuras se incrustan como **SVG** en bruto dentro del string.

## Estructura general

```json
{
  "meta": {
    "titulo": "Tecnología e Ingeniería II",
    "subtitulo": "Universidades Públicas de la Comunidad de Madrid · Curso 2025-2026 · Examen resuelto y comentado",
    "cabecera_titulo": "PAU 2026 · Tecnología e Ingeniería II · Convocatoria Extraordinaria",
    "pill": "90 min · 2 pt/cuestión",
    "enunciado_pdf": "tec_2026_ext.pdf",
    "footer": "Dpto. Tecnología del IES CASTILLA · Prof. Enrique Torres Pérez",
    "intro_inicio": "Selecciona un bloque o una cuestión en la barra lateral. Cada cuestión incluye el enunciado oficial, una introducción con los conceptos que vamos a aplicar y la solución paso a paso. Recuerda: en los bloques con opción se responde una de las dos cuestiones."
  },
  "bloques": [
    {
      "id": "b1",
      "titulo": "Bloque 1 · Proyectos",
      "color": "#f59e0b",
      "descripcion_tarjeta": "Técnicas de trabajo en equipo y metodologías de desarrollo.",
      "svg_tarjeta": "<svg ...>...</svg>",
      "cuestiones": [
        {
          "id": "q1",
          "titulo": "Cuestión 1 · Trabajo en equipo y metodologías",
          "etiqueta": "BLOQUE 1",
          "meta": "Cuestión única y obligatoria · 2 puntos (a: 1,0 · b: 1,0)",
          "menu": "Cuestión 1 · Trabajo en equipo y metodologías",
          "enunciado_html": "<p>Una fábrica...</p><ol type=\"a\"><li>Razone... <span class=\"pts\">(1 punto)</span></li></ol>",
          "figura_enunciado_svg": "",
          "aplica_html": "<p>Aplicaremos...</p><ul><li>...</li></ul>",
          "solucion_html": "<h5>a) ...</h5><p>...</p><div class=\"formula\">$$E=\\frac{\\sigma}{\\varepsilon}$$</div><div class=\"res\"><b>Resultado</b></div>"
        }
      ]
    }
  ]
}
```

## Notas por campo

- **meta.cabecera_titulo**: aparece en la barra superior; puedes resaltar la materia envolviéndola en `<span>…</span>` (se pinta en color de acento).
- **meta.enunciado_pdf**: nombre del PDF original del enunciado (opcional); si existe, se enlaza en inicio y en cada cuestión.
- **bloque.color**: color hex del bloque; se usa en el punto de la barra lateral, la etiqueta y el borde de la tarjeta.
- **bloque.svg_tarjeta**: pequeña ilustración representativa (60–120 px) para la tarjeta de inicio. Ver `resolver.md` para ejemplos.
- **cuestion.etiqueta**: texto de la píldora de color junto al título (p. ej. "BLOQUE 2").
- **cuestion.figura_enunciado_svg**: SVG de la figura del enunciado (curva, circuito, viga…). Vacío si no hay.
- **cuestion.solucion_html**: usa `<h5>` para los apartados, `<div class="formula">$$...$$</div>` para fórmulas en bloque, `<div class="res">` para resultados destacados, `<figure class="fig">…<figcaption>…</figcaption></figure>` para diagramas de la solución, y `<table class="dat">` para tablas.

## Clases CSS disponibles (ya definidas en la plantilla)
`enun`, `aplica`, `sol`, `formula`, `res`, `fig`, `dat` (tabla), `pts` (puntuación), `tag` + `t1..t5` (etiquetas de color). El script asigna automáticamente los colores de bloque, así que basta con respetar la estructura.

## Reglas KaTeX
- Nunca uses `·` dentro de `\text{}`. Para "N·m" escribe `\mathrm{N{\cdot}m}`.
- Escapa las barras invertidas en el JSON: `\\frac`, `\\sqrt`, `\\cdot`, etc.
