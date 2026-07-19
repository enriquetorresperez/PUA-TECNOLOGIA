#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Cantabria PAU 2025 · Ordinaria (Junio)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt
from cyllib import gate

FIG = "fig"


def img(name, alt, maxw=430, cap=None):
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return (f"<figure class='fig'><img src='fig/{name}' alt='{alt}' "
            f"style='max-width:{maxw}px;width:100%;background:#fff;border-radius:8px;padding:8px'>"
            f"{c}</figure>")


def fig_traccion():
    """Diagrama tensión-deformación en la zona elástica (recta hasta el límite)."""
    s = svg_open('440 300', 440)
    x0, y0 = 60, 250          # origen
    xe, ye = 360, 70          # punto límite elástico
    s += line(x0, y0, x0, 40) + line(x0, y0, 410, y0)          # ejes
    s += txt(x0 - 8, 34, 'σ (MPa)', '#94a3c0', 12, 'end') if False else ''
    s += txt(30, 45, 'σ', '#e2e8f0', 15) + txt(400, y0 + 22, 'ε', '#e2e8f0', 15)
    s += arrow(x0, y0, x0, 40) + arrow(x0, y0, 410, y0)
    # recta elástica 0 -> límite
    s += f"<line x1='{x0}' y1='{y0}' x2='{xe}' y2='{ye}' stroke='#22d3ee' stroke-width='2.6'/>"
    s += f"<circle cx='{xe}' cy='{ye}' r='4' fill='#22d3ee'/>"
    # guías
    s += f"<line x1='{xe}' y1='{ye}' x2='{xe}' y2='{y0}' stroke='#94a3c0' stroke-width='1' stroke-dasharray='4 4'/>"
    s += f"<line x1='{xe}' y1='{ye}' x2='{x0}' y2='{ye}' stroke='#94a3c0' stroke-width='1' stroke-dasharray='4 4'/>"
    s += txt(xe, y0 + 20, '0,00125', '#94a3c0', 12, 'middle')
    s += txt(x0 - 8, ye + 4, '67,9', '#94a3c0', 12, 'end')
    s += txt(xe + 6, ye - 6, 'límite elástico', '#4ade80', 12)
    return s + "</svg>"


def fig_nand_a3p2():
    """S = b·c + a'·c' con 5 NAND-2 (dos como inversores)."""
    s = svg_open('470 280', 470)
    s += txt(14, 60, 'a', '#e2e8f0', 15)
    s += txt(14, 150, 'b', '#e2e8f0', 15)
    s += txt(14, 210, 'c', '#e2e8f0', 15)
    # I1 = NAND(a,a) = a'
    g1, (o1x, o1y) = gate(80, 34, 'NAND')
    s += line(24, 56, 80, 44) + line(24, 56, 80, 58) + g1
    s += txt(o1x + 4, 40, "a'", '#94a3c0', 12)
    # I2 = NAND(c,c) = c'
    g2, (o2x, o2y) = gate(80, 120, 'NAND')
    s += line(24, 206, 60, 206) + line(60, 206, 60, 130) + line(60, 130, 80, 130) + line(60, 130, 80, 146) + g2
    s += txt(o2x + 4, 126, "c'", '#94a3c0', 12)
    # N1 = NAND(b,c) = (bc)'
    g3, (o3x, o3y) = gate(80, 190, 'NAND')
    s += line(24, 150, 80, 200) + line(24, 206, 44, 206) + line(44, 206, 44, 216) + line(44, 216, 80, 216) + g3
    # N2 = NAND(a',c') = (a'c')'
    g4, (o4x, o4y) = gate(220, 70, 'NAND')
    s += line(o1x, o1y, 220, 80) + line(o2x, o2y, 220, 96) + g4
    # N3 = NAND(N2,N1) = bc + a'c' = S
    g5, (o5x, o5y) = gate(350, 138, 'NAND')
    s += line(o4x, o4y, 350, 148) + line(o3x, o3y, 350, 172) + g5
    s += arrow(o5x, o5y, o5x + 40, o5y)
    s += txt(o5x + 48, o5y + 5, 'S', '#4ade80', 16)
    return s + "</svg>"


def fig_control_simpl():
    """Sistema reducido: G1(G2+G3+G4) con realimentación H1H2."""
    s = svg_open('700 210', 640)
    ym = 100
    s += txt(18, ym + 5, 'R', '#e2e8f0', 15)
    s += arrow(34, ym, 68, ym)
    s += summer(86, ym)
    s += txt(70, ym - 12, '+', '#4ade80', 15) + txt(72, ym + 30, '−', '#fb7185', 17)
    s += arrow(102, ym, 190, ym)
    s += box(190, 78, 120, 44, 'G₁(G₂+G₃+G₄)', '#22d3ee', 14)
    s += arrow(310, ym, 470, ym)
    s += "<circle cx='470' cy='100' r='3.4' fill='#cbd5e1'/>"
    s += arrow(470, ym, 520, ym)
    s += txt(532, ym + 5, 'C', '#e2e8f0', 15)
    s += line(470, ym, 470, 170) + line(470, 170, 300, 170)
    s += box(230, 148, 70, 40, 'H₁H₂', '#a78bfa', 14)
    s += line(230, 170, 86, 170) + arrow(86, 170, 86, 115)
    return s + "</svg>"


