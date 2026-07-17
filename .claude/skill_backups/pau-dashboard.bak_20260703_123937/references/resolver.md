# Cómo resolver y cómo dibujar los diagramas

## Principios generales de resolución
- Resuelve **todas** las cuestiones del examen, incluidas las opcionales (el alumno elige, pero el material debe cubrir ambas).
- Estructura cada solución por apartados con `<h5>a) …</h5>`, `<h5>b) …</h5>`.
- Muestra el **desarrollo**, no solo el resultado: enunciado del método, sustitución de datos, operación y resultado con unidades.
- Cierra cada apartado con un recuadro `<div class="res"><b>…</b></div>` con el resultado.
- Cuando un valor dependa de leer una gráfica, dilo explícitamente y da un rango razonable.

## Por familia de asignatura

### Física / Química / Tecnología e Ingeniería
- Fórmulas en KaTeX. Define símbolos y unidades.
- Reproduce las figuras del enunciado como SVG (curvas, circuitos, montajes) y añade diagramas propios en la solución (diagramas de fuerzas, de esfuerzos, fasoriales, etc.).
- Comprueba coherencia dimensional.

### Matemáticas / Dibujo Técnico
- Pasos algebraicos completos; en geometría, un SVG con la construcción.
- Para funciones, un SVG con ejes, la curva y los puntos notables.

### Biología / Geología
- Esquemas SVG sencillos (ciclos, estructuras) y respuestas con vocabulario preciso.

### Historia / Filosofía / Economía / Lengua / Idiomas (letras)
- No hay cálculo: la "solución" es una **respuesta modelo** argumentada, estructurada en párrafos o listas, con tesis, desarrollo y ejemplos.
- La sección "¿Qué vamos a aplicar?" resume el enfoque (qué se pide: comentar, comparar, definir…) y los conceptos clave.
- En comentarios de texto/fuentes, indica la estructura esperada de respuesta.

## Diagramas SVG: recomendaciones
- `viewBox` proporcional; ancho `width="100%"` con `style="max-width:…px"`.
- Colores mediante variables ya definidas o hex directos; sobre el fondo oscuro de `.fig` usa trazos claros (`#22d3ee`, `#f59e0b`, `#4ade80`, `#a78bfa`, `#fb7185`) y texto `#e7ecf7`.
- Ejes y rejilla en tonos apagados (`#94a3c0`, `#26324e`).
- Etiqueta los ejes y los puntos relevantes.

### Ejemplos de SVG para tarjetas de inicio (60–120 px)
Iconos simples y reconocibles del tema del bloque. Ejemplos: dos figuras de personas + engranaje (trabajo en equipo), una curva ascendente sobre ejes (ensayo/tracción), una viga con cargas (mecánica), una senoidal (corriente alterna), un escudo con check (ciberseguridad). Mantén 2–3 trazos, sin relleno pesado.

### Ejemplos de SVG en soluciones
- **Gráfica carga–alargamiento**: ejes, rejilla, `path` de la curva, líneas discontinuas a los puntos leídos.
- **Viga**: rectángulo (viga), triángulo (apoyo fijo) y círculo (apoyo móvil), flechas de carga, cotas; debajo, diagramas de cortante (polígonos) y flector (trapecio).
- **Circuito**: líneas para conductores, zig-zag para resistencias, bobina (semicírculos), condensador (dos placas), círculo con senoidal para el generador.
- **Mapa de Karnaugh**: rejilla 4×4 con etiquetas Gray, ceros/unos coloreados y rectángulos redondeados para los grupos.
- **Diagrama de bloques**: rectángulos etiquetados, sumador (círculo con ⊗), flechas con puntas y lazo de realimentación.

Reutiliza y adapta los patrones del dashboard de referencia; no hace falta reinventar cada figura.
