#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JSON del examen UCLM 2024 · Extraordinaria (curso 2023/24).

El enunciado oficial (sin plantilla de soluciones) es casi idéntico al de la
convocatoria ordinaria; la única diferencia está en la opción 1b (probeta Charpy
de 8 mm de lado en vez de 10 mm). Se reutilizan las figuras de la ordinaria y se
aportan soluciones propias con la misma metodología que la plantilla oficial.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, txt, line
from cyllib import INK, MUT, ROSE
from build_clm_2024_ordinaria import (
    fig_bloques_q3, fig_beam_voladizo, fig_V_voladizo, fig_M_voladizo,
    fig_beam_apoyada, fig_nor_q4a, fig_gates_q4b, NOTA_ETERCERA,
)


def fig_probeta8():
    """Probeta Charpy 8x8 mm con entalla de 2 mm (sección resistente 8x6 mm)."""
    s = svg_open('420 240', 440)
    fx, fy, W, H = 70, 120, 250, 70
    dx, dy = 55, -40
    s += f"<polygon points='{fx},{fy} {fx+W},{fy} {fx+W},{fy+H} {fx},{fy+H}' fill='#1b2640' stroke='{INK}' stroke-width='2'/>"
    s += f"<polygon points='{fx},{fy} {fx+dx},{fy+dy} {fx+W+dx},{fy+dy} {fx+W},{fy}' fill='#22304d' stroke='{INK}' stroke-width='2'/>"
    s += f"<polygon points='{fx+W},{fy} {fx+W+dx},{fy+dy} {fx+W+dx},{fy+H+dy} {fx+W},{fy+H}' fill='#141d33' stroke='{INK}' stroke-width='2'/>"
    nx = fx + W*0.55
    s += f"<polygon points='{nx-14},{fy} {nx},{fy+18} {nx+14},{fy} {nx+14+dx*0.5},{fy+dy*0.5} {nx-14+dx*0.5},{fy+dy*0.5}' fill='#0d1220' stroke='{ROSE}' stroke-width='1.6'/>"
    s += f"<line x1='{nx-14}' y1='{fy}' x2='{nx}' y2='{fy+18}' stroke='{ROSE}' stroke-width='2'/>"
    s += f"<line x1='{nx+14}' y1='{fy}' x2='{nx}' y2='{fy+18}' stroke='{ROSE}' stroke-width='2'/>"
    s += line(fx-14, fy, fx-14, fy+H, MUT)
    s += txt(fx-20, fy+H/2+4, '8 mm', MUT, 12, 'end')
    s += txt(nx+30, fy-4, '2 mm', ROSE, 12, 'start')
    s += line(nx+18, fy-2, nx, fy+16, ROSE)
    s += line(fx+W+dx+8, fy+dy, fx+W+dx+8, fy+H+dy, MUT)
    s += txt(fx+W+dx+14, fy+H/2+dy, '8 mm', MUT, 12, 'start')
    s += txt(fx+W/2, fy+H+26, 'sección resistente 8 × (8−2) mm', MUT, 12, 'middle')
    return s + "</svg>"


