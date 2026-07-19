#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JSON del examen UCLM 2025/26 · Modelo B (RC/alterna, máquina térmica/motor, Karnaugh/alarma, neumática)."""
import json, os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, txt, line, arrow
from cyllib import Plot, power_triangle, gate, INK, MUT, ACC, OK, ROSE, VIOL, CURVE, AMBER
from build_clm_2024_ordinaria import _and_inputs


def fig_power_1a():
    return power_triangle(1161.6, 1548.8, 1936, 53.13, inductive=False, w=470, h=280, maxw=450,
                          labels={'P': 'P = 1161,6 W', 'Q': 'Q = 1548,8 VAr', 'S': 'S = 1936 VA'})


def fig_wave_1b():
    p = Plot((0, 16), (-290, 290), w=560, h=300, xlabel='t (ms)', ylabel='v (V)', maxw=540)
    p.axes(xticks=[0, 4, 8, 12, 16], yticks=[-250, 0, 250], grid=True)
    pts = [(i * 0.2, 250 * math.sin(800 * (i * 0.2) / 1000)) for i in range(0, 81)]
    p.polyline(pts, color=CURVE, width=2.6)
    p.point(5, 250 * math.sin(4), 't = 5 ms → v ≈ −189 V', color=ROSE, dx=8, dy=20, anchor='start')
    p.hline(250, 0, 16, color=MUT, dash='3 4')
    p.rawtext(p.mx(15.4), p.my(250) - 8, 'V₀ = 250 V', color=MUT, fs=11, anchor='end')
    return p.close()


def fig_nand_3a():
    """S = B̄D̄ + BD + ĀC̄D̄ con NAND-NAND (los literales negados salen de NAND-inversores)."""
    s = svg_open('560 320', 540)
    n1, (o1x, o1y) = gate(160, 20, 'NAND', w=56, h=52)
    s = _and_inputs(s, 160, o1y, ['B̄', 'D̄'])
    s += n1
    n2, (o2x, o2y) = gate(160, 125, 'NAND', w=56, h=52)
    s = _and_inputs(s, 160, o2y, ['B', 'D'])
    s += n2
    n3, (o3x, o3y) = gate(160, 228, 'NAND', w=56, h=64)
    s = _and_inputs(s, 160, o3y, ['Ā', 'C̄', 'D̄'])
    s += n3
    n4, (o4x, o4y) = gate(400, 110, 'NAND', w=64, h=150)
    yt, ym, yb = 110 + 40, 110 + 75, 110 + 110
    s += line(o1x, o1y, 380, o1y) + line(380, o1y, 380, yt) + line(380, yt, 400, yt)
    s += line(o2x, o2y, 400, ym)
    s += line(o3x, o3y, 380, o3y) + line(380, o3y, 380, yb) + line(380, yb, 400, yb)
    s += n4
    s += arrow(o4x, o4y, o4x + 40, o4y)
    s += txt(o4x + 48, o4y + 5, 'S', OK, 16)
    s += txt(20, 300, 'Los literales negados (Ā, B̄, C̄, D̄) se obtienen con NAND-inversores.', MUT, 11)
    return s + "</svg>"


def fig_gates_3b():
    """S = C·D + A·D + A·B·C con tres AND y una OR."""
    s = svg_open('540 320', 520)
    a1, (a1x, a1y) = gate(170, 25, 'AND', w=58, h=48)
    s = _and_inputs(s, 170, a1y, ['C', 'D'])
    s += a1
    a2, (a2x, a2y) = gate(170, 130, 'AND', w=58, h=48)
    s = _and_inputs(s, 170, a2y, ['A', 'D'])
    s += a2
    a3, (a3x, a3y) = gate(170, 232, 'AND', w=58, h=62)
    s = _and_inputs(s, 170, a3y, ['A', 'B', 'C'])
    s += a3
    orf, (ox, oy) = gate(380, 110, 'OR', w=62, h=150)
    yt, ym, yb = 110 + 42, 110 + 75, 110 + 108
    s += line(a1x, a1y, 360, a1y) + line(360, a1y, 360, yt) + line(360, yt, 380, yt)
    s += line(a2x, a2y, 380, ym)
    s += line(a3x, a3y, 360, a3y) + line(360, a3y, 360, yb) + line(360, yb, 380, yb)
    s += orf
    s += arrow(ox, oy, ox + 40, oy)
    s += txt(ox + 48, oy + 5, 'S', OK, 16)
    return s + "</svg>"


