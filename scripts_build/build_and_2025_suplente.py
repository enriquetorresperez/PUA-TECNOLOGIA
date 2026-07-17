#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Andalucía 2025 (suplente2-a) para pau-dashboard."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt

def g_and(x,y,w,h,color='#22d3ee'):
    return f"<path d='M{x},{y} L{x+w-h/2},{y} A{h/2},{h/2} 0 0 1 {x+w-h/2},{y+h} L{x},{y+h} Z' stroke='{color}'/>"
def g_or(x,y,w,h,color='#34d399'):
    return f"<path d='M{x},{y} Q{x+w*0.55},{y} {x+w},{y+h/2} Q{x+w*0.55},{y+h} {x},{y+h} Q{x+w*0.32},{y+h/2} {x},{y} Z' stroke='{color}'/>"
def bubble(cx,cy,color='#e2e8f0'):
    return f"<circle cx='{cx}' cy='{cy}' r='4' stroke='{color}'/>"
def g_not(x,y,w,h,color='#a78bfa'):
    return f"<path d='M{x},{y} L{x},{y+h} L{x+w},{y+h/2} Z' stroke='{color}'/>"

# --- Fig Ej3B b) lazo de control E->G1->sum->G2->C, H1 realim ---
def fig_lazo_h():
    s=svg_open('480 200',480)
    y=70
    s+=arrow(20,y,60,y); s+=txt(14,y-8,'E','#e2e8f0',15)
    s+=box(60,y-18,58,36,'G₁','#22d3ee'); s+=arrow(118,y,150,y)
    s+=summer(168,y); s+=txt(156,y-6,'+','#4ade80',12); s+=txt(156,y+18,'−','#f87171',13)
    s+=arrow(183,y,230,y)
    s+=box(230,y-18,58,36,'G₂','#22d3ee'); s+=arrow(288,y,400,y); s+=txt(406,y-6,'C','#e2e8f0',15)
    fx=350
    s+=f"<circle cx='{fx}' cy='{y}' r='3' fill='#cbd5e1'/>"
    s+=line(fx,y,fx,150); s+=line(fx,150,230,150)
    s+=box(178,132,58,36,'H₁','#34d399'); s+=line(178,150,168,150); s+=arrow(168,150,168,y+15)
    return s+"</svg>"

# --- Fig Ej3A a.2: circuito F = BD + ACD' ---
def fig_impl_ej3a():
    s=svg_open('460 240',460)
    for lab,yy in [('A',40),('C',80),('D',140),('B',200)]:
        s+=txt(24,yy+4,lab,'#e2e8f0',15,'middle')
    # D' (NOT de D)
    s+=line(38,140,110,140); s+=g_not(110,127,26,26,'#a78bfa'); s+=bubble(140,140,'#a78bfa'); s+=txt(150,135,"D'",'#a78bfa',12)
    # AND(A,C,D')
    s+=line(38,40,250,40); s+=line(38,80,250,80); s+=line(144,140,250,140)
    s+=g_and(250,26,50,128,'#f59e0b'); s+=line(300,90,360,90); s+=txt(258,96,'ACD′','#94a3b8',10)
    # AND(B,D): necesita B y D
    s+=f"<circle cx='90' cy='140' r='3' fill='#cbd5e1'/>"; s+=line(90,140,90,175); s+=line(90,175,250,175)
    s+=line(38,200,250,200)
    s+=g_and(250,168,50,44,'#22d3ee'); s+=line(300,190,360,190); s+=txt(258,194,'BD','#94a3b8',10)
    # OR final
    s+=g_or(360,60,52,90,'#4ade80')
    s+=line(300,90,360,90); s+=line(300,190,360,135)
    s+=arrow(412,105,450,105); s+=txt(456,110,'F','#4ade80',15)
    return s+"</svg>"

