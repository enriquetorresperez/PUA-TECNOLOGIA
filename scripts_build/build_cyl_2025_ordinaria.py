#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Castilla y León EBAU 2025 · Ordinaria (Propuesta 5)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt
from cyllib import beam, diagram_VM, ac_series, power_triangle

FIG = "fig"


def fig_viga():
    return beam(loads=[{'type': 'P', 'xm': 0, 'val': 'P₂ = 2000 N'},
                       {'type': 'P', 'xm': 5, 'val': 'P₁ = 2000 N'}],
                supports=[{'xm': 0, 'kind': 'roller', 'label': 'A'},
                          {'xm': 10, 'kind': 'pin', 'label': 'C'}],
                span_m=10, dims=[(0, 5, '5 m'), (5, 10, '5 m')])


def fig_V():
    return diagram_VM([(0, 1000), (5, 1000), (5, -1000), (10, -1000)], 10, kind='V', unit='N',
                      title='Esfuerzo cortante V (N)')


def fig_M():
    return diagram_VM([(0, 0), (5, 5000), (10, 0)], 10, kind='M', unit='N·m',
                      title='Momento flector M (N·m)')


def fig_ac():
    return ac_series([('R', 'R'), ('L', 'L = 0,7 H'), ('C', 'C = 40 µF')], V='230 V', f='50 Hz')


def fig_triangulo():
    return power_triangle(188.0, 202.1, 276.0, 47.1, inductive=True,
                          labels={'P': 'P = 188 W', 'Q': 'Q = 202 VAr (ind.)', 'S': 'S = 276 VA'})


def fig_bloques_yr():
    """P8: Y/R = (G1+G2)/(1+(G1+G2)H1)."""
    s = svg_open('720 300', 640)
    ym = 150
    s += txt(24, ym + 5, 'R', '#e2e8f0', 15)
    s += arrow(40, ym, 74, ym); s += summer(90, ym)
    s += txt(74, ym - 12, '+', '#4ade80', 15); s += txt(78, ym + 30, '−', '#fb7185', 17)
    s += arrow(106, ym, 160, ym); s += "<circle cx='160' cy='150' r='3.4' fill='#cbd5e1'/>"
    s += arrow(160, ym, 210, ym)
    s += box(210, 128, 70, 44, 'G<tspan dy=\"4\" font-size=\"11\">1</tspan>', '#22d3ee')
    s += arrow(280, ym, 372, ym); s += summer(388, ym)
    s += txt(370, ym + 30, '+', '#4ade80', 15); s += txt(400, ym - 12, '+', '#4ade80', 15)
    s += arrow(404, ym, 460, ym); s += "<circle cx='460' cy='150' r='3.4' fill='#cbd5e1'/>"
    s += arrow(460, ym, 500, ym); s += txt(512, ym + 5, 'Y', '#e2e8f0', 15)
    # G2 en paralelo desde nodo tras sumador 1
    s += box(230, 66, 70, 40, 'G<tspan dy=\"4\" font-size=\"11\">2</tspan>', '#a78bfa')
    s += line(160, ym, 160, 86); s += line(160, 86, 230, 86)
    s += line(300, 86, 388, 86); s += arrow(388, 86, 388, 135)
    # H1 realimentación
    s += box(230, 228, 70, 40, 'H<tspan dy=\"4\" font-size=\"11\">1</tspan>', '#38bdf8')
    s += line(460, ym, 460, 248); s += line(460, 248, 300, 248)
    s += line(230, 248, 90, 248); s += arrow(90, 248, 90, 165)
    return s + "</svg>"


