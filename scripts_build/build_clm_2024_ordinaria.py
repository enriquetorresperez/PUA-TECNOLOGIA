#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen UCLM (Castilla-La Mancha) 2024 · Ordinaria (curso 2023/24).

Examen oficial con solución publicada por la UCLM. 5 ejercicios; en cada uno se
elige la opción a o b. Aquí se resuelven todas las opciones.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt
from cyllib import beam, diagram_VM, gate, INK, MUT, ACC, OK, ROSE, VIOL, AMBER, CURVE


# ---------------------------------------------------------------------------
#  Figuras
# ---------------------------------------------------------------------------
def fig_probeta():
    """Probeta Charpy: prisma isométrico 10x10 mm con entalla en la cara superior."""
    s = svg_open('420 240', 440)
    # cara frontal
    fx, fy, W, H = 70, 120, 250, 70
    dx, dy = 55, -40  # profundidad isométrica
    fill = "#1b2640"
    # cuerpo (frontal + superior + lateral)
    s += f"<polygon points='{fx},{fy} {fx+W},{fy} {fx+W},{fy+H} {fx},{fy+H}' fill='{fill}' stroke='{INK}' stroke-width='2'/>"
    s += f"<polygon points='{fx},{fy} {fx+dx},{fy+dy} {fx+W+dx},{fy+dy} {fx+W},{fy}' fill='#22304d' stroke='{INK}' stroke-width='2'/>"
    s += f"<polygon points='{fx+W},{fy} {fx+W+dx},{fy+dy} {fx+W+dx},{fy+H+dy} {fx+W},{fy+H}' fill='#141d33' stroke='{INK}' stroke-width='2'/>"
    # entalla en V en la cara superior (hacia el centro)
    nx = fx + W*0.55
    s += f"<polygon points='{nx-14},{fy} {nx},{fy+18} {nx+14},{fy} {nx+14+dx*0.5},{fy+dy*0.5} {nx-14+dx*0.5},{fy+dy*0.5}' fill='#0d1220' stroke='{ROSE}' stroke-width='1.6'/>"
    s += f"<line x1='{nx-14}' y1='{fy}' x2='{nx}' y2='{fy+18}' stroke='{ROSE}' stroke-width='2'/>"
    s += f"<line x1='{nx+14}' y1='{fy}' x2='{nx}' y2='{fy+18}' stroke='{ROSE}' stroke-width='2'/>"
    # cotas
    s += line(fx-14, fy, fx-14, fy+H, MUT)
    s += txt(fx-20, fy+H/2+4, '10 mm', MUT, 12, 'end')
    s += txt(nx+30, fy-4, '2 mm', ROSE, 12, 'start')
    s += line(nx+18, fy-2, nx, fy+16, ROSE)
    s += line(fx+W+dx+8, fy+dy, fx+W+dx+8, fy+H+dy, MUT)
    s += txt(fx+W+dx+14, fy+H/2+dy, '10 mm', MUT, 12, 'start')
    s += txt(fx+W/2, fy+H+26, 'sección resistente 10 × (10−2) mm', MUT, 12, 'middle')
    return s + "</svg>"


def fig_bloques_q3():
    """Diagrama de bloques: P1 en paralelo con P2, realimentación P3."""
    s = svg_open('560 250', 560)
    ym = 120
    s += txt(18, ym+5, 'X', INK, 15)
    s += arrow(30, ym, 78, ym)
    s += summer(95, ym)
    s += txt(78, ym-13, '+', OK, 15) + txt(78, ym+30, '−', ROSE, 16)
    s += line(110, ym, 155, ym)
    s += "<circle cx='155' cy='120' r='3.2' fill='#cbd5e1'/>"
    # rama P1 (arriba)
    s += line(155, ym, 155, 60) + arrow(155, 60, 205, 60)
    s += box(205, 43, 74, 34, 'P<tspan dy="4" font-size="11">1</tspan>', CURVE, 15)
    # rama P2 (centro)
    s += arrow(155, ym, 205, ym)
    s += box(205, ym-17, 74, 34, 'P<tspan dy="4" font-size="11">2</tspan>', CURVE, 15)
    # sumador de salida
    s += line(279, 60, 330, 60) + line(330, 60, 330, ym-14)
    s += line(279, ym, 322, ym)
    s += summer(340, ym)
    s += txt(322, ym-13, '+', OK, 14) + txt(346, ym-13, '+', OK, 14)
    s += line(355, ym, 405, ym)
    s += "<circle cx='405' cy='120' r='3.2' fill='#cbd5e1'/>"
    s += arrow(405, ym, 480, ym)
    s += txt(492, ym+5, 'Y', INK, 15)
    # realimentación P3
    s += line(405, ym, 405, 210) + arrow(405, 210, 344, 210)
    s += box(270, 193, 74, 34, 'P<tspan dy="4" font-size="11">3</tspan>', VIOL, 15)
    s += line(270, 210, 95, 210) + arrow(95, 210, 95, 137)
    return s + "</svg>"


def fig_beam_voladizo():
    return beam(
        [{'type': 'P', 'xm': 5, 'val': 'F = 10 kN'}],
        [{'xm': 0, 'kind': 'fixed', 'side': 'left', 'label': 'A'}],
        span_m=6, dims=[(0, 5, 'd₁ = 5 m'), (5, 6, 'd₂ = 1 m')],
        w=560, h=205, maxw=520)