# --- Fig Ej3B a.2: F = NAND(NAND(M,L), NAND(S,S)) ---
def fig_nand_luces():
    s=svg_open('440 220',440)
    for lab,yy in [('M',50),('L',100),('S',170)]:
        s+=txt(24,yy+4,lab,'#e2e8f0',15,'middle')
    # NAND(M,L)
    s+=line(38,50,150,50); s+=line(38,100,150,85)
    s+=g_and(150,36,50,60,'#f59e0b'); s+=bubble(204,66); s+=line(208,66,300,66); s+=txt(150,30,'(ML)′','#94a3b8',10)
    # NAND(S,S) = NOT S
    s+=line(38,170,150,158); s+=line(38,170,80,170); s+=f"<circle cx='80' cy='170' r='3' fill='#cbd5e1'/>"; s+=line(80,170,80,190); s+=line(80,190,150,190)
    s+=g_and(150,150,50,50,'#a78bfa'); s+=bubble(204,175); s+=line(208,175,300,175); s+=txt(150,146,'S′','#94a3b8',10)
    # NAND final
    s+=g_and(300,80,52,80,'#4ade80'); s+=bubble(356,120)
    s+=line(300,66,300,66); s+=line(300,175,300,175)
    s+=arrow(360,120,410,120); s+=txt(416,125,'F','#4ade80',16)
    return s+"</svg>"

tj_mat="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#f59e0b' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='M30 60L44 20l14 40M35 48h18'/><path d='M66 60V20h8a8 8 0 0 1 0 16h-8'/></svg>"
tj_ter="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#22d3ee' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><rect x='22' y='22' width='38' height='34' rx='4'/><path d='M60 32h16M60 46h16M31 62v6M45 62v6'/></svg>"
tj_log="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#34d399' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='M22 26h20a16 16 0 0 1 0 28H22z'/><circle cx='64' cy='40' r='4'/><path d='M68 40h12'/></svg>"
tj_proj="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#a78bfa' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><circle cx='40' cy='40' r='20'/><path d='M40 28v12l8 6M66 20l10-6M66 60l10 6'/></svg>"

data={"meta":{
  "titulo":"Tecnología e Ingeniería II",
  "subtitulo":"Andalucía, Ceuta, Melilla y centros en Marruecos · Curso 2024-2025 · Examen resuelto y comentado",
  "cabecera_titulo":"PEvAU 2025 · <span>Tecnología e Ingeniería II</span> · Andalucía · Suplente (A)",
  "pill":"90 min · 10 puntos",
  "enunciado_pdf":"../../examens/Andalucia/Tecnologia_Andalucia_2025_ordinaria_suplente2-a.pdf",
  "pdf_dir":"pdf_and_2025_suplente",
  "footer":"Dpto. Tecnología · Solucionario PEvAU 2025 · Andalucía · Tecnología e Ingeniería II (Suplente A)",
  "intro_inicio":"Selecciona un ejercicio o cuestión en la barra lateral. En los <b>ejercicios 1, 2 y 3</b> se responde <b>solo una</b> opción (A o B) y el <b>ejercicio 4</b> es de opción única. Aquí se resuelven <b>todas</b> para repasar."},
 "bloques":[]}