data = {
 "meta": {
  "titulo": "Tecnología e Ingeniería II",
  "subtitulo": "Prueba de Acceso a la Universidad · UCLM (Castilla-La Mancha) · Extraordinaria 2024 (curso 2023/24) · Examen resuelto",
  "cabecera_titulo": "PAU 2024 · <span>Tecnología e Ingeniería II</span> · UCLM · Extraordinaria",
  "pill": "Elige 4 de 5 ejercicios · una opción (a o b) · 90 min",
  "enunciado_pdf": "../../examens/UCLM/TECNOLOGIA 23_24_e.pdf",
  "pdf_dir": "pdf_clm_2024_extraordinaria",
  "footer": "Solucionario PAU · UCLM (Castilla-La Mancha) · Tecnología e Ingeniería II (Extraordinaria 2024)",
  "intro_inicio": "El alumno debe escoger <b>4 de los 5 ejercicios</b> y resolver <b>una</b> de las dos opciones (a o b) de cada uno. Aquí se resuelven <b>todas</b>. <b>Nota:</b> el enunciado de esta convocatoria extraordinaria es casi idéntico al de la ordinaria 2024; la única diferencia es la <b>opción 1b</b> (probeta Charpy de 8 mm de lado). Las soluciones son propias, con la misma metodología que la plantilla oficial de la UCLM.",
  "indice_nombre": "Exámenes de Castilla-La Mancha",
  "indice_url": "index.html"
 },
 "bloques": [
  {
   "id": "b1", "titulo": "Ejercicio 1 · Ensayos de materiales", "color": "#f59e0b",
   "descripcion_tarjeta": "Dureza Brinell del plomo y ensayo de resiliencia Charpy (probeta 8 mm).",
   "svg_tarjeta": "<svg viewBox='0 0 90 60' fill='none' stroke='#f59e0b' stroke-width='3'><rect x='14' y='30' width='62' height='18' rx='2'/><path d='M45 8 L45 28'/><circle cx='45' cy='39' r='4' fill='#f59e0b' stroke='none'/></svg>",
   "cuestiones": [
    {
     "id": "q1a", "titulo": "Opción a · Dureza Brinell (plomo)", "etiqueta": "MATERIALES",
     "menu": "1a · Dureza Brinell", "titulo_corto": "1a",
     "meta": "Opción a · 2,5 puntos (a 1 · b 1 · c 0,5)",
     "enunciado_html": "<p>Se tiene una pieza de plomo con una dureza de Brinell <b>23 HB 5 100 15</b>:</p><ol type='a'><li>¿Cuál es la profundidad de la huella que dejó el ensayo? <span class='pts'>(1 punto)</span></li><li>Se quiere realizar un nuevo ensayo con la misma pieza durante <b>20 s</b> que deje una profundidad de huella <b>0,5 mm</b>. ¿Cuánto debería valer la carga que hay que aplicar? <span class='pts'>(1 punto)</span></li><li>¿Cuál sería la expresión de dureza normalizada a partir del nuevo ensayo? <span class='pts'>(0,5 puntos)</span></li></ol>",
     "aplica_html": "<p>La designación <b>HB D F t</b>: dureza, diámetro de bola (mm), carga (kp) y tiempo (s). Aquí <b>23 HB 5 100 15</b> ⇒ HB = 23 kp/mm², D = 5 mm, F = 100 kp, t = 15 s. Con la superficie del casquete \\(S=\\pi D f\\), la dureza es \\(HB=\\dfrac{F}{\\pi D f}\\).</p>",
     "solucion_html":
       "<h5>a) Profundidad de la huella</h5>"
       "<div class='formula'>$$HB=\\dfrac{F}{\\pi D f}\\;\\Rightarrow\\; f=\\dfrac{F}{\\pi D\\,HB}=\\dfrac{100}{\\pi\\cdot 5\\cdot 23}$$</div>"
       "<div class='res'><b>f = 0,28 mm</b></div>"
       "<h5>b) Carga para f = 0,5 mm</h5>"
       "<div class='formula'>$$F=HB\\cdot\\pi D f=23\\cdot\\pi\\cdot 5\\cdot 0{,}5$$</div>"
       "<div class='res'><b>F = 180,64 kp</b></div>"
       "<h5>c) Expresión normalizada del nuevo ensayo</h5>"
       "<div class='res'><b>23 HB 5 181 20</b></div>"
    },
    {
     "id": "q1b", "titulo": "Opción b · Resiliencia (ensayo Charpy)", "etiqueta": "MATERIALES",
     "menu": "1b · Resiliencia (Charpy)", "titulo_corto": "1b",
     "meta": "Opción b · 2,5 puntos (a 1,25 · b 1,25)",
     "enunciado_html": "<p>Se quiere medir la resiliencia de un material bajo un ensayo de <b>Charpy</b>. Para ello se usa una probeta de área resistente de <b>8 mm de lado</b> sobre la que se lanza un péndulo de <b>20 kg</b> de masa desde una altura de <b>1 m</b>. Tras el impacto el péndulo alcanza una altura de <b>300 mm</b>. Calcule:</p><ol type='a'><li>La energía que se ha empleado en partir la probeta expresada en J. <span class='pts'>(1,25 puntos)</span></li><li>La resiliencia del material expresada en J/cm². <span class='pts'>(1,25 puntos)</span></li></ol>",
     "figura_enunciado_svg": fig_probeta8(),
     "aplica_html": "<p>El <b>péndulo de Charpy</b> mide la energía absorbida como la diferencia de energía potencial \\(E=m\\,g\\,(h_0-h_1)\\). La <b>resiliencia</b> es esa energía por unidad de sección resistente bajo la entalla \\(\\rho=E/S\\). La probeta es de 8×8 mm con una entalla de 2 mm, luego la sección resistente es 8×(8−2) mm.</p>",
     "solucion_html":
       "<h5>a) Energía absorbida en la rotura</h5>"
       "<div class='formula'>$$E=m\\,g\\,(h_0-h_1)=20\\cdot 9{,}8\\cdot(1-0{,}3)$$</div>"
       "<div class='res'><b>E = 137,2 J</b> (con g = 9,8 m/s²)</div>"
       "<h5>b) Resiliencia del material</h5>"
       "<div class='formula'>$$S=8\\cdot(8-2)=48\\ \\mathrm{mm^2}=0{,}48\\ \\mathrm{cm^2}$$</div>"
       "<div class='formula'>$$\\rho=\\dfrac{E}{S}=\\dfrac{137{,}2\\ \\mathrm{J}}{0{,}48\\ \\mathrm{cm^2}}$$</div>"
       "<div class='res'><b>ρ ≈ 285,8 J/cm²</b></div>"
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
     "aplica_html": "<p>Rendimiento de Carnot \\(\\eta_{ideal}=\\dfrac{T_1-T_2}{T_1}\\). El trabajo y el calor cedido salen del balance \\(W=Q_1-Q_2\\) con \\(W=\\eta Q_1\\). Temperaturas: 230 ºC = 503 K, 10 ºC = 283 K.</p>",
     "solucion_html":
       "<h5>a) Rendimiento real</h5>"
       "<div class='formula'>$$\\eta_{ideal}=\\dfrac{503-283}{503}=0{,}44$$</div>"
       "<div class='formula'>$$\\eta_{real}=\\eta_{ideal}\\cdot 0{,}3=0{,}44\\cdot 0{,}3=0{,}132$$</div>"
       "<div class='res'><b>η<sub>real</sub> = 0,132</b></div>"
       + NOTA_ETERCERA +
       "<h5>b) Calor cedido y trabajo</h5>"
       "<div class='formula'>$$Q_2=(1-\\eta_{real})\\,Q_1=(1-0{,}132)\\cdot 2500=2170\\ \\mathrm{J}=520{,}8\\ \\mathrm{cal}$$</div>"
       "<div class='formula'>$$W=Q_1-Q_2=2500-2170=330\\ \\mathrm{J}$$</div>"
       "<div class='res'><b>Q<sub>2</sub> = 2170 J (≈ 520,8 cal) · W = 330 J</b></div>"
       "<h5>c) Temperatura para η<sub>Carnot</sub> = 58 %</h5>"
       "<div class='formula'>$$T_1=\\dfrac{T_2}{1-\\eta_{Carnot}}=\\dfrac{283}{1-0{,}58}$$</div>"
       "<div class='res'><b>T<sub>1</sub> = 673,8 K</b></div>"
    },
    {
     "id": "q2b", "titulo": "Opción b · Cajón congelador", "etiqueta": "TERMODINÁMICA",
     "menu": "2b · Cajón congelador", "titulo_corto": "2b",
     "meta": "Opción b · 2,5 puntos (a 1 · b 1,5)",
     "enunciado_html": "<p>Un cajón congelador que consume <b>250 W</b> mantiene una temperatura interior de <b>−8 ºC</b> mientras que en el exterior hay una temperatura de <b>21 ºC</b>. Calcula:</p><ol type='a'><li>La eficiencia del cajón congelador si su funcionamiento es según un ciclo de Carnot. <span class='pts'>(1 punto)</span></li><li>El calor cedido y el absorbido por el congelador en <b>24 h</b> sabiendo que la eficiencia real del cajón es la mitad de la de Carnot. <span class='pts'>(1,5 puntos)</span></li></ol>",
     "aplica_html": "<p>Máquina frigorífica: COP de Carnot \\(\\varepsilon=\\dfrac{T_2}{T_1-T_2}\\). Trabajo \\(W=P\\,t\\); calor absorbido \\(Q_2=\\varepsilon W\\); cedido \\(Q_1=W+Q_2\\). Temperaturas: 21 ºC = 294 K, −8 ºC = 265 K.</p>",
     "solucion_html":
       "<h5>a) Eficiencia ideal (COP de Carnot)</h5>"
       "<div class='formula'>$$\\varepsilon_{ideal}=\\dfrac{T_2}{T_1-T_2}=\\dfrac{265}{294-265}=9{,}14$$</div>"
       "<div class='res'><b>ε<sub>ideal</sub> = 9,14</b></div>"
       "<h5>b) Calor cedido y absorbido en 24 h</h5>"
       "<div class='formula'>$$\\varepsilon_{real}=\\dfrac{9{,}14}{2}=4{,}57$$</div>"
       "<div class='formula'>$$W=P\\,t=250\\cdot 24\\cdot 3600=21\\,600\\ \\mathrm{kJ}$$</div>"
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
     "meta": "Opción a · 2,5 puntos",
     "enunciado_html": "<p>Obtenga la <b>Función de Transferencia</b> del diagrama de bloques de la figura.</p>",
     "figura_enunciado_svg": fig_bloques_q3(),
     "aplica_html": "<p>P<sub>1</sub> y P<sub>2</sub> están en <b>paralelo</b> (misma entrada, salidas que se suman) ⇒ \\(P_1+P_2\\); ese bloque directo está realimentado por P<sub>3</sub> en <b>lazo negativo</b> \\(\\dfrac{G}{1+GH}\\).</p>",
     "solucion_html":
       "<h5>Paso 1 · Ramas en paralelo</h5>"
       "<div class='formula'>$$M_1=P_1+P_2$$</div>"
       "<h5>Paso 2 · Cierre del lazo con P<sub>3</sub></h5>"
       "<div class='formula'>$$M=\\dfrac{Y}{X}=\\dfrac{P_1+P_2}{1+(P_1+P_2)P_3}=\\dfrac{P_1+P_2}{1+P_1P_3+P_2P_3}$$</div>"
       "<div class='res'><b>M = (P₁ + P₂) / (1 + P₁P₃ + P₂P₃)</b></div>"
    },
    {
     "id": "q3b", "titulo": "Opción b · Estabilidad (polos)", "etiqueta": "CONTROL",
     "menu": "3b · Estabilidad y polos", "titulo_corto": "3b",
     "meta": "Opción b · 2,5 puntos",
     "enunciado_html": "<p>Un sistema de control está representado con la siguiente función de transferencia:</p><div class='formula'>$$F(s)=\\dfrac{1}{s+k}$$</div><p>Donde <b>k</b> puede tomar cualquier valor. Analizando los polos, determina para qué valores de <b>k</b> el sistema es estable. Razone la respuesta.</p>",
     "aplica_html": "<p>Los <b>polos</b> son las raíces del denominador. El sistema es <b>estable</b> si todos los polos tienen <b>parte real negativa</b> (semiplano izquierdo).</p>",
     "solucion_html":
       "<h5>Polo del sistema</h5>"
       "<div class='formula'>$$s+k=0\\;\\Rightarrow\\; p=-k$$</div>"
       "<h5>Condición de estabilidad</h5>"
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
     "aplica_html": "<p>Se evalúa \\(S=(A+B)(\\bar A+C)\\) para las 8 combinaciones. Para implementarla solo con <b>NOR</b> se usa la doble negación y De Morgan (\\(\\overline{A\\cdot B}=\\bar A+\\bar B\\); una NOR con las entradas unidas es un inversor).</p>",
     "solucion_html":
       "<h5>a) Tabla de verdad</h5>"
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
       "<div class='formula'>$$S=(A+B)(\\bar A+C)=\\mathrm{NOR}\\!\\big(\\mathrm{NOR}(A,B),\\ \\mathrm{NOR}(\\bar A,C)\\big),\\quad \\bar A=\\mathrm{NOR}(A,A)$$</div>"
       "<figure class='fig'>" + fig_nor_q4a() + "<figcaption>S = (A+B)·(Ā+C) implementada con 4 puertas NOR.</figcaption></figure>"
       "<div class='res'><b>S = NOR( NOR(A,B) , NOR( NOR(A,A) , C ) )</b></div>"
    },
    {
     "id": "q4b", "titulo": "Opción b · Diseño lógico (Karnaugh)", "etiqueta": "DIGITAL",
     "menu": "4b · Diseño y Karnaugh", "titulo_corto": "4b",
     "meta": "Opción b · 2,5 puntos (a 1 · b 0,75 · c 0,75)",
     "enunciado_html": "<p>Diseña un circuito con puertas lógicas formado por cuatro sensores (<b>A, B, C y D</b>) y una salida (<b>S</b>):</p><ol><li>Siempre que <b>A y B</b> están desactivados a la vez, la salida también lo está.</li><li>Si <b>A y D</b> están activados, pero <b>B</b> no, la salida estará activada.</li><li>Si <b>B</b> está activado la salida también lo estará, siempre y cuando no coincidan activados <b>C y D</b>.</li></ol><p>Obtener:</p><ol type='a'><li>La tabla de verdad. <span class='pts'>(1 punto)</span></li><li>El mapa de Karnaugh y función reducida. <span class='pts'>(0,75 puntos)</span></li><li>El diagrama con puertas lógicas. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "aplica_html": "<p>Se traduce cada condición a la <b>tabla de verdad</b> de 16 filas (A,B,C,D), los unos se llevan al <b>mapa de Karnaugh</b> 4×4 (columnas AB, filas CD en Gray) y se agrupan en potencias de 2.</p>",
     "solucion_html":
       "<h5>a) Tabla de verdad</h5>"
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
     "enunciado_html": "<p>Se tiene la viga en voladizo de la figura con una carga puntual <b>F = 10 kN</b> (d₁ = 5 m, d₂ = 1 m). Se pide:</p><ol type='a'><li>Calcular las reacciones en el empotramiento. <span class='pts'>(1 punto)</span></li><li>Calcular y representar los diagramas del momento flector y esfuerzo cortante. <span class='pts'>(1,5 puntos)</span></li></ol>",
     "figura_enunciado_svg": fig_beam_voladizo(),
     "aplica_html": "<p>El empotramiento tiene reacción horizontal, vertical y un <b>momento</b>. Con \\(\\sum F=0\\) y \\(\\sum M=0\\) se obtienen; luego se estudian los tramos para dibujar V y M.</p>",
     "solucion_html":
       "<h5>a) Reacciones en el empotramiento</h5>"
       "<div class='formula'>$$\\sum F_y=F_{Ay}-F=0\\;\\Rightarrow\\; F_{Ay}=10\\ \\mathrm{kN}$$</div>"
       "<div class='formula'>$$\\sum M_A=-M_A+F\\,d_1=0\\;\\Rightarrow\\; M_A=10\\cdot 5=50\\ \\mathrm{kN\\,m}$$</div>"
       "<div class='res'><b>F<sub>Ay</sub> = 10 kN · M<sub>A</sub> = 50 kN·m</b></div>"
       "<h5>b) Diagramas de cortante y flector</h5>"
       "<p><b>Tramo 1</b> (0 ≤ x ≤ 5): \\(V_1=10\\ \\mathrm{kN}\\); \\(M_1=10x-50\\) (−50 en x=0, 0 en x=5). <b>Tramo 2</b>: \\(V_2=0\\); \\(M_2=0\\).</p>"
       "<figure class='fig'>" + fig_V_voladizo() + "<figcaption>Cortante: 10 kN hasta la carga, 0 después.</figcaption></figure>"
       "<figure class='fig'>" + fig_M_voladizo() + "<figcaption>Flector: recta de −50 kN·m en el empotramiento a 0 bajo la carga.</figcaption></figure>"
       "<div class='res'><b>V = 10 kN (tramo 1), 0 (tramo 2) · M<sub>máx</sub> = −50 kN·m</b></div>"
    },
    {
     "id": "q5b", "titulo": "Opción b · Viga simplemente apoyada", "etiqueta": "ESTRUCTURAS",
     "menu": "5b · Viga apoyada · esfuerzos", "titulo_corto": "5b",
     "meta": "Opción b · 2,5 puntos (a 1 · b 0,75 · c 0,75)",
     "enunciado_html": "<p>Se tiene la viga simplemente apoyada de la figura con las cargas puntuales <b>F₁ = 10 kN</b> y <b>F₂ = 10 kN</b> (d₁ = 2 m, d₂ = 4 m, d₃ = 2 m). Se pide:</p><ol type='a'><li>Calcular las reacciones en los apoyos. <span class='pts'>(1 punto)</span></li><li>Enumere los tipos de esfuerzos a los que puede estar sometida una estructura. <span class='pts'>(0,75 puntos)</span></li><li>De los tipos de esfuerzo, nombre y defina los que se dan en la viga de la imagen. <span class='pts'>(0,75 puntos)</span></li></ol>",
     "figura_enunciado_svg": fig_beam_apoyada(),
     "aplica_html": "<p>Dos apoyos ⇒ dos reacciones verticales. Se calculan con \\(\\sum M=0\\) en un apoyo y \\(\\sum F_y=0\\). Por simetría ambas valen lo mismo.</p>",
     "solucion_html":
       "<h5>a) Reacciones en los apoyos</h5>"
       "<div class='formula'>$$F_{By}=\\dfrac{F_1 d_1+F_2(d_1+d_2)}{d_1+d_2+d_3}=\\dfrac{10\\cdot 2+10\\cdot 6}{8}=10\\ \\mathrm{kN}$$</div>"
       "<div class='formula'>$$F_{Ay}=F_1+F_2-F_{By}=10+10-10=10\\ \\mathrm{kN}$$</div>"
       "<div class='res'><b>F<sub>Ay</sub> = 10 kN · F<sub>By</sub> = 10 kN</b></div>"
       "<h5>b) Tipos de esfuerzos</h5>"
       "<ul><li><b>Tracción</b></li><li><b>Compresión</b></li><li><b>Flexión</b></li><li><b>Torsión</b></li><li><b>Cortante</b> (cizalladura)</li></ul>"
       "<h5>c) Esfuerzo que sufre la viga</h5>"
       "<p><b>Flexión:</b> esfuerzo que aparece cuando una carga tiende a doblar la estructura, provocando <b>compresión</b> en un lado y <b>tracción</b> en el opuesto de la sección.</p>"
       "<div class='res'><b>La viga trabaja a flexión (con cortante asociado en los apoyos).</b></div>"
    }
   ]
  }
 ]
}

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "clm_2024_extraordinaria.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("JSON escrito:", out)