def fig_V_voladizo():
    return diagram_VM([(0, 10), (5, 10), (5, 0), (6, 0)], span_m=6, kind='V',
                      unit='kN', title='Esfuerzo cortante V', w=520, h=180, maxw=480)


def fig_M_voladizo():
    return diagram_VM([(0, -50), (5, 0), (6, 0)], span_m=6, kind='M',
                      unit='kN·m', title='Momento flector M', w=520, h=180, maxw=480)


def fig_beam_apoyada():
    return beam(
        [{'type': 'P', 'xm': 2, 'val': 'F₁ = 10 kN'}, {'type': 'P', 'xm': 6, 'val': 'F₂ = 10 kN'}],
        [{'xm': 0, 'kind': 'pin', 'label': 'A'}, {'xm': 8, 'kind': 'roller', 'label': 'B'}],
        span_m=8, dims=[(0, 2, 'd₁ = 2 m'), (2, 6, 'd₂ = 4 m'), (6, 8, 'd₃ = 2 m')],
        w=560, h=210, maxw=520)


def fig_nor_q4a():
    """S = (A+B)·(Ā+C) con 4 puertas NOR de 2 entradas."""
    s = svg_open('560 250', 540)
    s += txt(16, 60, 'A', INK, 15)
    s += txt(16, 118, 'B', INK, 15)
    s += txt(16, 205, 'C', INK, 15)
    # N1 = NOR(A,A) = Ā
    g1, (o1x, o1y) = gate(150, 20, 'NOR')
    s += line(28, 55, 95, 55)                       # bus A
    s += "<circle cx='95' cy='55' r='3' fill='#cbd5e1'/>"
    s += line(95, 55, 150, 30) + line(95, 55, 150, 44) + g1
    s += txt(o1x+8, 30, 'Ā', MUT, 12)
    # N2 = NOR(A,B) = (A+B)'
    g2, (o2x, o2y) = gate(150, 90, 'NOR')
    s += line(95, 55, 95, 100) + line(95, 100, 150, 100)   # A a N2
    s += line(28, 113, 150, 114)                             # B a N2
    s += g2
    # N3 = NOR(Ā,C)
    g3, (o3x, o3y) = gate(310, 150, 'NOR')
    s += line(o1x, o1y, 250, 37) + line(250, 37, 250, 160) + line(250, 160, 310, 160)
    s += line(28, 200, 310, 176) + g3
    # N4 = NOR(N2,N3) = S
    g4, (o4x, o4y) = gate(440, 95, 'NOR')
    s += line(o2x, o2y, 440, 102)
    s += line(o3x, o3y, 400, o3y) + line(400, o3y, 400, 124) + line(400, 124, 440, 124)
    s += g4
    s += arrow(o4x, o4y, o4x+40, o4y)
    s += txt(o4x+48, o4y+5, 'S', OK, 16)
    return s + "</svg>"


def _and_inputs(s, gx, cy, labels):
    """Dibuja stubs de entrada rotulados a la izquierda de una puerta en gx."""
    n = len(labels)
    ys = [cy + (i - (n-1)/2)*16 for i in range(n)]
    for y, lab in zip(ys, labels):
        s += line(gx-40, y, gx, y)
        s += txt(gx-46, y+4, lab, INK, 13, 'end')
    return s


def fig_gates_q4b():
    """S = A·B̄·D + B·C̄ + B·D̄: inversores + tres AND + una OR (entradas rotuladas)."""
    s = svg_open('600 340', 560)
    # --- inversores (columna izquierda) ---
    s += txt(30, 30, 'Inversores', MUT, 12)
    for (var, y) in [('B', 55), ('C', 115), ('D', 175)]:
        s += txt(30, y+5, var, INK, 14)
        g, (gx, gy) = gate(60, y-14, 'NOT', w=36, h=28)
        s += line(44, y, 60, y) + g
        s += arrow(gx, gy, gx+26, gy)
        s += txt(gx+32, gy+5, f'{var}̄', VIOL, 14)
    # --- AND gates ---
    a1, (a1x, a1y) = gate(330, 25, 'AND', w=58, h=64)
    s = _and_inputs(s, 330, a1y, ['A', 'B̄', 'D'])
    s += a1
    a2, (a2x, a2y) = gate(330, 140, 'AND', w=58, h=48)
    s = _and_inputs(s, 330, a2y, ['B', 'C̄'])
    s += a2
    a3, (a3x, a3y) = gate(330, 240, 'AND', w=58, h=48)
    s = _and_inputs(s, 330, a3y, ['B', 'D̄'])
    s += a3
    # --- OR final ---
    orf, (ox, oy) = gate(460, 120, 'OR', w=60, h=100)
    oy_top, oy_mid, oy_bot = 120+30, 120+50, 120+70
    s += line(a1x, a1y, 440, a1y) + line(440, a1y, 440, oy_top) + line(440, oy_top, 460, oy_top)
    s += line(a2x, a2y, 460, oy_mid)
    s += line(a3x, a3y, 440, a3y) + line(440, a3y, 440, oy_bot) + line(440, oy_bot, 460, oy_bot)
    s += orf
    s += arrow(ox, oy, ox+38, oy)
    s += txt(ox+46, oy+5, 'S', OK, 16)
    return s + "</svg>"