# ---- Ejercicio 1
data["bloques"].append({"id":"b1","titulo":"Ejercicio 1 · Materiales","color":"#f59e0b",
 "descripcion_tarjeta":"Ensayo Charpy (energía y resiliencia) y durezas Vickers/Brinell.",
 "svg_tarjeta":tj_mat,"cuestiones":[
  {"id":"q1","titulo":"Ejercicio 1 · Opción A · Ensayo Charpy","titulo_corto":"E1·A Charpy",
   "etiqueta":"EJERCICIO 1 · OPCIÓN A","meta":"Materiales · 2,5 puntos (a:0,75 · b:0,75 · c:1)","menu":"E1·A · Ensayo Charpy",
   "enunciado_html":("<p>Se realiza un ensayo Charpy a una probeta de acero de <b>sección cuadrada de 10 mm</b> de lado con un péndulo de <b>20 kg</b>. Parte de una altura inicial de <b>1,2 m</b> y tras el impacto alcanza una altura final de <b>30 cm</b>. Se pide:</p>"
     "<ol type='a'><li>La energía absorbida por la probeta. <span class='pts'>(0,75 puntos)</span></li>"
     "<li>La resiliencia del material. <span class='pts'>(0,75 puntos)</span></li>"
     "<li>Con un péndulo de <b>18 kg</b>, ¿desde qué altura debería caer para alcanzar la misma altura final tras romper la probeta? <span class='pts'>(1 punto)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Energía absorbida = energía potencial perdida: \\(E=mg(h_0-h_f)\\).</li>"
     "<li>Resiliencia \\(\\rho=E/S\\), con \\(S\\) la sección de la probeta.</li>"
     "<li>La energía absorbida por la probeta es la misma (mismo material y rotura); se despeja la nueva altura para otra masa.</li></ul>"),
   "solucion_html":("<h5>a) Energía absorbida</h5>"
     "<div class='formula'>$$E=mg(h_0-h_f)=20\\times9{,}81\\times(1{,}2-0{,}30)=176{,}6\\ \\mathrm J$$</div>"
     "<div class='res'><b>Resultado:</b> \\(E\\approx 176{,}6\\ \\mathrm J\\).</div>"
     "<h5>b) Resiliencia</h5>"
     "<p>Sección de la probeta \\(S=10\\times10=100\\ \\mathrm{mm^2}=1\\ \\mathrm{cm^2}\\):</p>"
     "<div class='formula'>$$\\rho=\\frac{E}{S}=\\frac{176{,}6}{1}=176{,}6\\ \\mathrm{J/cm^2}\\;(=1{,}77\\ \\mathrm{J/mm^2})$$</div>"
     "<div class='res'><b>Resultado:</b> \\(\\rho\\approx 176{,}6\\ \\mathrm{J/cm^2}\\).</div>"
     "<h5>c) Altura con péndulo de 18 kg</h5>"
     "<p>La energía absorbida es la misma (176,6 J) y la altura final 0,30 m:</p>"
     "<div class='formula'>$$176{,}6=18\\times9{,}81\\,(h_0'-0{,}30)=176{,}6\\,(h_0'-0{,}30)\\Rightarrow h_0'-0{,}30=1{,}0$$</div>"
     "<div class='res'><b>Resultado:</b> el péndulo debe caer desde \\(h_0'=1{,}30\\ \\mathrm m\\).</div>")
  },
  {"id":"q2","titulo":"Ejercicio 1 · Opción B · Durezas Vickers y Brinell","titulo_corto":"E1·B Durezas",
   "etiqueta":"EJERCICIO 1 · OPCIÓN B","meta":"Materiales · 2,5 puntos (a:1,25 · b:1,25)","menu":"E1·B · Vickers y Brinell",
   "enunciado_html":("<p>Dos planchas de acero con durezas normalizadas: la primera <b>700 HV 25</b> y la segunda <b>120 HB 5 250 30</b>. Se pide:</p>"
     "<ol type='a'><li>La diagonal de la huella del ensayo Vickers de la primera plancha. <span class='pts'>(1,25 puntos)</span></li>"
     "<li>La profundidad de la huella del ensayo Brinell de la segunda plancha. <span class='pts'>(1,25 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Vickers: \\(HV=1{,}8544\\,\\dfrac{F}{d^2}\\Rightarrow d=\\sqrt{\\dfrac{1{,}8544\\,F}{HV}}\\).</li>"
     "<li>Brinell (profundidad del casquete): \\(HB=\\dfrac{F}{\\pi D h}\\Rightarrow h=\\dfrac{F}{\\pi D\\,HB}\\).</li></ul>"),
   "solucion_html":("<h5>a) Diagonal de la huella Vickers</h5>"
     "<p>Primera plancha: \\(HV=700\\), \\(F=25\\ \\mathrm{kp}\\):</p>"
     "<div class='formula'>$$d=\\sqrt{\\frac{1{,}8544\\times25}{700}}=\\sqrt{0{,}0662}=0{,}257\\ \\mathrm{mm}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(d\\approx 0{,}257\\ \\mathrm{mm}\\).</div>"
     "<h5>b) Profundidad de la huella Brinell</h5>"
     "<p>Segunda plancha: \\(HB=120\\), \\(D=5\\ \\mathrm{mm}\\), \\(F=250\\ \\mathrm{kp}\\):</p>"
     "<div class='formula'>$$h=\\frac{F}{\\pi D\\,HB}=\\frac{250}{\\pi\\cdot5\\cdot120}=0{,}133\\ \\mathrm{mm}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(h\\approx 0{,}133\\ \\mathrm{mm}\\).</div>")
  }
 ]})

