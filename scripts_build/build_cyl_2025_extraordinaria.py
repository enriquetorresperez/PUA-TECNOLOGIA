#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Castilla y León EBAU 2025 · Extraordinaria (Propuesta 1)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt
from cyllib import Plot, beam, diagram_VM, ac_series, power_triangle, gate, CURVE, ACC, MUT, INK

FIG = "fig"


def fig_traccion():
    p = Plot((0, 0.002), (0, 50), w=480, h=330,
             xlabel='&epsilon;', ylabel='&sigma; (MPa)', maxw=480)
    p.axes(xticks=[0, 0.0005, 0.001, 0.0015, 0.002],
           yticks=[0, 10, 20, 30, 40, 50],
           xfmt=lambda v: ('0' if v == 0 else f'{v:.4f}'.rstrip('0')),
           grid=True)
    p.polyline([(0, 0), (0.00012, 12)], color=CURVE, width=2.6)
    p.polyline([(0.00012, 12), (0.0002, 19), (0.0003, 24), (0.0005, 29.5),
                (0.0007, 35), (0.001, 41), (0.0013, 46), (0.0015, 48.5), (0.0016, 50)],
               color=CURVE, width=2.6)
    p.point(0.00012, 12, '', color=ACC)
    p.rawtext(p.mx(0.00012) + 70, p.my(12) + 4, 'Límite proporcional', color=MUT, fs=11, anchor='start')
    p.s += f"<line x1='{p.mx(0.00012)+8:.1f}' y1='{p.my(12):.1f}' x2='{p.mx(0.00012)+62:.1f}' y2='{p.my(12):.1f}' stroke='{MUT}' stroke-width='1'/>"
    return p.close()


def fig_viga():
    return beam(loads=[{'type': 'P', 'xm': 4, 'val': 'P = 5000 N'}],
                supports=[{'xm': 0, 'kind': 'roller', 'label': 'A'},
                          {'xm': 10, 'kind': 'pin', 'label': 'C'}],
                span_m=10, dims=[(0, 4, '4 m'), (4, 10, '6 m')])


def fig_V():
    return diagram_VM([(0, 3000), (4, 3000), (4, -2000), (10, -2000)], 10, kind='V', unit='N',
                      title='Esfuerzo cortante V (N)')


def fig_M():
    return diagram_VM([(0, 0), (4, 12000), (10, 0)], 10, kind='M', unit='N·m',
                      title='Momento flector M (N·m)')


def fig_ac():
    return ac_series([('R', 'R'), ('L', 'L = 0,4 H'), ('C', 'C = 20 µF')], V='230 V', f='50 Hz')


def fig_triangulo():
    return power_triangle(271.8, 48.2, 276.0, 10.1, inductive=False,
                          labels={'P': 'P = 271,8 W', 'Q': 'Q = 48,2 VAr (cap.)', 'S': 'S = 276 VA'})


def fig_alarma():
    s = svg_open('440 210', 400)
    g1, o1 = gate(150, 30, 'AND')
    g2, o2 = gate(150, 120, 'AND')
    g3, o3 = gate(300, 78, 'OR')
    # entradas
    for lbl, y in [('a', 40), ('b', 58), ('c', 130), ('d', 148)]:
        s += line(70, y, 150, y)
        s += txt(58, y + 4, lbl, INK, 14)
    s += g1 + g2 + g3
    # salidas AND -> OR
    s += line(o1[0], o1[1], 285, o1[1]); s += line(285, o1[1], 285, 88); s += line(285, 88, 300, 88)
    s += line(o2[0], o2[1], 285, o2[1]); s += line(285, o2[1], 285, 108); s += line(285, 108, 300, 108)
    s += line(o3[0], o3[1], 400, o3[1]); s += txt(408, o3[1] + 4, 'f', INK, 15)
    return s + "</svg>"


