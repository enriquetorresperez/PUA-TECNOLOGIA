#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JSON del examen UCLM 2025/26 · Modelo A (prensa neumática, control, bomba de calor, Brinell)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, txt, line, arrow
from cyllib import INK, MUT, OK, ROSE, VIOL, CURVE


def img(name, alt, maxw=430, cap=None):
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return (f"<figure class='fig'><img src='fig/{name}' alt='{alt}' "
            f"style='max-width:{maxw}px;width:100%;background:#fff;border-radius:8px;padding:10px'>"
            f"{c}</figure>")


def fig_control_2a():
    """X → Σ → Σ → [3] → Y → comparador → actuador, con realimentación [2] y unitaria."""
    s = svg_open('700 270', 690)
    ym = 105
    s += txt(18, ym + 5, 'X', INK, 15)
    s += arrow(30, ym, 58, ym)
    s += summer(76, ym)
    s += txt(60, ym - 14, '+', OK, 14) + txt(60, ym + 30, '−', ROSE, 16)
    s += arrow(92, ym, 138, ym)
    s += summer(156, ym)
    s += txt(140, ym - 14, '+', OK, 14) + txt(140, ym + 30, '−', ROSE, 16)
    s += arrow(172, ym, 206, ym)
    s += box(206, ym - 18, 48, 36, '3', CURVE, 16)
    s += line(254, ym, 300, ym) + "<circle cx='300' cy='105' r='3.2' fill='#cbd5e1'/>"
    s += txt(300, ym - 12, 'Y', INK, 15, 'middle')
    s += arrow(300, ym, 336, ym)
    s += box(336, ym - 22, 122, 44, 'COMPARADOR', '#38bdf8', 13)
    s += txt(470, ym - 12, 'S', INK, 15, 'middle')
    s += arrow(458, ym, 494, ym)
    s += box(494, ym - 22, 108, 44, 'ACTUADOR', OK, 13)
    # realimentación con ganancia 2 (de Y a Σ2)
    s += line(300, ym, 300, 180) + arrow(300, 180, 236, 180)
    s += box(170, 162, 48, 34, '2', VIOL, 15)
    s += line(170, 180, 156, 180) + arrow(156, 180, 156, ym + 16)
    # realimentación unitaria (de Y a Σ1)
    s += line(300, ym, 300, 232) + arrow(300, 232, 76, 232)
    s += line(76, 232, 76, ym + 16) + arrow(76, ym + 20, 76, ym + 16)
    return s + "</svg>"