# ---- Ejercicio 2
data["bloques"].append({"id":"b2","titulo":"Ejercicio 2 · Máquinas térmicas","color":"#22d3ee",
 "descripcion_tarjeta":"Climatización (bomba de calor / frigorífica) y prestaciones de un motor de combustión.",
 "svg_tarjeta":tj_ter,"cuestiones":[
  {"id":"q3","titulo":"Ejercicio 2 · Opción A · Climatización de un local","titulo_corto":"E2·A Climatización",
   "etiqueta":"EJERCICIO 2 · OPCIÓN A","meta":"Máquinas térmicas · 2,5 puntos (a:1 · b:1,5)","menu":"E2·A · Climatización",
   "enunciado_html":("<p>Un acondicionador mantiene un local a <b>25 °C</b> todo el año. La temperatura exterior media es <b>10 °C</b> en invierno y <b>35 °C</b> en verano. La eficiencia es el <b>35 %</b> de la ideal y la potencia del compresor es <b>4 kW</b>. Calcular:</p>"
     "<ol type='a'><li>La eficiencia de la máquina en invierno y en verano. <span class='pts'>(1 punto)</span></li>"
     "<li>El calor extraído del local cada día en verano y el cedido en invierno, con 5 h de funcionamiento diario. <span class='pts'>(1,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Invierno (bomba de calor): \\(COP_{ideal}=\\dfrac{T_{int}}{T_{int}-T_{ext}}\\).</li>"
     "<li>Verano (frigorífica): \\(EER_{ideal}=\\dfrac{T_{int}}{T_{ext}-T_{int}}\\). En ambos casos, eficiencia real = 0,35 · ideal.</li>"
     "<li>Trabajo diario \\(W=P\\cdot t\\); calor \\(Q=\\text{eficiencia}\\cdot W\\). Temperaturas en kelvin.</li></ul>"),
   "solucion_html":("<h5>a) Eficiencias</h5>"
     "<p>\\(T_{int}=298\\ \\mathrm K\\), \\(T_{inv}=283\\ \\mathrm K\\), \\(T_{ver}=308\\ \\mathrm K\\).</p>"
     "<div class='formula'>$$COP_{inv}=0{,}35\\cdot\\frac{298}{298-283}=0{,}35\\cdot19{,}87=6{,}95$$</div>"
     "<div class='formula'>$$EER_{ver}=0{,}35\\cdot\\frac{298}{308-298}=0{,}35\\cdot29{,}8=10{,}43$$</div>"
     "<div class='res'><b>Resultado:</b> eficiencia \\(\\approx 6{,}95\\) en invierno y \\(\\approx 10{,}43\\) en verano.</div>"
     "<h5>b) Calor diario</h5>"
     "<p>Trabajo diario \\(W=P\\,t=4\\ \\mathrm{kW}\\times5\\ \\mathrm h=20\\ \\mathrm{kWh}\\).</p>"
     "<div class='formula'>$$Q_{ver}=EER_{ver}\\cdot W=10{,}43\\times20=208{,}6\\ \\mathrm{kWh/día}$$</div>"
     "<div class='formula'>$$Q_{inv}=COP_{inv}\\cdot W=6{,}95\\times20=139{,}0\\ \\mathrm{kWh/día}$$</div>"
     "<div class='res'><b>Resultado:</b> se extraen \\(\\approx 208{,}6\\ \\mathrm{kWh/día}\\) en verano y se ceden \\(\\approx 139{,}0\\ \\mathrm{kWh/día}\\) en invierno.</div>")
  },
  {"id":"q4","titulo":"Ejercicio 2 · Opción B · Prototipo de motor de combustión","titulo_corto":"E2·B Motor",
   "etiqueta":"EJERCICIO 2 · OPCIÓN B","meta":"Máquinas térmicas · 2,5 puntos (a:1,5 · b:1)","menu":"E2·B · Motor de combustión",
   "enunciado_html":("<p>En un banco de pruebas de un motor se mide: consumo <b>9,5 l/h</b>, par <b>110 N·m</b>, régimen <b>2750 rpm</b>, densidad <b>0,8 kg/dm³</b> y poder calorífico <b>41 700 kJ/kg</b>. Calcular:</p>"
     "<ol type='a'><li>La potencia suministrada y el consumo específico en g/(kW·h). <span class='pts'>(1,5 puntos)</span></li>"
     "<li>El rendimiento del motor. <span class='pts'>(1 punto)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Potencia efectiva: \\(P=M\\,\\omega\\), con \\(\\omega=\\dfrac{2\\pi n}{60}\\).</li>"
     "<li>Consumo específico: \\(C_e=\\dfrac{\\dot m}{P}\\) (masa de combustible por energía útil).</li>"
     "<li>Rendimiento: \\(\\eta=\\dfrac{P}{\\dot m\\,PCI}\\).</li></ul>"),
   "solucion_html":("<h5>a) Potencia y consumo específico</h5>"
     "<div class='formula'>$$\\omega=\\frac{2\\pi\\cdot2750}{60}=287{,}98\\ \\mathrm{rad/s}\\qquad P=M\\,\\omega=110\\times287{,}98=31{,}68\\ \\mathrm{kW}$$</div>"
     "<p>Consumo másico \\(\\dot m=9{,}5\\times0{,}8=7{,}6\\ \\mathrm{kg/h}=7600\\ \\mathrm{g/h}\\):</p>"
     "<div class='formula'>$$C_e=\\frac{\\dot m}{P}=\\frac{7600}{31{,}68}=239{,}9\\ \\mathrm{g/(kW\\,h)}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(P\\approx 31{,}7\\ \\mathrm{kW}\\) y \\(C_e\\approx 240\\ \\mathrm{g/(kW\\,h)}\\).</div>"
     "<h5>b) Rendimiento</h5>"
     "<div class='formula'>$$\\dot Q=\\dot m\\,PCI=\\frac{7{,}6\\times41700}{3600}=88{,}0\\ \\mathrm{kW}\\qquad \\eta=\\frac{P}{\\dot Q}=\\frac{31{,}68}{88{,}0}=0{,}36$$</div>"
     "<div class='res'><b>Resultado:</b> el rendimiento del motor es \\(\\eta\\approx 36\\,\\%\\).</div>")
  }
 ]})