def fig_bloques():
    """P8: Y/R = G1 G2 G3 /(1 + G2 G3 + G3 H1)."""
    s = svg_open('720 320', 660)
    ym = 140
    s += txt(20, ym + 5, 'R', '#e2e8f0', 15)
    s += arrow(34, ym, 60, ym)
    s += box(60, ym - 22, 66, 44, 'G<tspan dy=\"4\" font-size=\"11\">1</tspan>', '#22d3ee')
    s += arrow(126, ym, 156, ym); s += summer(172, ym)
    s += txt(156, ym - 12, '+', '#4ade80', 14); s += txt(160, ym + 30, '−', '#fb7185', 16)
    s += arrow(188, ym, 214, ym)
    s += box(214, ym - 22, 66, 44, 'G<tspan dy=\"4\" font-size=\"11\">2</tspan>', '#22d3ee')
    s += arrow(280, ym, 318, ym); s += summer(334, ym)
    s += txt(318, ym - 12, '+', '#4ade80', 14); s += txt(322, ym + 30, '−', '#fb7185', 16)
    s += arrow(350, ym, 388, ym)
    s += box(388, ym - 22, 66, 44, 'G<tspan dy=\"4\" font-size=\"11\">3</tspan>', '#22d3ee')
    s += arrow(454, ym, 512, ym)
    s += "<circle cx='486' cy='140' r='3.4' fill='#cbd5e1'/>"
    s += "<circle cx='512' cy='140' r='3.4' fill='#cbd5e1'/>"
    s += arrow(512, ym, 545, ym); s += txt(556, ym + 5, 'Y', '#e2e8f0', 15)
    # H1 inner loop (desde 512 hasta sumador 2, negativo)
    s += box(360, 214, 66, 40, 'H<tspan dy=\"4\" font-size=\"11\">1</tspan>', '#a78bfa')
    s += line(512, ym, 512, 234); s += line(512, 234, 426, 234)
    s += line(360, 234, 334, 234); s += arrow(334, 234, 334, 156)
    # outer unity loop (desde 486 hasta sumador 1, negativo)
    s += line(486, ym, 486, 288); s += line(486, 288, 172, 288)
    s += arrow(172, 288, 172, 156)
    return s + "</svg>"


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · Castilla y León · Extraordinaria 2025 · Examen resuelto y comentado",
  "cabecera_titulo": "EBAU 2025 · <span>Tecnología e Ingeniería II</span> · Castilla y León · Extraordinaria",
  "pill": "90 min · 2,5 pt/pregunta · 4 apartados",
  "enunciado_pdf": "../../examens/Castilla y Leon/Tecnologia_CastillayLeon_2025_extraordinaria.pdf",
  "pdf_dir": "pdf_cyl_2025_extraordinaria",
  "footer": "Dpto. Tecnología · Solucionario EBAU · Castilla y León · Tecnología e Ingeniería II (Extraordinaria 2025)",
  "intro_inicio": "El ejercicio consta de <b>cuatro apartados obligatorios</b>. El primero tiene una única pregunta; en los otros tres se elige <b>una de las dos</b>. Aquí se resuelven <b>todas</b>. Selecciona un apartado o una pregunta en la barra lateral.",
  "indice_nombre": "Exámenes de Castilla y León",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Apartado 1 · Propiedades y ensayo (obligatoria)", "color": "#f59e0b",
   "descripcion_tarjeta": "Ensayo de tracción de una barra de aluminio a partir de su diagrama tensión–deformación.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><path d='M10 50 Q16 20 32 16 T82 22'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Pregunta única · Tracción de una barra de aluminio", "etiqueta": "APARTADO 1",
     "menu": "P única · Tracción (aluminio)", "titulo_corto": "P1",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 1,0 · b 1,0)",
     "enunciado_html": "<p><b>Cuestión.</b> ¿En qué consiste el ensayo Charpy? <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Una barra de aluminio de 1 m de longitud y 20 mm de diámetro se somete a una fuerza P de tracción. La figura muestra su diagrama tensión–deformación.</p><ol type='a'><li>Determina la longitud que adquiere la barra si P = 3 kN. <span class='pts'>(1 pto.)</span></li><li>Determina el módulo de elasticidad del material. <span class='pts'>(1 pto.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_traccion() + "<figcaption>Diagrama σ–ε del aluminio. El límite proporcional está en ≈ 12 MPa (ε ≈ 0,00012); la zona recta inicial define el módulo E.</figcaption></figure>",
     "aplica_html": "<p>Sección \\(A=\\frac{\\pi D^2}{4}\\). Tensión \\(\\sigma=F/A\\). El módulo de elasticidad es la pendiente de la recta elástica, \\(E=\\sigma/\\varepsilon\\). En la zona elástica \\(\\Delta L=\\varepsilon L_0=\\frac{\\sigma}{E}L_0\\).</p>",
     "solucion_html":
       "<h5>Cuestión · ensayo Charpy</h5>"
       "<p>El <b>ensayo Charpy</b> mide la <b>resiliencia/tenacidad</b>: un péndulo golpea una probeta entallada y se mide la <b>energía absorbida</b> en la rotura (diferencia de altura del péndulo antes y después). Indica la resistencia del material al <b>impacto</b>.</p>"
       "<p>Sección: \\(A=\\frac{\\pi\\cdot20^2}{4}=314{,}16\\ \\mathrm{mm^2}\\).</p>"
       "<h5>a) Longitud con P = 3 kN</h5>"
       "<div class='formula'>$$\\sigma=\\frac{F}{A}=\\frac{3000}{314{,}16}=9{,}55\\ \\mathrm{MPa}$$</div>"
       "<p>9,55 MPa < 12 MPa (límite proporcional) → zona elástica. Con E = 100 GPa (apartado b):</p>"
       "<div class='formula'>$$\\varepsilon=\\frac{\\sigma}{E}=\\frac{9{,}55}{100000}=9{,}55\\cdot10^{-5}$$</div>"
       "<div class='formula'>$$\\Delta L=\\varepsilon L_0=9{,}55\\cdot10^{-5}\\cdot1000\\ \\mathrm{mm}=0{,}0955\\ \\mathrm{mm}\\Rightarrow L=1000{,}10\\ \\mathrm{mm}$$</div>"
       "<div class='res'><b>L ≈ 1000,1 mm (1,0001 m)</b></div>"
       "<h5>b) Módulo de elasticidad</h5>"
       "<p>Se toma la pendiente de la recta inicial, hasta el límite proporcional (σ ≈ 12 MPa, ε ≈ 0,00012):</p>"
       "<div class='formula'>$$E=\\frac{\\sigma}{\\varepsilon}=\\frac{12}{0{,}00012}=1{,}0\\cdot10^{5}\\ \\mathrm{MPa}$$</div>"
       "<div class='res'><b>E ≈ 100 GPa</b> (valor leído de la gráfica)</div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Apartado 2 · Estructuras / Máquinas térmicas", "color": "#22d3ee",
   "descripcion_tarjeta": "Elige: viga con carga puntual o bomba de calor de Carnot (energías aportada y retirada).",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><path d='M8 34h74'/><path d='M40 12v18'/><path d='M35 18l5-6 5 6'/><path d='M8 34l-4 8h8zM82 34l-4 8h8z'/></svg>",
   "cuestiones": [
    {
     "id": "q2", "titulo": "Pregunta 1 (Opción A) · Estructuras: carga puntual", "etiqueta": "APARTADO 2 · A",
     "menu": "P1 (A) · Viga con carga puntual", "titulo_corto": "P2",
     "meta": "Pregunta de 2,5 puntos (a 0,5 · b 1,25 · c 0,75)",
     "enunciado_html": "<p><b>Problema.</b> La viga de la figura tiene aplicada la fuerza puntual indicada (P = 5000 N).</p><ol type='a'><li>Calcula las reacciones en los apoyos. <span class='pts'>(0,5 ptos.)</span></li><li>Calcula los esfuerzos cortantes y momentos flectores. <span class='pts'>(1,25 ptos.)</span></li><li>Representa los diagramas. <span class='pts'>(0,75 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_viga() + "<figcaption>Viga apoyada en A y C (10 m) con carga P = 5000 N en B, a 4 m de A.</figcaption></figure>",
     "aplica_html": "<p>Equilibrio: \\(\\sum M_A=0\\), \\(\\sum F_y=0\\). Cortante constante por tramos; momento máximo bajo la carga.</p>",
     "solucion_html":
       "<h5>a) Reacciones</h5>"
       "<div class='formula'>$$R_C\\cdot10=5000\\cdot4=20000\\Rightarrow R_C=2000\\ \\mathrm N\\qquad R_A=5000-2000=3000\\ \\mathrm N$$</div>"
       "<div class='res'><b>R<sub>A</sub> = 3000 N · R<sub>C</sub> = 2000 N</b></div>"
       "<h5>b) Cortantes y momentos</h5>"
       "<p>A–B (0–4 m): V = +3000 N. B–C (4–10 m): V = 3000 − 5000 = −2000 N. Momento en B: M = 3000·4 = 12000 N·m.</p>"
       "<div class='res'><b>V = +3000 / −2000 N · M<sub>máx</sub> = 12000 N·m (en B)</b></div>"
       "<h5>c) Diagramas</h5>"
       "<figure class='fig'>" + fig_V() + "<figcaption>Esfuerzo cortante.</figcaption></figure>"
       "<figure class='fig'>" + fig_M() + "<figcaption>Momento flector.</figcaption></figure>"
    },
    {
     "id": "q3", "titulo": "Pregunta 2 (Opción B) · Bomba de calor de Carnot", "etiqueta": "APARTADO 2 · B",
     "menu": "P2 (B) · Bomba de calor (Carnot)", "titulo_corto": "P3",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,75 · a 0,5 · b 0,5 · c 0,75)",
     "enunciado_html": "<p><b>Cuestión.</b> Explica el ciclo termodinámico de los motores de cuatro tiempos de encendido provocado (MEP) y dibuja la gráfica p–V. <span class='pts'>(0,75 ptos.)</span></p><p><b>Problema.</b> Un local con exterior a 5 °C necesita una bomba de calor de 10 kW para mantener el interior a 22 °C (ciclo de Carnot reversible). Calcula:</p><ol type='a'><li>La eficiencia de la máquina. <span class='pts'>(0,5 ptos.)</span></li><li>La energía aportada al interior en una hora. <span class='pts'>(0,5 ptos.)</span></li><li>La energía retirada al exterior en una hora. <span class='pts'>(0,75 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>COP de Carnot: \\(\\mathrm{COP}=\\frac{T_c}{T_c-T_f}\\). El calor aportado \\(\\dot Q_c=\\mathrm{COP}\\cdot\\dot W\\); la energía en una hora es \\(Q=\\dot Q\\cdot t\\). Balance: \\(Q_f=Q_c-W\\).</p>",
     "solucion_html":
       "<h5>Cuestión · ciclo MEP de 4 tiempos (Otto)</h5>"
       "<p>Cuatro tiempos: <b>admisión</b> (entra mezcla aire-gasolina, isóbara), <b>compresión</b> (adiabática), <b>explosión-expansión</b> (la bujía inflama la mezcla: combustión isócora + expansión adiabática que da el trabajo) y <b>escape</b> (salida de gases). En p–V, el ciclo Otto ideal: dos adiabáticas y dos isócoras; el área encerrada es el trabajo. \\(\\eta=1-\\frac{1}{r_c^{\\gamma-1}}\\).</p>"
       "<h5>a) Eficiencia (COP)</h5>"
       "<p>T<sub>c</sub> = 22 °C = 295 K, T<sub>f</sub> = 5 °C = 278 K.</p>"
       "<div class='formula'>$$\\mathrm{COP}=\\frac{T_c}{T_c-T_f}=\\frac{295}{295-278}=\\frac{295}{17}=17{,}35$$</div>"
       "<div class='res'><b>COP ≈ 17,35</b></div>"
       "<h5>b) Energía aportada al interior en 1 hora</h5>"
       "<div class='formula'>$$\\dot Q_c=\\mathrm{COP}\\cdot\\dot W=17{,}35\\cdot10=173{,}5\\ \\mathrm{kW}$$</div>"
       "<div class='formula'>$$Q_c=\\dot Q_c\\cdot t=173{,}5\\ \\mathrm{kW}\\cdot3600\\ \\mathrm s=624{,}7\\ \\mathrm{MJ}\\ (=173{,}5\\ \\mathrm{kWh})$$</div>"
       "<div class='res'><b>Q<sub>c</sub> ≈ 624,7 MJ (173,5 kWh)</b></div>"
       "<h5>c) Energía retirada al exterior en 1 hora</h5>"
       "<div class='formula'>$$Q_f=Q_c-W=624{,}7-36=588{,}7\\ \\mathrm{MJ}\\quad(W=10\\ \\mathrm{kW}\\cdot3600\\ \\mathrm s=36\\ \\mathrm{MJ})$$</div>"
       "<div class='res'><b>Q<sub>f</sub> ≈ 588,7 MJ (163,5 kWh)</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Apartado 3 · Neumática / Corriente alterna", "color": "#a78bfa",
   "descripcion_tarjeta": "Elige: circuito neumático con finales de carrera o circuito RLC en serie.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M8 30h12l4-10 8 20 8-20 8 20 4-10h26'/></svg>",
   "cuestiones": [
    {
     "id": "q4", "titulo": "Pregunta 1 (Opción A) · Neumática e hidráulica", "etiqueta": "APARTADO 3 · A",
     "menu": "P1 (A) · Circuito neumático", "titulo_corto": "P4",
     "meta": "Pregunta de 2,5 puntos (a 1,25 · b 1,25)",
     "enunciado_html": "<p><b>Problema.</b> En el circuito neumático de la figura:</p><ol type='a'><li>Describe los distintos elementos. <span class='pts'>(1,25 ptos.)</span></li><li>Explica el funcionamiento. <span class='pts'>(1,25 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'><img src='" + FIG + "/cyl25ext_neumatica.png' alt='Circuito neumático' style='max-width:380px;width:100%;background:#fff;border-radius:8px;padding:8px'><figcaption>Cilindro de doble efecto (A), finales de carrera 3/2 con rodillo (a₀, a₁), distribuidor 5/2 con doble pilotaje (1.1) y válvula de puesta en marcha (0.1).</figcaption></figure>",
     "aplica_html": "<p>Se identifican el actuador, el distribuidor con memoria (5/2 doble pilotaje) y las válvulas de mando (finales de carrera 3/2 con rodillo). El ciclo es un <b>automatismo de vaivén</b>: cada final de carrera pilota el distribuidor hacia el movimiento contrario.</p>",
     "solucion_html":
       "<h5>a) Elementos</h5><ul>"
       "<li><b>A (1.0)</b> — Cilindro de <b>doble efecto</b> (avanza y retrocede con aire a presión).</li>"
       "<li><b>a₀</b> — Válvula <b>3/2 con rodillo</b> (final de carrera) que detecta el cilindro <b>recogido</b>.</li>"
       "<li><b>a₁</b> — Válvula <b>3/2 con rodillo</b> que detecta el cilindro <b>extendido</b>.</li>"
       "<li><b>1.1</b> — <b>Distribuidor 5/2 con doble pilotaje</b> neumático (válvula de memoria): dirige el aire a cada cámara.</li>"
       "<li><b>0.1</b> — Válvula <b>3/2 de puesta en marcha</b> (arranque del circuito).</li></ul>"
       "<h5>b) Funcionamiento (ciclo de vaivén A+ / A−)</h5>"
       "<p>Al dar la señal de marcha (0.1), el aire pilota el distribuidor 1.1 y el cilindro <b>avanza (A+)</b>. Al llegar al final, acciona el rodillo <b>a₁</b>, que pilota el distribuidor por el otro extremo y el cilindro <b>retrocede (A−)</b>. Al volver, acciona <b>a₀</b>, que vuelve a pilotar el avance, repitiéndose el ciclo automáticamente. Por ser un distribuidor con <b>memoria</b>, mantiene la posición aunque cese la señal, hasta recibir la contraria.</p>"
    },
    {
     "id": "q5", "titulo": "Pregunta 2 (Opción B) · Corriente alterna: RLC serie", "etiqueta": "APARTADO 3 · B",
     "menu": "P2 (B) · Circuito RLC serie", "titulo_corto": "P5",
     "meta": "Pregunta de 2,5 puntos (a 0,75 · b 0,25 · c 0,75 · d 0,75)",
     "enunciado_html": "<p><b>Problema.</b> En un circuito serie con corriente eficaz 1,2 A hay una resistencia, una bobina de 0,4 H y un condensador de 20 µF, con 230 V eficaces y 50 Hz. Calcula:</p><ol type='a'><li>La resistencia del circuito. <span class='pts'>(0,75 ptos.)</span></li><li>El factor de potencia. <span class='pts'>(0,25 ptos.)</span></li><li>El balance de potencias. <span class='pts'>(0,75 ptos.)</span></li><li>Dibuja el triángulo de potencias. <span class='pts'>(0,75 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_ac() + "<figcaption>Circuito serie R–L–C (230 V, 50 Hz, I = 1,2 A).</figcaption></figure>",
     "aplica_html": "<p>\\(X_L=2\\pi f L\\), \\(X_C=\\frac1{2\\pi f C}\\). \\(Z=V/I=\\sqrt{R^2+(X_L-X_C)^2}\\Rightarrow R\\). \\(\\cos\\varphi=R/Z\\). \\(P=I^2R\\), \\(Q=I^2(X_L-X_C)\\), \\(S=VI\\).</p>",
     "solucion_html":
       "<h5>a) Resistencia</h5>"
       "<div class='formula'>$$X_L=2\\pi\\cdot50\\cdot0{,}4=125{,}66\\ \\Omega\\qquad X_C=\\frac{1}{2\\pi\\cdot50\\cdot20\\cdot10^{-6}}=159{,}15\\ \\Omega$$</div>"
       "<div class='formula'>$$Z=\\frac{230}{1{,}2}=191{,}67\\ \\Omega\\Rightarrow R=\\sqrt{191{,}67^2-(125{,}66-159{,}15)^2}=\\sqrt{191{,}67^2-33{,}49^2}=188{,}7\\ \\Omega$$</div>"
       "<div class='res'><b>R ≈ 188,7 Ω</b></div>"
       "<h5>b) Factor de potencia</h5>"
       "<p>Como X<sub>C</sub> > X<sub>L</sub>, el circuito es <b>capacitivo</b> (corriente en adelanto).</p>"
       "<div class='formula'>$$\\cos\\varphi=\\frac{R}{Z}=\\frac{188{,}7}{191{,}67}=0{,}985\\quad(\\varphi=-10{,}1^\\circ)$$</div>"
       "<div class='res'><b>cos&phi; ≈ 0,985 (capacitivo)</b></div>"
       "<h5>c) Balance de potencias</h5>"
       "<div class='formula'>$$P=I^2R=1{,}44\\cdot188{,}7=271{,}8\\ \\mathrm W$$</div>"
       "<div class='formula'>$$Q=I^2(X_L-X_C)=1{,}44\\cdot(-33{,}49)=-48{,}2\\ \\mathrm{VAr}\\ (\\text{cap.})$$</div>"
       "<div class='formula'>$$S=V\\,I=230\\cdot1{,}2=276\\ \\mathrm{VA}$$</div>"
       "<div class='res'><b>P ≈ 271,8 W · Q ≈ −48,2 VAr · S = 276 VA</b></div>"
       "<h5>d) Triángulo de potencias</h5>"
       "<figure class='fig'>" + fig_triangulo() + "<figcaption>Circuito casi resistivo (fp ≈ 0,99) y ligeramente capacitivo.</figcaption></figure>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Apartado 4 · Electrónica digital / Control", "color": "#4ade80",
   "descripcion_tarjeta": "Elige: alarma con 4 sensores (con indiferencias) o función de transferencia de un diagrama de bloques.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#4ade80' stroke-width='3'><path d='M20 20h20a12 12 0 0 1 0 24H20z'/><path d='M8 26h12M8 38h12M64 32h18'/></svg>",
   "cuestiones": [
    {
     "id": "q6", "titulo": "Pregunta 1 (Opción A) · Electrónica digital: alarma", "etiqueta": "APARTADO 4 · A",
     "menu": "P1 (A) · Alarma de 4 sensores", "titulo_corto": "P6",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,75 · a 0,5 · b 0,5 · c 0,75)",
     "enunciado_html": "<p><b>Cuestión.</b> Explica qué ventajas prácticas aporta la simplificación de funciones lógicas y enumera los principales métodos. <span class='pts'>(0,75 ptos.)</span></p><p><b>Problema.</b> Una alarma <i>f</i> con cuatro sensores a, b, c, d: suena con <b>tres o cuatro</b> sensores activos; con <b>dos</b> activos es indiferente (0 ó 1); nunca con uno o ninguno.</p><ol type='a'><li>Tabla de verdad. <span class='pts'>(0,5 ptos.)</span></li><li>Mapa de Karnaugh. <span class='pts'>(0,5 ptos.)</span></li><li>Función más simplificada y su circuito. <span class='pts'>(0,75 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>La función es la <i>mayoría</i> (≥3 de 4). Las combinaciones de exactamente dos sensores son <b>indiferencias (X)</b>, que aprovechamos en el Karnaugh para simplificar al máximo.</p>",
     "solucion_html":
       "<h5>Cuestión · ventajas de simplificar y métodos</h5>"
       "<p>Ventajas: menos puertas y entradas → circuito más <b>barato</b>, <b>rápido</b>, con <b>menos consumo</b> y más fiable. Métodos principales: <b>álgebra de Boole</b> (propiedades y teoremas de De Morgan), <b>mapas de Karnaugh</b> y el método tabular de <b>Quine-McCluskey</b>.</p>"
       "<h5>a) Tabla de verdad (X = indiferencia)</h5>"
       "<table class='dat'><tr><th>nº de 1</th><th>combinaciones</th><th>f</th></tr>"
       "<tr><td>0 ó 1</td><td>0000, 0001, 0010, 0100, 1000</td><td>0</td></tr>"
       "<tr><td>2</td><td>0011, 0101, 0110, 1001, 1010, 1100</td><td>X</td></tr>"
       "<tr><td>3</td><td>0111, 1011, 1101, 1110</td><td>1</td></tr>"
       "<tr><td>4</td><td>1111</td><td>1</td></tr></table>"
       "<h5>b) y c) Karnaugh, función y circuito</h5>"
       "<p>En el mapa de 4 variables agrupamos los 1 (minitérminos 7, 11, 13, 14, 15) aprovechando las indiferencias de dos sensores. Cada par de variables (p. ej. a·b y c·d) forma un cuadrado de cuatro casillas que cubre los unos usando indiferencias. La función mínima resulta:</p>"
       "<div class='formula'>$$f=a\\,b+c\\,d$$</div>"
       "<p>(otras parejas equivalentes: \\(a c+b d\\) ó \\(a d+b c\\)). Se comprueba: con tres o cuatro sensores siempre hay al menos una de las dos parejas activa; con uno o ninguno, ninguna. Circuito: <b>dos puertas AND</b> (a·b y c·d) y una <b>OR</b>.</p>"
       "<figure class='fig'>" + fig_alarma() + "<figcaption>Implementación: f = a·b + c·d (2 AND + 1 OR).</figcaption></figure>"
    },
    {
     "id": "q7", "titulo": "Pregunta 2 (Opción B) · Sistemas de control", "etiqueta": "APARTADO 4 · B",
     "menu": "P2 (B) · Función de transferencia Y/R", "titulo_corto": "P7",
     "meta": "Pregunta de 2,5 puntos (a 0,5 · b 0,5 · problema 1,5)",
     "enunciado_html": "<p><b>Cuestiones.</b></p><ol type='a'><li>¿Cuál es la rama de la IA que traduce texto de un idioma a otro? Pon un ejemplo de servicio actual. <span class='pts'>(0,5 ptos.)</span></li><li>En un control en lazo cerrado, ¿qué función realiza el comparador? <span class='pts'>(0,5 ptos.)</span></li></ol><p><b>Problema.</b> Calcula la función de transferencia Y(s)/R(s) del sistema de la figura. <span class='pts'>(1,5 ptos.)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloques() + "<figcaption>G<sub>1</sub>, G<sub>2</sub>, G<sub>3</sub> en cascada con un lazo interior H<sub>1</sub> (sobre G<sub>3</sub>) y realimentación unitaria exterior negativa.</figcaption></figure>",
     "aplica_html": "<p>Se resuelve de dentro afuera: el lazo interno (G<sub>3</sub> con H<sub>1</sub>) se reduce a \\(\\frac{G_3}{1+G_3H_1}\\); con G<sub>2</sub> en serie y realimentación unitaria exterior se obtiene la función total.</p>",
     "solucion_html":
       "<h5>a) IA para traducir idiomas</h5>"
       "<p>Es el <b>Procesamiento de Lenguaje Natural (PLN)</b>, en concreto la <b>traducción automática</b>. Ejemplo actual: <b>Google Translate</b> o <b>DeepL</b>, que traducen texto (y voz) entre idiomas en tiempo real.</p>"
       "<h5>b) El comparador</h5>"
       "<p>El <b>comparador</b> (sumador/restador) calcula el <b>error</b>: resta a la señal de referencia la señal realimentada (salida medida). Ese error es lo que el controlador usa para corregir el sistema.</p>"
       "<h5>Problema · Y/R</h5>"
       "<p>Sea W la salida del primer sumador: \\(W=G_1R-Y\\) (realimentación unitaria exterior). El segundo sumador y G<sub>3</sub> con su lazo H<sub>1</sub>:</p>"
       "<div class='formula'>$$Y=G_3\\big(G_2W-H_1Y\\big)\\ \\Rightarrow\\ Y(1+G_3H_1)=G_2G_3\\,W$$</div>"
       "<div class='formula'>$$Y(1+G_3H_1)=G_2G_3(G_1R-Y)\\ \\Rightarrow\\ Y(1+G_3H_1+G_2G_3)=G_1G_2G_3\\,R$$</div>"
       "<div class='formula'>$$\\boxed{\\ \\dfrac{Y(s)}{R(s)}=\\dfrac{G_1G_2G_3}{1+G_2G_3+G_3H_1}\\ }$$</div>"
       "<div class='res'><b>Y/R = G<sub>1</sub>G<sub>2</sub>G<sub>3</sub> / (1 + G<sub>2</sub>G<sub>3</sub> + G<sub>3</sub>H<sub>1</sub>)</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cyl_2025_extraordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
