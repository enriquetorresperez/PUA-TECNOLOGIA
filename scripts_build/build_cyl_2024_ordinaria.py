#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Castilla y León EBAU 2024 · Ordinaria (Propuesta 5)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt
from cyllib import beam, diagram_VM, ac_series, power_triangle

FIG = "fig"


def fig_viga():
    return beam(loads=[{'type': 'P', 'xm': 3, 'val': 'P = 1000 N'}],
                supports=[{'xm': 0, 'kind': 'pin', 'label': 'A'},
                          {'xm': 3, 'kind': 'roller', 'label': 'B'},
                          {'xm': 5, 'kind': 'roller', 'label': 'C'}],
                span_m=5, dims=[(0, 3, '3 m'), (3, 5, '2 m')])


def fig_V():
    return diagram_VM([(0, 400), (3, 400), (3, -600), (5, -600)], 5, kind='V', unit='N',
                      title='Esfuerzo cortante V (N)')


def fig_M():
    return diagram_VM([(0, 0), (3, 1200), (5, 0)], 5, kind='M', unit='N·m',
                      title='Momento flector M (N·m)')


def fig_ac():
    return ac_series([('R', 'R'), ('L', 'L = 0,2 H'), ('C', 'C = 25 µF')], V='230 V', f='50 Hz')


def fig_triangulo():
    return power_triangle(380.9, 258.0, 460.0, 34.1, inductive=False,
                          labels={'P': 'P = 380,9 W', 'Q': 'Q = 258 VAr (cap.)', 'S': 'S = 460 VA'})