# ---- Ejercicio 3
data["bloques"].append({"id":"b3","titulo":"Ejercicio 3 · Electrónica digital y control","color":"#34d399",
 "descripcion_tarjeta":"Simplificación con indiferentes, diseño con NAND y función de transferencia.",
 "svg_tarjeta":tj_log,"cuestiones":[
  {"id":"q5","titulo":"Ejercicio 3 · Opción A · Función con indiferentes y perturbaciones","titulo_corto":"E3·A Karnaugh",
   "etiqueta":"EJERCICIO 3 · OPCIÓN A","meta":"Digital y control · 2,5 puntos (a:1,5 · b:1)","menu":"E3·A · Función + perturbaciones",
   "enunciado_html":("<p><b>a)</b> Dada la tabla de verdad (X = estado indiferente):</p>"
     "<table class='dat'><tr><th>#</th><th>A</th><th>B</th><th>C</th><th>D</th><th>F</th></tr>"
     "<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
     "<tr><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
     "<tr><td>2</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr>"
     "<tr><td>3</td><td>0</td><td>0</td><td>1</td><td>1</td><td>X</td></tr>"
     "<tr><td>4</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>"
     "<tr><td>5</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
     "<tr><td>6</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr>"
     "<tr><td>7</td><td>0</td><td>1</td><td>1</td><td>1</td><td>X</td></tr>"
     "<tr><td>8</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
     "<tr><td>9</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
     "<tr><td>10</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>"
     "<tr><td>11</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
     "<tr><td>12</td><td>1</td><td>1</td><td>0</td><td>0</td><td>X</td></tr>"
     "<tr><td>13</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
     "<tr><td>14</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr>"
     "<tr><td>15</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>"
     "<ul><li><b>a.1)</b> Obtener F lo más simplificada posible. <span class='pts'>(1 punto)</span></li>"
     "<li><b>a.2)</b> Diseñar un circuito con puertas lógicas. <span class='pts'>(0,5 puntos)</span></li></ul>"
     "<p><b>b)</b> ¿Qué son las perturbaciones en un sistema de control y sus causas? ¿Qué tipo de sistema corrige su efecto? Razonar. <span class='pts'>(1 punto)</span></p>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<p>Se colocan los unos y los estados indiferentes (X) en un mapa de Karnaugh; los X se usan para formar los mayores grupos posibles y minimizar la expresión en suma de productos.</p>"),
   "solucion_html":("<h5>a.1) Simplificación de F</h5>"
     "<p>F = 1 en los minterms 5, 10, 13, 14, 15 e indiferentes (X) en 3, 7 y 12. En el mapa de Karnaugh se forman dos grupos aprovechando los indiferentes:</p>"
     "<ul><li>Un <b>cuádruple</b> con B = 1 y D = 1 (minterms 5, 7·X, 13, 15) → <b>B·D</b>.</li>"
     "<li>Un <b>par</b> con A = 1, C = 1, D = 0 (minterms 10, 14) → <b>A·C·D′</b>.</li></ul>"
     "<div class='formula'>$$F=B\\,D+A\\,C\\,D'$$</div>"
     "<div class='res'><b>Resultado:</b> \\(F=B\\,D+A\\,C\\,\\overline{D}\\).</div>"
     "<h5>a.2) Circuito con puertas lógicas</h5>"
     "<figure class='fig'>"+fig_impl_ej3a()+"<figcaption>Implementación de F = B·D + A·C·D′.</figcaption></figure>"
     "<h5>b) Perturbaciones en sistemas de control</h5>"
     "<p>Una <b>perturbación</b> es cualquier señal o efecto <b>no deseado</b>, ajeno a la entrada de referencia, que altera la variable controlada (p. ej. cambios de carga, de temperatura ambiente, rozamientos, variaciones de tensión). "
     "Los <b>sistemas de control en lazo cerrado</b> (realimentados) son capaces de corregir su efecto: al medir la salida real y compararla con la consigna, generan un error que el controlador usa para <b>contrarrestar la perturbación</b>, algo imposible en lazo abierto.</p>")
  },
  {"id":"q6","titulo":"Ejercicio 3 · Opción B · Control de luces y función de transferencia","titulo_corto":"E3·B Luces",
   "etiqueta":"EJERCICIO 3 · OPCIÓN B","meta":"Digital y control · 2,5 puntos (a:1,75 · b:0,75)","menu":"E3·B · Luces + transferencia",
   "enunciado_html":("<p><b>a)</b> Un sistema controla las luces F según: sensor de movimiento M, sensor de luz ambiente L (insuficiente = 1) e interruptor manual S. Las luces se encienden si <i>i)</i> hay movimiento y luz insuficiente, o <i>ii)</i> el interruptor manual está activado. Se pide:</p>"
     "<ul><li><b>a.1)</b> Tabla de verdad de F y función canónica. <span class='pts'>(0,75 puntos)</span></li>"
     "<li><b>a.2)</b> Simplificar por Karnaugh e implementar con puertas NAND. <span class='pts'>(1 punto)</span></li></ul>"
     "<p><b>b)</b> Obtener la función de transferencia C/E del sistema de control de la figura. <span class='pts'>(0,75 puntos)</span></p>"
     "<figure class='fig'>"+fig_lazo_h()+"<figcaption>Sistema de control con G₁ en serie y realimentación H₁.</figcaption></figure>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>La condición se traduce directamente: \\(F=M\\cdot L+S\\).</li>"
     "<li>Para NAND: \\(F=M L+S=\\big((ML)'\\cdot S'\\big)'\\) (doble negación + De Morgan).</li>"
     "<li>Álgebra de bloques: \\(C=G_2(G_1E-H_1C)\\Rightarrow C/E=\\dfrac{G_1G_2}{1+G_2H_1}\\).</li></ul>"),
   "solucion_html":("<h5>a.1) Tabla de verdad y función canónica</h5>"
     "<p>\\(F=M\\cdot L+S\\). Vale 1 siempre que S = 1, o cuando M = L = 1:</p>"
     "<table class='dat'><tr><th>M</th><th>L</th><th>S</th><th>F</th></tr>"
     "<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td></tr>"
     "<tr><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
     "<tr><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
     "<tr><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>"
     "<div class='formula'>$$F=\\sum m(1,3,5,6,7)$$</div>"
     "<h5>a.2) Simplificación e implementación con NAND</h5>"
     "<p>El mapa de Karnaugh agrupa directamente a la forma mínima:</p>"
     "<div class='formula'>$$F=M\\,L+S$$</div>"
     "<p>Con puertas NAND, \\(F=\\big(\\,(M L)'\\cdot S'\\,\\big)'=\\mathrm{NAND}\\big(\\mathrm{NAND}(M,L),\\ \\mathrm{NAND}(S,S)\\big)\\):</p>"
     "<figure class='fig'>"+fig_nand_luces()+"<figcaption>Implementación de F = M·L + S con tres puertas NAND.</figcaption></figure>"
     "<h5>b) Función de transferencia C/E</h5>"
     "<p>\\(G_1\\) está en serie con la entrada y \\(H_1\\) realimenta la salida al sumador (signo −):</p>"
     "<div class='formula'>$$C=G_2\\,(G_1E-H_1C)\\Rightarrow C\\,(1+G_2H_1)=G_1G_2E$$</div>"
     "<div class='formula'>$$\\frac{C}{E}=\\frac{G_1\\,G_2}{1+G_2\\,H_1}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(\\dfrac{C}{E}=\\dfrac{G_1G_2}{1+G_2H_1}\\).</div>")
  }
 ]})

