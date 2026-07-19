#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JSON del examen UCLM 2025 · Extraordinaria (curso 2024/25). 4 ejercicios."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, txt, line, arrow
from cyllib import gate, INK, MUT, ACC, OK, ROSE, VIOL, CURVE
from build_clm_2024_ordinaria import _and_inputs


def fig_xor_nand():
    """S = B ⊕ D con 4 puertas NAND de 2 entradas."""
    s = svg_open('560 250', 540)
    s += txt(20, 60, 'B', INK, 15)
    s += txt(20, 180, 'D', INK, 15)
    s += line(30, 55, 80, 55) + "<circle cx='80' cy='55' r='3' fill='#cbd5e1'/>"
    s += line(30, 175, 80, 175) + "<circle cx='80' cy='175' r='3' fill='#cbd5e1'/>"
    # N1 = NAND(B,D)
    n1, (o1x, o1y) = gate(150, 85, 'NAND', w=54, h=52)
    s += line(80, 55, 80, 98) + line(80, 98, 150, 98)
    s += line(80, 175, 80, 124) + line(80, 124, 150, 124)
    s += n1
    # N2 = NAND(B, N1)
    n2, (o2x, o2y) = gate(300, 40, 'NAND', w=54, h=48)
    s += line(80, 55, 270, 55) + line(270, 55, 270, 52) + line(270, 52, 300, 52)
    s += line(o1x, o1y, 270, 111) + line(270, 111, 270, 76) + line(270, 76, 300, 76)
    s += n2
    # N3 = NAND(N1, D)
    n3, (o3x, o3y) = gate(300, 150, 'NAND', w=54, h=48)
    s += line(o1x, o1y, 250, 111) + line(250, 111, 250, 162) + line(250, 162, 300, 162)
    s += line(80, 175, 285, 175) + line(285, 175, 285, 186) + line(285, 186, 300, 186)
    s += n3
    # N4 = NAND(N2, N3) = S
    n4, (o4x, o4y) = gate(430, 85, 'NAND', w=56, h=52)
    s += line(o2x, o2y, 400, o2y) + line(400, o2y, 400, 99) + line(400, 99, 430, 99)
    s += line(o3x, o3y, 400, o3y) + line(400, o3y, 400, 123) + line(400, 123, 430, 123)
    s += n4
    s += arrow(o4x, o4y, o4x + 40, o4y)
    s += txt(o4x + 48, o4y + 5, 'S', OK, 16)
    return s + "</svg>"


def fig_gates_1b():
    """S = A·B + C̄ con una AND, un inversor y una OR."""
    s = svg_open('470 210', 460)
    s += txt(20, 50, 'A', INK, 15)
    s += txt(20, 90, 'B', INK, 15)
    s += txt(20, 155, 'C', INK, 15)
    a1, (ax, ay) = gate(160, 25, 'AND', w=56, h=48)
    s += line(34, 45, 160, 40) + line(34, 85, 160, 66)
    s += a1
    nc, (ncx, ncy) = gate(150, 138, 'NOT', w=38, h=28)
    s += line(34, 152, 150, 152) + nc
    s += txt(ncx + 30, ncy + 5, 'C̄', VIOL, 13)
    orf, (ox, oy) = gate(300, 55, 'OR', w=58, h=90)
    s += line(ax, ay, 300, 82)
    s += line(ncx, ncy, 270, ncy) + line(270, ncy, 270, 128) + line(270, 128, 300, 128)
    s += orf
    s += arrow(ox, oy, ox + 40, oy)
    s += txt(ox + 48, oy + 5, 'S', OK, 16)
    return s + "</svg>"