def fig_control_2b():
    """R(s) → Σ → [500/((s+1)(s+4))] → C(s), realimentación unitaria."""
    s = svg_open('620 220', 600)
    ym = 92
    s += txt(16, ym + 5, 'R(s)', INK, 15)
    s += arrow(48, ym, 96, ym)
    s += summer(114, ym)
    s += txt(98, ym - 14, '+', OK, 14) + txt(98, ym + 30, '−', ROSE, 16)
    s += arrow(130, ym, 176, ym)
    s += box(176, ym - 26, 210, 52, '', CURVE, 14)
    s += txt(281, ym - 4, '500', INK, 15, 'middle')
    s += line(214, ym + 4, 348, ym + 4, INK)
    s += txt(281, ym + 20, '(s+1)(s+4)', INK, 13, 'middle')
    s += line(386, ym, 452, ym) + "<circle cx='452' cy='92' r='3.2' fill='#cbd5e1'/>"
    s += arrow(452, ym, 500, ym) + txt(510, ym + 5, 'C(s)', INK, 15)
    s += line(452, ym, 452, 168) + arrow(452, 168, 114, 168)
    s += line(114, 168, 114, ym + 16) + arrow(114, ym + 20, 114, ym + 16)
    return s + "</svg>"


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · UCLM (Castilla-La Mancha) · Curso 2025/26 · Modelo A · Examen resuelto",
  "cabecera_titulo": "PAU 2026 · <span>Tecnología e Ingeniería II</span> · UCLM · Modelo A",
  "pill": "4 ejercicios · 2,5 pt cada uno · 90 min",
  "enunciado_pdf": "../../examens/UCLM/Tecnologia e Ingenieria.pdf",
  "pdf_dir": "pdf_clm_2026_modelo_a",
  "footer": "Solucionario PAU · UCLM (Castilla-La Mancha) · Tecnología e Ingeniería II (Modelo A, curso 2025/26)",
  "intro_inicio": "Modelo orientativo del curso 2025/26. La prueba consta de <b>4 ejercicios</b> de 2,5 puntos; en los ejercicios <b>1, 2 y 3</b> se elige una de las dos opciones (a o b) y el <b>ejercicio 4</b> es obligatorio. Aquí se resuelven <b>todas</b> las opciones con el enunciado oficial, los conceptos aplicados y la solución paso a paso.",
  "indice_nombre": "Exámenes de Castilla-La Mancha",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Ejercicio 1 · Neumática", "color": "#38bdf8",
   "descripcion_tarjeta": "Prensa neumática con cilindro de doble efecto e identificación de un circuito neumático.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#38bdf8' stroke-width='3'><rect x='12' y='22' width='40' height='16' rx='2'/><path d='M52 30h16M20 30h24'/><circle cx='72' cy='30' r='4'/></svg>",
   "cuestiones": [
    {
     "id": "q1a", "titulo": "Opción a · Prensa neumática (doble efecto)", "etiqueta": "NEUMÁTICA",
     "menu": "1a · Prensa neumática", "titulo_corto": "1a",
     "meta": "Opción a · 2,5 puntos (a 1 · b 1 · c 0,5)",
     "enunciado_html": "<p>Se diseña una prensa neumática con un <b>cilindro de doble efecto</b> para compactar material. El cilindro tiene: diámetro de émbolo <b>12 cm</b>, diámetro de vástago <b>4 cm</b>, carrera <b>50 cm</b> y rendimiento del <b>90 %</b>. El sistema trabaja a <b>6 bar</b> y realiza <b>80 ciclos por hora</b> (compresión y liberación). Se pide:</p><ol type='a'><li>Calcular la fuerza máxima de avance (en N) y la fuerza máxima de retorno (en N). <span class='pts'>(1 punto)</span></li><li>Determinar el consumo de aire de la instalación en condiciones normales (en m³/h). <span class='pts'>(1 punto)</span></li><li>Calcular el trabajo realizado en la carrera de avance. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>En el <b>avance</b> la presión actúa sobre toda el área del émbolo \\(A_1=\\pi D^2/4\\); en el <b>retorno</b>, sobre el área anular \\(A_2=A_1-A_v\\) (descontando el vástago). La fuerza útil es \\(F=p\\,A\\,\\eta\\). El <b>consumo de aire</b> a condiciones normales es el volumen barrido (avance + retorno) multiplicado por la <b>relación de compresión</b> \\((p_{man}+1)/1\\) y por los ciclos.</p>",
     "solucion_html":
       "<h5>a) Fuerzas de avance y retorno</h5>"
       "<div class='formula'>$$A_1=\\dfrac{\\pi D^2}{4}=\\dfrac{\\pi\\,0{,}12^2}{4}=0{,}01131\\ \\mathrm{m^2},\\quad A_2=A_1-\\dfrac{\\pi d_v^2}{4}=0{,}01005\\ \\mathrm{m^2}$$</div>"
       "<div class='formula'>$$F_{av}=p\\,A_1\\,\\eta=6\\cdot10^{5}\\cdot 0{,}01131\\cdot 0{,}9=6107\\ \\mathrm{N}$$</div>"
       "<div class='formula'>$$F_{ret}=p\\,A_2\\,\\eta=6\\cdot10^{5}\\cdot 0{,}01005\\cdot 0{,}9=5429\\ \\mathrm{N}$$</div>"
       "<div class='res'><b>F<sub>avance</sub> ≈ 6107 N · F<sub>retorno</sub> ≈ 5429 N</b></div>"
       "<h5>b) Consumo de aire (condiciones normales)</h5>"
       "<p>Volumen barrido por ciclo (avance + retorno) a la presión de trabajo:</p>"
       "<div class='formula'>$$V_{ciclo}=(A_1+A_2)\\,L=(0{,}01131+0{,}01005)\\cdot 0{,}5=0{,}01068\\ \\mathrm{m^3}$$</div>"
       "<p>Multiplicado por la relación de compresión \\((6+1)/1=7\\) y por los 80 ciclos/h:</p>"
       "<div class='formula'>$$Q=V_{ciclo}\\cdot 7\\cdot 80=0{,}01068\\cdot 7\\cdot 80\\approx 5{,}98\\ \\mathrm{m^3/h}$$</div>"
       "<div class='res'><b>Q ≈ 5,98 m³/h (aire en condiciones normales)</b></div>"
       "<h5>c) Trabajo en la carrera de avance</h5>"
       "<div class='formula'>$$W=F_{av}\\cdot L=6107\\cdot 0{,}5=3054\\ \\mathrm{J}$$</div>"
       "<div class='res'><b>W ≈ 3054 J</b></div>"
    },
    {
     "id": "q1b", "titulo": "Opción b · Circuito neumático", "etiqueta": "NEUMÁTICA",
     "menu": "1b · Circuito neumático", "titulo_corto": "1b",
     "meta": "Opción b · 2,5 puntos (a 1 · b 1,5)",
     "enunciado_html": "<p>Dado el siguiente circuito neumático, responde:</p><ol type='a'><li>Nombra los elementos que forman el circuito neumático. En las válvulas distribuidoras indica qué tipo de accionamiento y retorno tienen. <span class='pts'>(1 punto)</span></li><li>Explica su funcionamiento. <span class='pts'>(1,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": img("clm26a_neumatica.png", "Circuito neumático: cilindro 1.0 de simple efecto, válvulas 3/2 (1.1 y 1.2) y unidad de mantenimiento 0Z1", 430, "Circuito neumático del enunciado: cilindro 1.0, válvula 3/2 pilotada 1.1, válvula 3/2 de pulsador 1.2 y unidad de mantenimiento 0Z1 alimentada por la toma 0P."),
     "aplica_html": "<p>Hay que reconocer la <b>simbología neumática</b> (norma ISO 1219): el actuador (cilindro), las <b>válvulas distribuidoras 3/2</b> con su accionamiento y retorno, y la unidad de acondicionamiento del aire; después se razona la lógica de mando (mando indirecto o pilotado).</p>",
     "solucion_html":
       "<h5>a) Elementos del circuito</h5>"
       "<ul>"
       "<li><b>1.0 · Cilindro de simple efecto</b> con <b>retorno por muelle</b>. Es el actuador: el aire a presión lo hace avanzar y el muelle lo devuelve a su posición inicial.</li>"
       "<li><b>1.1 · Válvula distribuidora 3/2</b> (3 vías, 2 posiciones), normalmente cerrada, con <b>accionamiento neumático (pilotada)</b> y <b>retorno por muelle</b>. Es la válvula de potencia que alimenta el cilindro; se pilota con la señal que llega de 1.2.</li>"
       "<li><b>1.2 · Válvula distribuidora 3/2</b> (3 vías, 2 posiciones), normalmente cerrada, con <b>accionamiento manual por pulsador</b> y <b>retorno por muelle</b>. Es la válvula de mando.</li>"
       "<li><b>0Z1 · Unidad de mantenimiento</b> (filtro-regulador con manómetro) que acondiciona el aire.</li>"
       "<li><b>0P · Toma de aire comprimido</b> (fuente de energía).</li>"
       "</ul>"
       "<h5>b) Funcionamiento</h5>"
       "<p>Es un <b>mando indirecto</b>. El aire llega desde la toma <b>0P</b> a través de la unidad de mantenimiento <b>0Z1</b>. Al <b>pulsar la válvula 1.2</b>, ésta deja pasar aire que <b>pilota la válvula 1.1</b>; la 1.1 conmuta y envía aire a la cámara del cilindro <b>1.0</b>, que <b>avanza</b> comprimiendo el material.</p>"
       "<p>Al <b>soltar el pulsador</b>, el muelle de 1.2 la devuelve a su posición de reposo, cesa el pilotaje y el muelle de 1.1 la recoloca, comunicando la cámara del cilindro con el escape (vía 3). El <b>muelle del cilindro 1.0</b> lo hace <b>retroceder</b> a la posición inicial.</p>"
       "<div class='res'><b>Mando indirecto: el pulsador 1.2 pilota la 3/2 (1.1), que gobierna el avance del cilindro de simple efecto; todo retorna por muelle al soltar.</b></div>"
    }
   ]
  },
  {
   "id": "b2", "titulo": "Ejercicio 2 · Sistemas de control", "color": "#22d3ee",
   "descripcion_tarjeta": "Señal Y = f(X) con comparador y actuador, y función de transferencia + estabilidad de un lazo.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#22d3ee' stroke-width='3'><rect x='34' y='22' width='24' height='16' rx='3'/><path d='M8 30h26M58 30h24'/><circle cx='20' cy='30' r='6'/></svg>",
   "cuestiones": [
    {
     "id": "q2a", "titulo": "Opción a · Señal Y = f(X) y actuador", "etiqueta": "CONTROL",
     "menu": "2a · Señal Y = f(X)", "titulo_corto": "2a",
     "meta": "Opción a · 2,5 puntos (a 1,5 · b 1)",
     "enunciado_html": "<p>En la figura se muestra un sistema de control de una variable física X con una red de amplificación, un comparador y un actuador. La señal intermedia Y depende de X. El comparador cumple:</p><div class='formula'>$$Y<5\\Rightarrow S=1,\\qquad Y\\ge 5\\Rightarrow S=0$$</div><p>El actuador se activa con nivel alto (S = 1).</p><ol type='a'><li>Obtenga la expresión de la señal Y = f(X). <span class='pts'>(1,5 puntos)</span></li><li>Determine el rango de valores de X para los cuales se activa el actuador. <span class='pts'>(1 punto)</span></li></ol>",
     "figura_enunciado_svg": fig_control_2a(),
     "aplica_html": "<p>Se plantean las ecuaciones de los dos sumadores del lazo: la realimentación <b>unitaria</b> de Y al primer sumador y la de <b>ganancia 2</b> al segundo. Con el bloque de ganancia 3 se despeja Y = f(X). El actuador se activa cuando el comparador da S = 1, es decir cuando <b>Y &lt; 5</b>.</p>",
     "solucion_html":
       "<h5>a) Expresión de Y = f(X)</h5>"
       "<p>Sea \\(v_1\\) la salida del primer sumador y \\(v_2\\) la del segundo:</p>"
       "<div class='formula'>$$v_1=X-Y,\\qquad v_2=v_1-2Y,\\qquad Y=3\\,v_2$$</div>"
       "<div class='formula'>$$Y=3\\,(X-Y-2Y)=3X-9Y\\;\\Rightarrow\\;10Y=3X$$</div>"
       "<div class='formula'>$$\\boxed{\\ Y=\\dfrac{3}{10}\\,X=0{,}3\\,X\\ }$$</div>"
       "<h5>b) Rango de X que activa el actuador</h5>"
       "<p>El actuador se activa con S = 1, es decir con Y &lt; 5:</p>"
       "<div class='formula'>$$Y<5\\;\\Rightarrow\\;0{,}3X<5\\;\\Rightarrow\\;X<\\dfrac{5}{0{,}3}=16{,}67$$</div>"
       "<div class='res'><b>El actuador se activa para X &lt; 16,67 (Y = 0,3·X &lt; 5).</b></div>"
    },
    {
     "id": "q2b", "titulo": "Opción b · Función de transferencia y estabilidad", "etiqueta": "CONTROL",
     "menu": "2b · FT y estabilidad", "titulo_corto": "2b",
     "meta": "Opción b · 2,5 puntos (a 1 · b 1,5)",
     "enunciado_html": "<p>Para el sistema de la figura:</p><ol type='a'><li>Obtener la función de transferencia del sistema. <span class='pts'>(1 punto)</span></li><li>Determina si el sistema de control es estable averiguando los polos del sistema. <span class='pts'>(1,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": fig_control_2b(),
     "aplica_html": "<p>Con realimentación <b>unitaria negativa</b>, la función de transferencia en lazo cerrado es \\(\\dfrac{C}{R}=\\dfrac{G}{1+G}\\). Los <b>polos</b> son las raíces del denominador; el sistema es estable si todos tienen parte real negativa.</p>",
     "solucion_html":
       "<h5>a) Función de transferencia en lazo cerrado</h5>"
       "<p>Con \\(G(s)=\\dfrac{500}{(s+1)(s+4)}\\) y realimentación unitaria:</p>"
       "<div class='formula'>$$\\dfrac{C}{R}=\\dfrac{G}{1+G}=\\dfrac{500}{(s+1)(s+4)+500}=\\dfrac{500}{s^2+5s+504}$$</div>"
       "<div class='res'><b>C/R = 500 / (s² + 5s + 504)</b></div>"
       "<h5>b) Polos y estabilidad</h5>"
       "<p>La ecuación característica es \\(s^2+5s+504=0\\):</p>"
       "<div class='formula'>$$s=\\dfrac{-5\\pm\\sqrt{25-2016}}{2}=-2{,}5\\pm j\\,22{,}3$$</div>"
       "<p>Ambos polos tienen <b>parte real negativa</b> (−2,5):</p>"
       "<div class='res'><b>El sistema es ESTABLE</b> (polos en el semiplano izquierdo).</div>"
    }
   ]
  },
  {
   "id": "b3", "titulo": "Ejercicio 3 · Termodinámica", "color": "#fb7185",
   "descripcion_tarjeta": "Bomba de calor según Carnot y motor térmico con rendimiento real.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#fb7185' stroke-width='3'><circle cx='45' cy='30' r='16'/><path d='M45 14v-8M45 54v-8M61 30h8M13 30h8'/></svg>",
   "cuestiones": [
    {
     "id": "q3a", "titulo": "Opción a · Bomba de calor (Carnot)", "etiqueta": "TERMODINÁMICA",
     "menu": "3a · Bomba de calor", "titulo_corto": "3a",
     "meta": "Opción a · 2,5 puntos (a 1 · b 1 · c 0,5)",
     "enunciado_html": "<p>Una bomba de calor funciona según el ciclo de Carnot. Extrae calor del exterior, que está a <b>5 ºC</b>, y lo cede al interior de una vivienda que se mantiene a <b>25 ºC</b>. La bomba suministra calor a un ritmo de <b>36 000 kJ/h</b>. Calcula:</p><ol type='a'><li>Rendimiento (COP) de la bomba de calor. <span class='pts'>(1 punto)</span></li><li>Trabajo realizado por la bomba de calor en 1 hora. <span class='pts'>(1 punto)</span></li><li>Potencia del motor de la bomba de calor. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>En una <b>bomba de calor</b>, el COP relaciona el calor cedido al foco caliente con el trabajo: \\(COP=\\dfrac{T_c}{T_c-T_f}\\) (Carnot). El trabajo es \\(W=Q_c/COP\\) y la potencia \\(P=W/t\\). Temperaturas: 25 ºC = 298 K (interior), 5 ºC = 278 K (exterior).</p>",
     "solucion_html":
       "<h5>a) COP de la bomba de calor</h5>"
       "<div class='formula'>$$COP=\\dfrac{T_c}{T_c-T_f}=\\dfrac{298}{298-278}=\\dfrac{298}{20}=14{,}9$$</div>"
       "<div class='res'><b>COP = 14,9</b></div>"
       "<h5>b) Trabajo en 1 hora</h5>"
       "<div class='formula'>$$W=\\dfrac{Q_c}{COP}=\\dfrac{36\\,000}{14{,}9}=2416\\ \\mathrm{kJ}$$</div>"
       "<div class='res'><b>W ≈ 2416 kJ (en 1 h)</b></div>"
       "<h5>c) Potencia del motor</h5>"
       "<div class='formula'>$$P=\\dfrac{W}{t}=\\dfrac{2416\\cdot10^{3}\\ \\mathrm{J}}{3600\\ \\mathrm{s}}=671\\ \\mathrm{W}$$</div>"
       "<div class='res'><b>P ≈ 671 W</b></div>"
    },
    {
     "id": "q3b", "titulo": "Opción b · Motor térmico", "etiqueta": "TERMODINÁMICA",
     "menu": "3b · Motor térmico", "titulo_corto": "3b",
     "meta": "Opción b · 2,5 puntos (a 1 · b 1 · c 0,5)",
     "enunciado_html": "<p>Un motor térmico funciona entre una fuente caliente a <b>600 K</b> y una fuente fría a <b>300 K</b>. Consume <b>2,5 kg/h</b> de combustible con un poder calorífico de <b>40 000 kJ/kg</b>. El motor tiene un rendimiento real del <b>40 %</b> del rendimiento de Carnot. Calcula:</p><ol type='a'><li>El rendimiento de Carnot y el rendimiento real del motor. <span class='pts'>(1 punto)</span></li><li>El calor útil desarrollado. <span class='pts'>(1 punto)</span></li><li>La potencia útil en W. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>El rendimiento de Carnot es \\(\\eta_C=1-\\dfrac{T_f}{T_c}\\). El calor aportado por hora es \\(Q_1=\\dot m\\cdot PC\\). El trabajo (calor útil) es \\(W=\\eta_{real}\\,Q_1\\) y la potencia \\(P=W/t\\).</p>",
     "solucion_html":
       "<h5>a) Rendimientos</h5>"
       "<div class='formula'>$$\\eta_C=1-\\dfrac{T_f}{T_c}=1-\\dfrac{300}{600}=0{,}5$$</div>"
       "<div class='formula'>$$\\eta_{real}=0{,}4\\cdot\\eta_C=0{,}4\\cdot 0{,}5=0{,}2$$</div>"
       "<div class='res'><b>η<sub>Carnot</sub> = 0,5 (50 %) · η<sub>real</sub> = 0,2 (20 %)</b></div>"
       "<h5>b) Calor útil desarrollado</h5>"
       "<p>Calor aportado por el combustible en 1 h: \\(Q_1=2{,}5\\cdot 40\\,000=100\\,000\\ \\mathrm{kJ}\\).</p>"
       "<div class='formula'>$$W=\\eta_{real}\\,Q_1=0{,}2\\cdot 100\\,000=20\\,000\\ \\mathrm{kJ}$$</div>"
       "<div class='res'><b>W = 20 000 kJ (por hora)</b></div>"
       "<h5>c) Potencia útil</h5>"
       "<div class='formula'>$$P=\\dfrac{W}{t}=\\dfrac{20\\,000\\cdot10^{3}\\ \\mathrm{J}}{3600\\ \\mathrm{s}}=5556\\ \\mathrm{W}$$</div>"
       "<div class='res'><b>P ≈ 5556 W ≈ 5,56 kW</b></div>"
    }
   ]
  },
  {
   "id": "b4", "titulo": "Ejercicio 4 · Dureza Brinell (ejes)", "color": "#f59e0b",
   "descripcion_tarjeta": "Control de calidad por dureza Brinell de ejes de transmisión y análisis de la huella.",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><rect x='14' y='30' width='62' height='16' rx='2'/><path d='M45 8 L45 28'/><circle cx='45' cy='39' r='4' fill='#f59e0b' stroke='none'/></svg>",
   "cuestiones": [
    {
     "id": "q4", "titulo": "Ejercicio 4 · Ensayo Brinell de ejes de transmisión", "etiqueta": "MATERIALES",
     "menu": "E4 · Dureza Brinell (ejes)", "titulo_corto": "E4",
     "meta": "Obligatorio · 2,5 puntos (a 1,5 · b 0,5 · c 0,5)",
     "enunciado_html": "<p>Una empresa de Toledo produce ejes de transmisión para maquinaria industrial pesada. En el control de calidad se realiza un <b>ensayo de dureza Brinell</b> con una bola de acero durante <b>45 s</b>. El diámetro de la bola es <b>10 mm</b> y la constante del ensayo es <b>k = 30</b>. Se mide una huella de diámetro medio <b>d = 4 mm</b>. Los ejes son aptos si su dureza está entre <b>200 HB</b> y <b>300 HB</b>. Se pide:</p><ol type='a'><li>Calcula la carga aplicada durante el ensayo y la dureza Brinell del material del eje. <span class='pts'>(1,5 puntos)</span></li><li>Expresa la dureza Brinell de forma normalizada e indica si estos ejes son adecuados. <span class='pts'>(0,5 puntos)</span></li><li>Explica matemáticamente cómo afectaría un aumento del diámetro de la huella al valor de la dureza. <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>La <b>carga</b> se fija con la constante del ensayo: \\(F=k\\,D^2\\). La <b>dureza Brinell</b> es \\(HB=\\dfrac{2F}{\\pi D\\left(D-\\sqrt{D^2-d^2}\\right)}\\), con d el diámetro de la huella.</p>",
     "solucion_html":
       "<h5>a) Carga aplicada y dureza Brinell</h5>"
       "<div class='formula'>$$F=k\\,D^2=30\\cdot 10^2=3000\\ \\mathrm{kp}$$</div>"
       "<div class='formula'>$$HB=\\dfrac{2F}{\\pi D\\left(D-\\sqrt{D^2-d^2}\\right)}=\\dfrac{2\\cdot 3000}{\\pi\\cdot 10\\left(10-\\sqrt{100-16}\\right)}=228{,}8$$</div>"
       "<div class='res'><b>F = 3000 kp · HB ≈ 228,8 kp/mm²</b></div>"
       "<h5>b) Expresión normalizada y aptitud</h5>"
       "<p>Con D = 10 mm, F = 3000 kp y t = 45 s:</p>"
       "<div class='res'><b>229 HB 10 3000 45</b> — como 200 ≤ 229 ≤ 300, <b>los ejes son APTOS</b>.</div>"
       "<h5>c) Efecto de un aumento del diámetro de la huella</h5>"
       "<p>Si <b>d aumenta</b>, el radical \\(\\sqrt{D^2-d^2}\\) <b>disminuye</b>, con lo que el paréntesis \\((D-\\sqrt{D^2-d^2})\\) <b>aumenta</b> y, al estar en el denominador, la dureza <b>HB disminuye</b>.</p>"
       "<div class='res'><b>A mayor huella (mayor d), menor dureza HB: la relación es inversa.</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "clm_2026_modelo_a.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
