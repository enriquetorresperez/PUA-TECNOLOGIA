# Reproducción fiel de figuras (enunciado y solución)

La calidad de los diagramas es lo que distingue un material profesional de uno
mediocre. Una figura mal proporcionada o que no coincide con el enunciado
confunde al alumno. Por eso **nunca se dibuja "a ojo"**: se observa la figura
original, se miden sus rasgos y se reproduce con fidelidad verificada.

## Regla de oro
Toda figura del enunciado debe reproducirse a partir de la **observación directa
de la imagen original**, no de la imaginación ni solo del texto. El diagrama
final debe ser reconociblemente el mismo que el del examen: mismas proporciones,
mismos valores en los ejes, mismos puntos marcados, mismas etiquetas.

## Flujo obligatorio para CADA figura del enunciado

1. **Rasteriza y observa.** Ejecuta `scripts/extract_figures.py examen.pdf fig/`
   y luego usa la herramienta `view` sobre cada `pagina_NN.png` (y sobre las
   `imagen_*` extraídas). No pases a dibujar hasta haber *visto* la figura.

2. **Mide y anota** antes de dibujar. Para cada figura apunta:
   - Tipo (gráfica de ejes, circuito, viga, montaje, diagrama de bloques…).
   - **Rango y escala de los ejes** (valores mínimo/máximo, separación de la
     rejilla, unidades) — cópialos EXACTOS del original.
   - **Puntos y coordenadas clave**: dónde empieza/acaba una curva, dónde está el
     codo elástico, los máximos, los cruces por cero.
   - **Elementos y su posición relativa**: p. ej. cargas a 6 m y 9 m sobre una
     viga de 15 m → sus posiciones en el SVG deben respetar esas proporciones.
   - **Etiquetas y textos** literales (R₁, X_L, F₂, "500 N", nombres de ejes).
   - **Proporción global** (relación ancho/alto) para fijar el `viewBox`.

3. **Fija el sistema de coordenadas.** Elige un `viewBox` cuyo tamaño facilite el
   mapeo. Para gráficas, define márgenes para los ejes y calcula la posición de
   cada punto con una regla lineal:
   `x_svg = x0 + (valor - min)/(max - min) * ancho_util`
   (y análogamente en Y, recordando que en SVG el eje Y crece hacia abajo).
   Esto garantiza que los puntos caen donde deben, no aproximados a mano.

4. **Dibuja con precisión.** Usa `path`/`line`/`circle`/`rect`/`text`. Reglas:
   - Ejes y rejilla completos, con **los mismos valores numéricos** del original.
   - La curva debe pasar por los puntos medidos (usa segmentos o curvas Bézier
     ajustadas a esos puntos, no un trazo genérico).
   - Marca con líneas discontinuas y un punto los valores que la solución va a
     usar (p. ej. el punto (0,5 mm; 60 kN) del que se obtiene E).
   - Etiqueta ejes y puntos con el mismo texto del examen.

5. **Verifica superponiendo.** Renderiza tu SVG a PNG y compáralo con la figura
   original abriendo ambos con `view`:
   ```bash
   # convierte el SVG a PNG para comparar (usa el navegador headless del skill)
   node scripts/svg_to_png.js figura.svg figura.png
   ```
   Comprueba: ¿coinciden las proporciones? ¿los ejes marcan los mismos números?
   ¿los puntos están en el mismo sitio? Si no, corrige el mapeo y repite. No des
   una figura por buena hasta que la comparación sea claramente fiel.

## Estándares de calidad del SVG
- `viewBox` proporcional a la figura real; `width="100%"` con `style="max-width:…px"`.
- Trazos limpios: grosores 1–3 px, uniones redondeadas en curvas
  (`stroke-linecap="round" stroke-linejoin="round"`).
- Tipografía coherente: `font-family="JetBrains Mono"` para números de ejes,
  tamaño ~11–13 px; nada de texto que se salga del lienzo o se solape.
- Sobre el fondo oscuro de `.fig`: trazos claros (`#22d3ee`, `#f59e0b`,
  `#4ade80`, `#a78bfa`, `#fb7185`), texto `#e7ecf7`, rejilla `#26324e`/`#94a3c0`.
- Sin deformaciones: si el original es más ancho que alto, el SVG también.

## Patrones por tipo de figura (mídelos, no los copies literalmente)

### Gráfica de ejes (curva carga–alargamiento, funciones, tensión–deformación)
Ejes con flechas o líneas, rejilla a los intervalos del original, etiquetas
numéricas EXACTAS, curva ajustada a los puntos observados, líneas guía
discontinuas a los puntos que usa la solución. Verifica que el máximo y el codo
caen a la altura correcta.

### Viga / estructura
Rectángulo para la viga; triángulo = apoyo fijo, círculo (o rodillo) = apoyo
móvil; flechas verticales para cargas puntuales; cotas con los valores del
enunciado. Las distancias entre cargas y apoyos deben respetar la escala real
(p. ej. si una carga está en el punto medio, dibújala en el punto medio).

### Circuito eléctrico/electrónico
Conductores en líneas rectas ortogonales; resistencia = zig-zag o rectángulo
según el estilo del examen; bobina = semicírculos; condensador = dos placas
paralelas; generador = círculo con senoidal. Respeta la **topología** (qué está
en serie y qué en paralelo) y coloca cada componente y etiqueta como en el original.

### Diagrama de bloques (control)
Rectángulos etiquetados en el mismo orden; sumador = círculo con signos +/−;
flechas con punta indicando el sentido; lazo de realimentación desde la salida
hacia el sumador con su bloque (H). Conserva el recorrido de las señales.

### Mapa de Karnaugh / tablas
Rejilla con el mismo número de casillas y el mismo orden de código Gray; valores
0/1 en las mismas posiciones; agrupaciones marcadas con rectángulos redondeados.

## Figuras de la SOLUCIÓN (nuevas, no del enunciado)
Aunque no existan en el examen, se construyen con el mismo rigor: por ejemplo,
los diagramas de esfuerzo cortante y momento flector deben ser coherentes con
las reacciones calculadas (saltos del cortante en cada carga, momento máximo en
el valor correcto y en la posición correcta). Verifícalos también con `svg_to_png.js`.

## Cuándo conservar la imagen original en vez de redibujar
Si una figura es una fotografía o un esquema muy complejo difícil de vectorizar
con fidelidad, es preferible **incrustar la imagen original** (extraída con
`extract_figures.py`, guardada junto al dashboard y referenciada con `<img>`)
antes que ofrecer un SVG impreciso. Un diagrama fiel en mapa de bits es mejor
que un vector engañoso. En ese caso, avisa al usuario de la decisión.