def fig_neumatica_e4():
    """Esquema de bloques del circuito neumático diseñado (mando indirecto con memoria)."""
    s = svg_open('680 320', 660)
    # alimentación
    s += box(20, 130, 70, 40, '0P', MUT, 13)
    s += arrow(90, 150, 128, 150)
    s += box(128, 122, 104, 56, '0Z1<tspan x="180" dy="18" font-size="11">unidad mant.</tspan>', ACC, 13)
    s += arrow(232, 150, 300, 150)
    # válvula 5/2 central
    s += box(300, 118, 110, 64, '1.1<tspan x="355" dy="18" font-size="10.5">válvula 5/2</tspan><tspan x="355" dy="14" font-size="10.5">biestable</tspan>', CURVE, 13)
    # pulsador arriba
    s += box(300, 24, 110, 44, '1.2 · pulsador 3/2', VIOL, 12)
    s += arrow(355, 68, 355, 116)
    s += txt(362, 96, 'avance', OK, 10, 'start')
    # regulador de caudal + cilindro
    s += arrow(410, 150, 452, 150)
    s += box(452, 128, 70, 44, '1.01<tspan x="487" dy="16" font-size="10">regulador Q</tspan>', AMBER, 12)
    s += arrow(522, 150, 560, 150)
    s += box(560, 130, 90, 40, '1.0 cilindro D.E.', OK, 12)
    # final de carrera abajo
    s += box(300, 232, 110, 44, '1.3 · rodillo 3/2', VIOL, 12)
    s += line(605, 170, 605, 254) + arrow(605, 254, 410, 254)
    s += txt(500, 246, 'final de carrera', MUT, 10, 'middle')
    s += arrow(355, 232, 355, 184)
    s += txt(362, 210, 'retorno', ROSE, 10, 'start')
    return s + "</svg>"