# ---- Ejercicio 4
data["bloques"].append({"id":"b4","titulo":"Ejercicio 4 · IA, datos y medio ambiente","color":"#a78bfa",
 "descripcion_tarjeta":"Aprendizaje automático, bases de datos distribuidas, impacto ambiental y Big Data.",
 "svg_tarjeta":tj_proj,"cuestiones":[
  {"id":"q7","titulo":"Ejercicio 4 · Opción única · Cuestiones teóricas","titulo_corto":"E4 · Teoría",
   "etiqueta":"EJERCICIO 4 · OPCIÓN ÚNICA","meta":"Cuestiones cortas · 2,5 puntos (a:0,5 · b:0,5 · c:0,75 · d:0,75)","menu":"E4 · Cuestiones teóricas",
   "enunciado_html":("<ol type='a'><li>Un algoritmo clasifica imágenes de perros y gatos usando imágenes <b>etiquetadas</b> con su resultado. Identificar y razonar si es aprendizaje automático supervisado o no supervisado. <span class='pts'>(0,5 puntos)</span></li>"
     "<li>¿Qué es una base de datos distribuida? Indicar dos ventajas frente a una centralizada. <span class='pts'>(0,5 puntos)</span></li>"
     "<li>¿Qué es un informe de evaluación de impacto ambiental? Indicar cuatro apartados que debe contener. <span class='pts'>(0,75 puntos)</span></li>"
     "<li>Definir <i>Big Data</i> y enumerar cuatro de sus atributos. <span class='pts'>(0,75 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<p>Cuestiones conceptuales sobre inteligencia artificial, gestión de datos y legislación medioambiental.</p>"),
   "solucion_html":("<h5>a) Tipo de aprendizaje automático</h5>"
     "<p>Es <b>aprendizaje supervisado</b>: el algoritmo se entrena con <b>datos etiquetados</b> (cada imagen viene marcada como “perro” o “gato”), de modo que aprende la relación entre las características (color, forma, tamaño) y la etiqueta conocida. En el <b>no supervisado</b> no habría etiquetas y el sistema agruparía por similitud sin conocer la clase.</p>"
     "<h5>b) Base de datos distribuida</h5>"
     "<p>Es una base de datos cuyos datos están <b>repartidos en varios nodos o ubicaciones físicas</b> conectados por red, funcionando como un único sistema lógico. Ventajas frente a la centralizada:</p><ul>"
     "<li><b>Mayor disponibilidad y tolerancia a fallos:</b> si un nodo cae, los demás siguen operando.</li>"
     "<li><b>Escalabilidad y rendimiento:</b> se accede a los datos localmente y se reparte la carga entre nodos.</li></ul>"
     "<h5>c) Informe de evaluación de impacto ambiental</h5>"
     "<p>Es el documento técnico que <b>identifica, describe y valora los efectos de un proyecto sobre el medio ambiente</b> y propone medidas para evitarlos o reducirlos. Cuatro apartados:</p><ul>"
     "<li>Descripción del proyecto y sus acciones.</li>"
     "<li>Inventario ambiental (estado inicial del entorno).</li>"
     "<li>Identificación y valoración de impactos.</li>"
     "<li>Medidas protectoras/correctoras y programa de vigilancia ambiental.</li></ul>"
     "<h5>d) Big Data</h5>"
     "<p><b>Big Data</b> es el conjunto de tecnologías y técnicas para <b>almacenar, procesar y analizar volúmenes enormes de datos</b> que las herramientas tradicionales no pueden manejar. Cuatro atributos (las “V”):</p><ul>"
     "<li><b>Volumen</b> (gran cantidad de datos).</li><li><b>Velocidad</b> (generación y procesamiento rápidos).</li>"
     "<li><b>Variedad</b> (datos estructurados y no estructurados).</li><li><b>Veracidad</b> (fiabilidad/calidad de los datos).</li></ul>")
  }
 ]})

out=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","and_2025_suplente.json"))
with open(out,"w",encoding="utf-8") as f: json.dump(data,f,ensure_ascii=False,indent=1)
print("JSON escrito:",out)
