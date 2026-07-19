#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JSON del examen UCLM 2025 · Ordinaria (curso 2024/25). 4 ejercicios."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, txt, line, arrow
from cyllib import (Plot, beam, diagram_VM, gate, power_triangle,
                    INK, MUT, ACC, OK, ROSE, VIOL, AMBER, CURVE, GRID)
from build_clm_2024_ordinaria import _and_inputs


# --------------------------------------------------------------------------
def fig_stress_strain():
    """Curva tensión-deformación típica de un metal dúctil con sus zonas."""
    p = Plot((0, 14), (0, 520), w=540, h=350, xlabel='ε (deformación)',
             ylabel='σ (tensión)', maxw=520, pl=46, pb=44)
    p.axes(xticks=[], yticks=[], grid=False)
    pts = [(0, 0), (1.6, 320), (2.1, 330), (2.6, 328), (4, 380),
           (8, 470), (10.5, 450), (12, 360)]
    p.polyline(pts, color=CURVE, width=3)
    # límites y puntos notables
    p.point(1.6, 320, 'Límite elástico (Re)', color=ACC, dx=8, dy=22, anchor='start')
    p.point(8, 470, 'Resistencia máxima (Rm)', color=ROSE, dx=6, dy=22, anchor='middle')
    p.point(12, 360, 'Rotura', color=AMBER, dx=6, dy=6)
    # separadores de zonas
    for xv in (1.6, 2.6, 8):
        p.vline(xv, 0, 520, color=GRID, dash='4 4')
    p.text(0.8, 500, 'Elástica', color=MUT, fs=11.5)
    p.text(2.1, 500, 'Fluencia', color=MUT, fs=10.5)
    p.text(5.2, 500, 'Plástica (endurecimiento)', color=MUT, fs=11)
    p.text(10.8, 500, 'Estricción', color=MUT, fs=11)
    return p.close()


def fig_beam_ap_2a():
    return beam(
        [{'type': 'P', 'xm': 3, 'val': 'F₁ = 15 kN'}, {'type': 'P', 'xm': 9, 'val': 'F₂ = 20 kN'}],
        [{'xm': 0, 'kind': 'pin', 'label': 'A'}, {'xm': 12, 'kind': 'roller', 'label': 'B'}],
        span_m=12, dims=[(0, 3, 'd₁ = 3 m'), (3, 9, 'd₂ = 6 m'), (9, 12, 'd₃ = 3 m')],
        w=560, h=210, maxw=520)


def fig_V_2a():
    return diagram_VM([(0, 16.25), (3, 16.25), (3, 1.25), (9, 1.25), (9, -18.75),
                       (12, -18.75), (12, 0)], span_m=12, kind='V', unit='kN',
                      title='Esfuerzo cortante V', w=540, h=200, maxw=500)


def fig_M_2a():
    return diagram_VM([(0, 0), (3, 48.75), (9, 56.25), (12, 0)], span_m=12, kind='M',
                      unit='kN·m', title='Momento flector M', w=540, h=200, maxw=500)


def fig_beam_vol_2b():
    return beam(
        [{'type': 'P', 'xm': 4, 'val': 'F = 50 kN'}],
        [{'xm': 0, 'kind': 'fixed', 'side': 'left', 'label': 'A'}],
        span_m=7, dims=[(0, 4, 'd₁ = 4 m'), (4, 7, 'd₂ = 3 m')],
        w=560, h=205, maxw=520)


def fig_V_2b():
    return diagram_VM([(0, 50), (4, 50), (4, 0), (7, 0)], span_m=7, kind='V',
                      unit='kN', title='Esfuerzo cortante V', w=520, h=190, maxw=480)


def fig_M_2b():
    return diagram_VM([(0, -200), (4, 0), (7, 0)], span_m=7, kind='M',
                      unit='kN·m', title='Momento flector M', w=520, h=190, maxw=480)