NOTA_2A = ("<p style='color:#94a3c0;font-size:.9em'><i>Nota:</i> en invierno la máquina "
           "funciona como <b>bomba de calor</b> (calienta la vivienda) pero extrae Q<sub>f</sub> "
           "del foco frío exterior; por el balance Q<sub>c</sub> = Q<sub>f</sub> + W se usa "
           "W = Q<sub>f</sub>/(COP−1). Con la aproximación de refrigerador W = Q<sub>f</sub>/COP "
           "saldría ≈ 13 kW.</p>")


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · UCLM (Castilla-La Mancha) · Curso 2025/26 · Modelo B · Examen resuelto",
  "cabecera_titulo": "PAU 2026 · <span>Tecnología e Ingeniería II</span> · UCLM · Modelo B",
  "pill": "4 ejercicios · 2,5 pt cada uno · 90 min",
  "enunciado_pdf": "../../examens/UCLM/Tecnologia e Ingenieria-26.pdf",
  "pdf_dir": "pdf_clm_2026_modelo_b",
  "footer": "Solucionario PAU · UCLM (Castilla-La Mancha) · Tecnología e Ingeniería II (Modelo B, curso 2025/26)",
  "intro_inicio": "Modelo orientativo del curso 2025/26. La prueba consta de <b>4 ejercicios</b> de 2,5 puntos; en los ejercicios <b>1, 2 y 3</b> se elige una de las dos opciones (a o b) y el <b>ejercicio 4</b> es obligatorio. Aquí se resuelven <b>todas</b> las opciones con el enunciado oficial, los conceptos aplicados y la solución paso a paso.",
  "indice_nombre": "Exámenes de Castilla-La Mancha",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Ejercicio 1 · Corriente alterna", "color": "#38bdf8",
   "descripcion_tarjeta": "Circuito serie RC (impedancia y potencias) y análisis de una señal alterna senoidal.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#38bdf8' stroke-width='3'><path d='M10 30 q10 -16 20 0 t20 0 t20 0'/><circle cx='78' cy='30' r='4'/></svg>",
   "cuestiones": [
    {
     "id": "q1a", "titulo": "Opción a · Circuito serie RC", "etiqueta": "ALTERNA",
     "menu": "1a · Circuito RC serie", "titulo_corto": "1a",
     "meta": "Opción a · 2,5 puntos (a 1 · b 0,5 · c 1)",
     "enunciado_html": "<p>Un circuito serie <b>RC</b> tiene un generador de <b>220 V</b> y <b>50 Hz</b>. Su resistencia es de <b>15 Ω</b> y la capacidad del condensador es de <b>159 µF</b>. Averigua:</p><ol type='a'><li>Impedancia del circuito. <span class='pts'>(1 punto)</span></li><li>La intensidad que pasa por el circuito. <span class='pts'>(0,5 puntos)</span></li><li>Potencia aparente, activa y reactiva del circuito. <span class='pts'>(1 punto)</span></li></ol>",
     "aplica_html": "<p>En un RC serie: reactancia capacitiva \\(X_C=\\dfrac{1}{2\\pi f C}\\), impedancia \\(Z=\\sqrt{R^2+X_C^2}\\) e intensidad \\(I=V/Z\\). Potencias: aparente \\(S=V\\,I\\), activa \\(P=I^2R\\) y reactiva \\(Q=I^2X_C\\) (capacitiva).</p>",
     "solucion_html":
       "<h5>a) Impedancia</h5>"
       "<div class='formula'>$$X_C=\\dfrac{1}{2\\pi f C}=\\dfrac{1}{2\\pi\\cdot 50\\cdot 159\\cdot10^{-6}}=20\\ \\Omega$$</div>"
       "<div class='formula'>$$Z=\\sqrt{R^2+X_C^2}=\\sqrt{15^2+20^2}=\\sqrt{625}=25\\ \\Omega$$</div>"
       "<div class='res'><b>Z = 25 Ω</b></div>"
       "<h5>b) Intensidad</h5>"
       "<div class='formula'>$$I=\\dfrac{V}{Z}=\\dfrac{220}{25}=8{,}8\\ \\mathrm{A}$$</div>"
       "<div class='res'><b>I = 8,8 A</b></div>"
       "<h5>c) Potencias</h5>"
       "<div class='formula'>$$S=V\\,I=220\\cdot 8{,}8=1936\\ \\mathrm{VA}$$</div>"
       "<div class='formula'>$$P=I^2R=8{,}8^2\\cdot 15=1161{,}6\\ \\mathrm{W}\\quad(\\cos\\varphi=R/Z=0{,}6)$$</div>"
       "<div class='formula'>$$Q=I^2X_C=8{,}8^2\\cdot 20=1548{,}8\\ \\mathrm{VAr}\\ (\\text{capacitiva})$$</div>"
       "<figure class='fig'>" + fig_power_1a() + "<figcaption>Triángulo de potencias (carga capacitiva): P = 1161,6 W, Q = 1548,8 VAr, S = 1936 VA.</figcaption></figure>"
       "<div class='res'><b>S = 1936 VA · P = 1161,6 W · Q = 1548,8 VAr (capacitiva)</b></div>"
    },
    {
     "id": "q1b", "titulo": "Opción b · Señal alterna senoidal", "etiqueta": "ALTERNA",
     "menu": "1b · Señal alterna", "titulo_corto": "1b",
     "meta": "Opción b · 2,5 puntos (a 0,5 · b 0,5 · c 1 · d 0,5)",
     "enunciado_html": "<p>Calcula, en la expresión de la señal alterna \\(v=250\\cdot\\operatorname{sen}(800\\,t)\\), las magnitudes que siguen:</p><ol type='a'><li>Periodo y frecuencia. <span class='pts'>(0,5 puntos)</span></li><li>Valor instantáneo para t = 5 ms. <span class='pts'>(0,5 puntos)</span></li><li>Valor máximo, medio y eficaz. <span class='pts'>(1 punto)</span></li><li>Factor de forma. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>En \\(v=V_0\\operatorname{sen}(\\omega t)\\): pulsación \\(\\omega=800\\ \\mathrm{rad/s}\\), frecuencia \\(f=\\omega/2\\pi\\) y periodo \\(T=1/f\\). Valores: máximo \\(V_0\\), medio (de un semiperiodo) \\(V_m=\\tfrac{2}{\\pi}V_0\\), eficaz \\(V_{ef}=V_0/\\sqrt2\\). Factor de forma \\(=V_{ef}/V_m\\).</p>",
     "solucion_html":
       "<h5>a) Periodo y frecuencia</h5>"
       "<div class='formula'>$$\\omega=800\\ \\mathrm{rad/s}\\;\\Rightarrow\\; f=\\dfrac{\\omega}{2\\pi}=\\dfrac{800}{2\\pi}=127{,}3\\ \\mathrm{Hz},\\quad T=\\dfrac1f=7{,}85\\ \\mathrm{ms}$$</div>"
       "<h5>b) Valor instantáneo en t = 5 ms</h5>"
       "<div class='formula'>$$v=250\\operatorname{sen}(800\\cdot 0{,}005)=250\\operatorname{sen}(4\\ \\mathrm{rad})=250\\cdot(-0{,}757)=-189{,}2\\ \\mathrm{V}$$</div>"
       "<figure class='fig'>" + fig_wave_1b() + "<figcaption>Señal v = 250·sen(800t): V₀ = 250 V, T ≈ 7,85 ms; en t = 5 ms, v ≈ −189 V.</figcaption></figure>"
       "<h5>c) Valor máximo, medio y eficaz</h5>"
       "<div class='formula'>$$V_0=250\\ \\mathrm{V},\\quad V_m=\\dfrac{2}{\\pi}V_0=159{,}2\\ \\mathrm{V},\\quad V_{ef}=\\dfrac{V_0}{\\sqrt2}=176{,}8\\ \\mathrm{V}$$</div>"
       "<h5>d) Factor de forma</h5>"
       "<div class='formula'>$$k_f=\\dfrac{V_{ef}}{V_m}=\\dfrac{176{,}8}{159{,}2}=1{,}11$$</div>"
       "<div class='res'><b>f = 127,3 Hz · T = 7,85 ms · v(5 ms) = −189,2 V · V₀ = 250 V · V<sub>m</sub> = 159,2 V · V<sub>ef</sub> = 176,8 V · k<sub>f</sub> = 1,11</b></div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Ejercicio 2 · Termodinámica y motores", "color": "#fb7185",
   "descripcion_tarjeta": "Máquina térmica reversible (verano/invierno) y motor alternativo de 6 cilindros.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#fb7185' stroke-width='3'><circle cx='45' cy='30' r='16'/><path d='M45 14v-8M45 54v-8M61 30h8M13 30h8'/></svg>",
   "cuestiones": [
    {
     "id": "q2a", "titulo": "Opción a · Máquina térmica reversible", "etiqueta": "TERMODINÁMICA",
     "menu": "2a · Máquina reversible (COP)", "titulo_corto": "2a",
     "meta": "Opción a · 2,5 puntos (a 1,25 · b 1,25)",
     "enunciado_html": "<p>Una máquina térmica reversible mantiene la temperatura de una vivienda a <b>22 ºC</b>. En verano el ambiente exterior está a <b>35 ºC</b>; en invierno desciende a <b>0 ºC</b>.</p><ol type='a'><li>Determina el COP ideal de la máquina tanto en verano como en invierno. <span class='pts'>(1,25 puntos)</span></li><li>Para la estación en la que la máquina opera con menor eficiencia, calcula la potencia del motor del compresor si se deben extraer <b>1000 kcal/min</b> del foco frío. La eficiencia real es el <b>40 %</b> del COP de Carnot. <span class='pts'>(1,25 puntos)</span></li></ol>",
     "aplica_html": "<p>En <b>verano</b> la máquina refrigera la vivienda (foco frío = interior): \\(COP_R=\\dfrac{T_f}{T_c-T_f}\\). En <b>invierno</b> actúa como bomba de calor (foco caliente = interior): \\(COP_{BC}=\\dfrac{T_c}{T_c-T_f}\\). Temperaturas: 22 ºC = 295 K, 35 ºC = 308 K, 0 ºC = 273 K.</p>",
     "solucion_html":
       "<h5>a) COP en verano y en invierno</h5>"
       "<p><b>Verano</b> (refrigerador; T<sub>f</sub> = 295 K interior, T<sub>c</sub> = 308 K exterior):</p>"
       "<div class='formula'>$$COP_{verano}=\\dfrac{T_f}{T_c-T_f}=\\dfrac{295}{308-295}=\\dfrac{295}{13}=22{,}7$$</div>"
       "<p><b>Invierno</b> (bomba de calor; T<sub>c</sub> = 295 K interior, T<sub>f</sub> = 273 K exterior):</p>"
       "<div class='formula'>$$COP_{invierno}=\\dfrac{T_c}{T_c-T_f}=\\dfrac{295}{295-273}=\\dfrac{295}{22}=13{,}4$$</div>"
       "<div class='res'><b>COP<sub>verano</sub> = 22,7 · COP<sub>invierno</sub> = 13,4</b></div>"
       "<h5>b) Potencia del compresor (estación de menor eficiencia)</h5>"
       "<p>La menor eficiencia es en <b>invierno</b> (COP = 13,4). Eficiencia real:</p>"
       "<div class='formula'>$$COP_{real}=0{,}4\\cdot 13{,}4=5{,}36$$</div>"
       "<p>Extrayendo \\(Q_f=1000\\ \\mathrm{kcal/min}\\) del foco frío, con \\(Q_c=Q_f+W\\) y \\(COP=Q_c/W\\):</p>"
       "<div class='formula'>$$W=\\dfrac{Q_f}{COP_{real}-1}=\\dfrac{1000}{5{,}36-1}=229{,}4\\ \\mathrm{kcal/min}$$</div>"
       "<div class='formula'>$$P=229{,}4\\ \\tfrac{\\mathrm{kcal}}{\\mathrm{min}}\\cdot\\dfrac{4186\\ \\mathrm{J/kcal}}{60\\ \\mathrm{s/min}}\\approx 16\\,000\\ \\mathrm{W}$$</div>"
       "<div class='res'><b>P ≈ 16 kW</b></div>"
       + NOTA_2A
    },
    {
     "id": "q2b", "titulo": "Opción b · Motor alternativo (6 cilindros)", "etiqueta": "MOTORES",
     "menu": "2b · Motor alternativo", "titulo_corto": "2b",
     "meta": "Opción b · 2,5 puntos (a 0,75 · b 1 · c 0,75)",
     "enunciado_html": "<p>Un motor alternativo de <b>6 cilindros</b> genera un par máximo de <b>M<sub>máx</sub> = 350 N·m</b> girando a <b>4200 rpm</b>. El diámetro de cada cilindro es <b>75 mm</b>, la carrera <b>85 mm</b> y el volumen de la cámara de combustión de cada cilindro es <b>62 cm³</b>. Determina:</p><ol type='a'><li>La cilindrada total del motor. <span class='pts'>(0,75 puntos)</span></li><li>La potencia desarrollada operando en par máximo. <span class='pts'>(1 punto)</span></li><li>La relación volumétrica de compresión. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "aplica_html": "<p>Cilindrada unitaria \\(V_u=\\dfrac{\\pi D^2}{4}\\,L\\); total \\(V_T=z\\,V_u\\). La potencia es \\(P=M\\,\\omega\\), con \\(\\omega=\\dfrac{2\\pi n}{60}\\). La relación de compresión \\(r=\\dfrac{V_u+V_c}{V_c}\\).</p>",
     "solucion_html":
       "<h5>a) Cilindrada total</h5>"
       "<div class='formula'>$$V_u=\\dfrac{\\pi D^2}{4}L=\\dfrac{\\pi\\,7{,}5^2}{4}\\cdot 8{,}5=375{,}5\\ \\mathrm{cm^3}$$</div>"
       "<div class='formula'>$$V_T=6\\cdot 375{,}5=2253\\ \\mathrm{cm^3}\\approx 2{,}25\\ \\mathrm{L}$$</div>"
       "<div class='res'><b>V<sub>T</sub> ≈ 2253 cm³ (2,25 L)</b></div>"
       "<h5>b) Potencia en par máximo</h5>"
       "<div class='formula'>$$\\omega=\\dfrac{2\\pi n}{60}=\\dfrac{2\\pi\\cdot 4200}{60}=439{,}8\\ \\mathrm{rad/s}$$</div>"
       "<div class='formula'>$$P=M\\,\\omega=350\\cdot 439{,}8=153\\,900\\ \\mathrm{W}\\approx 153{,}9\\ \\mathrm{kW}\\ (\\approx 209\\ \\mathrm{CV})$$</div>"
       "<div class='res'><b>P ≈ 153,9 kW</b></div>"
       "<h5>c) Relación de compresión</h5>"
       "<div class='formula'>$$r=\\dfrac{V_u+V_c}{V_c}=\\dfrac{375{,}5+62}{62}=7{,}06$$</div>"
       "<div class='res'><b>r ≈ 7,06 : 1</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Ejercicio 3 · Sistemas digitales", "color": "#a78bfa",
   "descripcion_tarjeta": "Forma canónica, Karnaugh e implementación NAND; diseño de una alarma con cuatro sensores.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M22 18 h14 a12 12 0 0 1 0 24 h-14 z'/><path d='M8 24h14M8 36h14M60 30h14'/><circle cx='78' cy='30' r='3'/></svg>",
   "cuestiones": [
    {
     "id": "q3a", "titulo": "Opción a · Karnaugh e implementación NAND", "etiqueta": "DIGITAL",
     "menu": "3a · Canónica, Karnaugh, NAND", "titulo_corto": "3a",
     "meta": "Opción a · 2,5 puntos (a 0,5 · b 1 · c 1)",
     "enunciado_html": "<p>Partiendo de la tabla de verdad mostrada (A, B, C, D entradas; S salida), se pide:</p><ol type='a'><li>Escribe la primera forma canónica de la función lógica. <span class='pts'>(0,5 puntos)</span></li><li>Simplificar al máximo la función mediante el mapa de Karnaugh. <span class='pts'>(1 punto)</span></li><li>Implementar el circuito con el menor número de puertas lógicas utilizando puertas <b>NAND</b>. <span class='pts'>(1 punto)</span></li></ol>"
       "<table class='dat'><thead><tr><th>A</th><th>B</th><th>C</th><th>D</th><th>S</th></tr></thead><tbody>"
       "<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "</tbody></table>",
     "aplica_html": "<p>La <b>1ª forma canónica</b> es la suma de minterms (filas con S = 1). Los unos se agrupan en el <b>mapa de Karnaugh</b> 4×4 (columnas AB, filas CD) y el resultado se implementa con <b>NAND</b> (estructura NAND-NAND de la suma de productos).</p>",
     "solucion_html":
       "<h5>a) Primera forma canónica (minterms)</h5>"
       "<div class='formula'>$$S=\\sum m(0,2,4,5,7,8,10,13,15)$$</div>"
       "<p>Es decir, la suma de los productos de las 9 filas con salida 1 (\\(\\bar A\\bar B\\bar C\\bar D+\\bar A\\bar B C\\bar D+\\dots+ABCD\\)).</p>"
       "<h5>b) Simplificación por Karnaugh</h5>"
       "<table class='dat'><thead><tr><th>CD\\AB</th><th>00</th><th>01</th><th>11</th><th>10</th></tr></thead><tbody>"
       "<tr><td><b>00</b></td><td>1</td><td>1</td><td>0</td><td>1</td></tr>"
       "<tr><td><b>01</b></td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td><b>11</b></td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td><b>10</b></td><td>1</td><td>0</td><td>0</td><td>1</td></tr>"
       "</tbody></table>"
       "<p>Grupos: <b>B̄·D̄</b> (B = 0 y D = 0, las cuatro esquinas), <b>B·D</b> (B = 1 y D = 1) y el par <b>Ā·C̄·D̄</b> que recoge el 1 restante (m4):</p>"
       "<div class='formula'>$$\\boxed{\\ S=\\bar B\\,\\bar D+B\\,D+\\bar A\\,\\bar C\\,\\bar D\\ }$$</div>"
       "<h5>c) Implementación con puertas NAND</h5>"
       "<p>Suma de tres productos ⇒ estructura <b>NAND-NAND</b>:</p>"
       "<div class='formula'>$$S=\\mathrm{NAND}\\big(\\overline{\\bar B\\bar D},\\ \\overline{BD},\\ \\overline{\\bar A\\bar C\\bar D}\\big)=\\mathrm{NAND}\\big(\\mathrm{NAND}(\\bar B,\\bar D),\\ \\mathrm{NAND}(B,D),\\ \\mathrm{NAND}(\\bar A,\\bar C,\\bar D)\\big)$$</div>"
       "<figure class='fig'>" + fig_nand_3a() + "<figcaption>S = B̄D̄ + BD + ĀC̄D̄ con estructura NAND-NAND (los literales negados salen de NAND-inversores).</figcaption></figure>"
       "<div class='res'><b>S = B̄·D̄ + B·D + Ā·C̄·D̄</b></div>"
    },
    {
     "id": "q3b", "titulo": "Opción b · Diseño de una alarma", "etiqueta": "DIGITAL",
     "menu": "3b · Alarma (Karnaugh)", "titulo_corto": "3b",
     "meta": "Opción b · 2,5 puntos (a 1 · b 1 · c 0,5)",
     "enunciado_html": "<p>Diseña un sistema de control para activar una alarma. Depende de cuatro sensores (A, B, C, D). La alarma se activa (<b>S = 1</b>) cuando:</p><ul><li>Se activan <b>3 o 4</b> sensores simultáneamente.</li><li>Se activan <b>2</b> sensores simultáneamente, siempre que sean <b>C y D</b> o <b>A y D</b>.</li></ul><ol type='a'><li>Obtén la tabla de verdad del sistema. <span class='pts'>(1 punto)</span></li><li>Simplifica la función lógica mediante mapas de Karnaugh. <span class='pts'>(1 punto)</span></li><li>Dibuja el diagrama lógico de la función simplificada. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>Se cuenta cuántos sensores están activos en cada combinación: S = 1 si hay 3 o 4 activos, o si hay exactamente 2 y son {C,D} o {A,D}. Con la tabla se rellena el mapa de Karnaugh y se agrupan los unos.</p>",
     "solucion_html":
       "<h5>a) Tabla de verdad</h5>"
       "<table class='dat'><thead><tr><th>A</th><th>B</th><th>C</th><th>D</th><th>S</th></tr></thead><tbody>"
       "<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "</tbody></table>"
       "<h5>b) Mapa de Karnaugh y función simplificada</h5>"
       "<table class='dat'><thead><tr><th>CD\\AB</th><th>00</th><th>01</th><th>11</th><th>10</th></tr></thead><tbody>"
       "<tr><td><b>00</b></td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
       "<tr><td><b>01</b></td><td>0</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td><b>11</b></td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td><b>10</b></td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "</tbody></table>"
       "<p>Grupos: fila CD = 11 (<b>C·D</b>), bloque A = 1 · D = 1 (<b>A·D</b>) y el par m14–m15 (<b>A·B·C</b>):</p>"
       "<div class='formula'>$$\\boxed{\\ S=C\\,D+A\\,D+A\\,B\\,C\\ }$$</div>"
       "<h5>c) Diagrama lógico</h5>"
       "<figure class='fig'>" + fig_gates_3b() + "<figcaption>S = C·D + A·D + A·B·C con tres puertas AND y una OR.</figcaption></figure>"
       "<div class='res'><b>S = C·D + A·D + A·B·C</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Ejercicio 4 · Diseño neumático", "color": "#38bdf8",
   "descripcion_tarjeta": "Automatización del prensado de piezas con un cilindro de doble efecto, velocidad controlada y retorno automático.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#38bdf8' stroke-width='3'><rect x='12' y='22' width='40' height='16' rx='2'/><path d='M52 30h16M20 30h24'/><circle cx='72' cy='30' r='4'/></svg>",
   "cuestiones": [
    {
     "id": "q4", "titulo": "Ejercicio 4 · Automatización del prensado", "etiqueta": "NEUMÁTICA",
     "menu": "E4 · Diseño neumático (prensado)", "titulo_corto": "E4",
     "meta": "Obligatorio · 2,5 puntos (a 2 · b 0,5)",
     "enunciado_html": "<p>En una planta de ensamblaje se automatiza el <b>prensado de piezas</b> con un <b>cilindro neumático de doble efecto</b>. El sistema debe cumplir:</p><ol><li>El prensado comienza cuando el operario acciona <b>momentáneamente</b> una válvula de <b>pulsador</b>, provocando de forma <b>indirecta</b> el avance del cilindro.</li><li>Durante el avance, el cilindro debe moverse a <b>velocidad controlada</b>.</li><li>Cuando el cilindro ha avanzado lo máximo, debe <b>retornar automáticamente</b> a la posición inicial.</li></ol><ol type='a'><li>Diseñar el circuito neumático que responda a los puntos anteriores. <span class='pts'>(2 puntos)</span></li><li>Indica el nombre de los elementos utilizados. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>Se necesita un <b>mando indirecto con memoria</b>: una válvula <b>5/2 biestable</b> gobierna el cilindro de doble efecto; un <b>pulsador 3/2</b> ordena el avance y un <b>final de carrera 3/2 (rodillo)</b> ordena el retorno automático; una <b>válvula reguladora de caudal</b> controla la velocidad de avance.</p>",
     "solucion_html":
       "<h5>a) Diseño del circuito</h5>"
       "<p>El esquema de mando (indirecto, con memoria) es:</p>"
       "<figure class='fig'>" + fig_neumatica_e4() + "<figcaption>Esquema del circuito: el pulsador 1.2 y el final de carrera 1.3 pilotan la válvula 5/2 biestable (1.1), que gobierna el cilindro de doble efecto 1.0; la reguladora 1.01 controla la velocidad de avance.</figcaption></figure>"
       "<p><b>Funcionamiento:</b> al <b>pulsar 1.2</b> (momentáneamente) se pilota un extremo de la válvula <b>5/2 biestable 1.1</b>, que envía aire a la cámara trasera del cilindro <b>1.0</b>: el vástago <b>avanza</b> a velocidad regulada por la <b>válvula de caudal 1.01</b>. Como la 5/2 es <b>biestable (memoria)</b>, el cilindro sigue avanzando aunque se suelte el pulsador. Al llegar al final de carrera, el vástago acciona el <b>rodillo 1.3</b>, que pilota el otro extremo de la 1.1; ésta conmuta y el cilindro <b>retrocede automáticamente</b> a su posición inicial.</p>"
       "<h5>b) Elementos utilizados</h5>"
       "<ul>"
       "<li><b>1.0 · Cilindro de doble efecto</b> (actuador de prensado).</li>"
       "<li><b>1.1 · Válvula distribuidora 5/2 biestable</b>, pilotada neumáticamente por ambos extremos (función memoria).</li>"
       "<li><b>1.2 · Válvula 3/2 NC de pulsador</b> con retorno por muelle (orden de marcha/avance).</li>"
       "<li><b>1.3 · Válvula 3/2 NC de rodillo</b> (final de carrera) con retorno por muelle (orden de retorno automático).</li>"
       "<li><b>1.01 · Válvula reguladora de caudal unidireccional</b> (estrangulamiento + antirretorno) para la velocidad de avance.</li>"
       "<li><b>0Z1 · Unidad de mantenimiento</b> y <b>0P · toma de aire comprimido</b>.</li>"
       "</ul>"
       "<div class='res'><b>Mando indirecto con memoria: 1.2 (marcha) y 1.3 (final de carrera) pilotan la 5/2 biestable 1.1, que gobierna el cilindro; 1.01 regula la velocidad de avance.</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "clm_2026_modelo_b.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
