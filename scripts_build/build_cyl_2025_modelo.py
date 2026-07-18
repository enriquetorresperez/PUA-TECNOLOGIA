#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Castilla y León EBAU 2025 · Modelo 0 (Tecnología e Ingeniería II).
Reutiliza las figuras del Modelo 2024 (idéntico contenido) y la estructura por apartados del 2026."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt
from cyllib import Plot, beam, diagram_VM, ac_parallel, power_triangle, CURVE, ACC, ROSE

FIG = "fig"


def fig_traccion():
    p = Plot((0, 55), (0, 300), w=470, h=330,
             xlabel='&epsilon; (&times;10&#8315;&#8308;)', ylabel='&sigma; (MPa)', maxw=470)
    p.axes(xticks=[0, 10, 20, 30, 40, 50], yticks=[0, 50, 90, 130, 200, 260, 300], grid=True)
    p.polyline([(0, 0), (4.5, 90)], color=CURVE, width=2.6)
    p.polyline([(4.5, 90), (6.3, 130)], color=CURVE, width=2.6)
    p.polyline([(6.3, 130), (9, 150), (11, 148), (13, 158), (15, 156)], color=CURVE, width=2.6)
    p.polyline([(15, 156), (30, 235), (48.9, 260)], color=CURVE, width=2.6)
    p.polyline([(48.9, 260), (53, 232)], color=CURVE, width=2.6)
    p.point(4.5, 90, 'P (4,5·10⁻⁴, 90)', color=ACC, dx=8, dy=16)
    p.point(6.3, 130, 'E (6,3·10⁻⁴, 130)', color=ACC, dx=8, dy=-8)
    p.point(15, 156, 'F', color=ROSE, dx=2, dy=-10)
    p.point(48.9, 260, 'R (48,9·10⁻⁴, 260)', color=ROSE, dx=-6, dy=-10, anchor='end')
    p.point(53, 232, '', color=ROSE)
    return p.close()


def fig_viga():
    return beam(loads=[{'type': 'P', 'xm': 1.5, 'val': 'P = 16 kN'}],
                supports=[{'xm': 0, 'kind': 'pin', 'label': 'A'},
                          {'xm': 6, 'kind': 'roller', 'label': 'B'}],
                span_m=6, dims=[(0, 1.5, '1,50 m'), (0, 6, '6,00 m')])


def fig_V():
    return diagram_VM([(0, 12), (1.5, 12), (1.5, -4), (6, -4)], 6, kind='V', unit='kN',
                      title='Esfuerzo cortante V (kN)')


def fig_M():
    return diagram_VM([(0, 0), (1.5, 18), (6, 0)], 6, kind='M', unit='kN·m',
                      title='Momento flector M (kN·m)')


def fig_ac():
    return ac_parallel([('R', '15 Ω'), ('L', '45j Ω'), ('C', '−15j Ω')], V='220 V', f='50 Hz')


def fig_triangulo():
    return power_triangle(3226.7, 2151.1, 3878.0, 33.69, inductive=False,
                          labels={'P': 'P = 3227 W', 'Q': 'Q = 2151 VAr (cap.)', 'S': 'S = 3878 VA'})


