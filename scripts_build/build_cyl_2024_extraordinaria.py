#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Castilla y León EBAU 2024 · Extraordinaria (Propuesta 6)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt
from cyllib import beam, diagram_VM, ac_parallel, power_triangle, phase_eutectic

FIG = "fig"


def fig_eutectic():
    return phase_eutectic(TfL=1250, TfR=1125, xe=60, Te=950, ymin=600, ymax=1350,
                          left='A', right='B', yticks=[600, 700, 800, 900, 950, 1100, 1250])


def fig_viga():
    return beam(loads=[{'type': 'q', 'x0': 0, 'x1': 10, 'val': 'W = 1000 N/m'}],
                supports=[{'xm': 0, 'kind': 'roller', 'label': 'A'},
                          {'xm': 10, 'kind': 'pin', 'label': 'B'}],
                span_m=10, dims=[(0, 10, '10 m')])


def fig_V():
    return diagram_VM([(0, 5000), (10, -5000)], 10, kind='V', unit='N',
                      title='Esfuerzo cortante V (N)')


def fig_M():
    pts = [(x, 5000 * x - 500 * x * x) for x in range(0, 11)]
    return diagram_VM(pts, 10, kind='M', unit='N·m', title='Momento flector M (N·m)')


def fig_ac():
    return ac_parallel([('R', '800 Ω'), ('L', 'X_L = 62,83 Ω')], V='230 V', f='50 Hz')


def fig_triangulo():
    return power_triangle(66.1, 842.0, 844.5, 85.5, inductive=True,
                          labels={'P': 'P = 66,1 W', 'Q': 'Q = 842 VAr (ind.)', 'S': 'S = 844,5 VA'})