def fig_bloques_yr():
    """P8: Y/R = G3(G1+G2)/(1+G3(G1+G2)). Unidad de realimentación (unitaria)."""
    s = svg_open('720 300', 640)
    ym = 165
    s += txt(24, ym + 5, 'R', '#e2e8f0', 15)
    s += arrow(40, ym, 74, ym)
    s += summer(90, ym)
    s += txt(74, ym - 12, '+', '#4ade80', 15); s += txt(78, ym + 30, '−', '#fb7185', 17)
    s += arrow(106, ym, 150, ym)
    s += "<circle cx='150' cy='165' r='3.4' fill='#cbd5e1'/>"
    s += arrow(150, ym, 188, ym)
    s += box(188, 143, 70, 44, 'G<tspan dy=\"4\" font-size=\"11\">1</tspan>', '#22d3ee')
    s += arrow(258, ym, 306, ym)
    s += summer(322, ym)
    s += txt(304, ym + 30, '+', '#4ade80', 15); s += txt(334, ym - 12, '+', '#4ade80', 15)
    s += arrow(338, ym, 378, ym)
    s += box(378, 143, 70, 44, 'G<tspan dy=\"4\" font-size=\"11\">3</tspan>', '#38bdf8')
    s += arrow(448, ym, 500, ym)
    s += "<circle cx='500' cy='165' r='3.4' fill='#cbd5e1'/>"
    s += arrow(500, ym, 540, ym)
    s += txt(552, ym + 5, 'Y', '#e2e8f0', 15)
    # G2 en paralelo (desde n1 hasta sumador 2)
    s += box(210, 70, 70, 40, 'G<tspan dy=\"4\" font-size=\"11\">2</tspan>', '#a78bfa')
    s += line(150, ym, 150, 90); s += line(150, 90, 210, 90)
    s += line(280, 90, 322, 90); s += arrow(322, 90, 322, 150)
    # realimentación unitaria desde n2 a sumador 1
    s += line(500, ym, 500, 250); s += line(500, 250, 90, 250)
    s += arrow(90, 250, 90, 180)
    s += txt(300, 245, 'realimentación unitaria (H = 1)', '#94a3c0', 12, 'middle')
    return s + "</svg>"


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · Castilla y León · Ordinaria 2024 · Examen resuelto y comentado",
  "cabecera_titulo": "EBAU 2024 · <span>Tecnología e Ingeniería II</span> · Castilla y León · Ordinaria",
  "pill": "90 min · 2,5 pt/pregunta · elige 4 de 8",
  "enunciado_pdf": "../../examens/Castilla y Leon/Tecnologia_CastillayLeon_2024_ordinaria.pdf",
  "pdf_dir": "pdf_cyl_2024_ordinaria",
  "footer": "Dpto. Tecnología · Solucionario EBAU · Castilla y León · Tecnología e Ingeniería II (Ordinaria 2024)",
  "intro_inicio": "El alumno debe escoger <b>cuatro preguntas de las ocho</b> propuestas (90 minutos, cada pregunta 2,5 puntos). Aquí se resuelven <b>todas</b>. Selecciona un bloque o una pregunta en la barra lateral: cada una incluye el enunciado oficial, una introducción con los conceptos que se aplican y la solución paso a paso.",
  "indice_nombre": "Exámenes de Castilla y León",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Bloque 1 · Materiales y fabricación", "color": "#f59e0b",
   "descripcion_tarjeta": "Dimensionado de una barra de acero a tracción y análisis de un diagrama de fases isomorfo.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><path d='M10 50 Q20 15 45 12 T82 20'/><circle cx='45' cy='12' r='3' fill='#f59e0b' stroke='none'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Pregunta 1 · Barra de acero a tracción", "etiqueta": "MATERIALES",
     "menu": "P1 · Barra de acero a tracción", "titulo_corto": "P1",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 1,0 · b 0,5 · c 0,5)",
     "enunciado_html": "<p><b>Cuestión.</b> ¿Qué propiedad del material se evalúa en el ensayo Charpy? <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Una barra cilíndrica de acero (E = 20,7·10⁴ MPa) con límite elástico 310 MPa se somete a una carga de 11000 N. Si la longitud de la barra es 510 mm, determina:</p><ol type='a'><li>El diámetro necesario para permitir un alargamiento de 0,38 mm. <span class='pts'>(1 pto.)</span></li><li>La tensión necesaria para que la deformación sea 0,0005. <span class='pts'>(0,5 ptos.)</span></li><li>La longitud inicial que tendría que tener la barra para que el alargamiento en el límite elástico sea de 1 mm. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>En régimen elástico rige la ley de Hooke: \\(\\sigma=E\\varepsilon\\), con \\(\\sigma=F/A\\), \\(\\varepsilon=\\Delta L/L_0\\) y \\(A=\\pi D^2/4\\). Combinando, el alargamiento es \\(\\Delta L=\\dfrac{F\\,L_0}{A\\,E}\\).</p>",
     "solucion_html":
       "<h5>Cuestión · ensayo Charpy</h5>"
       "<p>El péndulo <b>Charpy</b> mide la <b>tenacidad</b> o <b>resiliencia</b> del material: la energía que absorbe una probeta entallada al romperse por impacto (resistencia al choque).</p>"
       "<h5>a) Diámetro para ΔL = 0,38 mm</h5>"
       "<div class='formula'>$$\\Delta L=\\frac{F\\,L_0}{A\\,E}\\ \\Rightarrow\\ A=\\frac{F\\,L_0}{\\Delta L\\,E}=\\frac{11000\\cdot510}{0{,}38\\cdot207000}=71{,}3\\ \\mathrm{mm^2}$$</div>"
       "<div class='formula'>$$A=\\frac{\\pi D^2}{4}\\ \\Rightarrow\\ D=\\sqrt{\\frac{4A}{\\pi}}=\\sqrt{\\frac{4\\cdot71{,}3}{\\pi}}=9{,}53\\ \\mathrm{mm}$$</div>"
       "<p>Comprobación: &sigma; = F/A = 11000/71,3 = 154 MPa < 310 MPa (elástico). ✓</p>"
       "<div class='res'><b>D ≈ 9,53 mm</b></div>"
       "<h5>b) Tensión para ε = 0,0005</h5>"
       "<div class='formula'>$$\\sigma=E\\,\\varepsilon=207000\\cdot0{,}0005=103{,}5\\ \\mathrm{MPa}$$</div>"
       "<div class='res'><b>&sigma; = 103,5 MPa</b></div>"
       "<h5>c) Longitud inicial para ΔL = 1 mm en el límite elástico</h5>"
       "<p>En el límite elástico \\(\\varepsilon_e=\\sigma_e/E=310/207000=1{,}498\\cdot10^{-3}\\).</p>"
       "<div class='formula'>$$\\Delta L=\\varepsilon_e\\,L_0\\ \\Rightarrow\\ L_0=\\frac{\\Delta L}{\\varepsilon_e}=\\frac{1}{1{,}498\\cdot10^{-3}}=667{,}7\\ \\mathrm{mm}$$</div>"
       "<div class='res'><b>L<sub>0</sub> ≈ 667,7 mm</b></div>"
    },
    {
     "id": "q2", "titulo": "Pregunta 2 · Diagrama de equilibrio isomorfo", "etiqueta": "MATERIALES",
     "menu": "P2 · Diagrama de fases A-B", "titulo_corto": "P2",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 0,4 · b 0,4 · c 0,6 · d 0,6)",
     "enunciado_html": "<p><b>Cuestión.</b> ¿Qué tipos de <i>campos</i> se pueden encontrar en los diagramas de equilibrio de fases? Explícalos brevemente. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Dos supuestos elementos metálicos A y B presentan el equilibrio de fases del diagrama. <i>(Se admiten valores aproximados.)</i></p><ol type='a'><li>Indica qué tipo de solubilidad tiene. <span class='pts'>(0,4 ptos.)</span></li><li>Indica las temperaturas de fusión de los metales puros. <span class='pts'>(0,4 ptos.)</span></li><li>Describe el enfriamiento desde 1000 °C hasta 700 °C de una aleación [A:B] 50:50, indicando campos, fases y temperaturas significativas. <span class='pts'>(0,6 ptos.)</span></li><li>Determina la proporción de fases a 900 °C en una aleación [A:B] 40:60. <span class='pts'>(0,6 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'><img src='" + FIG + "/cyl24ord_fases.png' alt='Diagrama de fases A-B' style='max-width:420px;width:100%;background:#fff;border-radius:8px;padding:8px'><figcaption>Diagrama de fases isomorfo A–B. Eje x en % A (izq. 0 % A = B puro; der. 100 % A). T<sub>f</sub>(B) ≈ 1050 °C, T<sub>f</sub>(A) ≈ 700 °C.</figcaption></figure>",
     "aplica_html": "<p>Es un diagrama <b>isomorfo</b>: dos líneas (<i>liquidus</i> arriba, <i>solidus</i> abajo) que delimitan tres <b>campos</b> (regiones): líquido (L), líquido+sólido (L+&alpha;) y sólido (&alpha;). Para las proporciones se usa la <b>regla de la palanca</b>.</p>",
     "solucion_html":
       "<h5>Cuestión · campos de un diagrama de fases</h5>"
       "<p>Un <b>campo</b> es una región del diagrama en la que existe una determinada fase o combinación de fases:</p><ul>"
       "<li><b>Campos monofásicos:</b> una sola fase (líquido L, o sólido &alpha;, &beta;…).</li>"
       "<li><b>Campos bifásicos:</b> coexisten dos fases (L+&alpha;, &alpha;+&beta;…).</li></ul>"
       "<p>Los campos están separados por las líneas <i>liquidus</i>, <i>solidus</i>, <i>solvus</i>, etc.</p>"
       "<h5>a) Tipo de solubilidad</h5>"
       "<p>El diagrama tiene una única lente sin puntos eutécticos → los metales son <b>totalmente solubles</b> en estado líquido y sólido (aleación <b>isomorfa</b>, forman la solución sólida &alpha;).</p>"
       "<div class='res'><b>Solubilidad total (isomorfo)</b></div>"
       "<h5>b) Temperaturas de fusión de los metales puros</h5>"
       "<p>Extremos de la lente: a la izquierda (100 % B) ≈ 1050 °C; a la derecha (100 % A) ≈ 700 °C.</p>"
       "<div class='res'><b>T<sub>f</sub>(B) ≈ 1050 °C&nbsp;·&nbsp;T<sub>f</sub>(A) ≈ 700 °C</b></div>"
       "<h5>c) Enfriamiento de la aleación 50:50 de 1000 °C a 700 °C</h5>"
       "<ul><li><b>1000 °C:</b> por encima del liquidus → <b>campo L</b>, todo líquido.</li>"
       "<li><b>≈ 900 °C (liquidus):</b> comienza la solidificación; aparecen los primeros cristales de &alpha;. Se entra en el <b>campo L+&alpha;</b>.</li>"
       "<li><b>900 → ≈ 780 °C:</b> coexisten L y &alpha;; al enfriar aumenta la fracción de sólido.</li>"
       "<li><b>≈ 780 °C (solidus):</b> solidifica la última gota → <b>campo &alpha;</b>, todo sólido.</li>"
       "<li><b>780 → 700 °C:</b> enfriamiento del sólido &alpha; sin cambio de fase.</li></ul>"
       "<p style='color:#94a3c0;font-size:.85rem'>(Temperaturas leídas del diagrama, aproximadas.)</p>"
       "<h5>d) Proporción de fases a 900 °C con 40 % A</h5>"
       "<p>A 900 °C la isoterma corta el liquidus en ≈ 28 % A (líquido) y el solidus en ≈ 63 % A (sólido &alpha;). Regla de la palanca con C<sub>0</sub> = 40 % A:</p>"
       "<div class='formula'>$$\\%\\,L=\\frac{C_\\alpha-C_0}{C_\\alpha-C_L}=\\frac{63-40}{63-28}=\\frac{23}{35}\\approx66\\%$$</div>"
       "<div class='formula'>$$\\%\\,\\alpha=\\frac{C_0-C_L}{C_\\alpha-C_L}=\\frac{40-28}{35}\\approx34\\%$$</div>"
       "<div class='res'><b>≈ 66 % líquido y ≈ 34 % sólido &alpha;</b> (valores aproximados)</div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Bloque 2 · Sistemas mecánicos", "color": "#22d3ee",
   "descripcion_tarjeta": "Viga con carga puntual, bomba de calor de Carnot e instalación neumática de una puerta de garaje.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><path d='M8 34h74'/><path d='M45 12v18'/><path d='M40 18l5-6 5 6'/><path d='M8 34l-4 8h8zM82 34a5 5 0 1 0 0 8'/></svg>",
   "cuestiones": [
    {
     "id": "q3", "titulo": "Pregunta 3 · Estructuras: viga con voladizo", "etiqueta": "MECÁNICA",
     "menu": "P3 · Viga con carga puntual", "titulo_corto": "P3",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 0,5 · b 0,75 · c 0,5)",
     "enunciado_html": "<p><b>Cuestión.</b> Explica qué es una estructura. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> La viga de la figura tiene aplicada la fuerza indicada (P = 1000 N).</p><ol type='a'><li>Calcula las reacciones en los apoyos. <span class='pts'>(0,5 ptos.)</span></li><li>Calcula los esfuerzos cortantes y momentos flectores. <span class='pts'>(0,75 ptos.)</span></li><li>Representa los diagramas de esfuerzos axiales, cortantes y momentos flectores. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_viga() + "<figcaption>Viga apoyada en A y C (5 m) con carga puntual P = 1000 N en B, a 3 m de A.</figcaption></figure>",
     "aplica_html": "<p>La viga está en equilibrio: \\(\\sum F=0\\), \\(\\sum M=0\\). Con la carga vertical no hay esfuerzo axial (N = 0). El cortante V y el momento M se obtienen sección a sección; M es máximo bajo la carga.</p>",
     "solucion_html":
       "<h5>Cuestión · ¿qué es una estructura?</h5>"
       "<p>Una <b>estructura</b> es el conjunto de elementos resistentes, unidos entre sí, cuya misión es <b>soportar cargas</b> (peso propio y externas) y transmitirlas a los apoyos manteniendo la forma, sin romperse ni deformarse excesivamente.</p>"
       "<h5>a) Reacciones</h5>"
       "<p>\\(\\sum M_A=0\\): \\(R_C\\cdot5=1000\\cdot3\\Rightarrow R_C=600\\ \\mathrm N\\). \\(\\sum F_y=0\\): \\(R_A=1000-600=400\\ \\mathrm N\\).</p>"
       "<div class='res'><b>R<sub>A</sub> = 400 N&nbsp;·&nbsp;R<sub>C</sub> = 600 N</b> (N = 0, no hay esfuerzo axial)</div>"
       "<h5>b) Cortantes y momentos</h5>"
       "<p><b>Cortante:</b> A–B (0–3 m): V = +400 N. B–C (3–5 m): V = 400 − 1000 = −600 N.</p>"
       "<p><b>Momento:</b> en A, M = 0. Bajo la carga (x = 3 m): M<sub>B</sub> = 400·3 = 1200 N·m. En C, M = 0.</p>"
       "<div class='res'><b>V = +400 / −600 N&nbsp;·&nbsp;M<sub>máx</sub> = 1200 N·m (en B)</b></div>"
       "<h5>c) Diagramas</h5>"
       "<figure class='fig'>" + fig_V() + "<figcaption>Cortante: +400 N hasta B y −600 N hasta C.</figcaption></figure>"
       "<figure class='fig'>" + fig_M() + "<figcaption>Momento flector: 0 en A, 1200 N·m en B y 0 en C (el axial es nulo).</figcaption></figure>"
    },
    {
     "id": "q4", "titulo": "Pregunta 4 · Máquinas térmicas: bomba de calor", "etiqueta": "MECÁNICA",
     "menu": "P4 · Bomba de calor (Carnot)", "titulo_corto": "P4",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 0,75 · b 0,5 · c 0,75)",
     "enunciado_html": "<p><b>Cuestión.</b> Indica las diferencias entre un motor de explosión y un motor de encendido por compresión. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Un local con temperatura exterior media 6 °C necesita una bomba de calor de <b>10 kW</b> de potencia para mantener el interior a 25 °C. Funcionando según un ciclo de Carnot reversible, calcula:</p><ol type='a'><li>La eficiencia de la máquina. <span class='pts'>(0,75 ptos.)</span></li><li>La potencia aportada al interior del local. <span class='pts'>(0,5 ptos.)</span></li><li>La potencia retirada al exterior del local. <span class='pts'>(0,75 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>La eficiencia (COP) de una bomba de calor de Carnot es \\(\\mathrm{COP}=\\dfrac{T_c}{T_c-T_f}\\) (temperaturas en kelvin). El calor aportado al foco caliente es \\(\\dot Q_c=\\mathrm{COP}\\cdot\\dot W\\) y, por el balance de energía, \\(\\dot Q_f=\\dot Q_c-\\dot W\\).</p>",
     "solucion_html":
       "<h5>Cuestión · explosión vs. encendido por compresión</h5>"
       "<p>El <b>motor de explosión (Otto / MEP)</b> usa gasolina, comprime mezcla aire-combustible y la enciende con <b>bujía</b> (chispa); menor relación de compresión. El <b>motor de encendido por compresión (Diésel / MEC)</b> usa gasóleo, comprime solo aire hasta alta presión/temperatura y el combustible se <b>autoinflama</b> al inyectarse; mayor relación de compresión y rendimiento.</p>"
       "<h5>a) Eficiencia (COP)</h5>"
       "<p>T<sub>c</sub> = 25 °C = 298 K, T<sub>f</sub> = 6 °C = 279 K.</p>"
       "<div class='formula'>$$\\mathrm{COP}=\\frac{T_c}{T_c-T_f}=\\frac{298}{298-279}=\\frac{298}{19}=15{,}68$$</div>"
       "<div class='res'><b>COP ≈ 15,68</b></div>"
       "<h5>b) Potencia aportada al interior</h5>"
       "<div class='formula'>$$\\dot Q_c=\\mathrm{COP}\\cdot\\dot W=15{,}68\\cdot10=156{,}8\\ \\mathrm{kW}$$</div>"
       "<div class='res'><b>Q̇<sub>c</sub> ≈ 156,8 kW</b></div>"
       "<h5>c) Potencia retirada al exterior</h5>"
       "<div class='formula'>$$\\dot Q_f=\\dot Q_c-\\dot W=156{,}8-10=146{,}8\\ \\mathrm{kW}$$</div>"
       "<div class='res'><b>Q̇<sub>f</sub> ≈ 146,8 kW</b></div>"
    },
    {
     "id": "q5", "titulo": "Pregunta 5 · Neumática: puerta de garaje", "etiqueta": "MECÁNICA",
     "menu": "P5 · Instalación neumática", "titulo_corto": "P5",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 1,0 · b 0,5 · c 0,5)",
     "enunciado_html": "<p><b>Cuestión.</b> Cita 3 ventajas de los sistemas oleohidráulicos frente a los neumáticos. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Observa el esquema de la instalación neumática (accionamiento de una puerta de garaje).</p><ol type='a'><li>Identifica sus componentes. <span class='pts'>(1 pto.)</span></li><li>Explica cómo se activa la carrera de avance. <span class='pts'>(0,5 ptos.)</span></li><li>Si se emplea para abrir/cerrar una puerta de garaje, ¿qué ocurre si la puerta encuentra un obstáculo al cerrar? <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'><img src='" + FIG + "/cyl24ord_neumatica.png' alt='Instalación neumática' style='max-width:460px;width:100%;background:#fff;border-radius:8px;padding:8px'><figcaption>Cilindro de doble efecto (1.0), distribuidor 5/2 con doble pilotaje (1.1), reguladoras de caudal (1.02, 1.03), válvula selectora (1.01) y finales de carrera/pulsadores (1.2, 1.4).</figcaption></figure>",
     "aplica_html": "<p>Identificamos el actuador (cilindro), el distribuidor que lo gobierna, las válvulas de mando (pulsadores y finales de carrera 3/2) y los elementos de regulación. La carrera de avance se activa al pilotar el distribuidor por un lado.</p>",
     "solucion_html":
       "<h5>Cuestión · ventajas de la oleohidráulica frente a la neumática</h5><ul>"
       "<li>Desarrolla <b>fuerzas mucho mayores</b> (el aceite es prácticamente incompresible y trabaja a alta presión).</li>"
       "<li>Movimientos más <b>precisos y uniformes</b>, sin la elasticidad del aire comprimido.</li>"
       "<li>Permite <b>mantener cargas</b> de forma estable y posicionar con exactitud (mejor control de velocidad y posición).</li></ul>"
       "<h5>a) Componentes</h5><ul>"
       "<li><b>1.0</b> — Cilindro de <b>doble efecto</b> (mueve la puerta; flecha CIERRE indica el sentido).</li>"
       "<li><b>1.1</b> — <b>Distribuidor 5/2</b> con doble pilotaje neumático (memoria): dirige el aire a una u otra cámara.</li>"
       "<li><b>1.02 y 1.03</b> — Válvulas <b>reguladoras de caudal unidireccionales</b>: ajustan la velocidad de avance y de cierre.</li>"
       "<li><b>1.01</b> — Válvula <b>selectora (función OR)</b> que combina las señales de mando.</li>"
       "<li><b>1.2 y 1.4</b> — Válvulas <b>3/2</b> de accionamiento manual (pulsador) / final de carrera con retorno por muelle.</li></ul>"
       "<h5>b) Activación de la carrera de avance</h5>"
       "<p>Al accionar el <b>pulsador</b> correspondiente (p. ej. 1.2), se envía una señal de aire que <b>pilota el distribuidor 1.1</b> por un extremo; éste conmuta y deja pasar el aire a la cámara trasera del cilindro, que <b>avanza</b>. Por ser un distribuidor con memoria, mantiene la posición hasta recibir la señal contraria.</p>"
       "<h5>c) Obstáculo al cerrar</h5>"
       "<p>Si la puerta encuentra un obstáculo, el cilindro no puede completar su carrera: la presión sube pero <b>no llega a accionarse el final de carrera</b> que ordenaría el cambio, por lo que el sistema se queda bloqueado empujando. En una instalación de seguridad, el aumento de presión (o un detector) invertiría el distribuidor para <b>reabrir</b> la puerta y evitar el atrapamiento.</p>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Bloque 3 · Sistemas eléctricos y electrónicos", "color": "#a78bfa",
   "descripcion_tarjeta": "Circuito RLC serie (resistencia, factor de potencia, balance) y simplificación de una función de 4 variables por Karnaugh.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M8 30h12l4-10 8 20 8-20 8 20 4-10h26'/></svg>",
   "cuestiones": [
    {
     "id": "q6", "titulo": "Pregunta 6 · Corriente alterna: RLC serie", "etiqueta": "ELECTRICIDAD",
     "menu": "P6 · Circuito RLC serie", "titulo_corto": "P6",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a-d 0,5 c/u)",
     "enunciado_html": "<p><b>Cuestión.</b> Define la fuerza contraelectromotriz de un motor y la expresión que permite su cálculo. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> En un circuito serie por el que circula una corriente eficaz de 2 A hay una resistencia, una bobina de 0,2 H y un condensador de 25 µF. Con 230 V eficaces y 50 Hz, calcula:</p><ol type='a'><li>La resistencia del circuito. <span class='pts'>(0,5 ptos.)</span></li><li>El factor de potencia. <span class='pts'>(0,5 ptos.)</span></li><li>El balance de potencias (activa, reactiva, aparente). <span class='pts'>(0,5 ptos.)</span></li><li>Dibuja el triángulo de potencias. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_ac() + "<figcaption>Circuito serie R–L–C alimentado a 230 V / 50 Hz, con I = 2 A.</figcaption></figure>",
     "aplica_html": "<p>Reactancias: \\(X_L=2\\pi f L\\), \\(X_C=\\dfrac{1}{2\\pi f C}\\). La impedancia total es \\(Z=V/I=\\sqrt{R^2+(X_L-X_C)^2}\\), de donde se despeja R. El factor de potencia es \\(\\cos\\varphi=R/Z\\). Potencias: \\(P=I^2R\\), \\(Q=I^2(X_L-X_C)\\), \\(S=V\\,I\\).</p>",
     "solucion_html":
       "<h5>Cuestión · fuerza contraelectromotriz</h5>"
       "<p>La <b>fuerza contraelectromotriz (fcem)</b> es la tensión que genera un motor al girar y que se <b>opone</b> a la tensión de alimentación (ley de Lenz). Su valor: \\(E'=V-I\\,R_i\\) (tensión menos la caída en la resistencia del inducido), o bien \\(E'=k\\,\\phi\\,n\\), proporcional al flujo y a la velocidad de giro.</p>"
       "<h5>a) Resistencia del circuito</h5>"
       "<div class='formula'>$$X_L=2\\pi f L=2\\pi\\cdot50\\cdot0{,}2=62{,}83\\ \\Omega\\qquad X_C=\\frac{1}{2\\pi f C}=\\frac{1}{2\\pi\\cdot50\\cdot25\\cdot10^{-6}}=127{,}32\\ \\Omega$$</div>"
       "<div class='formula'>$$Z=\\frac{V}{I}=\\frac{230}{2}=115\\ \\Omega\\ \\Rightarrow\\ R=\\sqrt{Z^2-(X_L-X_C)^2}=\\sqrt{115^2-64{,}49^2}=95{,}2\\ \\Omega$$</div>"
       "<div class='res'><b>R ≈ 95,2 Ω</b></div>"
       "<h5>b) Factor de potencia</h5>"
       "<div class='formula'>$$\\cos\\varphi=\\frac{R}{Z}=\\frac{95{,}2}{115}=0{,}828\\quad(\\varphi=-34{,}1^\\circ,\\ \\text{capacitivo: } X_C>X_L)$$</div>"
       "<div class='res'><b>cos&phi; ≈ 0,83 (en adelanto, capacitivo)</b></div>"
       "<h5>c) Balance de potencias</h5>"
       "<div class='formula'>$$P=I^2R=2^2\\cdot95{,}2=380{,}9\\ \\mathrm W$$</div>"
       "<div class='formula'>$$Q=I^2(X_L-X_C)=4\\cdot(-64{,}49)=-258\\ \\mathrm{VAr}\\ (\\text{capacitiva})$$</div>"
       "<div class='formula'>$$S=V\\,I=230\\cdot2=460\\ \\mathrm{VA}\\quad(\\sqrt{P^2+Q^2}\\approx460)$$</div>"
       "<div class='res'><b>P ≈ 380,9 W · Q ≈ −258 VAr · S = 460 VA</b></div>"
       "<h5>d) Triángulo de potencias</h5>"
       "<figure class='fig'>" + fig_triangulo() + "<figcaption>Circuito capacitivo: la potencia reactiva Q queda por debajo de la activa P.</figcaption></figure>"
    },
    {
     "id": "q7", "titulo": "Pregunta 7 · Electrónica digital: Karnaugh 4 variables", "etiqueta": "ELECTRÓNICA",
     "menu": "P7 · Karnaugh de 4 variables", "titulo_corto": "P7",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a-d 0,5 c/u)",
     "enunciado_html": "<p><b>Cuestión.</b> Define las funciones elementales NOT y XOR, con sus ecuaciones lógicas, tablas de verdad y la diferencia entre ellas. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Dada la tabla de verdad de 4 entradas (W, X, Y, Z) y salida F, donde F = 1 sólo para WXYZ = 1110 y 1111:</p><ol type='a'><li>Simplifícala con mapas de Karnaugh. <span class='pts'>(0,5 ptos.)</span></li><li>Expresión booleana simplificada. <span class='pts'>(0,5 ptos.)</span></li><li>Circuito equivalente con puertas AND. <span class='pts'>(0,5 ptos.)</span></li><li>Circuito equivalente con puertas OR y NOT (NOR de cualquier nº de entradas). <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>La salida vale 1 únicamente en dos casillas adyacentes del mapa (WXYZ = 1110 y 1111), que se agrupan eliminando la variable Z. El resto es álgebra de Boole para pasar a AND o a OR/NOT.</p>",
     "solucion_html":
       "<h5>Cuestión · NOT y XOR</h5>"
       "<p><b>NOT (negación):</b> una entrada; invierte el valor. \\(F=\\overline A\\).</p>"
       "<table class='dat'><tr><th>A</th><th>NOT A</th></tr><tr><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td></tr></table>"
       "<p><b>XOR (o-exclusiva):</b> dos entradas; vale 1 si son <b>distintas</b>. \\(F=A\\oplus B=\\bar A B+A\\bar B\\).</p>"
       "<table class='dat'><tr><th>A</th><th>B</th><th>A⊕B</th></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td></tr></table>"
       "<p><b>Diferencia:</b> NOT tiene una sola entrada (inversor); XOR compara dos entradas y detecta desigualdad.</p>"
       "<h5>a) y b) Simplificación por Karnaugh</h5>"
       "<p>Los únicos 1 están en WXYZ = 1110 y 1111 (minitérminos 14 y 15), casillas adyacentes que difieren sólo en Z. Al agruparlas se elimina Z:</p>"
       "<div class='formula'>$$F=W\\,X\\,Y\\,\\overline Z+W\\,X\\,Y\\,Z=W\\,X\\,Y$$</div>"
       "<div class='res'><b>F = W · X · Y</b></div>"
       "<h5>c) Circuito con puertas AND</h5>"
       "<p>Basta una puerta <b>AND de 3 entradas</b> (o dos AND de 2 entradas encadenadas): \\(F=(W\\cdot X)\\cdot Y\\).</p>"
       "<h5>d) Circuito con OR y NOT (NOR)</h5>"
       "<p>Por De Morgan: \\(F=W X Y=\\overline{\\overline W+\\overline X+\\overline Y}\\). Se invierten W, X, Y (tres NOT) y se llevan a una <b>NOR de 3 entradas</b>:</p>"
       "<div class='formula'>$$F=\\overline{\\ \\overline W+\\overline X+\\overline Y\\ }=\\mathrm{NOR}(\\overline W,\\overline X,\\overline Y)$$</div>"
       "<div class='res'><b>3 inversores (NOT) + 1 puerta NOR de 3 entradas</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Bloque 4 · Sistemas emergentes y control", "color": "#4ade80",
   "descripcion_tarjeta": "Sesgos en IA, sensores en lazo cerrado y función de transferencia de un diagrama de bloques.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#4ade80' stroke-width='3'><rect x='34' y='22' width='24' height='16' rx='3'/><path d='M8 30h26M58 30h24'/><circle cx='20' cy='30' r='6'/></svg>",
   "cuestiones": [
    {
     "id": "q8", "titulo": "Pregunta 8 · Sistemas de control: función de transferencia", "etiqueta": "CONTROL",
     "menu": "P8 · Función de transferencia Y/R", "titulo_corto": "P8",
     "meta": "Pregunta de 2,5 puntos (a 0,5 · b 0,5 · problema 1,5)",
     "enunciado_html": "<p><b>Cuestiones.</b></p><ol type='a'><li>Dentro de la IA, ¿a qué se refieren los <i>sesgos</i>? Pon un ejemplo de sesgo en una aplicación práctica. <span class='pts'>(0,5 ptos.)</span></li><li>Explica para qué se utiliza un sensor en un sistema de control en lazo cerrado. <span class='pts'>(0,5 ptos.)</span></li></ol><p><b>Problema.</b> Calcula la función de transferencia Y(s)/R(s) del sistema de control cuyo diagrama de bloques se muestra en la figura. <span class='pts'>(1,5 ptos.)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloques_yr() + "<figcaption>G<sub>1</sub> y G<sub>2</sub> en paralelo, seguidos de G<sub>3</sub>, con realimentación unitaria negativa.</figcaption></figure>",
     "aplica_html": "<p>Se simplifica: las ramas en <b>paralelo</b> G<sub>1</sub> y G<sub>2</sub> se suman (G<sub>1</sub>+G<sub>2</sub>); en serie con G<sub>3</sub> quedan G<sub>3</sub>(G<sub>1</sub>+G<sub>2</sub>); el lazo con realimentación unitaria negativa da \\(\\dfrac{G}{1+G}\\).</p>",
     "solucion_html":
       "<h5>a) Sesgos en IA</h5>"
       "<p>Un <b>sesgo (bias)</b> es una desviación sistemática en los resultados de un modelo de IA, normalmente heredada de datos de entrenamiento poco representativos o de prejuicios humanos. <b>Ejemplo:</b> un sistema de selección de currículos entrenado con datos históricos que descarta candidatas mujeres porque en el pasado se contrataba mayoritariamente a hombres.</p>"
       "<h5>b) Sensor en lazo cerrado</h5>"
       "<p>El <b>sensor</b> mide la variable de salida (la magnitud controlada) y la convierte en una señal que se <b>realimenta</b> al comparador. Así el sistema conoce el valor real de la salida, calcula el <b>error</b> respecto a la referencia y lo corrige. Sin sensor no habría realimentación.</p>"
       "<h5>Problema · función de transferencia Y/R</h5>"
       "<p>Sea X la salida del primer sumador: \\(X=R-Y\\). Las ramas G<sub>1</sub> y G<sub>2</sub> parten del mismo punto y se suman:</p>"
       "<div class='formula'>$$\\text{tras el 2.º sumador: } (G_1+G_2)\\,X \\quad\\Rightarrow\\quad Y=G_3\\,(G_1+G_2)\\,X=G_3(G_1+G_2)(R-Y)$$</div>"
       "<div class='formula'>$$Y\\big[1+G_3(G_1+G_2)\\big]=G_3(G_1+G_2)\\,R$$</div>"
       "<div class='formula'>$$\\boxed{\\ \\dfrac{Y(s)}{R(s)}=\\dfrac{G_3\\,(G_1+G_2)}{1+G_3\\,(G_1+G_2)}\\ }$$</div>"
       "<div class='res'><b>Y/R = G<sub>3</sub>(G<sub>1</sub>+G<sub>2</sub>) / [1 + G<sub>3</sub>(G<sub>1</sub>+G<sub>2</sub>)]</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cyl_2024_ordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