P = "<span class='pts'>"


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · Cantabria · Ordinaria (Junio) 2025 · Examen resuelto y comentado",
  "cabecera_titulo": "PAU 2025 · <span>Tecnología e Ingeniería II</span> · Cantabria · Ordinaria",
  "pill": "5 apartados · elige 1 pregunta de cada uno · 2 puntos cada apartado",
  "enunciado_pdf": "../../examens/Cantabria/Tecnologia_Cantabria_2025_ordinaria_criterios.pdf",
  "pdf_dir": "pdf_cant_2025_ordinaria",
  "footer": "Solucionario PAU · Cantabria · Tecnología e Ingeniería II (Ordinaria 2025)",
  "intro_inicio": "El examen consta de <b>5 apartados</b> de 2 puntos; en cada uno se elige <b>una</b> de las dos preguntas propuestas (el apartado 5 es único). Aquí se resuelven <b>todas</b>. Selecciona un apartado o una pregunta en la barra lateral: cada una incluye el enunciado oficial, una introducción con los conceptos que se aplican y la solución paso a paso.",
  "indice_nombre": "Exámenes de Cantabria",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Apartado 1 · Materiales", "color": "#f59e0b",
   "descripcion_tarjeta": "Elige una: diagrama Hierro-Carbono de un acero hipoeutectoide o ensayo de tracción de una probeta cilíndrica.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><path d='M10 12 C40 12 40 48 80 48'/><path d='M10 30 L70 30'/><circle cx='70' cy='30' r='3' fill='#f59e0b' stroke='none'/></svg>",
   "cuestiones": [
    {
     "id": "a1p1", "titulo": "Apartado 1 · Pregunta 1 · Diagrama Hierro-Carbono", "etiqueta": "MATERIALES",
     "menu": "A1·P1 · Diagrama Fe-C", "titulo_corto": "A1P1",
     "meta": "2 puntos (a 0,6 · b 0,7 · c 0,7)",
     "enunciado_html": "<p>Disponemos de una aleación Hierro-Carbono de <b>180 kg</b> con el <b>0,39 % de Carbono</b>. A partir del diagrama de equilibrio Hierro-Carbono en la zona de los aceros de la Figura 1, se pide calcular:</p><ol type='a'><li>Masa sólida y líquida a la temperatura de 910 °C. " + P + "(0,6 ptos.)</span></li><li>Masa de ferrita y de cementita a la temperatura de 723,1 °C. " + P + "(0,7 ptos.)</span></li><li>Masa de ferrita dentro de la perlita a la temperatura de 722,9 °C. " + P + "(0,7 ptos.)</span></li></ol>",
     "figura_enunciado_svg": img("cant25ord_fases.png", "Diagrama Hierro-Carbono con 1130, 910 y 723 ºC y eutectoide en 0,89 % C", 470, "Figura 1. Diagrama Fe-C simplificado: aleación de 0,39 % C (acero hipoeutectoide). Eutectoide a 0,89 % C y 723 ºC; cementita a 6,67 % C."),
     "aplica_html": "<p>Es un <b>acero hipoeutectoide</b> (0,39 % &lt; 0,89 %). A 910 ºC el punto está en pleno campo de la <b>austenita</b> (una sola fase sólida). Al enfriar precipita <b>ferrita proeutectoide</b> y, al cruzar los 723 ºC, la austenita restante (0,89 % C) forma <b>perlita</b> (ferrita + cementita). Se resuelve con la <b>regla de la palanca</b> (ferrita ≈ 0 % C, cementita 6,67 % C).</p>",
     "solucion_html":
       "<h5>a) Masa sólida y líquida a 910 °C</h5>"
       "<p>A 910 ºC la vertical del 0,39 % C está por encima de la línea A₃ y muy por debajo de la solidus: el material es <b>austenita</b> (sólido monofásico). No hay fase líquida.</p>"
       "<div class='formula'>$$m_{s\\acute olido}=180\\ \\text{kg (austenita)}\\qquad m_{l\\acute\\i quido}=0\\ \\text{kg}$$</div>"
       "<div class='res'><b>Sólido = 180 kg · Líquido = 0 kg</b></div>"
       "<h5>b) Masa de ferrita y de cementita</h5>"
       "<p>Justo por debajo de la eutectoide la estructura es <b>ferrita</b> (≈ 0 % C) + <b>cementita</b> (6,67 % C). Palanca global sobre el 0,39 % C:</p>"
       "<div class='formula'>$$m_{Fe_3C}=\\dfrac{0{,}39-0}{6{,}67-0}\\cdot180=0{,}0585\\cdot180=10{,}5\\ \\text{kg}$$</div>"
       "<div class='formula'>$$m_{\\alpha}=\\dfrac{6{,}67-0{,}39}{6{,}67}\\cdot180=0{,}9415\\cdot180=169{,}5\\ \\text{kg}$$</div>"
       "<div class='res'><b>Ferrita total ≈ 169,5 kg · Cementita ≈ 10,5 kg</b> (169,5 + 10,5 = 180 kg)</div>"
       "<h5>c) Ferrita dentro de la perlita a 722,9 °C</h5>"
       "<p>La <b>perlita</b> procede de la austenita (0,89 % C) presente antes de la eutectoide:</p>"
       "<div class='formula'>$$m_{perlita}=\\dfrac{0{,}39-0}{0{,}89-0}\\cdot180=0{,}4382\\cdot180=78{,}9\\ \\text{kg}$$</div>"
       "<p>Dentro de la perlita (0,89 % C), la fracción de ferrita eutectoide es:</p>"
       "<div class='formula'>$$m_{\\alpha}^{perlita}=\\dfrac{6{,}67-0{,}89}{6{,}67}\\cdot78{,}9=0{,}8666\\cdot78{,}9=68{,}4\\ \\text{kg}$$</div>"
       "<div class='res'><b>Ferrita dentro de la perlita ≈ 68,4 kg</b> (el resto, 169,5 − 68,4 ≈ 101,1 kg, es ferrita proeutectoide)</div>"
    },
    {
     "id": "a1p2", "titulo": "Apartado 1 · Pregunta 2 · Ensayo de tracción", "etiqueta": "MATERIALES",
     "menu": "A1·P2 · Ensayo de tracción", "titulo_corto": "A1P2",
     "meta": "2 puntos (a 0,5 · b 0,5 · c 0,5 · d 0,5)",
     "enunciado_html": "<p>Se realiza un ensayo de tracción de un cierto material utilizando una probeta cilíndrica de <b>15 mm de diámetro</b> y <b>20 cm de longitud</b>. Se aplica una fuerza de tracción sobre la probeta, la cual se deforma elásticamente hasta que la fuerza alcanza los <b>12000 N</b>, presentando la probeta en ese momento un alargamiento de <b>0,25 mm</b>. Al aplicar una fuerza superior empiezan a producirse deformaciones plásticas hasta llegar a los <b>16000 N</b> donde se produce la rotura de la probeta. Se pide:</p><ol type='a'><li>La tensión en el límite elástico. " + P + "(0,5 ptos.)</span></li><li>La tensión de rotura. " + P + "(0,5 ptos.)</span></li><li>El módulo de elasticidad E del material. " + P + "(0,5 ptos.)</span></li><li>El diagrama de tracción en la zona de comportamiento elástico del material. " + P + "(0,5 ptos.)</span></li></ol>",
     "aplica_html": "<p>La <b>tensión</b> es fuerza entre sección inicial, \\(\\sigma=F/S_0\\), con \\(S_0=\\frac{\\pi}{4}D^2\\). En la zona <b>elástica</b> se cumple la <b>ley de Hooke</b> \\(\\sigma=E\\,\\varepsilon\\), con la deformación unitaria \\(\\varepsilon=\\Delta l/L_0\\); el <b>módulo de elasticidad</b> \\(E\\) es la pendiente de la recta.</p>",
     "solucion_html":
       "<h5>Sección inicial de la probeta</h5>"
       "<div class='formula'>$$S_0=\\dfrac{\\pi}{4}D^2=\\dfrac{\\pi}{4}(15)^2=176{,}7\\ \\mathrm{mm^2}$$</div>"
       "<h5>a) Tensión en el límite elástico</h5>"
       "<div class='formula'>$$\\sigma_e=\\dfrac{F_e}{S_0}=\\dfrac{12000}{176{,}7}=67{,}9\\ \\mathrm{N/mm^2}=67{,}9\\ \\text{MPa}$$</div>"
       "<div class='res'><b>σ<sub>e</sub> ≈ 67,9 MPa</b></div>"
       "<h5>b) Tensión de rotura</h5>"
       "<div class='formula'>$$\\sigma_r=\\dfrac{F_r}{S_0}=\\dfrac{16000}{176{,}7}=90{,}5\\ \\mathrm{N/mm^2}=90{,}5\\ \\text{MPa}$$</div>"
       "<div class='res'><b>σ<sub>r</sub> ≈ 90,5 MPa</b></div>"
       "<h5>c) Módulo de elasticidad E</h5>"
       "<p>La deformación unitaria en el límite elástico (\\(L_0=200\\) mm):</p>"
       "<div class='formula'>$$\\varepsilon=\\dfrac{\\Delta l}{L_0}=\\dfrac{0{,}25}{200}=1{,}25\\cdot10^{-3}$$</div>"
       "<div class='formula'>$$E=\\dfrac{\\sigma_e}{\\varepsilon}=\\dfrac{67{,}9}{1{,}25\\cdot10^{-3}}=54325\\ \\text{MPa}\\approx 54{,}3\\ \\text{GPa}$$</div>"
       "<div class='res'><b>E ≈ 54,3 GPa</b> (≈ 54325 MPa)</div>"
       "<h5>d) Diagrama de tracción (zona elástica)</h5>"
       "<p>En la zona elástica es una <b>recta</b> desde el origen (0, 0) hasta el límite elástico (ε = 1,25·10⁻³ ; σ = 67,9 MPa):</p>"
       "<figure class='fig'>" + fig_traccion() + "<figcaption>Recta de Hooke: pendiente E = σ/ε en el tramo elástico.</figcaption></figure>"
       "<div class='res'><b>Recta (0,0) → (0,00125 ; 67,9 MPa), de pendiente E ≈ 54,3 GPa</b></div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Apartado 2 · Termodinámica y neumática", "color": "#38bdf8",
   "descripcion_tarjeta": "Elige una: máquina de aire acondicionado (ciclo de Carnot) o análisis de un circuito neumático con regulador de caudal.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#38bdf8' stroke-width='3'><rect x='12' y='20' width='40' height='18' rx='2'/><path d='M52 29h16'/><circle cx='72' cy='29' r='4'/><path d='M20 29h24'/></svg>",
   "cuestiones": [
    {
     "id": "a2p1", "titulo": "Apartado 2 · Pregunta 1 · Máquina de aire acondicionado", "etiqueta": "TERMODINÁMICA",
     "menu": "A2·P1 · Aire acondicionado", "titulo_corto": "A2P1",
     "meta": "2 puntos (a 0,8 · b 0,6 · c 0,6)",
     "enunciado_html": "<p>Se instala en un aula una máquina de aire acondicionado para conseguir una temperatura de <b>21 ºC</b>. La temperatura en el exterior es de <b>28 ºC</b> y el rendimiento de la máquina es del <b>45 % del ciclo de Carnot</b>. Se pide:</p><ol type='a'><li>Eficiencia de la máquina. " + P + "(0,8 ptos.)</span></li><li>Calor que cede la máquina al exterior si la máquina absorbe 1875 kJ del interior del aula. " + P + "(0,6 ptos.)</span></li><li>Trabajo realizado por el compresor de la máquina. " + P + "(0,6 ptos.)</span></li></ol>",
     "aplica_html": "<p>El aire acondicionado es una <b>máquina frigorífica</b>: extrae calor del foco frío (aula, 21 ºC) y lo cede al foco caliente (exterior, 28 ºC). Su eficiencia máxima (Carnot) es \\(\\varepsilon_{C}=\\frac{T_f}{T_c-T_f}\\); la real es el 45 % de ella. El balance energético es \\(Q_c=Q_f+W\\), con \\(\\varepsilon=Q_f/W\\).</p>",
     "solucion_html":
       "<h5>a) Eficiencia de la máquina</h5>"
       "<p>Temperaturas absolutas: \\(T_f=21+273=294\\text{ K}\\), \\(T_c=28+273=301\\text{ K}\\).</p>"
       "<div class='formula'>$$\\varepsilon_C=\\dfrac{T_f}{T_c-T_f}=\\dfrac{294}{301-294}=\\dfrac{294}{7}=42$$</div>"
       "<div class='formula'>$$\\varepsilon=0{,}45\\cdot\\varepsilon_C=0{,}45\\cdot42=18{,}9$$</div>"
       "<div class='res'><b>ε = 18,9</b> (COP frigorífico real)</div>"
       "<h5>b) Calor cedido al exterior</h5>"
       "<p>El trabajo del compresor sale de \\(\\varepsilon=Q_f/W\\) con \\(Q_f=1875\\text{ kJ}\\), y el calor cedido del balance \\(Q_c=Q_f+W\\):</p>"
       "<div class='formula'>$$W=\\dfrac{Q_f}{\\varepsilon}=\\dfrac{1875}{18{,}9}=99{,}2\\ \\text{kJ}$$</div>"
       "<div class='formula'>$$Q_c=Q_f+W=1875+99{,}2=1974{,}2\\ \\text{kJ}$$</div>"
       "<div class='res'><b>Q<sub>c</sub> ≈ 1974,2 kJ</b> cedidos al exterior</div>"
       "<h5>c) Trabajo del compresor</h5>"
       "<div class='formula'>$$W=\\dfrac{Q_f}{\\varepsilon}=\\dfrac{1875}{18{,}9}\\approx 99{,}2\\ \\text{kJ}$$</div>"
       "<div class='res'><b>W ≈ 99,2 kJ</b></div>"
    },
    {
     "id": "a2p2", "titulo": "Apartado 2 · Pregunta 2 · Circuito neumático", "etiqueta": "NEUMÁTICA",
     "menu": "A2·P2 · Circuito neumático", "titulo_corto": "A2P2",
     "meta": "2 puntos (a 0,7 · b 1 · c 0,3)",
     "enunciado_html": "<p>Respecto al circuito neumático representado en la Figura 2 adjunta, se solicita:</p><ol type='a'><li>Identificar los componentes del circuito. " + P + "(0,7 ptos.)</span></li><li>Explicar el funcionamiento del circuito. " + P + "(1 pto.)</span></li><li>¿Cómo se podría aumentar la velocidad de salida del vástago? " + P + "(0,3 ptos.)</span></li></ol>",
     "figura_enunciado_svg": img("cant25ord_neumatica.png", "Circuito neumático: cilindro 1.0, regulador 1.01, válvula 5/2 (1.1) y válvulas 3/2 (1.2, 1.3), final de carrera A1", 470, "Figura 2. Cilindro de doble efecto 1.0, regulador de caudal 1.01 (al 50 %), distribuidor 5/2 (1.1) y válvulas 3/2 (1.2 de marcha y 1.3 accionada por el final de carrera A1)."),
     "aplica_html": "<p>Hay que reconocer la <b>simbología neumática</b> (norma ISO 1219) —cilindro, distribuidor, válvula reguladora de caudal y válvulas de mando— y razonar la secuencia de <b>avance</b> y <b>retroceso</b> del vástago, así como el papel del regulador en la velocidad.</p>",
     "solucion_html":
       "<h5>a) Componentes del circuito</h5>"
       "<ul>"
       "<li><b>1.0 · Cilindro de doble efecto</b> (con amortiguación). Actuador: avanza y retrocede con aire a presión en cada cámara. Lleva un <b>final de carrera A1</b> al final de su recorrido.</li>"
       "<li><b>1.01 · Válvula reguladora de caudal unidireccional</b> (estranguladora con antirretorno), ajustada al <b>50 %</b>. Estrangula el aire en un sentido (regulando la velocidad) y lo deja pasar libre en el contrario.</li>"
       "<li><b>1.1 · Distribuidor 5/2</b> (biestable, pilotado neumáticamente por ambos extremos). Mando principal: 5 vías (1 alimentación, 2 y 4 utilización, 3 y 5 escapes) y 2 posiciones.</li>"
       "<li><b>1.2 · Válvula 3/2</b> (NC, retorno por muelle) accionada por <b>pulsador/palanca</b>: señal de <b>marcha</b> que pilota la 5/2 para el avance.</li>"
       "<li><b>1.3 · Válvula 3/2</b> (NC, muelle) accionada por el <b>final de carrera A1</b>: pilota la 5/2 en sentido contrario para el retroceso.</li>"
       "</ul>"
       "<h5>b) Funcionamiento del circuito</h5>"
       "<ol>"
       "<li><b>Reposo:</b> la 5/2 mantiene el vástago recogido; nada actúa.</li>"
       "<li><b>Accionamiento:</b> al pulsar <b>1.2</b> se pilota la 5/2, que conmuta y envía aire a la cámara trasera del cilindro: el vástago <b>avanza</b>. La válvula reguladora <b>1.01</b> estrangula el caudal, de modo que el avance se produce a <b>velocidad controlada</b> (≈ 50 %).</li>"
       "<li><b>Secuencia:</b> al llegar el vástago al final de su carrera acciona el <b>final de carrera A1</b>, que abre la válvula <b>1.3</b>; ésta pilota la 5/2 por el otro extremo y el vástago <b>retrocede</b>.</li>"
       "<li><b>Vuelta a reposo:</b> el cilindro queda recogido; como la 5/2 es <b>biestable</b>, memoriza la posición hasta una nueva orden de marcha.</li>"
       "</ol>"
       "<div class='res'><b>Ciclo: marcha (1.2) → avance regulado → A1 → retroceso (1.3) → reposo</b></div>"
       "<h5>c) Aumentar la velocidad de salida del vástago</h5>"
       "<p>El avance está frenado por el regulador <b>1.01</b> (al 50 %). Para que el vástago salga más rápido se puede <b>abrir más (o eliminar) el regulador 1.01</b>, aumentando el caudal de entrada; alternativamente, instalar una <b>válvula de escape rápido</b> en la cámara que se vacía durante el avance, para evacuar su aire directamente a la atmósfera.</p>"
       "<div class='res'><b>Abrir/quitar el regulador 1.01 o añadir una válvula de escape rápido</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Apartado 3 · Sistemas digitales", "color": "#a78bfa",
   "descripcion_tarjeta": "Elige una: obtener y simplificar la función de un circuito lógico, o analizar y simplificar (Karnaugh + NAND/NOR) una función booleana dada.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M18 18 h14 a12 12 0 0 1 0 24 h-14 z'/><path d='M6 24h12M6 36h12M56 30h14'/><circle cx='74' cy='30' r='3'/></svg>",
   "cuestiones": [
    {
     "id": "a3p1", "titulo": "Apartado 3 · Pregunta 1 · Función de un circuito lógico", "etiqueta": "DIGITAL",
     "menu": "A3·P1 · Función de un circuito", "titulo_corto": "A3P1",
     "meta": "2 puntos (salidas 1,1 · función 0,4 · simplificación 0,5)",
     "enunciado_html": "<p>Obtener la ecuación lógica correspondiente al circuito de la Figura 3 y simplificar algebraicamente todo lo posible.</p>",
     "figura_enunciado_svg": img("cant25ord_logica.png", "Circuito lógico de 4 entradas A, B, C, D con puertas XOR, NOT, NAND, NOR, OR y AND", 600, "Figura 3. Circuito lógico: XOR(A,B), inversor de C, NAND(C,D), NOR(D); una OR y una NOR intermedias, una AND y una OR final que da S."),
     "aplica_html": "<p>Se recorre el circuito por <b>niveles</b>, escribiendo la salida de cada puerta (XOR = 1, NOT, NAND/NOR con círculo, OR = ≥1, AND = &). Luego se agrupa el álgebra de Boole aplicando De Morgan y la propiedad \\(A\\cdot(A\\oplus B)=A\\bar B\\).</p>",
     "solucion_html":
       "<h5>Nivel 1 — salida de las puertas de entrada</h5>"
       "<div class='formula'>$$A\\oplus B\\ (\\text{XOR}),\\quad \\bar C\\ (\\text{NOT}),\\quad \\overline{C\\cdot D}\\ (\\text{NAND}),\\quad \\bar D\\ (\\text{NOR de una entrada})$$</div>"
       "<p>Además, la entrada <b>A</b> se lleva directamente (por arriba) a la puerta AND del nivel 3.</p>"
       "<h5>Nivel 2 — puertas OR y NOR</h5>"
       "<p>La <b>OR</b> superior combina la XOR y \\(\\bar C\\); la <b>NOR</b> inferior combina la NAND y \\(\\bar D\\):</p>"
       "<div class='formula'>$$M=(A\\oplus B)+\\bar C$$</div>"
       "<div class='formula'>$$N=\\overline{\\overline{CD}+\\bar D}=\\overline{\\bar C+\\bar D+\\bar D}=\\overline{\\bar C+\\bar D}=C\\cdot D$$</div>"
       "<h5>Nivel 3 — puerta AND</h5>"
       "<div class='formula'>$$P=A\\cdot M=A\\big[(A\\oplus B)+\\bar C\\big]$$</div>"
       "<h5>Nivel 4 — puerta OR de salida</h5>"
       "<div class='formula'>$$S=P+N=A\\big[(A\\oplus B)+\\bar C\\big]+C\\,D$$</div>"
       "<h5>Simplificación algebraica</h5>"
       "<p>Como \\(A\\cdot(A\\oplus B)=A(\\bar AB+A\\bar B)=A\\bar B\\):</p>"
       "<div class='formula'>$$S=A\\bar B+A\\bar C+C\\,D$$</div>"
       "<div class='formula'>$$\\boxed{\\ S=A\\bar B+A\\bar C+C\\,D\\ }$$</div>"
       "<div class='res'><b>S = A·B̄ + A·C̄ + C·D</b> &nbsp;(minterms de S = 3, 7, 8, 9, 10, 11, 12, 13 y 15)</div>"
    },
    {
     "id": "a3p2", "titulo": "Apartado 3 · Pregunta 2 · Función booleana (Karnaugh y NAND)", "etiqueta": "DIGITAL",
     "menu": "A3·P2 · Karnaugh y NAND", "titulo_corto": "A3P2",
     "meta": "2 puntos (a 0,6 · b 0,4 · c 0,5 · d 0,5)",
     "enunciado_html": "<p>Una máquina dispone de tres pulsadores identificados como a, b y c. El funcionamiento sigue la función booleana S:</p><div class='formula'>$$S=b\\cdot c+\\bar a\\cdot\\bar b\\cdot\\bar c+\\bar a\\cdot b$$</div><p>Se pide:</p><ol type='a'><li>Obtener la tabla de verdad de la función lógica. " + P + "(0,6 ptos.)</span></li><li>Obtener su función booleana en primera forma canónica (suma de productos o minterms). " + P + "(0,4 ptos.)</span></li><li>Simplificar la función mediante el método de Karnaugh. " + P + "(0,5 ptos.)</span></li><li>Implementar la función simplificada utilizando únicamente puertas lógicas de dos entradas NAND o NOR. " + P + "(0,5 ptos.)</span></li></ol>",
     "aplica_html": "<p>Se evalúa la expresión en las 8 combinaciones para construir la <b>tabla de verdad</b>, de la que sale la <b>forma canónica en minterms</b>. El <b>mapa de Karnaugh</b> agrupa los unos adyacentes, y la forma mínima se implementa con <b>NAND</b> (doble negación + De Morgan).</p>",
     "solucion_html":
       "<h5>a) Tabla de verdad</h5>"
       "<p>Evaluando \\(S=bc+\\bar a\\bar b\\bar c+\\bar a b\\) en cada fila:</p>"
       "<table class='dat'><thead><tr><th>a</th><th>b</th><th>c</th><th>S</th></tr></thead><tbody>"
       "<tr><td>0</td><td>0</td><td>0</td><td><b>1</b></td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td><b>0</b></td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td><b>1</b></td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td><b>1</b></td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td><b>0</b></td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td><b>0</b></td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td><b>0</b></td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td><b>1</b></td></tr>"
       "</tbody></table>"
       "<h5>b) Primera forma canónica (minterms)</h5>"
       "<div class='formula'>$$S=\\sum m(0,2,3,7)=\\bar a\\,\\bar b\\,\\bar c+\\bar a\\,b\\,\\bar c+\\bar a\\,b\\,c+a\\,b\\,c$$</div>"
       "<h5>c) Simplificación por Karnaugh</h5>"
       "<table class='dat'><thead><tr><th>a\\bc</th><th>00</th><th>01</th><th>11</th><th>10</th></tr></thead><tbody>"
       "<tr><td><b>0</b></td><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td><b>1</b></td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "</tbody></table>"
       "<p>Columna <b>bc = 11</b> (m3, m7) &rarr; \\(b\\,c\\). Unos de la fila <b>a = 0</b> en 00 y 10 (m0, m2), es decir \\(a=0,\\ c=0\\) &rarr; \\(\\bar a\\,\\bar c\\):</p>"
       "<div class='formula'>$$\\boxed{\\ S=b\\,c+\\bar a\\,\\bar c\\ }$$</div>"
       "<h5>d) Implementación con NAND de dos entradas</h5>"
       "<p>Como \\(S=bc+\\bar a\\bar c=\\overline{\\overline{bc}\\cdot\\overline{\\bar a\\bar c}}\\), y usando inversores NAND para \\(\\bar a\\) y \\(\\bar c\\), bastan <b>5 puertas NAND-2</b>:</p>"
       "<div class='formula'>$$\\bar a=\\overline{a\\cdot a},\\quad \\bar c=\\overline{c\\cdot c},\\quad S=\\overline{\\ \\overline{b\\cdot c}\\cdot\\overline{\\bar a\\cdot\\bar c}\\ }$$</div>"
       "<figure class='fig'>" + fig_nand_a3p2() + "<figcaption>S = b·c + a′·c′ con 5 NAND-2 (dos actúan de inversores).</figcaption></figure>"
       "<div class='res'><b>S = b·c + ā·c̄ = NAND( NAND(b,c) , NAND(ā,c̄) )</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Apartado 4 · Ciberseguridad e IA", "color": "#4ade80",
   "descripcion_tarjeta": "Elige una: concepto de ciberseguridad con phishing y malware, o concepto de inteligencia artificial con impactos positivos y negativos.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#4ade80' stroke-width='3'><path d='M45 10 L68 20 V32 C68 45 45 52 45 52 C45 52 22 45 22 32 V20 Z'/><path d='M37 30l6 6 12-13'/></svg>",
   "cuestiones": [
    {
     "id": "a4p1", "titulo": "Apartado 4 · Pregunta 1 · Ciberseguridad (phishing y malware)", "etiqueta": "CIBERSEGURIDAD",
     "menu": "A4·P1 · Phishing y malware", "titulo_corto": "A4P1",
     "meta": "2 puntos · pregunta teórica",
     "enunciado_html": "<p>Defina qué es la <b>ciberseguridad</b> y describa qué es y cómo funcionan el <b>phishing</b> y el <b>malware</b>.</p>",
     "aplica_html": "<p>Definir el concepto y explicar el funcionamiento de dos amenazas muy habituales.</p>",
     "solucion_html":
       "<h5>¿Qué es la ciberseguridad?</h5>"
       "<p>La <b>ciberseguridad</b> es el conjunto de técnicas, herramientas y buenas prácticas destinadas a <b>proteger</b> los sistemas informáticos, las redes y los datos frente a accesos no autorizados, ataques o daños, garantizando la <b>confidencialidad, integridad y disponibilidad</b> de la información.</p>"
       "<h5>Phishing</h5>"
       "<p>El <b>phishing</b> es una técnica de <b>ingeniería social</b>: el atacante envía correos, mensajes o crea webs <b>falsos</b> que suplantan a una entidad de confianza (banco, red social, administración). Engaña a la víctima para que <b>revele datos sensibles</b> (contraseñas, números de tarjeta) o haga clic en enlaces/adjuntos maliciosos. Funciona explotando la confianza y la urgencia (\"su cuenta será bloqueada\"), no un fallo técnico.</p>"
       "<h5>Malware</h5>"
       "<p>El <b>malware</b> (software malicioso) es cualquier programa diseñado para <b>dañar o infiltrarse</b> en un equipo sin permiso: virus, troyanos, gusanos, <b>ransomware</b> o spyware. Se instala al abrir un archivo infectado, un enlace o una descarga, y una vez dentro puede robar información, cifrar los datos para pedir un rescate, espiar al usuario o tomar control del sistema.</p>"
       "<div class='res'><b>Ciberseguridad = proteger sistemas y datos · Phishing = engaño/suplantación para robar datos · Malware = software que daña o infecta el equipo</b></div>"
    },
    {
     "id": "a4p2", "titulo": "Apartado 4 · Pregunta 2 · Inteligencia artificial", "etiqueta": "IA",
     "menu": "A4·P2 · Inteligencia artificial", "titulo_corto": "A4P2",
     "meta": "2 puntos · pregunta teórica",
     "enunciado_html": "<p>¿Qué se entiende por <b>Inteligencia artificial</b>? Describa <b>dos impactos positivos</b> y <b>dos negativos</b> que la inteligencia artificial puede tener en la sociedad.</p>",
     "aplica_html": "<p>Definir el concepto de IA y valorar de forma equilibrada sus efectos sociales.</p>",
     "solucion_html":
       "<h5>¿Qué es la inteligencia artificial?</h5>"
       "<p>La <b>inteligencia artificial (IA)</b> es la rama de la informática que desarrolla sistemas capaces de realizar tareas que normalmente requieren <b>inteligencia humana</b> —aprender de los datos, razonar, reconocer patrones, comprender el lenguaje o tomar decisiones—, mejorando su comportamiento con la experiencia (aprendizaje automático).</p>"
       "<h5>Dos impactos positivos</h5>"
       "<ul>"
       "<li><b>Avances en medicina y ciencia:</b> ayuda al diagnóstico precoz (análisis de imágenes médicas), al descubrimiento de fármacos y a la investigación, salvando vidas y ganando precisión.</li>"
       "<li><b>Automatización y productividad:</b> libera a las personas de tareas repetitivas o peligrosas, mejora la eficiencia industrial y ofrece servicios personalizados (asistentes, traducción, accesibilidad).</li>"
       "</ul>"
       "<h5>Dos impactos negativos</h5>"
       "<ul>"
       "<li><b>Destrucción/transformación del empleo:</b> la automatización puede eliminar puestos de trabajo y aumentar la desigualdad si no se acompaña de formación y reorientación laboral.</li>"
       "<li><b>Privacidad, sesgos y desinformación:</b> el uso masivo de datos personales amenaza la privacidad, los algoritmos pueden heredar <b>sesgos</b> discriminatorios y la IA generativa facilita bulos y <b>deepfakes</b>.</li>"
       "</ul>"
       "<div class='res'>La IA es una herramienta muy potente: su efecto depende de un uso <b>ético, regulado y responsable</b>.</div>"
    }
   ]
  },
  {
   "id": "b5", "titulo": "Apartado 5 · Sistemas de control", "color": "#22d3ee",
   "descripcion_tarjeta": "Simplificación de un sistema de control con tres bloques en paralelo y estudio de estabilidad por el criterio de Routh.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><rect x='34' y='12' width='22' height='12' rx='2'/><rect x='34' y='36' width='22' height='12' rx='2'/><path d='M8 30h26M56 18h16M56 42h16M72 18v24'/></svg>",
   "cuestiones": [
    {
     "id": "a5", "titulo": "Apartado 5 · Sistema de control y estabilidad (Routh)", "etiqueta": "CONTROL",
     "menu": "A5 · Control y Routh", "titulo_corto": "A5",
     "meta": "2 puntos (simplificación 1,2 · estabilidad 0,8)",
     "enunciado_html": "<p>Dado el sistema de control de la Figura 4, se pide:</p><ol type='a'><li>Simplifica al máximo el sistema de control (obtén su función de transferencia). " + P + "(1,2 ptos.)</span></li><li>La expresión (2) representa el denominador de la función de transferencia del sistema. Determinar, mediante el método de Routh, si el sistema es estable e indicar el número de polos. " + P + "(0,8 ptos.)</span></li></ol><div class='formula'>$$s^5+2s^4+18s^3+20s^2+46s+64=0\\quad(2)$$</div>",
     "figura_enunciado_svg": img("cant25ord_control.png", "Sistema de control: G1 seguido de G2, G3 y G4 en paralelo, con realimentación H1·H2", 560, "Figura 4. Bloque G1 seguido de tres bloques en paralelo (G2, G3, G4) sumados, con realimentación negativa a través de H2 y H1."),
     "aplica_html": "<p>Las ramas en <b>paralelo</b> se suman (G₂+G₃+G₄); los bloques de realimentación en serie se multiplican (H₁·H₂); y el <b>lazo cerrado</b> con realimentación negativa aplica \\(\\frac{G}{1+GH}\\). La estabilidad se estudia con el <b>criterio de Routh</b> sobre el denominador.</p>",
     "solucion_html":
       "<h5>a) Simplificación del sistema</h5>"
       "<p>Los tres bloques reciben la misma entrada (salida de G₁) y sus salidas se suman: van en <b>paralelo</b> &rarr; \\(G_2+G_3+G_4\\). La cadena directa es entonces \\(G_1(G_2+G_3+G_4)\\). La realimentación en serie es \\(H_1H_2\\).</p>"
       "<figure class='fig'>" + fig_control_simpl() + "<figcaption>Sistema equivalente: un bloque directo con realimentación negativa H₁H₂.</figcaption></figure>"
       "<p>Cerrando el lazo (realimentación negativa) con \\(\\frac{G}{1+GH}\\):</p>"
       "<div class='formula'>$$\\boxed{\\ \\dfrac{C(s)}{R(s)}=\\dfrac{G_1(G_2+G_3+G_4)}{1+G_1(G_2+G_3+G_4)\\,H_1H_2}\\ }$$</div>"
       "<div class='res'><b>C/R = G₁(G₂+G₃+G₄) / [ 1 + G₁(G₂+G₃+G₄)·H₁H₂ ]</b></div>"
       "<h5>b) Estabilidad por el criterio de Routh</h5>"
       "<p>Denominador (grado 5): coeficientes 1, 2, 18, 20, 46, 64. Tabla de Routh:</p>"
       "<table class='dat'><tbody>"
       "<tr><th>s⁵</th><td>1</td><td>18</td><td>46</td></tr>"
       "<tr><th>s⁴</th><td>2</td><td>20</td><td>64</td></tr>"
       "<tr><th>s³</th><td>8</td><td>14</td><td>0</td></tr>"
       "<tr><th>s²</th><td>16,5</td><td>64</td><td></td></tr>"
       "<tr><th>s¹</th><td>−17,03</td><td>0</td><td></td></tr>"
       "<tr><th>s⁰</th><td>64</td><td></td><td></td></tr>"
       "</tbody></table>"
       "<div class='formula'>$$s^3:\\ \\dfrac{2\\cdot18-1\\cdot20}{2}=8,\\ \\dfrac{2\\cdot46-1\\cdot64}{2}=14$$</div>"
       "<div class='formula'>$$s^2:\\ \\dfrac{8\\cdot20-2\\cdot14}{8}=16{,}5,\\ \\dfrac{8\\cdot64}{8}=64;\\quad s^1:\\ \\dfrac{16{,}5\\cdot14-8\\cdot64}{16{,}5}=-17{,}03;\\quad s^0:\\ 64$$</div>"
       "<p>Primera columna: \\(1,\\ 2,\\ 8,\\ 16{,}5,\\ -17{,}03,\\ 64\\). Hay <b>dos cambios de signo</b> (de 16,5 a −17,03 y de −17,03 a 64).</p>"
       "<div class='res'><b>Sistema INESTABLE</b> · 2 cambios de signo &rarr; 2 polos con parte real positiva. El sistema tiene <b>5 polos</b> (2 en el semiplano derecho y 3 en el izquierdo).</div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cant_2025_ordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