T = ("<table class='dat'><tr><th>Carga (N)</th><th>Longitud (cm)</th></tr>"
     "<tr><td>0</td><td>5,08</td></tr><tr><td>4448</td><td>5,0825</td></tr>"
     "<tr><td>13344</td><td>5,0876</td></tr><tr><td>22240</td><td>5,0927</td></tr>"
     "<tr><td>31136</td><td>5,0978</td></tr><tr><td>33360</td><td>5,1562</td></tr>"
     "<tr><td>35139</td><td>5,2832</td></tr><tr><td>35584 (máx.)</td><td>5,3848</td></tr>"
     "<tr><td>35361</td><td>5,4864</td></tr><tr><td>33804 (rotura)</td><td>5,6007</td></tr></table>")


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · Castilla y León · Ordinaria 2025 · Examen resuelto y comentado",
  "cabecera_titulo": "EBAU 2025 · <span>Tecnología e Ingeniería II</span> · Castilla y León · Ordinaria",
  "pill": "90 min · 2,5 pt/pregunta · 4 apartados",
  "enunciado_pdf": "../../examens/Castilla y Leon/Tecnologia_CastillayLeon_2025_ordinaria.pdf",
  "pdf_dir": "pdf_cyl_2025_ordinaria",
  "footer": "Dpto. Tecnología · Solucionario EBAU · Castilla y León · Tecnología e Ingeniería II (Ordinaria 2025)",
  "intro_inicio": "El ejercicio consta de <b>cuatro apartados obligatorios</b>. El primero tiene una única pregunta; en los otros tres se elige <b>una de las dos</b>. Aquí se resuelven <b>todas</b>. Selecciona un apartado o una pregunta en la barra lateral.",
  "indice_nombre": "Exámenes de Castilla y León",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Apartado 1 · Propiedades y ensayo (obligatoria)", "color": "#f59e0b",
   "descripcion_tarjeta": "Ensayo de tensión de una barra de aluminio a partir de la tabla de datos carga–longitud.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><path d='M10 50 Q18 18 34 15 T82 24'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Pregunta única · Ensayo de tensión (tabla)", "etiqueta": "APARTADO 1",
     "menu": "P única · Ensayo de tensión", "titulo_corto": "P1",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a-d 0,5 c/u)",
     "enunciado_html": "<p><b>Cuestión.</b> Define la resiliencia de un material. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Los resultados de un ensayo de tensión de una barra de aluminio son los de la tabla. La probeta tiene longitud calibrada L<sub>0</sub> = 5,08 cm y diámetro D<sub>0</sub> = 1,283 cm. Tras la rotura, L<sub>f</sub> = 5,575 cm y D<sub>f</sub> = 1,01 cm. El límite elástico es 248 MPa. Determina:</p>" + T + "<ol type='a'><li>Resistencia a la tracción. <span class='pts'>(0,5 ptos.)</span></li><li>Módulo de Young. <span class='pts'>(0,5 ptos.)</span></li><li>Porcentaje de elongación máxima. <span class='pts'>(0,5 ptos.)</span></li><li>Deformación correspondiente a una carga de 31136 N. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>Sección inicial \\(A_0=\\frac{\\pi D_0^2}{4}\\). La resistencia a la tracción es \\(R_m=\\frac{F_{\\max}}{A_0}\\). El módulo de Young es la pendiente de la zona elástica \\(E=\\frac{\\sigma}{\\varepsilon}\\). La elongación \\(\\%=\\frac{L_f-L_0}{L_0}\\cdot100\\). La deformación \\(\\varepsilon=\\frac{\\Delta L}{L_0}\\).</p>",
     "solucion_html":
       "<h5>Cuestión · resiliencia</h5>"
       "<p>La <b>resiliencia</b> es la energía que absorbe un material en la <b>zona elástica</b> (hasta el límite elástico) por unidad de volumen; es el área bajo la curva σ–ε en dicha zona. Representa la capacidad de absorber energía sin deformarse permanentemente.</p>"
       "<p>Datos: \\(A_0=\\frac{\\pi\\cdot1{,}283^2}{4}=1{,}293\\ \\mathrm{cm^2}=129{,}3\\ \\mathrm{mm^2}\\).</p>"
       "<h5>a) Resistencia a la tracción</h5>"
       "<p>Con la carga máxima F<sub>máx</sub> = 35584 N:</p>"
       "<div class='formula'>$$R_m=\\frac{F_{\\max}}{A_0}=\\frac{35584}{129{,}3}=275{,}2\\ \\mathrm{MPa}$$</div>"
       "<div class='res'><b>R<sub>m</sub> ≈ 275,2 MPa</b></div>"
       "<h5>b) Módulo de Young</h5>"
       "<p>En la zona elástica (lineal), usando el punto de 31136 N (aún por debajo del límite elástico), con ΔL = 5,0978 − 5,08 = 0,0178 cm:</p>"
       "<div class='formula'>$$\\sigma=\\frac{31136}{129{,}3}=240{,}8\\ \\mathrm{MPa}\\qquad \\varepsilon=\\frac{0{,}0178}{5{,}08}=3{,}5\\cdot10^{-3}$$</div>"
       "<div class='formula'>$$E=\\frac{\\sigma}{\\varepsilon}=\\frac{240{,}8}{3{,}5\\cdot10^{-3}}=68{,}7\\cdot10^{3}\\ \\mathrm{MPa}$$</div>"
       "<div class='res'><b>E ≈ 68,7 GPa</b> (≈ 69 GPa, típico del aluminio)</div>"
       "<h5>c) Porcentaje de elongación máxima</h5>"
       "<div class='formula'>$$\\%\\,\\text{elong.}=\\frac{L_f-L_0}{L_0}\\cdot100=\\frac{5{,}575-5{,}08}{5{,}08}\\cdot100=9{,}74\\%$$</div>"
       "<div class='res'><b>≈ 9,74 %</b></div>"
       "<h5>d) Deformación con carga de 31136 N</h5>"
       "<div class='formula'>$$\\varepsilon=\\frac{\\Delta L}{L_0}=\\frac{5{,}0978-5{,}08}{5{,}08}=3{,}5\\cdot10^{-3}$$</div>"
       "<div class='res'><b>&epsilon; = 0,0035 (0,35 %)</b></div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Apartado 2 · Estructuras / Máquinas térmicas", "color": "#22d3ee",
   "descripcion_tarjeta": "Elige: viga con dos cargas puntuales o bomba de calor real (30 % de un ciclo de Carnot).",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><path d='M8 34h74'/><path d='M24 12v18M60 12v18'/><path d='M8 34l-4 8h8zM82 34l-4 8h8z'/></svg>",
   "cuestiones": [
    {
     "id": "q2", "titulo": "Pregunta 1 (Opción A) · Estructuras: dos cargas", "etiqueta": "APARTADO 2 · A",
     "menu": "P1 (A) · Viga con dos cargas", "titulo_corto": "P2",
     "meta": "Pregunta de 2,5 puntos (a 0,5 · b 1,25 · c 0,75)",
     "enunciado_html": "<p><b>Problema.</b> La viga de la figura tiene aplicadas las dos fuerzas indicadas (P₁ = P₂ = 2000 N).</p><ol type='a'><li>Calcula las reacciones en los apoyos. <span class='pts'>(0,5 ptos.)</span></li><li>Calcula los esfuerzos cortantes y momentos flectores. <span class='pts'>(1,25 ptos.)</span></li><li>Representa los diagramas. <span class='pts'>(0,75 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_viga() + "<figcaption>Viga apoyada en A y C (10 m). P₂ = 2000 N sobre A y P₁ = 2000 N en B (centro, 5 m).</figcaption></figure>",
     "aplica_html": "<p>Equilibrio: \\(\\sum M_A=0\\), \\(\\sum F_y=0\\). La carga P₂ está aplicada sobre el apoyo A, por lo que pasa directamente a su reacción; sólo P₁ (en B) genera momento respecto a A.</p>",
     "solucion_html":
       "<h5>a) Reacciones</h5>"
       "<p>\\(\\sum M_A=0\\): \\(R_C\\cdot10=P_1\\cdot5=2000\\cdot5=10000\\Rightarrow R_C=1000\\ \\mathrm N\\).</p>"
       "<div class='formula'>$$\\sum F_y=0:\\quad R_A=P_1+P_2-R_C=4000-1000=3000\\ \\mathrm N$$</div>"
       "<div class='res'><b>R<sub>A</sub> = 3000 N&nbsp;·&nbsp;R<sub>C</sub> = 1000 N</b></div>"
       "<h5>b) Cortantes y momentos</h5>"
       "<p>Justo a la derecha de A, la carga P₂ ya se ha descontado: V = R<sub>A</sub> − P₂ = 3000 − 2000 = <b>+1000 N</b> (tramo A–B). En B baja P₁: V = 1000 − 2000 = <b>−1000 N</b> (tramo B–C).</p>"
       "<p>Momento en B (x = 5 m): \\(M_B=R_A\\cdot5-P_2\\cdot5=3000\\cdot5-2000\\cdot5=5000\\ \\mathrm{N\\,m}\\). En A y C, M = 0.</p>"
       "<div class='res'><b>V = +1000 / −1000 N&nbsp;·&nbsp;M<sub>máx</sub> = 5000 N·m (en B)</b></div>"
       "<h5>c) Diagramas</h5>"
       "<figure class='fig'>" + fig_V() + "<figcaption>Esfuerzo cortante.</figcaption></figure>"
       "<figure class='fig'>" + fig_M() + "<figcaption>Momento flector.</figcaption></figure>"
    },
    {
     "id": "q3", "titulo": "Pregunta 2 (Opción B) · Bomba de calor real", "etiqueta": "APARTADO 2 · B",
     "menu": "P2 (B) · Bomba de calor real", "titulo_corto": "P3",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 0,75 · b 0,5 · c 0,75)",
     "enunciado_html": "<p><b>Cuestión.</b> Explica la transformación isoterma para un gas: representa la gráfica p–V y escribe las fórmulas del trabajo y el calor. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Un local con temperatura exterior 5 °C necesita una bomba de calor que aporta a su interior 214·10³ kJ en una hora para mantenerlo a 21 °C. Sabiendo que la bomba real aprovecha sólo el 30 % de un ciclo de Carnot reversible, calcula:</p><ol type='a'><li>La eficiencia de la máquina reversible. <span class='pts'>(0,75 ptos.)</span></li><li>La eficiencia de la máquina real. <span class='pts'>(0,5 ptos.)</span></li><li>La potencia a la que funciona la bomba (kW). <span class='pts'>(0,75 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>COP de Carnot: \\(\\mathrm{COP}_{rev}=\\frac{T_c}{T_c-T_f}\\) (K). La real es el 30 %: \\(\\mathrm{COP}_{real}=0{,}30\\,\\mathrm{COP}_{rev}\\). La potencia sale de \\(\\dot W=\\dot Q_c/\\mathrm{COP}_{real}\\).</p>",
     "solucion_html":
       "<h5>Cuestión · transformación isoterma</h5>"
       "<p>A <b>temperatura constante</b> (ΔU = 0 para gas ideal). En p–V es una <b>hipérbola</b> (p·V = cte). Todo el calor absorbido se convierte en trabajo:</p>"
       "<div class='formula'>$$W=n R T\\ln\\frac{V_2}{V_1}=Q\\qquad(\\Delta U=0)$$</div>"
       "<h5>a) Eficiencia reversible (COP)</h5>"
       "<p>T<sub>c</sub> = 21 °C = 294 K, T<sub>f</sub> = 5 °C = 278 K.</p>"
       "<div class='formula'>$$\\mathrm{COP}_{rev}=\\frac{T_c}{T_c-T_f}=\\frac{294}{294-278}=\\frac{294}{16}=18{,}375$$</div>"
       "<div class='res'><b>COP<sub>rev</sub> ≈ 18,38</b></div>"
       "<h5>b) Eficiencia real</h5>"
       "<div class='formula'>$$\\mathrm{COP}_{real}=0{,}30\\cdot18{,}375=5{,}51$$</div>"
       "<div class='res'><b>COP<sub>real</sub> ≈ 5,51</b></div>"
       "<h5>c) Potencia de la bomba</h5>"
       "<p>Calor aportado \\(\\dot Q_c=214\\cdot10^{3}\\ \\mathrm{kJ/h}\\). El trabajo (energía eléctrica) por hora:</p>"
       "<div class='formula'>$$W=\\frac{\\dot Q_c}{\\mathrm{COP}_{real}}=\\frac{214\\cdot10^{3}}{5{,}51}=38{,}8\\cdot10^{3}\\ \\mathrm{kJ/h}$$</div>"
       "<div class='formula'>$$P=\\frac{38{,}8\\cdot10^{6}\\ \\mathrm J}{3600\\ \\mathrm s}=10{,}8\\cdot10^{3}\\ \\mathrm W$$</div>"
       "<div class='res'><b>P ≈ 10,8 kW</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Apartado 3 · Neumática / Corriente alterna", "color": "#a78bfa",
   "descripcion_tarjeta": "Elige: instalación oleohidráulica o circuito RLC en serie.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M8 30h12l4-10 8 20 8-20 8 20 4-10h26'/></svg>",
   "cuestiones": [
    {
     "id": "q4", "titulo": "Pregunta 1 (Opción A) · Neumática e hidráulica", "etiqueta": "APARTADO 3 · A",
     "menu": "P1 (A) · Instalación oleohidráulica", "titulo_corto": "P4",
     "meta": "Pregunta de 2,5 puntos (a 1,0 · b 1,0 · c 0,5)",
     "enunciado_html": "<p><b>Problema.</b> En la instalación oleohidráulica de la figura:</p><ol type='a'><li>Define sus componentes. <span class='pts'>(1 pto.)</span></li><li>Explica el funcionamiento. <span class='pts'>(1 pto.)</span></li><li>¿Qué ocurre si al montar la instalación el regulador «1.02» se conecta al revés? <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'><img src='" + FIG + "/cyl25ord_hidraulica.png' alt='Instalación oleohidráulica' style='max-width:400px;width:100%;background:#fff;border-radius:8px;padding:8px'><figcaption>Cilindro de doble efecto (1.0), reguladora de caudal (1.02), válvula pilotada (1.03), distribuidor 4/2 (1.1), limitadora (1.01) y grupo motor-bomba (0.1).</figcaption></figure>",
     "aplica_html": "<p>Identificamos el actuador, el distribuidor que lo gobierna, la reguladora de caudal (control de velocidad), la limitadora de presión (seguridad) y el grupo de presión (motor + bomba).</p>",
     "solucion_html":
       "<h5>a) Componentes</h5><ul>"
       "<li><b>1.0</b> — Cilindro hidráulico de <b>doble efecto</b>.</li>"
       "<li><b>1.1</b> — <b>Distribuidor 4/2</b> con pilotaje y retorno por muelle: dirige el aceite a cada cámara.</li>"
       "<li><b>1.02</b> — <b>Reguladora de caudal unidireccional</b> (estrangulador + antirretorno): controla la velocidad del émbolo.</li>"
       "<li><b>1.03</b> — Válvula <b>3/2</b> pilotada (mando).</li>"
       "<li><b>1.01</b> — Válvula <b>limitadora de presión</b> (seguridad, tara la presión máxima).</li>"
       "<li><b>0.1</b> — <b>Grupo de presión</b>: bomba movida por el motor eléctrico M (con depósito).</li></ul>"
       "<h5>b) Funcionamiento</h5>"
       "<p>El motor M acciona la bomba, que aspira aceite del depósito y lo impulsa a presión (limitada por 1.01). Según la posición del distribuidor 1.1, el aceite entra en una u otra cámara del cilindro produciendo el <b>avance</b> o el <b>retroceso</b>; el aceite de la cámara opuesta retorna al depósito. La reguladora 1.02 estrangula el caudal para fijar la <b>velocidad</b>. Al despilotar, el muelle devuelve el distribuidor a su posición de reposo.</p>"
       "<h5>c) Regulador 1.02 conectado al revés</h5>"
       "<p>La reguladora es <b>unidireccional</b>: si se monta al revés, el antirretorno deja pasar libremente el aceite en el sentido en el que debería estrangular y estrangula donde debería pasar libre. Resultado: <b>no se regula la velocidad</b> en la carrera prevista (el émbolo va a velocidad máxima) y se estrangula la otra, invirtiéndose el efecto de control.</p>"
    },
    {
     "id": "q5", "titulo": "Pregunta 2 (Opción B) · Corriente alterna: RLC serie", "etiqueta": "APARTADO 3 · B",
     "menu": "P2 (B) · Circuito RLC serie", "titulo_corto": "P5",
     "meta": "Pregunta de 2,5 puntos (a 0,75 · b 0,75 · c 0,5 · d 0,5)",
     "enunciado_html": "<p><b>Problema.</b> En un circuito serie con corriente eficaz 1,2 A hay una resistencia, una bobina de 0,7 H y un condensador de 40 µF, alimentados a 230 V eficaces y 50 Hz. Calcula:</p><ol type='a'><li>La resistencia del circuito. <span class='pts'>(0,75 ptos.)</span></li><li>Si es inductivo o capacitivo y el factor de potencia. <span class='pts'>(0,75 ptos.)</span></li><li>El balance de potencias. <span class='pts'>(0,5 ptos.)</span></li><li>Dibuja el triángulo de potencias. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_ac() + "<figcaption>Circuito serie R–L–C (230 V, 50 Hz, I = 1,2 A).</figcaption></figure>",
     "aplica_html": "<p>\\(X_L=2\\pi f L\\), \\(X_C=\\frac1{2\\pi f C}\\). \\(Z=V/I=\\sqrt{R^2+(X_L-X_C)^2}\\Rightarrow R\\). El signo de \\(X_L-X_C\\) indica si es inductivo o capacitivo. \\(P=I^2R\\), \\(Q=I^2(X_L-X_C)\\), \\(S=VI\\).</p>",
     "solucion_html":
       "<h5>a) Resistencia</h5>"
       "<div class='formula'>$$X_L=2\\pi\\cdot50\\cdot0{,}7=219{,}9\\ \\Omega\\qquad X_C=\\frac{1}{2\\pi\\cdot50\\cdot40\\cdot10^{-6}}=79{,}6\\ \\Omega$$</div>"
       "<div class='formula'>$$Z=\\frac{V}{I}=\\frac{230}{1{,}2}=191{,}7\\ \\Omega\\ \\Rightarrow\\ R=\\sqrt{Z^2-(X_L-X_C)^2}=\\sqrt{191{,}7^2-140{,}3^2}=130{,}5\\ \\Omega$$</div>"
       "<div class='res'><b>R ≈ 130,5 Ω</b></div>"
       "<h5>b) Carácter y factor de potencia</h5>"
       "<p>Como X<sub>L</sub> = 219,9 Ω > X<sub>C</sub> = 79,6 Ω, el circuito es <b>inductivo</b> (la corriente atrasa).</p>"
       "<div class='formula'>$$\\cos\\varphi=\\frac{R}{Z}=\\frac{130{,}5}{191{,}7}=0{,}681\\quad(\\varphi=+47{,}1^\\circ)$$</div>"
       "<div class='res'><b>Inductivo · cos&phi; ≈ 0,68 (en retraso)</b></div>"
       "<h5>c) Balance de potencias</h5>"
       "<div class='formula'>$$P=I^2R=1{,}2^2\\cdot130{,}5=188\\ \\mathrm W$$</div>"
       "<div class='formula'>$$Q=I^2(X_L-X_C)=1{,}44\\cdot140{,}3=202\\ \\mathrm{VAr}\\ (\\text{inductiva})$$</div>"
       "<div class='formula'>$$S=V\\,I=230\\cdot1{,}2=276\\ \\mathrm{VA}$$</div>"
       "<div class='res'><b>P ≈ 188 W · Q ≈ 202 VAr · S = 276 VA</b></div>"
       "<h5>d) Triángulo de potencias</h5>"
       "<figure class='fig'>" + fig_triangulo() + "<figcaption>Circuito inductivo: la Q queda por encima de la P.</figcaption></figure>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Apartado 4 · Electrónica digital / Control", "color": "#4ade80",
   "descripcion_tarjeta": "Elige: control digital del nivel de un depósito (3 lámparas) o función de transferencia de un diagrama de bloques.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#4ade80' stroke-width='3'><rect x='30' y='16' width='30' height='28' rx='2'/><circle cx='72' cy='24' r='4'/><circle cx='72' cy='36' r='4'/><path d='M8 24h22M8 36h22'/></svg>",
   "cuestiones": [
    {
     "id": "q6", "titulo": "Pregunta 1 (Opción A) · Control de nivel de un depósito", "etiqueta": "APARTADO 4 · A",
     "menu": "P1 (A) · Nivel de depósito", "titulo_corto": "P6",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 0,75 · b 0,75 · c 0,5)",
     "enunciado_html": "<p><b>Cuestión.</b> Define las funciones elementales OR y NOR, con sus ecuaciones lógicas, tablas de verdad y la diferencia entre ellas. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> El circuito digital CD indica el nivel de agua. Si no llega a S1, ninguna lámpara; si llega a S1, sólo L1; si llega a S2, sólo L2; si llega a S3, sólo L3. Cualquier combinación imposible (fallo) enciende las tres.</p><ol type='a'><li>Tabla de verdad de las tres salidas. <span class='pts'>(0,75 ptos.)</span></li><li>Simplifica por Karnaugh las tres funciones. <span class='pts'>(0,75 ptos.)</span></li><li>Expresión simplificada con lógica NAND. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'><img src='" + FIG + "/cyl25ord_deposito.png' alt='Depósito con sensores de nivel' style='max-width:420px;width:100%;background:#fff;border-radius:8px;padding:8px'><figcaption>Sensores S1 (bajo), S2 (medio) y S3 (alto); salidas L1, L2, L3.</figcaption></figure>",
     "aplica_html": "<p>Los sensores se activan de abajo arriba: son válidos 000, 100, 110, 111 (con salida un único LED); cualquier otra combinación es un <b>fallo</b> y enciende las tres lámparas. Se construye la tabla y se simplifica cada salida por Karnaugh.</p>",
     "solucion_html":
       "<h5>Cuestión · OR y NOR</h5>"
       "<p><b>OR:</b> \\(F=A+B\\), vale 1 si <b>alguna</b> entrada es 1. <b>NOR:</b> \\(F=\\overline{A+B}\\), es la OR negada (vale 1 sólo si <b>todas</b> son 0).</p>"
       "<table class='dat'><tr><th>A</th><th>B</th><th>OR</th><th>NOR</th></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td></tr></table>"
       "<h5>a) Tabla de verdad</h5>"
       "<p>Entradas (S1, S2, S3). Válidos: 000→ninguna, 100→L1, 110→L2, 111→L3; el resto son fallos (las tres).</p>"
       "<table class='dat'><tr><th>S1</th><th>S2</th><th>S3</th><th>L1</th><th>L2</th><th>L3</th></tr>"
       "<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
       "<tr><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr>"
       "<tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr></table>"
       "<h5>b) Simplificación por Karnaugh</h5>"
       "<div class='formula'>$$L_1=S_1\\overline{S_2}+\\overline{S_1}S_2+\\overline{S_1}S_3$$</div>"
       "<div class='formula'>$$L_2=S_2\\overline{S_3}+\\overline{S_2}S_3+\\overline{S_1}S_2$$</div>"
       "<div class='formula'>$$L_3=S_3+\\overline{S_1}S_2$$</div>"
       "<h5>c) Lógica NAND</h5>"
       "<p>Cada suma de productos se pasa a NAND con doble negación (De Morgan): un producto \\(A\\,B=\\overline{\\mathrm{NAND}(A,B)}\\) y la suma \\(P_1+P_2+\\dots=\\overline{\\overline{P_1}\\cdot\\overline{P_2}\\cdots}=\\mathrm{NAND}(\\overline{P_1},\\overline{P_2},\\dots)\\). Por ejemplo:</p>"
       "<div class='formula'>$$L_3=S_3+\\overline{S_1}S_2=\\mathrm{NAND}\\big(\\overline{S_3},\\ \\mathrm{NAND}(\\overline{S_1},S_2)\\big)$$</div>"
       "<p>Las tres funciones se implementan de forma análoga con puertas NAND (cada producto con una NAND y la unión con otra NAND).</p>"
    },
    {
     "id": "q7", "titulo": "Pregunta 2 (Opción B) · Sistemas de control", "etiqueta": "APARTADO 4 · B",
     "menu": "P2 (B) · Función de transferencia Y/R", "titulo_corto": "P7",
     "meta": "Pregunta de 2,5 puntos (a 0,5 · b 0,5 · problema 1,5)",
     "enunciado_html": "<p><b>Cuestiones.</b></p><ol type='a'><li>¿Cuál es la principal diferencia en la estructura de un control en lazo abierto y en lazo cerrado? <span class='pts'>(0,5 ptos.)</span></li><li>Explica una aplicación actual del Procesamiento de Lenguaje Natural (PLN). <span class='pts'>(0,5 ptos.)</span></li></ol><p><b>Problema.</b> Calcula la función de transferencia Y(s)/R(s) del sistema de la figura. <span class='pts'>(1,5 ptos.)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloques_yr() + "<figcaption>G<sub>1</sub> y G<sub>2</sub> en paralelo, con realimentación H<sub>1</sub>.</figcaption></figure>",
     "aplica_html": "<p>Las ramas en paralelo se suman (G<sub>1</sub>+G<sub>2</sub>) y el lazo con realimentación negativa da \\(\\frac{G}{1+GH}\\).</p>",
     "solucion_html":
       "<h5>a) Lazo abierto vs. lazo cerrado</h5>"
       "<p>La diferencia estructural es la <b>realimentación</b>: el lazo cerrado <b>mide la salida y la devuelve al comparador</b> para corregir el error; el lazo abierto no tiene realimentación (la salida no influye en la acción de control).</p>"
       "<h5>b) Aplicación del PLN</h5>"
       "<p>Los <b>asistentes virtuales y chatbots</b> (o los traductores automáticos): entienden y generan lenguaje humano para responder preguntas, traducir textos o transcribir voz a texto. También el análisis de sentimiento en redes sociales.</p>"
       "<h5>Problema · Y/R</h5>"
       "<p>Sea X la salida del sumador de entrada: \\(X=R-H_1Y\\). Las ramas G<sub>1</sub> y G<sub>2</sub> parten del mismo punto y se suman:</p>"
       "<div class='formula'>$$Y=(G_1+G_2)\\,X=(G_1+G_2)(R-H_1Y)$$</div>"
       "<div class='formula'>$$Y\\big[1+(G_1+G_2)H_1\\big]=(G_1+G_2)\\,R$$</div>"
       "<div class='formula'>$$\\boxed{\\ \\dfrac{Y(s)}{R(s)}=\\dfrac{G_1+G_2}{1+(G_1+G_2)\\,H_1}\\ }$$</div>"
       "<div class='res'><b>Y/R = (G<sub>1</sub>+G<sub>2</sub>) / [1 + (G<sub>1</sub>+G<sub>2</sub>)H<sub>1</sub>]</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cyl_2025_ordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