def fig_bloques_2a():
    """Diagrama de bloques G1-G2-G3 con realimentaciones H1, H2, H3 (todas desde C)."""
    s = svg_open('700 300', 680)
    ym = 140
    # cadena directa
    s += txt(20, ym + 5, 'E', INK, 15)
    s += arrow(32, ym, 55, ym)
    s += summer(72, ym)
    s += txt(56, ym - 14, '+', OK, 14) + txt(56, ym + 30, '−', ROSE, 16)
    s += arrow(88, ym, 128, ym)
    s += box(128, ym - 18, 66, 36, 'G<tspan dy="4" font-size="11">1</tspan>', CURVE, 15)
    s += arrow(194, ym, 226, ym)
    s += summer(244, ym)
    s += txt(228, ym - 14, '+', OK, 14) + txt(228, ym + 30, '−', ROSE, 16)
    s += arrow(260, ym, 300, ym)
    s += box(300, ym - 18, 66, 36, 'G<tspan dy="4" font-size="11">2</tspan>', CURVE, 15)
    s += arrow(366, ym, 398, ym)
    s += summer(416, ym)
    s += txt(400, ym - 14, '+', OK, 14) + txt(400, ym + 30, '−', ROSE, 16)
    s += arrow(432, ym, 472, ym)
    s += box(472, ym - 18, 66, 36, 'G<tspan dy="4" font-size="11">3</tspan>', CURVE, 15)
    s += line(538, ym, 600, ym) + "<circle cx='600' cy='140' r='3.2' fill='#cbd5e1'/>"
    s += arrow(600, ym, 650, ym) + txt(660, ym + 5, 'C', INK, 15)
    # H3 (arriba) desde C hasta sum3
    s += line(600, ym, 600, 52) + arrow(600, 52, 512, 52)
    s += box(438, 35, 66, 34, 'H<tspan dy="4" font-size="11">3</tspan>', VIOL, 15)
    s += line(438, 52, 416, 52) + arrow(416, 52, 416, ym - 16)
    # H1 desde C hasta sum2
    s += line(600, ym, 600, 214) + arrow(600, 214, 430, 214)
    s += box(364, 197, 66, 34, 'H<tspan dy="4" font-size="11">1</tspan>', VIOL, 15)
    s += line(364, 214, 244, 214) + arrow(244, 214, 244, ym + 16)
    # H2 desde C hasta sum1
    s += line(600, ym, 600, 258) + arrow(600, 258, 214, 258)
    s += box(148, 241, 66, 34, 'H<tspan dy="4" font-size="11">2</tspan>', VIOL, 15)
    s += line(148, 258, 72, 258) + arrow(72, 258, 72, ym + 16)
    return s + "</svg>"


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · UCLM (Castilla-La Mancha) · Extraordinaria 2025 (curso 2024/25) · Examen resuelto",
  "cabecera_titulo": "PAU 2025 · <span>Tecnología e Ingeniería II</span> · UCLM · Extraordinaria",
  "pill": "4 ejercicios · 2,5 pt cada uno · 90 min",
  "enunciado_pdf": "../../examens/UCLM/TECNOLOGIA24_25_e.pdf",
  "pdf_dir": "pdf_clm_2025_extraordinaria",
  "footer": "Solucionario PAU · UCLM (Castilla-La Mancha) · Tecnología e Ingeniería II (Extraordinaria 2025)",
  "intro_inicio": "La prueba consta de <b>4 ejercicios</b> de 2,5 puntos. En los ejercicios <b>1, 2 y 3</b> se elige una de las dos opciones (a o b); el <b>ejercicio 4</b> es obligatorio. Aquí se resuelven <b>todas</b> las opciones, con el enunciado oficial, los conceptos aplicados y la solución paso a paso.",
  "indice_nombre": "Exámenes de Castilla-La Mancha",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Ejercicio 1 · Sistemas digitales", "color": "#a78bfa",
   "descripcion_tarjeta": "Simplificación de una tabla de verdad con Karnaugh e implementación NAND; simplificación algebraica.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M22 18 h14 a12 12 0 0 1 0 24 h-14 z'/><path d='M8 24h14M8 36h14M60 30h14'/><circle cx='78' cy='30' r='3'/></svg>",
   "cuestiones": [
    {
     "id": "q1a", "titulo": "Opción a · Karnaugh e implementación NAND", "etiqueta": "DIGITAL",
     "menu": "1a · Karnaugh y NAND", "titulo_corto": "1a",
     "meta": "Opción a · 2,5 puntos (a 1,25 · b 1,25)",
     "enunciado_html": "<p>Partiendo de la tabla de verdad mostrada, donde A, B, C y D son entradas y S la salida, se pide:</p><ol type='a'><li>Simplificar la función al máximo mediante el mapa de Karnaugh. <span class='pts'>(1,25 puntos)</span></li><li>Implementar el circuito utilizando solo puertas <b>NAND</b>. <span class='pts'>(1,25 puntos)</span></li></ol>"
       "<table class='dat'><thead><tr><th>A</th><th>B</th><th>C</th><th>D</th><th>S</th></tr></thead><tbody>"
       "<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr>"
       "</tbody></table>",
     "aplica_html": "<p>Se vuelca la tabla en un <b>mapa de Karnaugh</b> 4×4 (columnas AB, filas CD en código Gray) y se agrupan los unos. El resultado se implementa con <b>NAND</b> aplicando doble negación.</p>",
     "solucion_html":
       "<h5>a) Simplificación por Karnaugh</h5>"
       "<table class='dat'><thead><tr><th>CD\\AB</th><th>00</th><th>01</th><th>11</th><th>10</th></tr></thead><tbody>"
       "<tr><td><b>00</b></td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td><b>01</b></td><td>1</td><td>0</td><td>0</td><td>1</td></tr>"
       "<tr><td><b>11</b></td><td>1</td><td>0</td><td>0</td><td>1</td></tr>"
       "<tr><td><b>10</b></td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "</tbody></table>"
       "<p>Los unos forman dos grupos de cuatro: <b>B̄·D</b> (B = 0 y D = 1) y <b>B·D̄</b> (B = 1 y D = 0). Es la función <b>OR-exclusiva</b> de B y D:</p>"
       "<div class='formula'>$$\\boxed{\\ S=\\bar B\\,D+B\\,\\bar D=B\\oplus D\\ }$$</div>"
       "<h5>b) Implementación con puertas NAND</h5>"
       "<p>La función XOR se implementa con <b>4 puertas NAND</b> de dos entradas:</p>"
       "<div class='formula'>$$N_1=\\overline{B\\,D},\\quad S=\\overline{\\overline{B\\,N_1}\\cdot\\overline{N_1\\,D}}=B\\oplus D$$</div>"
       "<figure class='fig'>" + fig_xor_nand() + "<figcaption>S = B ⊕ D implementada con 4 puertas NAND de dos entradas.</figcaption></figure>"
       "<div class='res'><b>S = B ⊕ D = NAND( NAND(B, N₁), NAND(N₁, D) ), con N₁ = NAND(B, D)</b></div>"
    },
    {
     "id": "q1b", "titulo": "Opción b · Simplificación algebraica", "etiqueta": "DIGITAL",
     "menu": "1b · Simplificación y circuito", "titulo_corto": "1b",
     "meta": "Opción b · 2,5 puntos (a 1,25 · b 0,75 · c 0,5)",
     "enunciado_html": "<p>Partiendo de la expresión lógica:</p><div class='formula'>$$S=AB+A\\bar C+\\bar A\\bar C+\\bar B\\bar C$$</div><p>Obtener:</p><ol type='a'><li>La tabla de verdad que representa la función lógica. Expresa la función en la 1ª forma canónica. <span class='pts'>(1,25 puntos)</span></li><li>La expresión lógica simplificada al máximo. <span class='pts'>(0,75 puntos)</span></li><li>El circuito implementado con puertas lógicas. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>Se evalúa la función para las 8 combinaciones (A, B, C). La <b>1ª forma canónica</b> es la suma de minterms (filas con S = 1). Se simplifica con álgebra de Boole sacando factor común.</p>",
     "solucion_html":
       "<h5>a) Tabla de verdad y 1ª forma canónica</h5>"
       "<table class='dat'><thead><tr><th>A</th><th>B</th><th>C</th><th>S</th></tr></thead><tbody>"
       "<tr><td>0</td><td>0</td><td>0</td><td>1</td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>1</td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "</tbody></table>"
       "<div class='formula'>$$S=\\sum m(0,2,4,6,7)=\\bar A\\bar B\\bar C+\\bar A B\\bar C+A\\bar B\\bar C+A B\\bar C+A B C$$</div>"
       "<h5>b) Simplificación algebraica</h5>"
       "<p>Agrupando: \\(A\\bar C+\\bar A\\bar C=\\bar C\\); y \\(\\bar C+\\bar B\\bar C=\\bar C\\). Queda:</p>"
       "<div class='formula'>$$S=AB+A\\bar C+\\bar A\\bar C+\\bar B\\bar C=AB+\\bar C\\;\\Rightarrow\\;\\boxed{\\ S=AB+\\bar C\\ }$$</div>"
       "<h5>c) Circuito con puertas lógicas</h5>"
       "<figure class='fig'>" + fig_gates_1b() + "<figcaption>S = A·B + C̄ con una AND, un inversor y una OR.</figcaption></figure>"
       "<div class='res'><b>S = A·B + C̄</b></div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Ejercicio 2 · Sistemas de control", "color": "#22d3ee",
   "descripcion_tarjeta": "Función de transferencia de un sistema con tres lazos de realimentación y análisis de estabilidad.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><rect x='34' y='22' width='24' height='16' rx='3'/><path d='M8 30h26M58 30h24'/><circle cx='20' cy='30' r='6'/></svg>",
   "cuestiones": [
    {
     "id": "q2a", "titulo": "Opción a · Función de transferencia", "etiqueta": "CONTROL",
     "menu": "2a · Función de transferencia", "titulo_corto": "2a",
     "meta": "Opción a · 2,5 puntos",
     "enunciado_html": "<p>Obtener la función de transferencia del sistema de control que representa el siguiente diagrama de bloques:</p>",
     "figura_enunciado_svg": fig_bloques_2a(),
     "aplica_html": "<p>Con tres bloques en cascada (G₁, G₂, G₃) y tres realimentaciones negativas tomadas de la salida C (H₃ al 3.er sumador, H₁ al 2.º y H₂ al 1.º), se plantean las ecuaciones de cada sumador y se despeja C/E.</p>",
     "solucion_html":
       "<h5>Ecuaciones de los sumadores</h5>"
       "<div class='formula'>$$e_1=E-H_2C,\\quad e_2=G_1e_1-H_1C,\\quad e_3=G_2e_2-H_3C,\\quad C=G_3e_3$$</div>"
       "<h5>Sustitución y despeje</h5>"
       "<p>Sustituyendo hacia atrás:</p>"
       "<div class='formula'>$$C=G_3\\big(G_2e_2-H_3C\\big)\\;\\Rightarrow\\; C(1+G_3H_3)=G_2G_3\\,e_2$$</div>"
       "<div class='formula'>$$e_2=G_1(E-H_2C)-H_1C=G_1E-(G_1H_2+H_1)C$$</div>"
       "<div class='formula'>$$C\\big[1+G_3H_3+G_2G_3H_1+G_1G_2G_3H_2\\big]=G_1G_2G_3\\,E$$</div>"
       "<div class='formula'>$$\\boxed{\\ \\dfrac{C}{E}=\\dfrac{G_1G_2G_3}{1+G_3H_3+G_2G_3H_1+G_1G_2G_3H_2}\\ }$$</div>"
       "<div class='res'><b>C/E = G₁G₂G₃ / (1 + G₃H₃ + G₂G₃H₁ + G₁G₂G₃H₂)</b></div>"
    },
    {
     "id": "q2b", "titulo": "Opción b · Estabilidad (ecuación característica)", "etiqueta": "CONTROL",
     "menu": "2b · Estabilidad", "titulo_corto": "2b",
     "meta": "Opción b · 2,5 puntos (a 1,25 · b 1,25)",
     "enunciado_html": "<p>Responde:</p><ol type='a'><li>Define el concepto de función de transferencia en un sistema de control. ¿Qué es la ecuación característica? ¿Cuándo un sistema es estable atendiendo a las raíces de la ecuación característica? <span class='pts'>(1,25 puntos)</span></li><li>Averigua si el sistema de control representado por la siguiente función de transferencia es estable:</li></ol><div class='formula'>$$F(s)=\\dfrac{s}{(s+3)(s^2+6s+25)}$$</div>",
     "aplica_html": "<p>La <b>función de transferencia</b> relaciona la salida y la entrada de un sistema en el dominio de Laplace. La <b>ecuación característica</b> es el denominador igualado a cero; sus raíces son los <b>polos</b>. El sistema es estable si todos los polos tienen <b>parte real negativa</b>.</p>",
     "solucion_html":
       "<h5>a) Conceptos</h5>"
       "<p><b>Función de transferencia:</b> cociente entre la transformada de Laplace de la salida y la de la entrada (con condiciones iniciales nulas), \\(F(s)=\\dfrac{C(s)}{R(s)}\\).</p>"
       "<p><b>Ecuación característica:</b> es el <b>denominador</b> de la función de transferencia igualado a cero. Sus raíces son los <b>polos</b> del sistema.</p>"
       "<p><b>Estabilidad:</b> el sistema es estable si <b>todas</b> las raíces de la ecuación característica tienen <b>parte real negativa</b> (polos en el semiplano izquierdo).</p>"
       "<h5>b) Estabilidad de F(s)</h5>"
       "<p>La ecuación característica es \\((s+3)(s^2+6s+25)=0\\). Sus raíces:</p>"
       "<div class='formula'>$$s_1=-3,\\qquad s_{2,3}=\\dfrac{-6\\pm\\sqrt{36-100}}{2}=-3\\pm 4j$$</div>"
       "<p>Los tres polos (−3 y −3 ± 4j) tienen <b>parte real negativa</b>:</p>"
       "<div class='res'><b>El sistema es ESTABLE</b> (todos los polos en el semiplano izquierdo).</div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Ejercicio 3 · Resistencia de materiales", "color": "#f59e0b",
   "descripcion_tarjeta": "Comportamiento elástico de una varilla de acero y diámetro mínimo de una barra de aluminio.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><path d='M20 12v36M20 30h50'/><path d='M62 22 L70 30 62 38'/></svg>",
   "cuestiones": [
    {
     "id": "q3a", "titulo": "Opción a · Varilla de acero", "etiqueta": "MATERIALES",
     "menu": "3a · Varilla de acero", "titulo_corto": "3a",
     "meta": "Opción a · 2,5 puntos (a 1 · b 0,75 · c 0,75)",
     "enunciado_html": "<p>Una varilla de acero estructural con una sección transversal de <b>20 mm²</b> está fijada en un extremo a un soporte rígido y sostiene una carga de <b>5000 N</b> en el otro. El material tiene un módulo de elasticidad de <b>110 GPa</b> y un límite elástico de <b>300 MPa</b>.</p><ol type='a'><li>Si se retira la carga, ¿la varilla recuperará su longitud original? Justifica la respuesta. <span class='pts'>(1 punto)</span></li><li>¿Cuál es la máxima carga que puede soportar la varilla sin sufrir deformación permanente? <span class='pts'>(0,75 puntos)</span></li><li>¿Cuál es el máximo alargamiento unitario que puede experimentar la varilla sin deformación permanente? <span class='pts'>(0,75 puntos)</span></li></ol>",
     "aplica_html": "<p>La tensión es \\(\\sigma=F/S\\). Si \\(\\sigma<\\sigma_e\\) (límite elástico) la deformación es <b>elástica</b> y reversible. La carga máxima sin deformación permanente es \\(F_{max}=\\sigma_e\\,S\\) y el alargamiento unitario máximo \\(\\varepsilon_{max}=\\sigma_e/E\\) (ley de Hooke).</p>",
     "solucion_html":
       "<h5>a) ¿Recupera la longitud original?</h5>"
       "<div class='formula'>$$\\sigma=\\dfrac{F}{S}=\\dfrac{5000\\ \\mathrm{N}}{20\\cdot10^{-6}\\ \\mathrm{m^2}}=250\\cdot10^{6}\\ \\mathrm{Pa}=250\\ \\mathrm{MPa}$$</div>"
       "<p>Como \\(\\sigma=250\\ \\mathrm{MPa}<\\sigma_e=300\\ \\mathrm{MPa}\\), la varilla trabaja en la <b>zona elástica</b>.</p>"
       "<div class='res'><b>Sí: al retirar la carga recupera su longitud original (deformación elástica).</b></div>"
       "<h5>b) Carga máxima sin deformación permanente</h5>"
       "<div class='formula'>$$F_{max}=\\sigma_e\\,S=300\\cdot10^{6}\\cdot 20\\cdot10^{-6}=6000\\ \\mathrm{N}$$</div>"
       "<div class='res'><b>F<sub>max</sub> = 6000 N</b></div>"
       "<h5>c) Alargamiento unitario máximo</h5>"
       "<div class='formula'>$$\\varepsilon_{max}=\\dfrac{\\sigma_e}{E}=\\dfrac{300\\cdot10^{6}}{110\\cdot10^{9}}=2{,}73\\cdot10^{-3}$$</div>"
       "<div class='res'><b>ε<sub>max</sub> = 2,73·10⁻³ = 0,273 %</b></div>"
    },
    {
     "id": "q3b", "titulo": "Opción b · Barra de aluminio", "etiqueta": "MATERIALES",
     "menu": "3b · Barra de aluminio", "titulo_corto": "3b",
     "meta": "Opción b · 2,5 puntos",
     "enunciado_html": "<p>Una barra cilíndrica de aluminio está sometida a una fuerza de tracción de <b>6200 kp</b>. Si su límite elástico es de <b>2800 kp/cm²</b>, su longitud es <b>350 mm</b> y su módulo de elasticidad es <b>0,7·10⁶ kp/cm²</b>, determina el diámetro mínimo que debe tener la barra para que su alargamiento no supere <b>0,30 mm</b>.</p>",
     "aplica_html": "<p>El alargamiento es \\(\\Delta L=\\dfrac{F\\,L}{E\\,S}\\). Imponiendo \\(\\Delta L\\le 0{,}30\\ \\mathrm{mm}\\) se obtiene la sección mínima y, de ella, el diámetro \\(d=\\sqrt{4S/\\pi}\\). Conviene trabajar en cm.</p>",
     "solucion_html":
       "<h5>Sección mínima a partir del alargamiento</h5>"
       "<p>La tensión máxima admisible por el alargamiento (L = 35 cm, ΔL = 0,03 cm):</p>"
       "<div class='formula'>$$\\sigma=E\\,\\dfrac{\\Delta L}{L}=0{,}7\\cdot10^{6}\\cdot\\dfrac{0{,}03}{35}=600\\ \\mathrm{kp/cm^2}$$</div>"
       "<p>Es menor que el límite elástico (2800 kp/cm²), así que manda el alargamiento. La sección:</p>"
       "<div class='formula'>$$S=\\dfrac{F}{\\sigma}=\\dfrac{6200}{600}=10{,}33\\ \\mathrm{cm^2}$$</div>"
       "<h5>Diámetro mínimo</h5>"
       "<div class='formula'>$$d=\\sqrt{\\dfrac{4S}{\\pi}}=\\sqrt{\\dfrac{4\\cdot 10{,}33}{\\pi}}=3{,}63\\ \\mathrm{cm}$$</div>"
       "<div class='res'><b>d<sub>mín</sub> ≈ 3,63 cm = 36,3 mm</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Ejercicio 4 · Planta termoeléctrica", "color": "#fb7185",
   "descripcion_tarjeta": "Rendimiento de Carnot de una central: temperatura de la caldera, calor absorbido y energía útil.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#fb7185' stroke-width='3'><circle cx='45' cy='30' r='16'/><path d='M45 14v-8M45 54v-8M61 30h8M13 30h8'/></svg>",
   "cuestiones": [
    {
     "id": "q4", "titulo": "Ejercicio 4 · Planta termoeléctrica (Carnot)", "etiqueta": "TERMODINÁMICA",
     "menu": "E4 · Planta termoeléctrica", "titulo_corto": "E4",
     "meta": "Obligatorio · 2,5 puntos (a 1 · b 1 · c 0,5)",
     "enunciado_html": "<p>Una planta termoeléctrica opera con vapor de agua. Extrae calor de la combustión de gas natural en una caldera y convierte parte en electricidad mediante una turbina. El rendimiento de la planta es del <b>30 %</b> y el calor residual se disipa en un río a <b>25 ºC</b>. En cada ciclo la planta libera <b>500 MJ</b> de calor al río. Suponiendo que opera cerca del límite de Carnot, determina:</p><ol type='a'><li>La temperatura de la caldera (foco caliente) en ºC. <span class='pts'>(1 punto)</span></li><li>La cantidad de calor absorbida por la planta en cada ciclo. <span class='pts'>(1 punto)</span></li><li>La cantidad de energía útil convertida en electricidad por ciclo. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>El rendimiento de Carnot es \\(\\eta=1-\\dfrac{T_2}{T_1}\\), con T en kelvin. El balance de una máquina térmica: \\(Q_1=Q_2+W\\), \\(\\eta=\\dfrac{W}{Q_1}\\), y \\(Q_2=Q_1(1-\\eta)\\). Aquí Q₂ = 500 MJ (cedido al río) y T₂ = 25 ºC = 298 K.</p>",
     "solucion_html":
       "<h5>a) Temperatura de la caldera</h5>"
       "<p>De \\(\\eta=1-\\dfrac{T_2}{T_1}\\) con η = 0,30 y T₂ = 298 K:</p>"
       "<div class='formula'>$$T_1=\\dfrac{T_2}{1-\\eta}=\\dfrac{298}{1-0{,}30}=425{,}7\\ \\mathrm{K}=152{,}6\\ ^\\circ\\mathrm{C}$$</div>"
       "<div class='res'><b>T<sub>1</sub> ≈ 425,7 K ≈ 152,6 ºC</b></div>"
       "<h5>b) Calor absorbido por ciclo</h5>"
       "<p>El calor cedido al río es \\(Q_2=Q_1(1-\\eta)\\):</p>"
       "<div class='formula'>$$Q_1=\\dfrac{Q_2}{1-\\eta}=\\dfrac{500}{1-0{,}30}=714{,}3\\ \\mathrm{MJ}$$</div>"
       "<div class='res'><b>Q<sub>1</sub> ≈ 714,3 MJ</b></div>"
       "<h5>c) Energía útil (electricidad) por ciclo</h5>"
       "<div class='formula'>$$W=\\eta\\,Q_1=0{,}30\\cdot 714{,}3=214{,}3\\ \\mathrm{MJ}\\quad(=Q_1-Q_2)$$</div>"
       "<div class='res'><b>W ≈ 214,3 MJ por ciclo</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "clm_2025_extraordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
