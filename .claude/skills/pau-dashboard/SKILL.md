---
name: pau-dashboard
description: Convierte el PDF de un examen oficial (PAU/EVAU/EBAU/Selectividad de cualquier asignatura y comunidad autónoma) en un dashboard HTML interactivo de examen resuelto, más un PDF de solución por cada cuestión y un PDF con todas las soluciones, reproduciendo con fidelidad las figuras del enunciado (curvas, circuitos, vigas, diagramas) como SVG de calidad verificados contra la imagen original. Usa este skill SIEMPRE que el usuario suba o mencione un examen de PAU, EVAU, EBAU, prueba de acceso, selectividad o convocatoria (ordinaria o extraordinaria) y pida resolverlo, corregirlo, crear un dashboard, una web de repaso, materiales de estudio, o "PDFs con la solución"; incluso si solo dice "hazme un dashboard de este examen" o "resuélveme este examen" adjuntando un PDF. También aplica a exámenes de Física, Química, Matemáticas, Tecnología e Ingeniería, Biología, Historia, Economía, Dibujo Técnico, etc. Cubre asignaturas de ciencias (con fórmulas y diagramas fieles al original) y de letras (respuestas argumentadas).
---

# Dashboard de examen PAU resuelto

Este skill automatiza el flujo completo: a partir del PDF de un examen oficial produce (1) un **dashboard HTML** autocontenido con barra lateral por bloques/cuestiones, enunciados, introducción de conceptos y soluciones desplegables con fórmulas KaTeX y diagramas SVG; (2) **un PDF por cuestión** (enunciado + solución); y (3) **un PDF con todas las soluciones**.

El resultado imita el estilo del dashboard de referencia: tema oscuro, cabecera con el título del examen, tarjetas ilustradas en la pantalla de inicio, y pie de página personalizable con el departamento y el profesor.

## Flujo de trabajo (síguelo en orden)

### Paso 1 — Leer el examen y observar sus figuras
El PDF estará en `/mnt/user-data/uploads/`. Léelo con la skill de lectura de PDF o directamente si el contenido ya está en contexto. Extrae **fielmente**:
- Título/materia, universidad o comunidad, curso y convocatoria (ordinaria/extraordinaria).
- La estructura de **bloques** y **cuestiones** (incluida la opcionalidad: p. ej. "responder una de las dos").
- El **enunciado completo** de cada cuestión y apartado, con su puntuación.
- Los **datos, figuras y gráficas** (curvas, circuitos, vigas, diagramas, tablas).

Si el examen tiene criterios de corrección, úsalos para repartir la puntuación.

**Inspección visual obligatoria de las figuras.** La calidad de los diagramas es lo que más distingue este material. No dibujes ninguna figura de memoria ni solo a partir del texto. Antes de resolver:
```bash
pip install pymupdf --break-system-packages   # si falta
python3 scripts/extract_figures.py /mnt/user-data/uploads/examen.pdf /tmp/fig/
```
Esto rasteriza cada página a alta resolución y extrae las imágenes incrustadas. **Usa la herramienta `view` sobre cada `pagina_NN.png`** para observar realmente cada figura (curva, circuito, viga, montaje…). Anota para cada una: rango y escala de los ejes, puntos y coordenadas clave, posiciones relativas de los elementos, etiquetas literales y la proporción ancho/alto. Estas notas son la base para reproducir el SVG con fidelidad. Lee `references/figuras.md` para el método completo.

### Paso 2 — Resolver cada cuestión y reproducir sus figuras
Para **cada** cuestión resuelve de forma completa y pedagógica:
- Una **introducción breve** ("¿Qué vamos a aplicar?") con los conceptos, leyes o fórmulas clave.
- La **solución paso a paso**, con desarrollo coherente, unidades correctas y el **resultado destacado**.
- En ciencias: fórmulas en KaTeX y, cuando el enunciado tenga una figura, un **diagrama SVG fiel** (ver abajo).
- En letras: respuesta argumentada, estructurada y con ejemplos.

**Reproducción fiel de cada figura (crítico).** Reproduce las figuras del enunciado como SVG a partir de lo que **observaste** en el Paso 1, respetando proporciones, escala de ejes, posiciones de puntos y etiquetas literales. Calcula la posición de cada punto con una regla lineal (mapeo valor→coordenada), no a ojo. Luego **verifica** cada figura convirtiéndola a PNG y comparándola con la original:
```bash
node scripts/svg_to_png.js /tmp/figura.svg /tmp/figura.png
```
Abre el PNG con `view` junto a la `pagina_NN.png` original y comprueba que coinciden proporciones, valores de ejes y ubicación de los puntos. **No des una figura por buena hasta que la comparación sea claramente fiel.** Aplica el mismo rigor a las figuras nuevas de la solución (diagramas de esfuerzos, fasoriales, etc.), que deben ser coherentes con los resultados calculados. Si una figura es demasiado compleja para vectorizar con fidelidad (fotografía, esquema muy denso), es preferible **incrustar la imagen original** extraída con `extract_figures.py` (guárdala junto al dashboard y referénciala con `<img>`) antes que ofrecer un SVG impreciso; avisa al usuario de esa decisión.