def fig_imp_triangle():
    return power_triangle(100, 175.47, 201.97, 60.32, w=460, h=280, maxw=440,
                          labels={'P': 'R = 100 Ω', 'Q': 'X = 175,5 Ω', 'S': 'Z = 202 Ω'})


def fig_volt_triangle():
    return power_triangle(54.46, 95.56, 110, 60.32, w=460, h=280, maxw=440,
                          labels={'P': 'V_R = 54,5 V', 'Q': 'V_X = 95,6 V', 'S': 'V = 110 V'})


def fig_power_triangle_3b():
    return power_triangle(467.9, 727.9, 865.3, 57.26, w=460, h=280, maxw=440,
                          labels={'P': 'P = 468 W', 'Q': 'Q = 728 VAr', 'S': 'S = 865 VA'})


def fig_nand_e4():
    """S = A·B + C·D + B·D con 3 NAND de 2 entradas y una NAND de 3 entradas."""
    s = svg_open('560 320', 540)
    n1, (o1x, o1y) = gate(150, 25, 'NAND', w=56, h=52)
    s = _and_inputs(s, 150, o1y, ['A', 'B'])
    s += n1
    n2, (o2x, o2y) = gate(150, 135, 'NAND', w=56, h=52)
    s = _and_inputs(s, 150, o2y, ['C', 'D'])
    s += n2
    n3, (o3x, o3y) = gate(150, 245, 'NAND', w=56, h=52)
    s = _and_inputs(s, 150, o3y, ['B', 'D'])
    s += n3
    n4, (o4x, o4y) = gate(380, 110, 'NAND', w=64, h=130)
    yt, ym, yb = 110+35, 110+65, 110+95
    s += line(o1x, o1y, 360, o1y) + line(360, o1y, 360, yt) + line(360, yt, 380, yt)
    s += line(o2x, o2y, 380, ym)
    s += line(o3x, o3y, 360, o3y) + line(360, o3y, 360, yb) + line(360, yb, 380, yb)
    s += n4
    s += arrow(o4x, o4y, o4x + 40, o4y)
    s += txt(o4x + 48, o4y + 5, 'S', OK, 16)
    return s + "</svg>"


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · UCLM (Castilla-La Mancha) · Ordinaria 2025 (curso 2024/25) · Examen resuelto",
  "cabecera_titulo": "PAU 2025 · <span>Tecnología e Ingeniería II</span> · UCLM · Ordinaria",
  "pill": "4 ejercicios · 2,5 pt cada uno · 90 min",
  "enunciado_pdf": "../../examens/UCLM/TECNOLOGIA24_25.pdf",
  "pdf_dir": "pdf_clm_2025_ordinaria",
  "footer": "Solucionario PAU · UCLM (Castilla-La Mancha) · Tecnología e Ingeniería II (Ordinaria 2025)",
  "intro_inicio": "La prueba consta de <b>4 ejercicios</b> de 2,5 puntos. En los ejercicios <b>1, 2 y 3</b> se elige una de las dos opciones (a o b); el <b>ejercicio 4</b> es obligatorio. Aquí se resuelven <b>todas</b> las opciones, con el enunciado oficial, los conceptos aplicados y la solución paso a paso.",
  "indice_nombre": "Exámenes de Castilla-La Mancha",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Ejercicio 1 · Ensayos de materiales", "color": "#f59e0b",
   "descripcion_tarjeta": "Dureza Brinell de un acero al carbono y ensayo de tracción.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><path d='M12 46 C30 18 60 18 78 46'/><circle cx='45' cy='26' r='4' fill='#f59e0b' stroke='none'/></svg>",
   "cuestiones": [
    {
     "id": "q1a", "titulo": "Opción a · Dureza Brinell (acero)", "etiqueta": "MATERIALES",
     "menu": "1a · Dureza Brinell", "titulo_corto": "1a",
     "meta": "Opción a · 2,5 puntos (a 1 · b 1 · c 0,5)",
     "enunciado_html": "<p>Se desea determinar la dureza de una pieza de acero al carbono mediante un ensayo de dureza <b>Brinell</b>. Se aplica una carga de <b>1200 kp</b>, generando una huella de diámetro <b>5,0 mm</b>. Responde:</p><ol type='a'><li>Determina el diámetro de la bola de ensayo, considerando que el acero al carbono tiene una constante <b>K = 12 kp/mm²</b>. <span class='pts'>(1 punto)</span></li><li>¿Cuál es la dureza Brinell (HB) de la pieza de acero? <span class='pts'>(1 punto)</span></li><li>Sabiendo que el tiempo de aplicación de la carga fue de <b>25 s</b>, escribe la expresión normalizada de la dureza Brinell. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>La <b>constante del ensayo</b> relaciona la carga con el cuadrado del diámetro de la bola: \\(F=K\\,D^2\\). La <b>dureza Brinell</b> es la carga entre la superficie del casquete de la huella: \\(HB=\\dfrac{2F}{\\pi D\\left(D-\\sqrt{D^2-d^2}\\right)}\\), con d el diámetro de la huella.</p>",
     "solucion_html":
       "<h5>a) Diámetro de la bola</h5>"
       "<p>De \\(F=K\\,D^2\\) despejamos el diámetro de la bola:</p>"
       "<div class='formula'>$$D=\\sqrt{\\dfrac{F}{K}}=\\sqrt{\\dfrac{1200}{12}}=\\sqrt{100}$$</div>"
       "<div class='res'><b>D = 10 mm</b></div>"
       "<h5>b) Dureza Brinell</h5>"
       "<p>La profundidad de la huella es \\(f=\\dfrac{D-\\sqrt{D^2-d^2}}{2}=\\dfrac{10-\\sqrt{100-25}}{2}=0{,}67\\ \\mathrm{mm}\\). Entonces:</p>"
       "<div class='formula'>$$HB=\\dfrac{F}{\\pi D f}=\\dfrac{2F}{\\pi D\\left(D-\\sqrt{D^2-d^2}\\right)}=\\dfrac{2\\cdot 1200}{\\pi\\cdot 10\\cdot(10-\\sqrt{75})}$$</div>"
       "<div class='res'><b>HB ≈ 57 kp/mm²</b></div>"
       "<h5>c) Expresión normalizada</h5>"
       "<p>Con D = 10 mm, F = 1200 kp y t = 25 s:</p>"
       "<div class='res'><b>57 HB 10 1200 25</b></div>"
    },
    {
     "id": "q1b", "titulo": "Opción b · Ensayo de tracción", "etiqueta": "MATERIALES",
     "menu": "1b · Ensayo de tracción", "titulo_corto": "1b",
     "meta": "Opción b · 2,5 puntos (a 0,5 · b 1 · c 1)",
     "enunciado_html": "<p>Responde a las siguientes cuestiones sobre el <b>ensayo de tracción</b>:</p><ol type='a'><li>Explica en qué consiste el ensayo de tracción. <span class='pts'>(0,5 puntos)</span></li><li>Dibuja el diagrama esfuerzo-deformación típico de un metal indicando las zonas que se distinguen en él. <span class='pts'>(1 punto)</span></li><li>Explica el comportamiento del metal en cada zona con sus datos más relevantes. <span class='pts'>(1 punto)</span></li></ol>",
     "aplica_html": "<p>El ensayo de tracción somete una probeta normalizada a una fuerza axial creciente hasta la rotura, registrando la <b>tensión</b> \\(\\sigma=F/S_0\\) frente a la <b>deformación</b> \\(\\varepsilon=\\Delta L/L_0\\). La curva resultante define las propiedades mecánicas del material.</p>",
     "solucion_html":
       "<h5>a) En qué consiste</h5>"
       "<p>Se coloca una <b>probeta normalizada</b> del material en una máquina universal de ensayos y se aplica una <b>fuerza axial de tracción</b> creciente hasta romperla. Se mide en todo momento la fuerza y el alargamiento, obteniendo la <b>tensión</b> \\(\\sigma=F/S_0\\) y la <b>deformación unitaria</b> \\(\\varepsilon=\\Delta L/L_0\\).</p>"
       "<h5>b) Diagrama esfuerzo-deformación</h5>"
       "<figure class='fig'>" + fig_stress_strain() + "<figcaption>Curva σ–ε de un metal dúctil: zona elástica, fluencia, zona plástica (endurecimiento) y estricción hasta la rotura.</figcaption></figure>"
       "<h5>c) Comportamiento por zonas</h5>"
       "<ul>"
       "<li><b>Zona elástica:</b> relación lineal entre σ y ε (ley de Hooke, \\(\\sigma=E\\,\\varepsilon\\)). Al retirar la carga la probeta recupera su forma. Termina en el <b>límite elástico (Re)</b>.</li>"
       "<li><b>Fluencia:</b> el material se deforma de forma apreciable sin apenas aumento de tensión (escalón de fluencia).</li>"
       "<li><b>Zona plástica (endurecimiento por deformación):</b> la deformación es permanente; la tensión vuelve a crecer hasta alcanzar la <b>resistencia máxima a tracción (Rm)</b>.</li>"
       "<li><b>Estricción:</b> la sección se reduce localmente (cuello); la tensión aparente baja hasta producirse la <b>rotura</b>.</li>"
       "</ul>"
       "<div class='res'><b>Datos clave: módulo de Young E (pendiente elástica), límite elástico Re, resistencia máxima Rm y alargamiento a rotura A (%).</b></div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Ejercicio 2 · Estructuras (vigas)", "color": "#4ade80",
   "descripcion_tarjeta": "Viga simplemente apoyada y viga en voladizo con diagramas de esfuerzos.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#4ade80' stroke-width='3'><rect x='12' y='26' width='66' height='10' rx='2'/><path d='M30 8 L30 24M60 8 L60 24'/><path d='M14 44 L22 36 30 44M60 44 L68 36 76 44'/></svg>",
   "cuestiones": [
    {
     "id": "q2a", "titulo": "Opción a · Viga simplemente apoyada", "etiqueta": "ESTRUCTURAS",
     "menu": "2a · Viga apoyada", "titulo_corto": "2a",
     "meta": "Opción a · 2,5 puntos (a 1 · b 1,5)",
     "enunciado_html": "<p>Se tiene la viga simplemente apoyada de la figura con las cargas puntuales <b>F₁ = 15 kN</b> y <b>F₂ = 20 kN</b> (d₁ = 3 m, d₂ = 6 m, d₃ = 3 m). Se pide:</p><ol type='a'><li>Las reacciones en los apoyos. <span class='pts'>(1 punto)</span></li><li>Cálculo y representación del diagrama de momento flector y esfuerzo cortante. <span class='pts'>(1,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": fig_beam_ap_2a(),
     "aplica_html": "<p>Con dos apoyos (fijo y móvil) hay dos reacciones verticales. Se obtienen con \\(\\sum M_A=0\\) y \\(\\sum F_y=0\\). Después, por tramos entre cargas, se calculan el cortante V y el flector M para representarlos.</p>",
     "solucion_html":
       "<h5>a) Reacciones en los apoyos</h5>"
       "<div class='formula'>$$\\sum M_A=F_1 d_1+F_2(d_1+d_2)-F_{By}(d_1+d_2+d_3)=0$$</div>"
       "<div class='formula'>$$F_{By}=\\dfrac{15\\cdot 3+20\\cdot 9}{12}=\\dfrac{225}{12}=18{,}75\\ \\mathrm{kN}$$</div>"
       "<div class='formula'>$$F_{Ay}=F_1+F_2-F_{By}=15+20-18{,}75=16{,}25\\ \\mathrm{kN}$$</div>"
       "<div class='res'><b>F<sub>Ay</sub> = 16,25 kN · F<sub>By</sub> = 18,75 kN</b></div>"
       "<h5>b) Diagramas de cortante y flector</h5>"
       "<p><b>Cortante:</b> \\(V=16{,}25\\) kN (tramo A–F₁); \\(16{,}25-15=1{,}25\\) kN (F₁–F₂); \\(1{,}25-20=-18{,}75\\) kN (F₂–B).</p>"
       "<p><b>Flector:</b> \\(M_{F_1}=16{,}25\\cdot 3=48{,}75\\) kN·m; \\(M_{F_2}=16{,}25\\cdot 9-15\\cdot 6=56{,}25\\) kN·m; nulo en los apoyos.</p>"
       "<figure class='fig'>" + fig_V_2a() + "<figcaption>Cortante: escalones en cada carga (16,25 → 1,25 → −18,75 kN).</figcaption></figure>"
       "<figure class='fig'>" + fig_M_2a() + "<figcaption>Flector: máximo de 56,25 kN·m bajo F₂.</figcaption></figure>"
       "<div class='res'><b>M<sub>máx</sub> = 56,25 kN·m (bajo F₂)</b></div>"
    },
    {
     "id": "q2b", "titulo": "Opción b · Viga en voladizo", "etiqueta": "ESTRUCTURAS",
     "menu": "2b · Viga en voladizo", "titulo_corto": "2b",
     "meta": "Opción b · 2,5 puntos (a 1 · b 1,5)",
     "enunciado_html": "<p>Se tiene la viga en voladizo de la figura con una carga puntual <b>F = 50 kN</b> (d₁ = 4 m, d₂ = 3 m). Se pide:</p><ol type='a'><li>Calcular las reacciones en el empotramiento. <span class='pts'>(1 punto)</span></li><li>Calcular y representar los diagramas del momento flector y esfuerzo cortante. <span class='pts'>(1,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": fig_beam_vol_2b(),
     "aplica_html": "<p>En el empotramiento hay reacción vertical y momento. Con \\(\\sum F_y=0\\) y \\(\\sum M_A=0\\) se obtienen; luego se estudian los tramos para dibujar V y M.</p>",
     "solucion_html":
       "<h5>a) Reacciones en el empotramiento</h5>"
       "<div class='formula'>$$\\sum F_y=F_{Ay}-F=0\\;\\Rightarrow\\; F_{Ay}=50\\ \\mathrm{kN}$$</div>"
       "<div class='formula'>$$\\sum M_A=-M_A+F\\,d_1=0\\;\\Rightarrow\\; M_A=50\\cdot 4=200\\ \\mathrm{kN\\,m}$$</div>"
       "<div class='res'><b>F<sub>Ay</sub> = 50 kN · M<sub>A</sub> = 200 kN·m</b></div>"
       "<h5>b) Diagramas de cortante y flector</h5>"
       "<p><b>Tramo 1</b> (0 ≤ x ≤ 4): \\(V=50\\) kN; \\(M=50x-200\\) (−200 en x=0, 0 en x=4). <b>Tramo 2</b> (4 ≤ x ≤ 7): \\(V=0\\); \\(M=0\\).</p>"
       "<figure class='fig'>" + fig_V_2b() + "<figcaption>Cortante: 50 kN hasta la carga, 0 después.</figcaption></figure>"
       "<figure class='fig'>" + fig_M_2b() + "<figcaption>Flector: −200 kN·m en el empotramiento, 0 bajo la carga.</figcaption></figure>"
       "<div class='res'><b>V = 50 kN (tramo 1), 0 (tramo 2) · M<sub>máx</sub> = −200 kN·m</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Ejercicio 3 · Corriente alterna", "color": "#38bdf8",
   "descripcion_tarjeta": "Circuito serie RLC (impedancia y tensiones) y circuito RL con corrección del factor de potencia.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#38bdf8' stroke-width='3'><path d='M10 30 q10 -16 20 0 t20 0 t20 0'/><circle cx='78' cy='30' r='4'/></svg>",
   "cuestiones": [
    {
     "id": "q3a", "titulo": "Opción a · Circuito serie RLC", "etiqueta": "ALTERNA",
     "menu": "3a · Circuito RLC serie", "titulo_corto": "3a",
     "meta": "Opción a · 2,5 puntos (a 0,75 · b 0,5 · c 1,25)",
     "enunciado_html": "<p>Tenemos un circuito serie <b>RLC</b> con un condensador de <b>30 µF</b>, una bobina de <b>0,7 H</b> y una resistencia de <b>100 Ω</b>, conectados a un generador de <b>110 V</b> y <b>60 Hz</b>.</p><ol type='a'><li>Calcula la reactancia inductiva, la capacitiva y la impedancia del circuito. <span class='pts'>(0,75 puntos)</span></li><li>Calcula la intensidad que circula por el circuito y exprésala en forma polar y binómica. <span class='pts'>(0,5 puntos)</span></li><li>Dibuja el triángulo de impedancia y de tensiones. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "aplica_html": "<p>En un RLC serie: \\(X_L=2\\pi f L\\), \\(X_C=\\dfrac{1}{2\\pi f C}\\), reactancia total \\(X=X_L-X_C\\) e impedancia \\(Z=\\sqrt{R^2+X^2}\\). La intensidad es \\(I=V/Z\\), con desfase \\(\\varphi=\\arctan(X/R)\\) (I retrasada respecto a V si el circuito es inductivo).</p>",
     "solucion_html":
       "<h5>a) Reactancias e impedancia</h5>"
       "<div class='formula'>$$X_L=2\\pi f L=2\\pi\\cdot 60\\cdot 0{,}7=263{,}9\\ \\Omega$$</div>"
       "<div class='formula'>$$X_C=\\dfrac{1}{2\\pi f C}=\\dfrac{1}{2\\pi\\cdot 60\\cdot 30\\cdot10^{-6}}=88{,}4\\ \\Omega$$</div>"
       "<div class='formula'>$$X=X_L-X_C=175{,}5\\ \\Omega,\\qquad Z=\\sqrt{100^2+175{,}5^2}=202{,}0\\ \\Omega$$</div>"
       "<div class='res'><b>X<sub>L</sub> = 263,9 Ω · X<sub>C</sub> = 88,4 Ω · Z = 202,0 Ω</b></div>"
       "<h5>b) Intensidad (polar y binómica)</h5>"
       "<div class='formula'>$$I=\\dfrac{V}{Z}=\\dfrac{110}{202{,}0}=0{,}545\\ \\mathrm{A},\\qquad \\varphi=\\arctan\\dfrac{175{,}5}{100}=60{,}3^\\circ$$</div>"
       "<div class='formula'>$$I=0{,}545\\,\\angle{-60{,}3^\\circ}\\ \\mathrm{A}=0{,}270-j\\,0{,}473\\ \\mathrm{A}$$</div>"
       "<div class='res'><b>I = 0,545 ∠ −60,3° A = 0,270 − j 0,473 A</b> (circuito inductivo: I retrasa a V)</div>"
       "<h5>c) Triángulo de impedancia y de tensiones</h5>"
       "<figure class='fig'>" + fig_imp_triangle() + "<figcaption>Triángulo de impedancia: R = 100 Ω, X = 175,5 Ω, Z = 202 Ω (φ = 60,3°).</figcaption></figure>"
       "<figure class='fig'>" + fig_volt_triangle() + "<figcaption>Triángulo de tensiones: V<sub>R</sub> = 54,5 V, V<sub>X</sub> = 95,6 V, V = 110 V.</figcaption></figure>"
       "<div class='res'><b>V<sub>R</sub> = I·R = 54,5 V · V<sub>X</sub> = I·X = 95,6 V · V = 110 V</b></div>"
    },
    {
     "id": "q3b", "titulo": "Opción b · Circuito RL y factor de potencia", "etiqueta": "ALTERNA",
     "menu": "3b · RL · factor de potencia", "titulo_corto": "3b",
     "meta": "Opción b · 2,5 puntos (a 1,5 · b 1)",
     "enunciado_html": "<p>Un circuito serie <b>RL</b> tiene un generador de <b>120 V</b> y <b>60 Hz</b>, la resistencia vale <b>9 Ω</b> y la bobina una reactancia inductiva de <b>14 Ω</b>.</p><ol type='a'><li>Averigua la potencia activa, reactiva y aparente del circuito. Dibuja el triángulo de potencias. <span class='pts'>(1,5 puntos)</span></li><li>Calcular la capacidad que hay que conectar en paralelo con el generador para obtener un factor de potencia de <b>0,9</b>. <span class='pts'>(1 punto)</span></li></ol>",
     "aplica_html": "<p>En un RL serie: \\(Z=\\sqrt{R^2+X_L^2}\\), \\(I=V/Z\\). Potencias: activa \\(P=I^2R\\), reactiva \\(Q=I^2X_L\\), aparente \\(S=V\\,I\\). Para <b>corregir el factor de potencia</b> se añade un condensador en paralelo que aporta \\(Q_C=Q-Q'\\), con \\(Q'=P\\tan\\varphi'\\), y \\(C=\\dfrac{Q_C}{\\omega V^2}\\).</p>",
     "solucion_html":
       "<h5>a) Potencias y triángulo</h5>"
       "<div class='formula'>$$Z=\\sqrt{9^2+14^2}=16{,}6\\ \\Omega,\\qquad I=\\dfrac{120}{16{,}6}=7{,}21\\ \\mathrm{A}$$</div>"
       "<div class='formula'>$$P=I^2R=7{,}21^2\\cdot 9=468\\ \\mathrm{W}$$</div>"
       "<div class='formula'>$$Q=I^2X_L=7{,}21^2\\cdot 14=728\\ \\mathrm{VAr},\\qquad S=V\\,I=120\\cdot 7{,}21=865\\ \\mathrm{VA}$$</div>"
       "<figure class='fig'>" + fig_power_triangle_3b() + "<figcaption>Triángulo de potencias: P = 468 W, Q = 728 VAr, S = 865 VA (φ = 57,3°).</figcaption></figure>"
       "<div class='res'><b>P = 468 W · Q = 728 VAr · S = 865 VA</b></div>"
       "<h5>b) Condensador para f.d.p. = 0,9</h5>"
       "<p>El nuevo desfase es \\(\\varphi'=\\arccos 0{,}9=25{,}84^\\circ\\). La potencia activa no cambia; la reactiva pasa a \\(Q'=P\\tan\\varphi'\\):</p>"
       "<div class='formula'>$$Q'=468\\cdot\\tan 25{,}84^\\circ=226{,}6\\ \\mathrm{VAr}$$</div>"
       "<div class='formula'>$$Q_C=Q-Q'=728-226{,}6=501{,}3\\ \\mathrm{VAr}$$</div>"
       "<div class='formula'>$$C=\\dfrac{Q_C}{\\omega V^2}=\\dfrac{501{,}3}{2\\pi\\cdot 60\\cdot 120^2}=9{,}23\\cdot10^{-5}\\ \\mathrm{F}$$</div>"
       "<div class='res'><b>C ≈ 92,3 µF en paralelo</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Ejercicio 4 · Alarma de una bodega", "color": "#a78bfa",
   "descripcion_tarjeta": "Sistema de seguridad con cuatro sensores: tabla de verdad, Karnaugh e implementación con NAND.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M22 18 h14 a12 12 0 0 1 0 24 h-14 z'/><path d='M8 24h14M8 36h14M60 30h14'/><circle cx='78' cy='30' r='3'/></svg>",
   "cuestiones": [
    {
     "id": "q4", "titulo": "Ejercicio 4 · Sistema de seguridad (bodega)", "etiqueta": "DIGITAL",
     "menu": "E4 · Alarma (Karnaugh y NAND)", "titulo_corto": "E4",
     "meta": "Obligatorio · 2,5 puntos (a 1 · b 0,75 · c 0,75)",
     "enunciado_html": "<p>Para proteger una bodega con botellas de vino valiosas se diseña un sistema de seguridad con <b>cuatro sensores</b> y una alarma. Los sensores son:</p><ul><li><b>A</b>: sensor de puerta principal (abierta/cerrada).</li><li><b>B</b>: sensor de movimiento (alguien dentro del almacén).</li><li><b>C</b>: sensor de ventana (rota o no).</li><li><b>D</b>: sensor de horario nocturno (de noche o de día).</li></ul><p>La alarma debe activarse (<b>S = 1</b>) cuando:</p><ol><li>La puerta está abierta y hay movimiento dentro de la bodega.</li><li>La ventana está rota y es de noche.</li><li>Hay movimiento dentro de la bodega y es de noche.</li></ol><p>Responde:</p><ol type='a'><li>Construye la tabla de verdad con las cuatro variables de entrada (A, B, C, D) y la salida (Alarma). <span class='pts'>(1 punto)</span></li><li>Obtén la función lógica simplificada usando mapas de Karnaugh. <span class='pts'>(0,75 puntos)</span></li><li>Implementa la función lógica obtenida mediante puertas <b>NAND</b>. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "aplica_html": "<p>Cada condición es un producto lógico: puerta y movimiento = <b>A·B</b>; ventana rota y noche = <b>C·D</b>; movimiento y noche = <b>B·D</b>. La salida es la suma (OR) de las tres. Se comprueba con la tabla de verdad, se minimiza por Karnaugh y se implementa con NAND aplicando doble negación.</p>",
     "solucion_html":
       "<h5>a) Tabla de verdad</h5>"
       "<p>S = 1 cuando A·B, o C·D, o B·D:</p>"
       "<table class='dat'><thead><tr><th>A</th><th>B</th><th>C</th><th>D</th><th>S</th></tr></thead><tbody>"
       "<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
       "<tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "</tbody></table>"
       "<h5>b) Mapa de Karnaugh y función simplificada</h5>"
       "<table class='dat'><thead><tr><th>CD\\AB</th><th>00</th><th>01</th><th>11</th><th>10</th></tr></thead><tbody>"
       "<tr><td><b>00</b></td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td><b>01</b></td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td><b>11</b></td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td><b>10</b></td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "</tbody></table>"
       "<p>Agrupaciones: columna AB=11 (<b>A·B</b>), fila CD=11 (<b>C·D</b>) y el bloque B=1·D=1 (<b>B·D</b>):</p>"
       "<div class='formula'>$$\\boxed{\\ S=A\\,B+C\\,D+B\\,D\\ }$$</div>"
       "<h5>c) Implementación con puertas NAND</h5>"
       "<p>Aplicando doble negación, \\(S=\\overline{\\overline{AB+CD+BD}}=\\overline{\\overline{AB}\\cdot\\overline{CD}\\cdot\\overline{BD}}\\):</p>"
       "<div class='formula'>$$S=\\mathrm{NAND}\\big(\\ \\mathrm{NAND}(A,B),\\ \\mathrm{NAND}(C,D),\\ \\mathrm{NAND}(B,D)\\ \\big)$$</div>"
       "<figure class='fig'>" + fig_nand_e4() + "<figcaption>S = A·B + C·D + B·D con tres NAND de 2 entradas y una NAND de 3 entradas.</figcaption></figure>"
       "<div class='res'><b>S = A·B + C·D + B·D = NAND( NAND(A,B), NAND(C,D), NAND(B,D) )</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "clm_2025_ordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