def fig_bloques_ext():
    """P8: Y/R = G1(1+G2)/(1+G1(1+G2)H1)."""
    s = svg_open('720 300', 640)
    ym = 150
    s += txt(24, ym + 5, 'R', '#e2e8f0', 15)
    s += arrow(40, ym, 74, ym)
    s += summer(90, ym)
    s += txt(74, ym - 12, '+', '#4ade80', 15); s += txt(78, ym + 30, '−', '#fb7185', 17)
    s += arrow(106, ym, 150, ym)
    s += box(150, 128, 70, 44, 'G<tspan dy=\"4\" font-size=\"11\">1</tspan>', '#22d3ee')
    s += arrow(220, ym, 262, ym)
    s += "<circle cx='262' cy='150' r='3.4' fill='#cbd5e1'/>"      # nodo tras G1
    s += arrow(262, ym, 300, ym)
    s += box(300, 128, 70, 44, 'G<tspan dy=\"4\" font-size=\"11\">2</tspan>', '#a78bfa')
    s += arrow(370, ym, 418, ym)
    s += summer(434, ym)
    s += txt(416, ym + 30, '+', '#4ade80', 15); s += txt(446, ym - 12, '+', '#4ade80', 15)
    s += arrow(450, ym, 500, ym)
    s += "<circle cx='500' cy='150' r='3.4' fill='#cbd5e1'/>"
    s += arrow(500, ym, 540, ym)
    s += txt(552, ym + 5, 'Y', '#e2e8f0', 15)
    # feedforward (unidad) desde nodo tras G1 hasta sumador 2
    s += line(262, ym, 262, 80); s += line(262, 80, 434, 80); s += arrow(434, 80, 434, 135)
    # H1 desde salida a sumador 1
    s += box(240, 228, 70, 40, 'H<tspan dy=\"4\" font-size=\"11\">1</tspan>', '#38bdf8')
    s += line(500, ym, 500, 248); s += line(500, 248, 310, 248)
    s += line(240, 248, 90, 248); s += arrow(90, 248, 90, 165)
    return s + "</svg>"


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · Castilla y León · Extraordinaria 2024 · Examen resuelto y comentado",
  "cabecera_titulo": "EBAU 2024 · <span>Tecnología e Ingeniería II</span> · Castilla y León · Extraordinaria",
  "pill": "90 min · 2,5 pt/pregunta · elige 4 de 8",
  "enunciado_pdf": "../../examens/Castilla y Leon/Tecnologia_CastillayLeon_2024_extraordinaria.pdf",
  "pdf_dir": "pdf_cyl_2024_extraordinaria",
  "footer": "Dpto. Tecnología · Solucionario EBAU · Castilla y León · Tecnología e Ingeniería II (Extraordinaria 2024)",
  "intro_inicio": "El alumno debe escoger <b>cuatro preguntas de las ocho</b> propuestas (90 minutos, cada pregunta 2,5 puntos). Aquí se resuelven <b>todas</b>. Selecciona un bloque o una pregunta en la barra lateral: cada una incluye el enunciado oficial, una introducción con los conceptos que se aplican y la solución paso a paso.",
  "indice_nombre": "Exámenes de Castilla y León",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Bloque 1 · Materiales y fabricación", "color": "#f59e0b",
   "descripcion_tarjeta": "Ensayo de tracción de una barra de aluminio (curva real) y diagrama de fases eutéctico.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><path d='M10 50 Q16 18 30 15 T82 24'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Pregunta 1 · Tracción de una barra de aluminio", "etiqueta": "MATERIALES",
     "menu": "P1 · Tracción (aluminio)", "titulo_corto": "P1",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a-d 0,5 c/u)",
     "enunciado_html": "<p><b>Cuestión.</b> ¿Qué parámetro del ensayo de tracción indica la ductilidad del material? <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Una barra de aluminio de 127 mm de longitud con sección cuadrada de 16,5 mm de lado se somete a un ensayo de tracción (figura).</p><ol type='a'><li>Determina el alargamiento máximo de la barra. <span class='pts'>(0,5 ptos.)</span></li><li>Si se somete a una carga de 6,67·10⁴ N, determina su alargamiento. <span class='pts'>(0,5 ptos.)</span></li><li>El alargamiento cuando se alcance la tensión máxima. <span class='pts'>(0,5 ptos.)</span></li><li>La tensión necesaria para que el alargamiento sea de 1,27 mm. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'><img src='" + FIG + "/cyl24ext_traccion.png' alt='Curva tensión-deformación del aluminio' style='max-width:480px;width:100%;background:#fff;border-radius:8px;padding:8px'><figcaption>Curva tensión (MPa) – deformación del aluminio. Sección A = 16,5² = 272,25 mm². Los valores se leen sobre la gráfica.</figcaption></figure>",
     "aplica_html": "<p>Sección \\(A=16{,}5^2=272{,}25\\ \\mathrm{mm^2}\\). La deformación es \\(\\varepsilon=\\Delta L/L_0\\Rightarrow\\Delta L=\\varepsilon\\,L_0\\). La tensión \\(\\sigma=F/A\\). En la zona elástica \\(\\varepsilon=\\sigma/E\\) (E ≈ 69 GPa, pendiente inicial); en la zona plástica se lee directamente de la curva.</p>",
     "solucion_html":
       "<h5>Cuestión · parámetro que indica la ductilidad</h5>"
       "<p>El <b>alargamiento a la rotura</b> (deformación máxima, % de elongación) y la <b>estricción</b> (reducción de sección). Cuanto mayores son, más dúctil es el material.</p>"
       "<h5>a) Alargamiento máximo</h5>"
       "<p>El alargamiento máximo se da en la rotura, cuya deformación (fin de la curva) es \\(\\varepsilon_{\\max}\\approx0{,}16\\):</p>"
       "<div class='formula'>$$\\Delta L_{\\max}=\\varepsilon_{\\max}\\,L_0\\approx0{,}16\\cdot127=20{,}3\\ \\mathrm{mm}$$</div>"
       "<div class='res'><b>ΔL<sub>máx</sub> ≈ 20 mm</b> (ε<sub>rotura</sub> ≈ 0,16)</div>"
       "<h5>b) Alargamiento con F = 6,67·10⁴ N</h5>"
       "<div class='formula'>$$\\sigma=\\frac{F}{A}=\\frac{66700}{272{,}25}=245\\ \\mathrm{MPa}$$</div>"
       "<p>245 MPa está en la zona elástica (por debajo del límite). Con E ≈ 69 GPa (pendiente inicial): \\(\\varepsilon=\\sigma/E=245/69000=3{,}55\\cdot10^{-3}\\).</p>"
       "<div class='formula'>$$\\Delta L=\\varepsilon\\,L_0=3{,}55\\cdot10^{-3}\\cdot127\\approx0{,}45\\ \\mathrm{mm}$$</div>"
       "<div class='res'><b>ΔL ≈ 0,45 mm</b></div>"
       "<h5>c) Alargamiento a la tensión máxima</h5>"
       "<p>La tensión máxima (resistencia a la tracción) se alcanza en el punto más alto de la curva, con deformación \\(\\varepsilon\\approx0{,}10\\):</p>"
       "<div class='formula'>$$\\Delta L=\\varepsilon\\,L_0\\approx0{,}10\\cdot127=12{,}7\\ \\mathrm{mm}$$</div>"
       "<div class='res'><b>ΔL ≈ 12,7 mm</b> (a σ<sub>máx</sub> ≈ 365 MPa)</div>"
       "<h5>d) Tensión para ΔL = 1,27 mm</h5>"
       "<div class='formula'>$$\\varepsilon=\\frac{\\Delta L}{L_0}=\\frac{1{,}27}{127}=0{,}01\\ (1\\%)$$</div>"
       "<p>ε = 0,01 cae en la zona plástica; leyendo la curva, la tensión correspondiente es \\(\\sigma\\approx300\\ \\mathrm{MPa}\\).</p>"
       "<div class='res'><b>&sigma; ≈ 300 MPa</b> (lectura sobre la gráfica)</div>"
    },
    {
     "id": "q2", "titulo": "Pregunta 2 · Diagrama de equilibrio eutéctico", "etiqueta": "MATERIALES",
     "menu": "P2 · Diagrama eutéctico", "titulo_corto": "P2",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 0,5 · b 0,5 · c 1,0)",
     "enunciado_html": "<p><b>Cuestión.</b> ¿Qué tipos de <i>líneas</i> se pueden encontrar en los diagramas de equilibrio de fases? Explícalas brevemente. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Dos elementos A y B totalmente solubles en estado líquido y completamente insolubles en estado sólido, que forman eutéctico (diagrama). <i>(Se admiten valores aproximados.)</i></p><ol type='a'><li>Indica gráficamente las líneas, regiones y puntos significativos. <span class='pts'>(0,5 ptos.)</span></li><li>¿Cómo se llama la aleación [A:B] 40:60 y cuáles son sus características? <span class='pts'>(0,5 ptos.)</span></li><li>Una mezcla [A:B] 80:20 se calienta hasta fusión y se enfría lentamente. Analiza las fases a 1250 °C, 1100 °C y 800 °C. <span class='pts'>(1 pto.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_eutectic() + "<figcaption>Diagrama eutéctico A–B (eje x en % B). T<sub>f</sub>(A)=1250 °C, T<sub>f</sub>(B)=1125 °C. Punto eutéctico E: 60 % B, 950 °C.</figcaption></figure>",
     "aplica_html": "<p>Es un <b>diagrama eutéctico</b> con insolubilidad total en sólido: dos ramas de <i>liquidus</i> que bajan hasta el <b>punto eutéctico E</b> y una <b>línea eutéctica</b> horizontal (solidus). Debajo, mezcla de los sólidos puros A + B. Para las proporciones se usa la <b>regla de la palanca</b>.</p>",
     "solucion_html":
       "<h5>Cuestión · tipos de líneas</h5><ul>"
       "<li><b>Liquidus:</b> por encima de ella todo es líquido; marca el inicio de la solidificación.</li>"
       "<li><b>Solidus:</b> por debajo todo es sólido; marca el fin de la solidificación (aquí, la línea eutéctica).</li>"
       "<li><b>Solvus:</b> límite de solubilidad en estado sólido (no aparece si son insolubles).</li>"
       "<li><b>Línea eutéctica:</b> isoterma donde L → A + B simultáneamente.</li></ul>"
       "<h5>a) Líneas, regiones y puntos</h5><ul>"
       "<li><b>Liquidus:</b> las dos rectas que bajan desde T<sub>f</sub>(A)=1250 °C y T<sub>f</sub>(B)=1125 °C hasta E.</li>"
       "<li><b>Punto eutéctico E:</b> 60 % B, 950 °C (mínima temperatura de fusión).</li>"
       "<li><b>Línea eutéctica:</b> horizontal a 950 °C.</li>"
       "<li><b>Regiones:</b> L (líquido) arriba; L+A a la izquierda de E; L+B a la derecha; A+B (sólidos) debajo de 950 °C.</li></ul>"
       "<h5>b) Aleación [A:B] 40:60</h5>"
       "<p>Es 60 % B, exactamente la composición del punto E: es la <b>aleación eutéctica</b>. Características: tiene la <b>temperatura de fusión más baja</b> (950 °C), solidifica <b>a temperatura constante</b> (como un metal puro) transformándose el líquido directamente en una <b>mezcla íntima y fina de cristales de A y B</b>.</p>"
       "<div class='res'><b>Aleación eutéctica (60 % B, funde/solidifica a 950 °C)</b></div>"
       "<h5>c) Enfriamiento de [A:B] 80:20 (20 % B)</h5>"
       "<ul><li><b>1250 °C:</b> el liquidus a 20 % B está en ≈ 1150 °C; a 1250 °C estamos por encima → <b>todo líquido (L)</b>.</li>"
       "<li><b>1100 °C:</b> región <b>L + A</b> (hipoeutéctica: precipita primero el sólido A puro). Regla de la palanca: el liquidus a 1100 °C tiene ≈ 30 % B; sólido A = 0 % B; C<sub>0</sub> = 20 % B:"
       "<div class='formula'>$$\\%L=\\frac{20-0}{30-0}=66{,}7\\%\\qquad \\%A=\\frac{30-20}{30-0}=33{,}3\\%$$</div></li>"
       "<li><b>800 °C:</b> por debajo de la eutéctica → <b>sólido A + B</b>. Palanca entre A (0 % B) y B (100 % B), C<sub>0</sub> = 20 % B:"
       "<div class='formula'>$$\\%B=\\frac{20-0}{100-0}=20\\%\\qquad \\%A=80\\%$$</div></li></ul>"
       "<div class='res'><b>1250 °C: L&nbsp;·&nbsp;1100 °C: 66,7 % L + 33,3 % A&nbsp;·&nbsp;800 °C: 80 % A + 20 % B</b></div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Bloque 2 · Sistemas mecánicos", "color": "#22d3ee",
   "descripcion_tarjeta": "Viga con carga distribuida, motor monocilíndrico de dos tiempos e instalación neumática (FluidSIM).",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><path d='M8 40h74'/><path d='M16 20v14M32 20v14M48 20v14M64 20v14M16 20h48'/></svg>",
   "cuestiones": [
    {
     "id": "q3", "titulo": "Pregunta 3 · Estructuras: viga con carga distribuida", "etiqueta": "MECÁNICA",
     "menu": "P3 · Viga con carga distribuida", "titulo_corto": "P3",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 0,5 · b 1,0 · c 0,5)",
     "enunciado_html": "<p><b>Cuestión.</b> Explica qué tiene que cumplir una estructura para estar en equilibrio. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> De la viga de la figura (carga distribuida W = 1000 N/m sobre 10 m):</p><ol type='a'><li>Calcula las reacciones en los apoyos. <span class='pts'>(0,5 ptos.)</span></li><li>Calcula los esfuerzos cortantes y momentos flectores. <span class='pts'>(1 pto.)</span></li><li>Representa los diagramas de esfuerzos cortantes y momentos flectores. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_viga() + "<figcaption>Viga biapoyada de 10 m con carga uniformemente distribuida W = 1000 N/m.</figcaption></figure>",
     "aplica_html": "<p>La carga distribuida equivale a una resultante \\(R=W\\cdot L\\) en el centro. El cortante varía linealmente \\(V(x)=R_A-W x\\) y el momento es una parábola \\(M(x)=R_A x-\\dfrac{W x^2}{2}\\), máximo en el centro.</p>",
     "solucion_html":
       "<h5>Cuestión · equilibrio de una estructura</h5>"
       "<p>Debe cumplir las <b>condiciones de equilibrio estático</b>: la suma de todas las fuerzas es nula (\\(\\sum F_x=0\\), \\(\\sum F_y=0\\)) y la suma de momentos respecto a cualquier punto es nula (\\(\\sum M=0\\)). Así no hay traslación ni giro.</p>"
       "<h5>a) Reacciones</h5>"
       "<p>Resultante de la carga: \\(R=W\\cdot L=1000\\cdot10=10000\\ \\mathrm N\\), aplicada en el centro (5 m). Por simetría:</p>"
       "<div class='formula'>$$R_A=R_B=\\frac{10000}{2}=5000\\ \\mathrm N$$</div>"
       "<div class='res'><b>R<sub>A</sub> = R<sub>B</sub> = 5000 N</b></div>"
       "<h5>b) Cortantes y momentos</h5>"
       "<div class='formula'>$$V(x)=R_A-W x=5000-1000\\,x\\quad\\Rightarrow\\quad V(0)=+5000,\\ V(5)=0,\\ V(10)=-5000\\ \\mathrm N$$</div>"
       "<div class='formula'>$$M(x)=R_A x-\\frac{W x^2}{2}=5000x-500x^2\\quad\\Rightarrow\\quad M_{\\max}=M(5)=12500\\ \\mathrm{N\\,m}$$</div>"
       "<div class='res'><b>V: de +5000 a −5000 N (0 en el centro) · M<sub>máx</sub> = 12500 N·m en el centro</b></div>"
       "<h5>c) Diagramas</h5>"
       "<figure class='fig'>" + fig_V() + "<figcaption>Cortante lineal: +5000 N en A, 0 en el centro, −5000 N en B.</figcaption></figure>"
       "<figure class='fig'>" + fig_M() + "<figcaption>Momento flector parabólico: máximo de 12500 N·m en el centro.</figcaption></figure>"
    },
    {
     "id": "q4", "titulo": "Pregunta 4 · Motor de dos tiempos", "etiqueta": "MECÁNICA",
     "menu": "P4 · Motor de 2 tiempos", "titulo_corto": "P4",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a-d 0,5 c/u)",
     "enunciado_html": "<p><b>Cuestión.</b> Explica las transformaciones termodinámicas isócora e isóbara para un gas. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Un motor monocilíndrico de dos tiempos y encendido por chispa tiene cilindrada 101,3 cm³ y volumen de cámara de combustión 12,66 cm³. Da una potencia máxima de 6 kW a 6200 rpm y un par máximo de 10 N·m a 4580 rpm. Con carrera 4,96 cm, calcula:</p><ol type='a'><li>La relación de compresión. <span class='pts'>(0,5 ptos.)</span></li><li>El diámetro del cilindro. <span class='pts'>(0,5 ptos.)</span></li><li>El par a potencia máxima. <span class='pts'>(0,5 ptos.)</span></li><li>La potencia a par máximo. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Relación de compresión \\(r_c=\\dfrac{V_u+V_c}{V_c}\\). El diámetro sale de \\(V_u=\\dfrac{\\pi D^2}{4}S\\). Y la relación par–potencia–velocidad: \\(P=M\\cdot\\omega\\) con \\(\\omega=\\dfrac{2\\pi n}{60}\\).</p>",
     "solucion_html":
       "<h5>Cuestión · transformaciones isócora e isóbara</h5>"
       "<p><b>Isócora</b> (volumen constante): no hay trabajo (W = 0); todo el calor cambia la temperatura y la presión. \\(Q=n\\,c_v\\,\\Delta T\\). En p–V es una recta vertical.</p>"
       "<p><b>Isóbara</b> (presión constante): el gas se dilata realizando trabajo \\(W=p\\,\\Delta V\\); \\(Q=n\\,c_p\\,\\Delta T\\). En p–V es una recta horizontal.</p>"
       "<h5>a) Relación de compresión</h5>"
       "<div class='formula'>$$r_c=\\frac{V_u+V_c}{V_c}=\\frac{101{,}3+12{,}66}{12{,}66}=\\frac{113{,}96}{12{,}66}=9{,}0$$</div>"
       "<div class='res'><b>r<sub>c</sub> ≈ 9 : 1</b></div>"
       "<h5>b) Diámetro del cilindro</h5>"
       "<div class='formula'>$$V_u=\\frac{\\pi D^2}{4}S\\ \\Rightarrow\\ D=\\sqrt{\\frac{4V_u}{\\pi S}}=\\sqrt{\\frac{4\\cdot101{,}3}{\\pi\\cdot4{,}96}}=5{,}10\\ \\mathrm{cm}$$</div>"
       "<div class='res'><b>D ≈ 5,1 cm = 51 mm</b></div>"
       "<h5>c) Par a potencia máxima (6 kW, 6200 rpm)</h5>"
       "<div class='formula'>$$\\omega=\\frac{2\\pi\\cdot6200}{60}=649{,}3\\ \\mathrm{rad/s}\\ \\Rightarrow\\ M=\\frac{P}{\\omega}=\\frac{6000}{649{,}3}=9{,}24\\ \\mathrm{N\\,m}$$</div>"
       "<div class='res'><b>M ≈ 9,24 N·m</b></div>"
       "<h5>d) Potencia a par máximo (10 N·m, 4580 rpm)</h5>"
       "<div class='formula'>$$\\omega=\\frac{2\\pi\\cdot4580}{60}=479{,}6\\ \\mathrm{rad/s}\\ \\Rightarrow\\ P=M\\,\\omega=10\\cdot479{,}6=4796\\ \\mathrm W$$</div>"
       "<div class='res'><b>P ≈ 4,8 kW</b></div>"
    },
    {
     "id": "q5", "titulo": "Pregunta 5 · Neumática (FluidSIM)", "etiqueta": "MECÁNICA",
     "menu": "P5 · Circuito neumático FluidSIM", "titulo_corto": "P5",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 1,0 · b 0,5 · c 0,5)",
     "enunciado_html": "<p><b>Cuestión.</b> Dibuja y explica cómo se comporta una válvula reguladora de caudal unidireccional. ¿Dónde debería colocarse para regular la velocidad de retroceso del vástago en un cilindro de doble efecto? <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> En el circuito montado en el simulador Festo FluidSIM:</p><ol type='a'><li>Identifica todos los elementos numerados. <span class='pts'>(1 pto.)</span></li><li>Indica la misión de los pulsadores manuales. <span class='pts'>(0,5 ptos.)</span></li><li>¿Qué logra la colocación de la válvula 1.01? <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'><img src='" + FIG + "/cyl24ext_neumatica.png' alt='Circuito neumático FluidSIM' style='max-width:460px;width:100%;background:#fff;border-radius:8px;padding:8px'><figcaption>Circuito neumático: cilindro (1.0), válvula 3/2 con rodillo (1.1), pulsadores 3/2 (1.2, 1.3), antirretorno (1.01), grupo de presión (0.1) y unidad de mantenimiento (0.2).</figcaption></figure>",
     "aplica_html": "<p>La reguladora de caudal unidireccional (estrangulador + antirretorno en paralelo) limita el caudal en un solo sentido. Para regular la <b>velocidad de retroceso</b> se coloca de modo que estrangule el aire que <b>sale</b> de la cámara del vástago (regulación por escape).</p>",
     "solucion_html":
       "<h5>Cuestión · válvula reguladora de caudal unidireccional</h5>"
       "<p>Consta de un <b>estrangulador regulable</b> en paralelo con un <b>antirretorno</b>: en un sentido el aire pasa libre por el antirretorno; en el otro se ve obligado a atravesar el estrangulador, que <b>limita el caudal</b> y, por tanto, la velocidad del émbolo. Para regular el <b>retroceso</b> de un cilindro de doble efecto se coloca en la línea de la <b>cámara del vástago estrangulando el escape</b> (el aire de esa cámara sale controlado).</p>"
       "<h5>a) Elementos numerados</h5><ul>"
       "<li><b>0.1</b> — Válvula de cierre / fuente de aire a presión del circuito.</li>"
       "<li><b>0.2</b> — <b>Unidad de mantenimiento</b> (filtro + regulador con manómetro + lubricador).</li>"
       "<li><b>1.0</b> — Cilindro de <b>simple efecto</b> con retorno por muelle.</li>"
       "<li><b>1.1</b> — Válvula <b>3/2</b> accionada por <b>rodillo</b> (final de carrera) con retorno por muelle.</li>"
       "<li><b>1.2 y 1.3</b> — Válvulas <b>3/2</b> de accionamiento manual por <b>pulsador</b> con retorno por muelle.</li>"
       "<li><b>1.01</b> — Válvula <b>antirretorno</b> (o selectora de circuito) que impide el retroceso del aire por esa línea.</li></ul>"
       "<h5>b) Misión de los pulsadores</h5>"
       "<p>Son los elementos de <b>mando</b>: al accionarlos dejan pasar aire de pilotaje que ordena el <b>avance</b> del cilindro. Colocados en paralelo (mediante la selectora) permiten el mando desde <b>varios puntos</b> (función OR).</p>"
       "<h5>c) Función de la válvula 1.01</h5>"
       "<p>Actúa como <b>válvula selectora / antirretorno</b>: combina las señales de los distintos pulsadores dejando pasar la de mayor presión e <b>impide que el aire retorne</b> hacia el pulsador no accionado, evitando fugas de la señal de mando.</p>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Bloque 3 · Sistemas eléctricos y electrónicos", "color": "#a78bfa",
   "descripcion_tarjeta": "Circuito R‖L en paralelo (impedancia, potencias) y función lógica de un circuito de interruptores.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M8 30h12l4-10 8 20 8-20 8 20 4-10h26'/></svg>",
   "cuestiones": [
    {
     "id": "q6", "titulo": "Pregunta 6 · Corriente alterna: R‖L paralelo", "etiqueta": "ELECTRICIDAD",
     "menu": "P6 · Circuito R‖L paralelo", "titulo_corto": "P6",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a-d 0,5 c/u)",
     "enunciado_html": "<p><b>Cuestión.</b> Explica, apoyándote en una gráfica, las características principales de la corriente alterna <i>trifásica</i>. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> En paralelo se conectan una resistencia de 800 Ω y una bobina de 0,2 H, con 230 V eficaces y 50 Hz. Calcula:</p><ol type='a'><li>La impedancia del circuito. <span class='pts'>(0,5 ptos.)</span></li><li>Las intensidades en todas las ramas. <span class='pts'>(0,5 ptos.)</span></li><li>El factor de potencia. <span class='pts'>(0,5 ptos.)</span></li><li>El balance de potencias. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_ac() + "<figcaption>Resistencia de 800 Ω y bobina de 0,2 H (X<sub>L</sub> = 62,83 Ω) en paralelo, 230 V / 50 Hz.</figcaption></figure>",
     "aplica_html": "<p>En paralelo se suman las admitancias: \\(Y=\\frac1R-\\frac{j}{X_L}\\), con \\(X_L=2\\pi f L\\). La impedancia es \\(Z=1/|Y|\\), la intensidad total \\(I=V|Y|\\) y cada rama \\(I=V/Z_{rama}\\). Potencias: \\(P=V^2/R\\), \\(Q=V^2/X_L\\), \\(S=V I\\).</p>",
     "solucion_html":
       "<h5>Cuestión · corriente alterna trifásica</h5>"
       "<p>La <b>corriente alterna trifásica</b> son tres tensiones senoidales de igual amplitud y frecuencia, <b>desfasadas 120°</b> entre sí. En cada instante suman cero (sistema equilibrado). Ventajas: transporte más económico, motores más sencillos y potencia constante. Gráficamente, tres senoides idénticas separadas 120° (T/3).</p>"
       "<h5>a) Impedancia</h5>"
       "<div class='formula'>$$X_L=2\\pi f L=2\\pi\\cdot50\\cdot0{,}2=62{,}83\\ \\Omega$$</div>"
       "<div class='formula'>$$Y=\\frac1{800}-\\frac{j}{62{,}83}=0{,}00125-0{,}01592\\,j\\ \\mathrm S\\ \\Rightarrow\\ |Y|=0{,}01596\\ \\mathrm S$$</div>"
       "<div class='formula'>$$Z=\\frac1{|Y|}=62{,}6\\ \\Omega$$</div>"
       "<div class='res'><b>Z ≈ 62,6 Ω (φ = +85,5°, inductivo)</b></div>"
       "<h5>b) Intensidades</h5>"
       "<div class='formula'>$$I_R=\\frac{230}{800}=0{,}288\\,\\mathrm A\\qquad I_L=\\frac{230}{62{,}83}=3{,}66\\,\\mathrm A$$</div>"
       "<div class='formula'>$$I=V\\,|Y|=230\\cdot0{,}01596=3{,}67\\ \\mathrm A$$</div>"
       "<div class='res'><b>I<sub>R</sub> = 0,288 A · I<sub>L</sub> = 3,66 A · I<sub>total</sub> = 3,67 A</b></div>"
       "<h5>c) Factor de potencia</h5>"
       "<div class='formula'>$$\\cos\\varphi=\\frac{G}{|Y|}=\\frac{0{,}00125}{0{,}01596}=0{,}078\\ (\\text{muy inductivo, en retraso})$$</div>"
       "<div class='res'><b>cos&phi; ≈ 0,078</b></div>"
       "<h5>d) Balance de potencias</h5>"
       "<div class='formula'>$$P=\\frac{V^2}{R}=\\frac{230^2}{800}=66{,}1\\ \\mathrm W\\qquad Q=\\frac{V^2}{X_L}=\\frac{230^2}{62{,}83}=842\\ \\mathrm{VAr}$$</div>"
       "<div class='formula'>$$S=V\\,I=230\\cdot3{,}67=844{,}5\\ \\mathrm{VA}$$</div>"
       "<div class='res'><b>P ≈ 66,1 W · Q ≈ 842 VAr (inductiva) · S ≈ 844,5 VA</b></div>"
       "<figure class='fig'>" + fig_triangulo() + "<figcaption>Circuito muy inductivo: Q casi igual a S; factor de potencia bajo.</figcaption></figure>"
    },
    {
     "id": "q7", "titulo": "Pregunta 7 · Función lógica de un circuito de interruptores", "etiqueta": "ELECTRÓNICA",
     "menu": "P7 · Circuito de interruptores", "titulo_corto": "P7",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a-d 0,5 c/u)",
     "enunciado_html": "<p><b>Cuestión.</b> Define la operación lógica <i>producto</i> mediante su tabla de verdad y su circuito eléctrico. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Del circuito de la figura, da la función lógica que vale 1 cuando la bombilla se enciende.</p><ol type='a'><li>Número de entradas y de funciones lógicas empleadas. <span class='pts'>(0,5 ptos.)</span></li><li>Tabla de verdad. <span class='pts'>(0,5 ptos.)</span></li><li>Mapas de Karnaugh necesarios. <span class='pts'>(0,5 ptos.)</span></li><li>Simplifica la función obtenida. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'><img src='" + FIG + "/cyl24ext_switches.png' alt='Circuito de interruptores' style='max-width:420px;width:100%;background:#fff;border-radius:8px;padding:8px'><figcaption>Rama superior: a · b · c̄ (en serie). Rama inferior: c · a (en serie). Ambas en paralelo alimentan la bombilla.</figcaption></figure>",
     "aplica_html": "<p>Interruptores en <b>serie</b> = producto lógico (AND); en <b>paralelo</b> = suma lógica (OR); un contacto normalmente cerrado (c̄) = negación. La bombilla luce si conduce alguna de las dos ramas.</p>",
     "solucion_html":
       "<h5>Cuestión · operación producto (AND)</h5>"
       "<p>El <b>producto lógico</b> F = A·B vale 1 sólo si <b>todas</b> las entradas valen 1. Su circuito eléctrico son dos interruptores <b>en serie</b>: la lámpara luce únicamente si A y B están cerrados.</p>"
       "<table class='dat'><tr><th>A</th><th>B</th><th>A·B</th></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>"
       "<h5>a) Entradas y funciones</h5>"
       "<p><b>3 entradas</b> (a, b, c) y <b>una única función de salida</b> F. La rama superior (serie) da a·b·c̄ y la inferior a·c; en paralelo se suman:</p>"
       "<div class='formula'>$$F=a\\,b\\,\\overline c+a\\,c$$</div>"
       "<h5>b) Tabla de verdad</h5>"
       "<table class='dat'><tr><th>a</th><th>b</th><th>c</th><th>F</th></tr>"
       "<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>"
       "<h5>c) y d) Karnaugh y simplificación</h5>"
       "<p>Los 1 están en a·b·c̄ (110), a·b·c (111) y a·b̄·c (101). Agrupando: (110+111) → a·b y (101+111) → a·c. Por álgebra de Boole, \\(b\\overline c+c=b+c\\), luego:</p>"
       "<div class='formula'>$$F=a\\,b\\,\\overline c+a\\,c=a\\,(b\\,\\overline c+c)=a\\,(b+c)=a\\,b+a\\,c$$</div>"
       "<div class='res'><b>F = a · (b + c)</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Bloque 4 · Sistemas emergentes y control", "color": "#4ade80",
   "descripcion_tarjeta": "IA en seguridad pública, señal de referencia y función de transferencia de un diagrama de bloques.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#4ade80' stroke-width='3'><rect x='34' y='22' width='24' height='16' rx='3'/><path d='M8 30h26M58 30h24'/><circle cx='20' cy='30' r='6'/></svg>",
   "cuestiones": [
    {
     "id": "q8", "titulo": "Pregunta 8 · Sistemas de control: función de transferencia", "etiqueta": "CONTROL",
     "menu": "P8 · Función de transferencia Y/R", "titulo_corto": "P8",
     "meta": "Pregunta de 2,5 puntos (a 0,5 · b 0,5 · problema 1,5)",
     "enunciado_html": "<p><b>Cuestiones.</b></p><ol type='a'><li>Explica una aplicación de la IA en el ámbito de la seguridad pública. <span class='pts'>(0,5 ptos.)</span></li><li>Explica qué es la señal de referencia en un sistema de control de lazo cerrado. Pon un ejemplo. <span class='pts'>(0,5 ptos.)</span></li></ol><p><b>Problema.</b> Calcula la función de transferencia Y(s)/R(s) del sistema de control cuyo diagrama de bloques se muestra en la figura. <span class='pts'>(1,5 ptos.)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloques_ext() + "<figcaption>G<sub>1</sub> en serie, luego G<sub>2</sub> con una rama directa (feed-forward) en paralelo, y realimentación H<sub>1</sub>.</figcaption></figure>",
     "aplica_html": "<p>La rama directa desde la salida de G<sub>1</sub> hasta el segundo sumador (en paralelo con G<sub>2</sub>) aporta el factor (1+G<sub>2</sub>). En serie con G<sub>1</sub> y con realimentación negativa H<sub>1</sub> se obtiene la función.</p>",
     "solucion_html":
       "<h5>a) IA en seguridad pública</h5>"
       "<p>La <b>videovigilancia inteligente</b>: cámaras con visión artificial que reconocen matrículas, detectan comportamientos anómalos o personas en zonas restringidas y avisan automáticamente. También el análisis predictivo para anticipar zonas de mayor riesgo o el reconocimiento facial en controles de acceso.</p>"
       "<h5>b) Señal de referencia</h5>"
       "<p>La <b>señal de referencia (consigna)</b> es el valor que queremos que alcance la salida del sistema; se compara con la salida realimentada para obtener el error. <b>Ejemplo:</b> en una calefacción, la temperatura que fijamos en el termostato (p. ej. 21 °C) es la referencia; el sistema actúa para que la temperatura real la iguale.</p>"
       "<h5>Problema · función de transferencia Y/R</h5>"
       "<p>Sea X la salida del primer sumador: \\(X=R-H_1\\,Y\\). Tras G<sub>1</sub>: \\(G_1X\\). Ese punto se bifurca: una rama pasa por G<sub>2</sub> y otra va directa (unidad) al segundo sumador, que las suma:</p>"
       "<div class='formula'>$$Y=\\big(G_2+1\\big)\\,G_1\\,X=G_1(1+G_2)(R-H_1Y)$$</div>"
       "<div class='formula'>$$Y\\big[1+G_1(1+G_2)H_1\\big]=G_1(1+G_2)\\,R$$</div>"
       "<div class='formula'>$$\\boxed{\\ \\dfrac{Y(s)}{R(s)}=\\dfrac{G_1\\,(1+G_2)}{1+G_1\\,(1+G_2)\\,H_1}\\ }$$</div>"
       "<div class='res'><b>Y/R = G<sub>1</sub>(1+G<sub>2</sub>) / [1 + G<sub>1</sub>(1+G<sub>2</sub>)H<sub>1</sub>]</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cyl_2024_extraordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