Consulta `references/resolver.md` para pautas por asignatura y `references/figuras.md` para el método completo de reproducción y verificación de figuras.

### Paso 3 — Generar el dashboard HTML
Genera un único archivo HTML autocontenido. **No escribas el HTML a mano desde cero**: usa `scripts/build_dashboard.py`, que recibe un JSON con el contenido del examen y produce el dashboard aplicando la plantilla y los estilos de referencia.

1. Escribe el contenido resuelto en un JSON siguiendo el esquema de `references/esquema_json.md`.
2. Ejecuta:
   ```bash
   python3 scripts/build_dashboard.py examen.json /mnt/user-data/outputs/dashboard.html
   ```
El script inserta cabecera, barra lateral coloreada por bloques, tarjetas de inicio, KaTeX, botones de solución desplegables, botones "Ver PDF" (que abren en pestaña nueva, **nunca** con `download`) y el pie de página.

### Paso 4 — Generar los PDFs
Con el mismo dashboard ya creado, genera los PDFs con `scripts/build_pdfs.js` (Playwright + Chromium). Produce un PDF por cuestión y el PDF completo, con estas reglas ya incorporadas (aprendidas de iteraciones reales):
- El contenido **empieza pegado a la cabecera** (sin salto de página inicial que deje la primera página casi vacía).
- Enunciado y solución van **seguidos**; solo figuras, tablas, fórmulas y recuadros de resultado no se parten.
- En el PDF completo, **cada cuestión (a partir de la segunda) empieza en página nueva**.
- Tema **claro** para imprimir; los diagramas SVG conservan su fondo oscuro.
- Pie con "Dpto. … · Prof. …" y numeración de página.

```bash
node scripts/build_pdfs.js /mnt/user-data/outputs/dashboard.html /mnt/user-data/outputs/pdf/
```
Si Chromium no está instalado: `npx playwright install chromium`. Si la red usa proxy con certificado propio, el script ya lanza el navegador con `ignoreHTTPSErrors`.

### Paso 5 — Entregar
Copia todo a `/mnt/user-data/outputs/`, crea un ZIP con el HTML, el PDF original del enunciado y la carpeta `pdf/`, y preséntalo con `present_files`. Recuerda al usuario que para publicarlo debe subir el HTML y la carpeta `pdf/` juntos a su hosting (los enlaces son relativos).

## Personalización

Antes de generar, pregunta (o infiere del contexto/memoria) el **pie de página**: departamento y profesor. Por defecto usa lo que el usuario haya indicado antes. Otros ajustes opcionales: colores por bloque, idioma (por defecto, el del examen), y si quiere incluir la portada del examen oficial enlazada.

## Reglas aprendidas (evita repetir errores)
- **KaTeX**: nunca metas el carácter `·` dentro de `\text{}` (rompe el render). Usa `\mathrm{N{\cdot}m}` o `\cdot`. Activa `throwOnError:false` y `strict:false`.
- **Enlaces a PDF en el HTML**: usa `target="_blank" rel="noopener"`, **sin** atributo `download`, para que se abran en el navegador en vez de forzar la descarga.
- **Fuentes/CDN dentro de Chromium**: si hay proxy corporativo, usa `ignoreHTTPSErrors:true` en el contexto.
- **Espacios en blanco en PDF**: no fuerces `break-before:page` en la primera cuestión ni `break-inside:avoid` en las cajas de texto largas; deja fluir el texto.

## Recursos del skill
- `scripts/extract_figures.py` — rasteriza las páginas del examen y extrae sus imágenes para inspección visual fiel (primer paso antes de dibujar).
- `scripts/svg_to_png.js` — convierte un SVG a PNG para verificar que una figura reproducida coincide con la original.
- `scripts/build_dashboard.py` — genera el dashboard HTML desde el JSON del examen.
- `scripts/build_pdfs.js` — genera los PDFs (por cuestión + completo) desde el HTML.
- `references/figuras.md` — método de reproducción fiel y verificación de figuras (léelo siempre que haya diagramas).
- `references/esquema_json.md` — esquema del JSON de entrada, con ejemplo.
- `references/resolver.md` — cómo resolver por asignatura y cómo dibujar los SVG.
- `assets/plantilla_estilos.css` — estilos de referencia (los usa el script del dashboard).