def fig_bloques_ce():
    s = svg_open('720 300', 640)
    ym = 150
    s += txt(24, ym + 5, 'E', '#e2e8f0', 15)
    s += arrow(38, ym, 66, ym); s += summer(82, ym)
    s += txt(66, ym - 12, '+', '#4ade80', 15); s += txt(70, ym + 30, '−', '#fb7185', 17)
    s += arrow(98, ym, 132, ym); s += "<circle cx='132' cy='150' r='3.4' fill='#cbd5e1'/>"
    s += arrow(132, ym, 168, ym)
    s += box(168, 128, 66, 44, 'G<tspan dy=\"4\" font-size=\"11\">1</tspan>', '#22d3ee')
    s += arrow(234, ym, 268, ym)
    s += box(268, 128, 66, 44, 'G<tspan dy=\"4\" font-size=\"11\">2</tspan>', '#22d3ee')
    s += arrow(334, ym, 402, ym); s += summer(418, ym)
    s += txt(400, ym + 30, '+', '#4ade80', 15); s += txt(430, ym - 12, '+', '#4ade80', 15)
    s += arrow(434, ym, 470, ym); s += "<circle cx='470' cy='150' r='3.4' fill='#cbd5e1'/>"
    s += arrow(470, ym, 512, ym); s += txt(524, ym + 5, 'C', '#e2e8f0', 15)
    s += box(240, 60, 66, 40, 'G<tspan dy=\"4\" font-size=\"11\">3</tspan>', '#38bdf8')
    s += line(132, ym, 132, 80); s += line(132, 80, 240, 80)
    s += line(306, 80, 418, 80); s += arrow(418, 80, 418, 135)
    s += box(240, 228, 66, 40, 'H<tspan dy=\"4\" font-size=\"11\">1</tspan>', '#a78bfa')
    s += line(470, ym, 470, 248); s += line(470, 248, 306, 248)
    s += line(240, 248, 82, 248); s += arrow(82, 248, 82, 165)
    return s + "</svg>"


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · Castilla y León · Modelo 0 · 2025 · Examen resuelto y comentado",
  "cabecera_titulo": "EBAU · <span>Tecnología e Ingeniería II</span> · Castilla y León · Modelo 0 (2025)",
  "pill": "90 min · 2,5 pt/pregunta · 4 apartados",
  "enunciado_pdf": "../../examens/Castilla y Leon/Tecnologia_CastillayLeon_2025_modelo.pdf",
  "pdf_dir": "pdf_cyl_2025_modelo",
  "footer": "Dpto. Tecnología · Solucionario EBAU · Castilla y León · Tecnología e Ingeniería II (Modelo 0 · 2025)",
  "intro_inicio": "El ejercicio consta de <b>cuatro apartados obligatorios</b>. El primero tiene una única pregunta; en los otros tres se elige <b>una de las dos</b>. Aquí se resuelven <b>todas</b>. Selecciona un apartado o una pregunta en la barra lateral.",
  "indice_nombre": "Exámenes de Castilla y León",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Apartado 1 (Bloque B) · Ensayo y diagramas de fases", "color": "#f59e0b",
   "descripcion_tarjeta": "Pregunta única: ensayo de tracción o diagrama de equilibrio de fases (Bi-Sb).",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><path d='M10 50 Q20 15 45 12 T82 20'/><circle cx='45' cy='12' r='3' fill='#f59e0b' stroke='none'/></svg>",
   "cuestiones": [
    {
     "id": "q1", "titulo": "Pregunta única (Tipo 1) · Ensayo de tracción", "etiqueta": "APARTADO 1",
     "menu": "P única · Tracción (Tipo 1)", "titulo_corto": "P1",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a-d 0,5 c/u)",
     "enunciado_html": "<p><i>El apartado 1 tiene una única pregunta. El modelo muestra dos ejemplos posibles (Tipo 1 y Tipo 2); en el examen sólo aparece uno.</i></p><p><b>Cuestión.</b> Explica en qué consiste el ensayo Brinell. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> En la figura se muestra el diagrama de tracción de una barra de <b>400 mm</b> y <b>25 mm²</b>.</p><ol type='a'><li>Comenta las características de la gráfica. <span class='pts'>(0,5 ptos.)</span></li><li>Calcula el módulo de elasticidad (en GPa). <span class='pts'>(0,5 ptos.)</span></li><li>Calcula la longitud de la barra (mm) al aplicar una fuerza de 2 kN. <span class='pts'>(0,5 ptos.)</span></li><li>Determina la fuerza (kN) que produce la rotura. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_traccion() + "<figcaption>Diagrama σ–ε. Puntos: P (proporcionalidad), E (límite elástico), F (fluencia), R (carga máxima).</figcaption></figure>",
     "aplica_html": "<p>Ley de Hooke en la zona elástica: \\(E=\\sigma/\\varepsilon\\) (pendiente inicial). Tensión \\(\\sigma=F/S\\); alargamiento elástico \\(\\Delta L=\\dfrac{\\sigma}{E}L_0\\). Fuerza de rotura \\(F=\\sigma_{\\max}\\cdot S\\).</p>",
     "solucion_html":
       "<h5>Cuestión · ensayo Brinell</h5>"
       "<p>El <b>ensayo Brinell</b> mide la <b>dureza</b>: se presiona una <b>bola de acero templado</b> (diámetro D) contra el material con una carga F durante un tiempo; se mide el diámetro de la huella y se calcula \\(HB=\\dfrac{2F}{\\pi D\\,(D-\\sqrt{D^2-d^2})}\\). A mayor huella, menor dureza.</p>"
       "<h5>a) Características de la gráfica</h5>"
       "<p>O–P recta elástica (Hooke); P límite de proporcionalidad; E límite elástico; F escalón de fluencia; endurecimiento hasta la carga máxima <b>R</b> (σ<sub>máx</sub> = 260 MPa) y después estricción y rotura.</p>"
       "<h5>b) Módulo de elasticidad</h5>"
       "<div class='formula'>$$E=\\frac{\\sigma_P}{\\varepsilon_P}=\\frac{90}{4{,}5\\cdot10^{-4}}=2{,}0\\cdot10^{5}\\ \\mathrm{MPa}=200\\ \\mathrm{GPa}$$</div>"
       "<div class='res'><b>E = 200 GPa</b></div>"
       "<h5>c) Longitud con F = 2 kN</h5>"
       "<div class='formula'>$$\\sigma=\\frac{F}{S}=\\frac{2000}{25}=80\\ \\mathrm{MPa}\\ (<90,\\ \\text{elástico})\\Rightarrow\\varepsilon=\\frac{\\sigma}{E}=\\frac{80}{2\\cdot10^{5}}=4\\cdot10^{-4}$$</div>"
       "<div class='formula'>$$\\Delta L=\\varepsilon L_0=4\\cdot10^{-4}\\cdot400=0{,}16\\ \\mathrm{mm}\\Rightarrow L=400{,}16\\ \\mathrm{mm}$$</div>"
       "<div class='res'><b>L ≈ 400,16 mm</b></div>"
       "<h5>d) Fuerza de rotura</h5>"
       "<div class='formula'>$$F_{\\text{rotura}}=\\sigma_{\\max}\\cdot S=260\\cdot25=6500\\ \\mathrm N=6{,}5\\ \\mathrm{kN}$$</div>"
       "<div class='res'><b>F<sub>rotura</sub> = 6,5 kN</b></div>"
    },
    {
     "id": "q2", "titulo": "Pregunta única (Tipo 2) · Diagrama de fases Bi-Sb", "etiqueta": "APARTADO 1",
     "menu": "P única · Fases Bi-Sb (Tipo 2)", "titulo_corto": "P2",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a-d 0,5 c/u)",
     "enunciado_html": "<p><b>Cuestión.</b> ¿Qué diferencia existe entre una transformación eutectoide y una eutéctica? Define cada una. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> A la vista del diagrama de fases de una aleación de bismuto y antimonio:</p><ol type='a'><li>Indica qué tipo de solubilidad tiene. <span class='pts'>(0,5 ptos.)</span></li><li>Indica la temperatura de fusión del Bi y del Sb puros. <span class='pts'>(0,5 ptos.)</span></li><li>Describe el enfriamiento desde 700 °C hasta ambiente de una aleación con 65 % de antimonio. <span class='pts'>(0,5 ptos.)</span></li><li>Determina la proporción de fases a 400 °C en una aleación con 80 % de bismuto. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'><img src='" + FIG + "/cyl24mod_fases.png' alt='Diagrama de fases Bi-Sb' style='max-width:430px;width:100%;background:#fff;border-radius:8px;padding:8px'><figcaption>Diagrama Bi–Sb (isomorfo): T<sub>f</sub>(Bi)=271,4 °C, T<sub>f</sub>(Sb)=630,5 °C.</figcaption></figure>",
     "aplica_html": "<p>Diagrama <b>isomorfo</b> (solubilidad total): liquidus y solidus encierran la lente L+&alpha;. Para las proporciones, <b>regla de la palanca</b>.</p>",
     "solucion_html":
       "<h5>Cuestión · eutéctica vs eutectoide</h5>"
       "<div class='formula'>$$\\text{Eutéctica: } L \\rightleftharpoons \\alpha+\\beta \\qquad \\text{Eutectoide: } \\gamma \\rightleftharpoons \\alpha+\\beta$$</div>"
       "<p>En la <b>eutéctica</b> se transforma un <b>líquido</b> en dos sólidos; en la <b>eutectoide</b>, un <b>sólido</b> se descompone en otros dos sólidos. Ambas a temperatura constante.</p>"
       "<h5>a) Solubilidad</h5><p>Una única lente sin eutéctico → <b>solubilidad total</b> (isomorfo, solución sólida &alpha;).</p>"
       "<div class='res'><b>Solubilidad total (isomorfo)</b></div>"
       "<h5>b) Temperaturas de fusión</h5>"
       "<div class='res'><b>T<sub>f</sub>(Bi) = 271,4 °C&nbsp;·&nbsp;T<sub>f</sub>(Sb) = 630,5 °C</b></div>"
       "<h5>c) Enfriamiento de 65 % Sb desde 700 °C</h5>"
       "<ul><li><b>700 °C:</b> todo líquido.</li>"
       "<li><b>≈ 545 °C (liquidus):</b> empieza a solidificar &alpha;.</li>"
       "<li><b>545 → 445 °C:</b> zona L+&alpha; (crece el sólido).</li>"
       "<li><b>≈ 445 °C (solidus):</b> todo sólido &alpha;.</li>"
       "<li><b>445 °C → ambiente:</b> enfriamiento del sólido.</li></ul>"
       "<h5>d) Proporción de fases a 400 °C con 80 % Bi (20 % Sb)</h5>"
       "<p>En la lente L+&alpha;; leyendo la isoterma: C<sub>L</sub> ≈ 10 % Sb, C<sub>&alpha;</sub> ≈ 42 % Sb, C<sub>0</sub> = 20 % Sb.</p>"
       "<div class='formula'>$$\\%\\alpha=\\frac{20-10}{42-10}\\approx31\\%\\qquad\\%L=\\frac{42-20}{42-10}\\approx69\\%$$</div>"
       "<div class='res'><b>≈ 31 % sólido &alpha; y ≈ 69 % líquido</b> (aprox.)</div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Apartado 2 (Bloque C) · Estructuras / Máquinas térmicas", "color": "#22d3ee",
   "descripcion_tarjeta": "Elige: viga con carga puntual o motor alternativo de 4 cilindros.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><path d='M8 34h74'/><path d='M45 12v18'/><path d='M40 18l5-6 5 6'/><path d='M8 34l-4 8h8zM82 34a5 5 0 1 0 0 8'/></svg>",
   "cuestiones": [
    {
     "id": "q3", "titulo": "Pregunta 1 (Opción A) · Estructuras: viga", "etiqueta": "APARTADO 2 · A",
     "menu": "P1 (A) · Viga con carga puntual", "titulo_corto": "P3",
     "meta": "Pregunta de 2,5 puntos (a 0,5 · b 1,5 · c 0,5)",
     "enunciado_html": "<p><b>Problema.</b> De la viga de la figura:</p><ol type='a'><li>Calcula las reacciones en los apoyos. <span class='pts'>(0,5 ptos.)</span></li><li>Calcula los momentos flectores y esfuerzos cortantes. <span class='pts'>(1,5 ptos.)</span></li><li>Representa los diagramas del momento flector y del esfuerzo cortante. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_viga() + "<figcaption>Viga simplemente apoyada de 6 m con carga P = 16 kN a 1,50 m de A.</figcaption></figure>",
     "aplica_html": "<p>Equilibrio: \\(\\sum M_A=0\\) y \\(\\sum F_y=0\\). El cortante es constante por tramos y el momento máximo se da bajo la carga.</p>",
     "solucion_html":
       "<h5>a) Reacciones</h5>"
       "<div class='formula'>$$R_B\\cdot6=16\\cdot1{,}5\\Rightarrow R_B=4\\ \\mathrm{kN}\\qquad R_A=16-4=12\\ \\mathrm{kN}$$</div>"
       "<div class='res'><b>R<sub>A</sub> = 12 kN · R<sub>B</sub> = 4 kN</b></div>"
       "<h5>b) Cortantes y momentos</h5>"
       "<p>A–P (0–1,5): V = +12 kN. P–B (1,5–6): V = 12 − 16 = −4 kN. Momento bajo la carga: M = 12·1,5 = 18 kN·m.</p>"
       "<div class='res'><b>V = +12 / −4 kN · M<sub>máx</sub> = 18 kN·m</b></div>"
       "<h5>c) Diagramas</h5>"
       "<figure class='fig'>" + fig_V() + "<figcaption>Esfuerzo cortante.</figcaption></figure>"
       "<figure class='fig'>" + fig_M() + "<figcaption>Momento flector.</figcaption></figure>"
    },
    {
     "id": "q4", "titulo": "Pregunta 2 (Opción B) · Máquinas térmicas: motor", "etiqueta": "APARTADO 2 · B",
     "menu": "P2 (B) · Motor de 4 cilindros", "titulo_corto": "P4",
     "meta": "Pregunta de 2,5 puntos (cuestión 1,0 · a-c 0,5 c/u)",
     "enunciado_html": "<p><b>Cuestión.</b> Dibuja el diagrama p–v de un ciclo de Carnot y explica sus transformaciones. <span class='pts'>(1 pto.)</span></p><p><b>Problema.</b> Motor de 4 cilindros, M<sub>máx</sub> = 300 N·m a 3750 rpm, D = 80 mm, carrera 92 mm, V<sub>c</sub> = 58,5 cm³. Determina:</p><ol type='a'><li>La cilindrada total. <span class='pts'>(0,5 ptos.)</span></li><li>La potencia en par máximo. <span class='pts'>(0,5 ptos.)</span></li><li>La relación de compresión. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>\\(V_u=\\frac{\\pi D^2}{4}S\\), \\(V_T=zV_u\\); \\(P=M\\omega\\) con \\(\\omega=\\frac{2\\pi n}{60}\\); \\(r_c=\\frac{V_u+V_c}{V_c}\\).</p>",
     "solucion_html":
       "<h5>Cuestión · ciclo de Carnot</h5>"
       "<p>Cuatro transformaciones reversibles: <b>expansión isoterma</b> (absorbe Q₁ a T<sub>cal</sub>), <b>expansión adiabática</b> (baja a T<sub>fría</sub>), <b>compresión isoterma</b> (cede Q₂ a T<sub>fría</sub>) y <b>compresión adiabática</b> (vuelve a T<sub>cal</sub>). En p–v son dos isotermas y dos adiabáticas; el área encerrada es el trabajo. \\(\\eta=1-T_2/T_1\\).</p>"
       "<h5>a) Cilindrada total</h5>"
       "<div class='formula'>$$V_u=\\frac{\\pi\\cdot8^2}{4}\\cdot9{,}2=462{,}4\\ \\mathrm{cm^3}\\Rightarrow V_T=4\\cdot462{,}4=1849{,}8\\ \\mathrm{cm^3}$$</div>"
       "<div class='res'><b>V<sub>T</sub> ≈ 1850 cm³ (1,85 L)</b></div>"
       "<h5>b) Potencia en par máximo</h5>"
       "<div class='formula'>$$\\omega=\\frac{2\\pi\\cdot3750}{60}=392{,}7\\ \\mathrm{rad/s}\\Rightarrow P=300\\cdot392{,}7=117{,}8\\ \\mathrm{kW}$$</div>"
       "<div class='res'><b>P ≈ 117,8 kW (≈ 160 CV)</b></div>"
       "<h5>c) Relación de compresión</h5>"
       "<div class='formula'>$$r_c=\\frac{462{,}4+58{,}5}{58{,}5}=8{,}9$$</div>"
       "<div class='res'><b>r<sub>c</sub> ≈ 8,9 : 1</b></div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Apartado 3 (Bloques C y D) · Neumática / Corriente alterna", "color": "#a78bfa",
   "descripcion_tarjeta": "Elige: instalación oleohidráulica o circuito RLC en paralelo.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#a78bfa' stroke-width='3'><path d='M8 30h12l4-10 8 20 8-20 8 20 4-10h26'/></svg>",
   "cuestiones": [
    {
     "id": "q5", "titulo": "Pregunta 1 (Opción A) · Neumática e hidráulica", "etiqueta": "APARTADO 3 · A",
     "menu": "P1 (A) · Instalación oleohidráulica", "titulo_corto": "P5",
     "meta": "Pregunta de 2,5 puntos (a 1,0 · b 0,75 · c 0,75)",
     "enunciado_html": "<p><b>Problema.</b> En la instalación oleohidráulica de la figura:</p><ol type='a'><li>Define cada componente numerado. <span class='pts'>(1 pto.)</span></li><li>Explica la misión de los pulsadores manuales. <span class='pts'>(0,75 ptos.)</span></li><li>¿Cuál es la primera operación al arrancar la bomba? <span class='pts'>(0,75 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'><img src='" + FIG + "/cyl24mod_hidraulica.png' alt='Instalación oleohidráulica' style='max-width:430px;width:100%;background:#fff;border-radius:8px;padding:8px'><figcaption>Cilindro de doble efecto (1.0), distribuidor 4/3 (1.1) y grupo de presión (0.1).</figcaption></figure>",
     "aplica_html": "<p>Identificamos el actuador, el distribuidor, los elementos de mando (pulsadores 3/2), las reguladoras de caudal y el grupo de presión con su limitadora.</p>",
     "solucion_html":
       "<h5>a) Componentes numerados</h5><ul>"
       "<li><b>1.0</b> — Cilindro hidráulico de <b>doble efecto</b>.</li>"
       "<li><b>1.1</b> (central) — <b>Distribuidor 4/3</b> con pilotaje: dirige el aceite a cada cámara (avance/retroceso/centro).</li>"
       "<li><b>1.02, 1.03</b> — <b>Reguladoras de caudal unidireccionales</b> (velocidad de avance y retroceso).</li>"
       "<li><b>1.1, 1.2, 1.3</b> (inferiores) — Válvulas <b>3/2</b> con <b>pulsador</b> y retorno por muelle.</li>"
       "<li><b>1.01</b> — Válvula <b>limitadora de presión</b> (seguridad).</li>"
       "<li><b>0.1</b> — <b>Bomba</b> hidráulica movida por el <b>motor eléctrico M</b>.</li></ul>"
       "<h5>b) Misión de los pulsadores</h5>"
       "<p>Son el <b>mando</b>: al accionarlos pilotan el distribuidor 1.1 y ordenan el <b>avance o retroceso</b> del cilindro.</p>"
       "<h5>c) Primera operación al arrancar</h5>"
       "<p>Sin accionar ningún pulsador, la bomba impulsa caudal y, al no haber consumo, la <b>limitadora 1.01 abre y descarga el aceite a tanque</b>. La primera operación es la <b>descarga a tanque</b> hasta dar una orden de maniobra.</p>"
    },
    {
     "id": "q6", "titulo": "Pregunta 2 (Opción B) · Corriente alterna: RLC paralelo", "etiqueta": "APARTADO 3 · B",
     "menu": "P2 (B) · Circuito RLC paralelo", "titulo_corto": "P6",
     "meta": "Pregunta de 2,5 puntos (a 0,5 · b 0,5 · c 1,0 · d 0,5)",
     "enunciado_html": "<p><b>Problema.</b> En el circuito de corriente alterna (220 V, 50 Hz) con R = 15 Ω, X<sub>L</sub> = 45j Ω y X<sub>C</sub> = −15j Ω en paralelo, determina:</p><ol type='a'><li>La impedancia total. <span class='pts'>(0,5 ptos.)</span></li><li>La intensidad total y por cada componente. <span class='pts'>(0,5 ptos.)</span></li><li>Las potencias activa, reactiva y aparente. <span class='pts'>(1 pto.)</span></li><li>Dibuja el triángulo de potencias. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_ac() + "<figcaption>R = 15 Ω, X<sub>L</sub> = 45 Ω y X<sub>C</sub> = 15 Ω en paralelo (220 V, 50 Hz).</figcaption></figure>",
     "aplica_html": "<p>En paralelo se suman admitancias: \\(Y=\\frac1R+\\frac1{jX_L}+\\frac1{-jX_C}\\). \\(Z=1/|Y|\\), \\(I=V|Y|\\). \\(P=V^2/R\\), \\(Q=V^2/X_L-V^2/X_C\\), \\(S=VI\\).</p>",
     "solucion_html":
       "<h5>a) Impedancia total</h5>"
       "<div class='formula'>$$Y=\\tfrac1{15}+\\tfrac1{45j}+\\tfrac1{-15j}=0{,}0667+0{,}0444j\\ \\mathrm S\\Rightarrow|Y|=0{,}0801\\ \\mathrm S$$</div>"
       "<div class='formula'>$$Z=1/|Y|=12{,}48\\ \\Omega\\quad(\\varphi=-33{,}7^\\circ,\\ \\text{capacitivo})$$</div>"
       "<div class='res'><b>Z ≈ 12,48 Ω</b></div>"
       "<h5>b) Intensidades</h5>"
       "<div class='formula'>$$I=V|Y|=220\\cdot0{,}0801=17{,}63\\ \\mathrm A$$</div>"
       "<div class='formula'>$$I_R=\\tfrac{220}{15}=14{,}67\\,\\mathrm A\\quad I_L=\\tfrac{220}{45}=4{,}89\\,\\mathrm A\\quad I_C=\\tfrac{220}{15}=14{,}67\\,\\mathrm A$$</div>"
       "<div class='res'><b>I = 17,63 A · I<sub>R</sub>=14,67 · I<sub>L</sub>=4,89 · I<sub>C</sub>=14,67 A</b></div>"
       "<h5>c) Potencias</h5>"
       "<div class='formula'>$$P=\\tfrac{220^2}{15}=3226{,}7\\ \\mathrm W\\qquad Q=\\tfrac{220^2}{45}-\\tfrac{220^2}{15}=-2151\\ \\mathrm{VAr}$$</div>"
       "<div class='formula'>$$S=220\\cdot17{,}63=3878\\ \\mathrm{VA}\\quad(\\cos\\varphi=0{,}83)$$</div>"
       "<div class='res'><b>P ≈ 3227 W · Q ≈ −2151 VAr (cap.) · S ≈ 3878 VA</b></div>"
       "<h5>d) Triángulo de potencias</h5>"
       "<figure class='fig'>" + fig_triangulo() + "<figcaption>Circuito capacitivo (Q por debajo de P).</figcaption></figure>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Apartado 4 (Bloques D, E, F) · Electrónica digital / Control", "color": "#4ade80",
   "descripcion_tarjeta": "Elige: diseño de una alarma con lógica digital o función de transferencia de un diagrama de bloques.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#4ade80' stroke-width='3'><rect x='34' y='22' width='24' height='16' rx='3'/><path d='M8 30h26M58 30h24'/><circle cx='20' cy='30' r='6'/></svg>",
   "cuestiones": [
    {
     "id": "q7", "titulo": "Pregunta 1 (Opción A) · Electrónica digital: alarma", "etiqueta": "APARTADO 4 · A",
     "menu": "P1 (A) · Alarma con NAND", "titulo_corto": "P7",
     "meta": "Pregunta de 2,5 puntos (cuestión 0,5 · a 0,75 · b 0,75 · c 0,5)",
     "enunciado_html": "<p><b>Cuestión.</b> Representa la tabla de verdad de la puerta lógica OR. <span class='pts'>(0,5 ptos.)</span></p><p><b>Problema.</b> Alarma de evacuación con tres sensores: incendio (A), humedad (B) y presión (C). Se activa si hay incendio, o si se superan conjuntamente presión y humedad.</p><ol type='a'><li>Tabla de verdad y función lógica. <span class='pts'>(0,75 ptos.)</span></li><li>Simplifica por Karnaugh. <span class='pts'>(0,75 ptos.)</span></li><li>Implementa con NAND de dos entradas. <span class='pts'>(0,5 ptos.)</span></li></ol>",
     "figura_enunciado_svg": "",
     "aplica_html": "<p>La alarma F = A + B·C. El mapa de Karnaugh confirma que ya es mínima. Para NAND se aplica doble negación y De Morgan.</p>",
     "solucion_html":
       "<h5>Cuestión · tabla de verdad OR</h5>"
       "<table class='dat'><tr><th>A</th><th>B</th><th>A+B</th></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>"
       "<h5>a) Tabla de verdad y función</h5>"
       "<table class='dat'><tr><th>A</th><th>B</th><th>C</th><th>F</th></tr>"
       "<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
       "<tr><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
       "<tr><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>"
       "<div class='formula'>$$F=A+B\\cdot C$$</div>"
       "<h5>b) Karnaugh</h5>"
       "<p>Bloque de 4 (toda la fila A=1) → A; bloque de 2 (B=C=1) → B·C. Mínima: <b>F = A + B·C</b>.</p>"
       "<h5>c) Con NAND de 2 entradas</h5>"
       "<div class='formula'>$$F=A+BC=\\overline{\\ \\overline A\\cdot\\overline{BC}\\ }=\\mathrm{NAND}\\big(\\mathrm{NAND}(A,A),\\ \\mathrm{NAND}(B,C)\\big)$$</div>"
       "<div class='res'><b>3 puertas NAND de 2 entradas</b></div>"
    },
    {
     "id": "q8", "titulo": "Pregunta 2 (Opción B) · Sistemas de control", "etiqueta": "APARTADO 4 · B",
     "menu": "P2 (B) · Función de transferencia C/E", "titulo_corto": "P8",
     "meta": "Pregunta de 2,5 puntos (a 0,5 · b 0,5 · problema 1,5)",
     "enunciado_html": "<p><b>Cuestiones.</b></p><ol type='a'><li>Explica alguna aplicación de la inteligencia artificial. <span class='pts'>(0,5 ptos.)</span></li><li>Ventajas e inconvenientes del lazo cerrado frente al abierto. <span class='pts'>(0,5 ptos.)</span></li></ol><p><b>Problema.</b> Calcula la función de transferencia C/E del sistema de control de la figura. <span class='pts'>(1,5 ptos.)</span></p>",
     "figura_enunciado_svg": "<figure class='fig'>" + fig_bloques_ce() + "<figcaption>G<sub>1</sub>, G<sub>2</sub> en serie con G<sub>3</sub> en paralelo y realimentación H<sub>1</sub>.</figcaption></figure>",
     "aplica_html": "<p>Ramas en paralelo se suman (G<sub>1</sub>G<sub>2</sub>+G<sub>3</sub>); el lazo con realimentación negativa da \\(\\frac{G}{1+GH}\\).</p>",
     "solucion_html":
       "<h5>a) Aplicación de la IA</h5>"
       "<p>Asistentes de voz y traductores (PLN), visión artificial para diagnóstico o conducción autónoma, sistemas de recomendación o mantenimiento predictivo: aprenden de datos para decidir o predecir.</p>"
       "<h5>b) Lazo cerrado frente a abierto</h5>"
       "<p><b>Ventajas:</b> mide la salida y corrige errores/perturbaciones, más preciso y estable. <b>Inconvenientes:</b> más complejo y caro (sensores, comparador) y puede volverse inestable si está mal diseñado.</p>"
       "<h5>Problema · C/E</h5>"
       "<p>Con \\(X=E-H_1C\\) y las dos vías directas en paralelo:</p>"
       "<div class='formula'>$$C=(G_1G_2+G_3)(E-H_1C)\\Rightarrow C[1+(G_1G_2+G_3)H_1]=(G_1G_2+G_3)E$$</div>"
       "<div class='formula'>$$\\boxed{\\ \\dfrac{C}{E}=\\dfrac{G_1G_2+G_3}{1+(G_1G_2+G_3)H_1}\\ }$$</div>"
       "<div class='res'><b>C/E = (G<sub>1</sub>G<sub>2</sub> + G<sub>3</sub>) / [1 + (G<sub>1</sub>G<sub>2</sub> + G<sub>3</sub>)H<sub>1</sub>]</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cyl_2025_modelo.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