NOTA_ETERCERA = ("<p style='color:#94a3c0;font-size:.9em'><i>Nota:</i> el enunciado dice "
                 "«una tercera parte». La plantilla oficial de la UCLM emplea el factor "
                 "0,3 (η<sub>real</sub> = 0,3·η<sub>ideal</sub> = 0,132). Con 1/3 exacto "
                 "sería η<sub>real</sub> = 0,146.</p>")


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · UCLM (Castilla-La Mancha) · Ordinaria 2024 (curso 2023/24) · Examen resuelto",
  "cabecera_titulo": "PAU 2024 · <span>Tecnología e Ingeniería II</span> · UCLM · Ordinaria",
  "pill": "Elige 4 de 5 ejercicios · una opción (a o b) · 90 min",
  "enunciado_pdf": "../../examens/UCLM/Tecnologia23_24.pdf",
  "pdf_dir": "pdf_clm_2024_ordinaria",
  "footer": "Solucionario PAU · UCLM (Castilla-La Mancha) · Tecnología e Ingeniería II (Ordinaria 2024)",
  "intro_inicio": "El alumno debe escoger <b>4 de los 5 ejercicios</b> y resolver <b>una</b> de las dos opciones (a o b) de cada uno. Aquí se resuelven <b>todas</b> las opciones. Este examen incluye la <b>solución oficial</b> publicada por la UCLM. Selecciona un ejercicio en la barra lateral: cada uno trae el enunciado oficial, los conceptos que se aplican y la solución paso a paso con figuras y fórmulas.",
  "indice_nombre": "Exámenes de Castilla-La Mancha",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Ejercicio 1 · Ensayos de materiales", "color": "#f59e0b",
   "descripcion_tarjeta": "Dureza Brinell del plomo y ensayo de resiliencia Charpy.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><rect x='14' y='30' width='62' height='18' rx='2'/><path d='M45 8 L45 28'/><circle cx='45' cy='39' r='4' fill='#f59e0b' stroke='none'/></svg>",
   "cuestiones": [
    {
     "id": "q1a", "titulo": "Opción a · Dureza Brinell (plomo)", "etiqueta": "MATERIALES",
     "menu": "1a · Dureza Brinell", "titulo_corto": "1a",
     "meta": "Opción a · 2,5 puntos (a 1 · b 1 · c 0,5)",
     "enunciado_html": "<p>Se tiene una pieza de plomo con una dureza de Brinell <b>23 HB 5 100 15</b>:</p><ol type='a'><li>¿Cuál es la profundidad de la huella que dejó el ensayo? <span class='pts'>(1 punto)</span></li><li>Se quiere realizar un nuevo ensayo con la misma pieza durante <b>20 s</b> que deje una profundidad de huella <b>0,5 mm</b>. ¿Cuánto debería valer la carga que hay que aplicar? <span class='pts'>(1 punto)</span></li><li>¿Cuál sería la expresión de dureza normalizada a partir del nuevo ensayo? <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>La designación normalizada <b>HB D F t</b> indica: dureza, diámetro de la bola (mm), carga (kp) y tiempo (s). Aquí <b>23 HB 5 100 15</b> ⇒ HB = 23 kp/mm², D = 5 mm, F = 100 kp, t = 15 s. La dureza Brinell relaciona la carga con la superficie de la huella; usando la profundidad <b>f</b> de la casquete esférico, \\(S=\\pi D f\\), de modo que \\(HB=\\dfrac{F}{\\pi D f}\\).</p>",
     "solucion_html":
       "<h5>a) Profundidad de la huella</h5>"
       "<p>Datos: HB = 23 kp/mm², F = 100 kp, D = 5 mm. Despejando la profundidad de la superficie del casquete \\(S=\\pi D f\\):</p>"
       "<div class='formula'>$$HB=\\dfrac{F}{S}=\\dfrac{F}{\\pi D f}\\;\\Rightarrow\\; f=\\dfrac{F}{\\pi D\\,HB}=\\dfrac{100}{\\pi\\cdot 5\\cdot 23}$$</div>"
       "<div class='res'><b>f = 0,28 mm</b></div>"
       "<h5>b) Carga para f = 0,5 mm</h5>"
       "<p>Con la misma expresión, despejamos la carga necesaria para dejar una huella de profundidad f = 0,5 mm (la dureza del material no cambia):</p>"
       "<div class='formula'>$$HB=\\dfrac{F}{\\pi D f}\\;\\Rightarrow\\; F=HB\\cdot\\pi D f=23\\cdot\\pi\\cdot 5\\cdot 0{,}5$$</div>"
       "<div class='res'><b>F = 180,64 kp</b></div>"
       "<h5>c) Expresión normalizada del nuevo ensayo</h5>"
       "<p>Cambian la carga (≈ 181 kp) y el tiempo (20 s); la dureza y el diámetro de bola se mantienen:</p>"
       "<div class='res'><b>23 HB 5 181 20</b></div>"
    },
    {
     "id": "q1b", "titulo": "Opción b · Resiliencia (ensayo Charpy)", "etiqueta": "MATERIALES",
     "menu": "1b · Resiliencia (Charpy)", "titulo_corto": "1b",
     "meta": "Opción b · 2,5 puntos (a 1,25 · b 1,25)",
     "enunciado_html": "<p>Se quiere medir la resiliencia de un material bajo un ensayo de <b>Charpy</b>. Para ello se usa una probeta de área resistente de <b>10 mm de lado</b> sobre la que se lanza un péndulo de <b>20 kg</b> de masa desde una altura de <b>1 m</b>. Tras el impacto el péndulo alcanza una altura de <b>300 mm</b>. Calcule:</p><ol type='a'><li>La energía que se ha empleado en partir la probeta expresada en J. <span class='pts'>(1,25 puntos)</span></li><li>La resiliencia del material expresada en J/cm². <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": fig_probeta(),
     "aplica_html": "<p>El <b>péndulo de Charpy</b> mide la energía absorbida en la rotura como la <b>diferencia de energía potencial</b> del péndulo entre la altura inicial y la final: \\(E=m\\,g\\,(h_0-h_1)\\). La <b>resiliencia</b> es esa energía por unidad de <b>sección resistente</b> bajo la entalla: \\(\\rho=E/S\\). La probeta es de 10×10 mm con una entalla de 2 mm, por lo que la sección resistente es 10×(10−2) mm.</p>",
     "solucion_html":
       "<h5>a) Energía absorbida en la rotura</h5>"
       "<p>La energía empleada es la que pierde el péndulo entre \\(h_0=1\\ \\mathrm{m}\\) y \\(h_1=0{,}3\\ \\mathrm{m}\\):</p>"
       "<div class='formula'>$$E=m\\,g\\,\\Delta h=m\\,g\\,(h_0-h_1)=20\\cdot 9{,}8\\cdot(1-0{,}3)$$</div>"
       "<div class='res'><b>E = 137,2 J</b> (con g = 9,8 m/s²)</div>"
       "<h5>b) Resiliencia del material</h5>"
       "<p>La sección resistente es la de la probeta bajo la entalla (10 mm de ancho por 10−2 = 8 mm de altura):</p>"
       "<div class='formula'>$$S=10\\cdot(10-2)=80\\ \\mathrm{mm^2}=0{,}8\\ \\mathrm{cm^2}$$</div>"
       "<div class='formula'>$$\\rho=\\dfrac{E}{S}=\\dfrac{137{,}2\\ \\mathrm{J}}{0{,}8\\ \\mathrm{cm^2}}$$</div>"
       "<div class='res'><b>ρ = 171,5 J/cm²</b></div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Ejercicio 2 · Termodinámica", "color": "#fb7185",
   "descripcion_tarjeta": "Máquina térmica y cajón congelador según el ciclo de Carnot.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#fb7185' stroke-width='3'><circle cx='45' cy='30' r='16'/><path d='M45 14v-8M45 54v-8M61 30h8M13 30h8'/></svg>",
   "cuestiones": [
    {
     "id": "q2a", "titulo": "Opción a · Máquina térmica", "etiqueta": "TERMODINÁMICA",
     "menu": "2a · Máquina térmica", "titulo_corto": "2a",
     "meta": "Opción a · 2,5 puntos (a 0,75 · b 1 · c 0,75)",
     "enunciado_html": "<p>El rendimiento de una máquina térmica es <b>una tercera parte</b> del ciclo de Carnot funcionando entre las temperaturas de <b>230 ºC</b> y <b>10 ºC</b>. Si el calor obtenido del foco caliente es de <b>2500 J</b>, determine:</p><ol type='a'><li>El rendimiento real de la máquina. <span class='pts'>(0,75 puntos)</span></li><li>El calor cedido al foco frío y el trabajo realizado. <span class='pts'>(1 punto)</span></li><li>La temperatura del foco caliente si queremos conseguir un rendimiento del ciclo de Carnot del 58 %. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "aplica_html": "<p>El rendimiento del <b>ciclo de Carnot</b> (ideal) depende solo de las temperaturas absolutas: \\(\\eta_{ideal}=1-\\dfrac{T_2}{T_1}=\\dfrac{T_1-T_2}{T_1}\\). El <b>trabajo</b> y el <b>calor cedido</b> salen del rendimiento real y del balance \\(W=Q_1-Q_2\\), con \\(W=\\eta\\,Q_1\\). Temperaturas en kelvin: 230 ºC = 503 K, 10 ºC = 283 K.</p>",
     "solucion_html":
       "<h5>a) Rendimiento real</h5>"
       "<p>Rendimiento ideal (Carnot) entre 503 K y 283 K:</p>"
       "<div class='formula'>$$\\eta_{ideal}=\\dfrac{T_1-T_2}{T_1}=\\dfrac{503-283}{503}=0{,}44$$</div>"
       "<div class='formula'>$$\\eta_{real}=\\eta_{ideal}\\cdot 0{,}3=0{,}44\\cdot 0{,}3=0{,}132$$</div>"
       "<div class='res'><b>η<sub>real</sub> = 0,132</b></div>"
       + NOTA_ETERCERA +
       "<h5>b) Calor cedido y trabajo</h5>"
       "<p>Con \\(Q_1=2500\\ \\mathrm{J}\\), el calor cedido al foco frío y el trabajo son:</p>"
       "<div class='formula'>$$Q_2=(1-\\eta_{real})\\,Q_1=(1-0{,}132)\\cdot 2500=2170\\ \\mathrm{J}=520{,}8\\ \\mathrm{cal}$$</div>"
       "<div class='formula'>$$W=Q_1-Q_2=2500-2170=330\\ \\mathrm{J}$$</div>"
       "<div class='res'><b>Q<sub>2</sub> = 2170 J (≈ 520,8 cal) · W = 330 J</b></div>"
       "<h5>c) Temperatura del foco caliente para η<sub>Carnot</sub> = 58 %</h5>"
       "<p>Manteniendo T<sub>2</sub> = 283 K y exigiendo \\(\\eta_{Carnot}=1-\\dfrac{T_2}{T_1}=0{,}58\\):</p>"
       "<div class='formula'>$$T_1=\\dfrac{T_2}{1-\\eta_{Carnot}}=\\dfrac{283}{1-0{,}58}$$</div>"
       "<div class='res'><b>T<sub>1</sub> = 673,8 K</b></div>"
    },
    {
     "id": "q2b", "titulo": "Opción b · Cajón congelador", "etiqueta": "TERMODINÁMICA",
     "menu": "2b · Cajón congelador", "titulo_corto": "2b",
     "meta": "Opción b · 2,5 puntos (a 1 · b 1,5)",
     "enunciado_html": "<p>Un cajón congelador que consume <b>250 W</b> mantiene una temperatura interior de <b>−8 ºC</b> mientras que en el exterior hay una temperatura de <b>21 ºC</b>. Calcula:</p><ol type='a'><li>La eficiencia del cajón congelador si su funcionamiento es según un ciclo de Carnot. <span class='pts'>(1 punto)</span></li><li>El calor cedido y el absorbido por el congelador en <b>24 h</b> sabiendo que la eficiencia real del cajón es la mitad de la de Carnot. <span class='pts'>(1,5 puntos)</span></li></ol>",
     "aplica_html": "<p>Un congelador es una <b>máquina frigorífica</b>: su eficiencia (COP) de Carnot es \\(\\varepsilon=\\dfrac{T_2}{T_1-T_2}\\), con T<sub>2</sub> el foco frío. El trabajo consumido es \\(W=P\\,t\\); el calor <b>absorbido</b> del foco frío es \\(Q_2=\\varepsilon\\,W\\) y el <b>cedido</b> al exterior \\(Q_1=W+Q_2\\). Temperaturas: 21 ºC = 294 K, −8 ºC = 265 K.</p>",
     "solucion_html":
       "<h5>a) Eficiencia ideal (COP de Carnot)</h5>"
       "<div class='formula'>$$\\varepsilon_{ideal}=\\dfrac{T_2}{T_1-T_2}=\\dfrac{265}{294-265}=9{,}14$$</div>"
       "<div class='res'><b>ε<sub>ideal</sub> = 9,14</b></div>"
       "<h5>b) Calor cedido y absorbido en 24 h</h5>"
       "<p>La eficiencia real es la mitad de la de Carnot; el trabajo consumido en 24 h:</p>"
       "<div class='formula'>$$\\varepsilon_{real}=\\dfrac{\\varepsilon_{ideal}}{2}=\\dfrac{9{,}14}{2}=4{,}57$$</div>"
       "<div class='formula'>$$W=P\\,t=250\\ \\mathrm{W}\\cdot 24\\ \\mathrm{h}\\cdot 3600\\ \\tfrac{\\mathrm{s}}{\\mathrm{h}}=21\\,600\\ \\mathrm{kJ}$$</div>"
       "<div class='formula'>$$Q_2=\\varepsilon_{real}\\,W=4{,}57\\cdot 21\\,600=98\\,712\\ \\mathrm{kJ}$$</div>"
       "<div class='formula'>$$Q_1=W+Q_2=21\\,600+98\\,712=120\\,312\\ \\mathrm{kJ}$$</div>"
       "<div class='res'><b>Q<sub>2</sub> (absorbido) = 98 712 kJ · Q<sub>1</sub> (cedido) = 120 312 kJ</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Ejercicio 3 · Sistemas de control", "color": "#22d3ee",
   "descripcion_tarjeta": "Función de transferencia de un diagrama de bloques y estabilidad por los polos.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><rect x='34' y='22' width='24' height='16' rx='3'/><path d='M8 30h26M58 30h24'/><circle cx='20' cy='30' r='6'/></svg>",
   "cuestiones": [
    {
     "id": "q3a", "titulo": "Opción a · Función de transferencia", "etiqueta": "CONTROL",
     "menu": "3a · Función de transferencia", "titulo_corto": "3a",
     "meta": "Opción a · 2,5 puntos (M₁ 0,75 · M 1,75)",
     "enunciado_html": "<p>Obtenga la <b>Función de Transferencia</b> del diagrama de bloques de la figura.</p>",
     "figura_enunciado_svg": fig_bloques_q3(),
     "aplica_html": "<p>Se reduce el diagrama por pasos: <b>P<sub>1</sub></b> y <b>P<sub>2</sub></b> están en <b>paralelo</b> (misma entrada, salidas que se suman) ⇒ equivalen a \\(P_1+P_2\\). Ese bloque directo está realimentado por <b>P<sub>3</sub></b> en un <b>lazo negativo</b>, al que se aplica \\(\\dfrac{G}{1+G\\,H}\\).</p>",
     "solucion_html":
       "<h5>Paso 1 · Suma de las ramas en paralelo</h5>"
       "<p>P<sub>1</sub> y P<sub>2</sub> reciben la misma señal y sus salidas se suman:</p>"
       "<div class='formula'>$$M_1=P_1+P_2$$</div>"
       "<h5>Paso 2 · Cierre del lazo con P<sub>3</sub></h5>"
       "<p>La rama directa \\(M_1\\) está realimentada negativamente por P<sub>3</sub>:</p>"
       "<div class='formula'>$$M=\\dfrac{Y}{X}=\\dfrac{P_1+P_2}{1+(P_1+P_2)P_3}=\\dfrac{P_1+P_2}{1+P_1P_3+P_2P_3}$$</div>"
       "<div class='res'><b>M = (P₁ + P₂) / (1 + P₁P₃ + P₂P₃)</b></div>"
    },
    {
     "id": "q3b", "titulo": "Opción b · Estabilidad (polos)", "etiqueta": "CONTROL",
     "menu": "3b · Estabilidad y polos", "titulo_corto": "3b",
     "meta": "Opción b · 2,5 puntos",
     "enunciado_html": "<p>Un sistema de control está representado con la siguiente función de transferencia:</p><div class='formula'>$$F(s)=\\dfrac{1}{s+k}$$</div><p>Donde <b>k</b> es una variable que puede tomar cualquier valor. Analizando los polos, determina para qué valores de <b>k</b> el sistema es estable. Razone la respuesta.</p>",
     "aplica_html": "<p>Los <b>polos</b> de la función de transferencia son las raíces del denominador. Un sistema es <b>estable</b> si todos sus polos están en el <b>semiplano izquierdo</b> del plano complejo, es decir, si tienen <b>parte real negativa</b>.</p>",
     "solucion_html":
       "<h5>Polo del sistema</h5>"
       "<p>El denominador \\(s+k=0\\) da un único polo:</p>"
       "<div class='formula'>$$p=-k$$</div>"
       "<h5>Condición de estabilidad</h5>"
       "<p>El sistema es estable si el polo está en la parte negativa del eje real:</p>"
       "<div class='formula'>$$-k<0\\;\\Rightarrow\\; k>0$$</div>"
       "<div class='res'><b>El sistema es estable siempre que k &gt; 0.</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Ejercicio 4 · Sistemas digitales", "color": "#a78bfa",
   "descripcion_tarjeta": "Tabla de verdad y circuito con NOR; diseño lógico con Karnaugh.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M22 18 h14 a12 12 0 0 1 0 24 h-14 z'/><path d='M8 24h14M8 36h14M60 30h14'/><circle cx='78' cy='30' r='3'/></svg>",
   "cuestiones": [
    {
     "id": "q4a", "titulo": "Opción a · Función lógica con puertas NOR", "etiqueta": "DIGITAL",
     "menu": "4a · Tabla de verdad y NOR", "titulo_corto": "4a",
     "meta": "Opción a · 2,5 puntos (a 1 · b 1,5)",
     "enunciado_html": "<p>Partiendo de la expresión lógica:</p><div class='formula'>$$S=(A+B)\\cdot(\\bar A+C)$$</div><p>Obtener:</p><ol type='a'><li>La tabla de verdad que representa la función lógica. <span class='pts'>(1 punto)</span></li><li>El circuito implementado únicamente con puertas <b>NOR</b>. <span class='pts'>(1,5 puntos)</span></li></ol>",
     "aplica_html": "<p>Se evalúa \\(S=(A+B)(\\bar A+C)\\) para las 8 combinaciones de A, B, C. Para implementarla solo con <b>NOR</b> se aplica la <b>doble negación</b> y De Morgan, recordando que \\(\\overline{A\\cdot B}=\\bar A+\\bar B\\) y \\(x=\\overline{\\overline{x}}\\); una NOR con las dos entradas unidas actúa de inversor.</p>",
     "solucion_html":
       "<h5>a) Tabla de verdad</h5>"
       "<p>Evaluando \\(S=(A+B)(\\bar A+C)\\) (la columna intermedia sería D en el enunciado):</p>"
       "<table class='dat'><thead><tr><th>A</th><th>B</th><th>C</th><th>S</th></tr></thead><tbody>"
       "<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>0</td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "</tbody></table>"
       "<h5>b) Circuito con puertas NOR</h5>"
       "<p>Aplicando doble negación a un producto, \\(X\\cdot Y=\\overline{\\overline{X\\cdot Y}}=\\overline{\\bar X+\\bar Y}\\), con \\(X=A+B\\) e \\(Y=\\bar A+C\\):</p>"
       "<div class='formula'>$$S=(A+B)(\\bar A+C)=\\overline{\\overline{(A+B)}+\\overline{(\\bar A+C)}}=\\mathrm{NOR}\\!\\big(\\mathrm{NOR}(A,B),\\ \\mathrm{NOR}(\\bar A,C)\\big)$$</div>"
       "<p>y \\(\\bar A=\\mathrm{NOR}(A,A)\\). Son <b>4 puertas NOR de dos entradas</b>:</p>"
       "<figure class='fig'>" + fig_nor_q4a() + "<figcaption>S = (A+B)·(Ā+C) implementada con 4 puertas NOR.</figcaption></figure>"
       "<div class='res'><b>S = NOR( NOR(A,B) , NOR( NOR(A,A) , C ) )</b></div>"
    },
    {
     "id": "q4b", "titulo": "Opción b · Diseño lógico (Karnaugh)", "etiqueta": "DIGITAL",
     "menu": "4b · Diseño y Karnaugh", "titulo_corto": "4b",
     "meta": "Opción b · 2,5 puntos (a 1 · b 0,75 · c 0,75)",
     "enunciado_html": "<p>Diseña un circuito con puertas lógicas formado por cuatro sensores (<b>A, B, C y D</b>) y una salida (<b>S</b>) que sigue el siguiente funcionamiento:</p><ol><li>Siempre que <b>A y B</b> están desactivados a la vez, la salida también lo está.</li><li>Si <b>A y D</b> están activados, pero <b>B</b> no, la salida estará activada.</li><li>Si <b>B</b> está activado la salida también lo estará, siempre y cuando no coincidan activados <b>C y D</b>.</li></ol><p>Obtener:</p><ol type='a'><li>La tabla de verdad. <span class='pts'>(1 punto)</span></li><li>El mapa de Karnaugh y función reducida. <span class='pts'>(0,75 puntos)</span></li><li>El diagrama con puertas lógicas. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "aplica_html": "<p>Se traduce cada condición a filas de la <b>tabla de verdad</b> de 16 combinaciones (A,B,C,D). Los unos se colocan en un <b>mapa de Karnaugh</b> 4×4 (columnas AB, filas CD en código Gray) y se agrupan en potencias de 2 para obtener la función mínima.</p>",
     "solucion_html":
       "<h5>a) Tabla de verdad</h5>"
       "<p>Regla 1 fuerza S = 0 con A = B = 0; regla 2 pone S = 1 con A = 1, B = 0, D = 1; regla 3 pone S = 1 con B = 1 salvo que C = D = 1:</p>"
       "<table class='dat'><thead><tr><th>A</th><th>B</th><th>C</th><th>D</th><th>S</th></tr></thead><tbody>"
       "<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
       "<tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr>"
       "</tbody></table>"
       "<h5>b) Mapa de Karnaugh y función reducida</h5>"
       "<table class='dat'><thead><tr><th>CD\\AB</th><th>00</th><th>01</th><th>11</th><th>10</th></tr></thead><tbody>"
       "<tr><td><b>00</b></td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td><b>01</b></td><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td><b>11</b></td><td>0</td><td>0</td><td>0</td><td>1</td></tr>"
       "<tr><td><b>10</b></td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "</tbody></table>"
       "<p>Agrupaciones: <b>B·C̄</b> (bloque AB=01/11 con CD=00/01), <b>B·D̄</b> (AB=01/11 con CD=00/10) y <b>A·B̄·D</b> (AB=10 con CD=01/11):</p>"
       "<div class='formula'>$$\\boxed{\\ S=A\\bar B D+B\\bar C+B\\bar D\\ }$$</div>"
       "<h5>c) Diagrama con puertas lógicas</h5>"
       "<figure class='fig'>" + fig_gates_q4b() + "<figcaption>S = A·B̄·D + B·C̄ + B·D̄ con tres AND, una OR y los inversores necesarios.</figcaption></figure>"
       "<div class='res'><b>S = A·B̄·D + B·C̄ + B·D̄</b></div>"
    }
   ]
  },
  {
   "id": "b5", "titulo": "Ejercicio 5 · Estructuras (vigas)", "color": "#4ade80",
   "descripcion_tarjeta": "Viga en voladizo con diagramas de esfuerzos y viga apoyada; tipos de esfuerzo.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#4ade80' stroke-width='3'><rect x='12' y='26' width='66' height='10' rx='2'/><path d='M45 8 L45 24'/><path d='M18 44 L26 36 34 44M56 44 L64 36 72 44'/></svg>",
   "cuestiones": [
    {
     "id": "q5a", "titulo": "Opción a · Viga en voladizo", "etiqueta": "ESTRUCTURAS",
     "menu": "5a · Viga en voladizo", "titulo_corto": "5a",
     "meta": "Opción a · 2,5 puntos (a 1 · b 1,5)",
     "enunciado_html": "<p>Se tiene la viga en voladizo de la figura con una carga puntual <b>F = 10 kN</b> (con d₁ = 5 m y d₂ = 1 m). Se pide:</p><ol type='a'><li>Calcular las reacciones en el empotramiento. <span class='pts'>(1 punto)</span></li><li>Calcular y representar los diagramas del momento flector y esfuerzo cortante. <span class='pts'>(1,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": fig_beam_voladizo(),
     "aplica_html": "<p>En un <b>empotramiento</b> hay tres reacciones: horizontal, vertical y un <b>momento</b>. Se obtienen con las ecuaciones de equilibrio \\(\\sum F=0\\) y \\(\\sum M=0\\). Luego se estudian los <b>tramos</b> por secciones para dibujar el <b>cortante V</b> y el <b>flector M</b>.</p>",
     "solucion_html":
       "<h5>a) Reacciones en el empotramiento</h5>"
       "<div class='formula'>$$\\sum F_x=0$$</div>"
       "<div class='formula'>$$\\sum F_y=F_{Ay}-F=0\\;\\Rightarrow\\; F_{Ay}=F=10\\ \\mathrm{kN}$$</div>"
       "<div class='formula'>$$\\sum M_A=-M_A+F\\,d_1=0\\;\\Rightarrow\\; M_A=F\\,d_1=10\\cdot 5=50\\ \\mathrm{kN\\,m}$$</div>"
       "<div class='res'><b>F<sub>Ay</sub> = 10 kN · M<sub>A</sub> = 50 kN·m</b></div>"
       "<h5>b) Diagramas de cortante y flector</h5>"
       "<p><b>Tramo 1</b> (0 ≤ x ≤ d₁): \\(V_1=F_{Ay}=10\\ \\mathrm{kN}\\); \\(M_1=F_{Ay}\\,x-M_A=10x-50\\). En x = 0, M = −50 kN·m; en x = 5, M = 0.</p>"
       "<p><b>Tramo 2</b> (d₁ ≤ x ≤ d₁+d₂): \\(V_2=F_{Ay}-F=0\\ \\mathrm{kN}\\); \\(M_2=0\\).</p>"
       "<figure class='fig'>" + fig_V_voladizo() + "<figcaption>Cortante: 10 kN constante hasta la carga, 0 después.</figcaption></figure>"
       "<figure class='fig'>" + fig_M_voladizo() + "<figcaption>Flector: recta de −50 kN·m en el empotramiento a 0 bajo la carga.</figcaption></figure>"
       "<div class='res'><b>V = 10 kN (tramo 1), 0 (tramo 2) · M<sub>máx</sub> = −50 kN·m en el empotramiento</b></div>"
    },
    {
     "id": "q5b", "titulo": "Opción b · Viga simplemente apoyada", "etiqueta": "ESTRUCTURAS",
     "menu": "5b · Viga apoyada · esfuerzos", "titulo_corto": "5b",
     "meta": "Opción b · 2,5 puntos (a 1 · b 0,75 · c 0,75)",
     "enunciado_html": "<p>Se tiene la viga simplemente apoyada de la figura con las cargas puntuales <b>F₁ = 10 kN</b> y <b>F₂ = 10 kN</b> (d₁ = 2 m, d₂ = 4 m, d₃ = 2 m). Se pide:</p><ol type='a'><li>Calcular las reacciones en los apoyos. <span class='pts'>(1 punto)</span></li><li>Enumere los tipos de esfuerzos a los que puede estar sometida una estructura. <span class='pts'>(0,75 puntos)</span></li><li>De los tipos de esfuerzo, nombre y defina los que se dan en la viga de la imagen. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "figura_enunciado_svg": fig_beam_apoyada(),
     "aplica_html": "<p>Con dos apoyos (uno fijo, uno móvil) hay dos reacciones verticales. Se calculan con \\(\\sum M=0\\) en un apoyo y \\(\\sum F_y=0\\). Por simetría de cargas iguales y simétricas, ambas reacciones valen lo mismo.</p>",
     "solucion_html":
       "<h5>a) Reacciones en los apoyos</h5>"
       "<div class='formula'>$$\\sum F_x=0$$</div>"
       "<div class='formula'>$$\\sum M_A=F_1 d_1+F_2(d_1+d_2)-F_{By}(d_1+d_2+d_3)=0$$</div>"
       "<div class='formula'>$$F_{By}=\\dfrac{F_1 d_1+F_2(d_1+d_2)}{d_1+d_2+d_3}=\\dfrac{10\\cdot 2+10\\cdot(2+4)}{2+4+2}=10\\ \\mathrm{kN}$$</div>"
       "<div class='formula'>$$\\sum F_y=F_{Ay}+F_{By}-F_1-F_2=0\\;\\Rightarrow\\; F_{Ay}=10+10-10=10\\ \\mathrm{kN}$$</div>"
       "<div class='res'><b>F<sub>Ay</sub> = 10 kN · F<sub>By</sub> = 10 kN</b></div>"
       "<h5>b) Tipos de esfuerzos</h5>"
       "<p>Una estructura puede estar sometida a cinco tipos de esfuerzo:</p>"
       "<ul><li><b>Tracción</b></li><li><b>Compresión</b></li><li><b>Flexión</b></li><li><b>Torsión</b></li><li><b>Cortante</b> (cizalladura)</li></ul>"
       "<h5>c) Esfuerzo que sufre la viga</h5>"
       "<p><b>Flexión:</b> es el esfuerzo que ocurre cuando se aplica una carga que tiende a doblar una estructura sobre sí misma. Provoca <b>tensiones de compresión</b> en un lado y <b>tensiones de tracción</b> en el lado opuesto de la sección transversal.</p>"
       "<div class='res'><b>La viga trabaja a flexión (con cortante asociado en los apoyos).</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "clm_2024_ordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
