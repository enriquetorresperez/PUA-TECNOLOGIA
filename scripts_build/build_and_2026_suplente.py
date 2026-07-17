#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Andalucía 2026 (suplente) para pau-dashboard."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt, MARK

# ---------- gate shapes (circuito lógico) ----------
def g_and(x,y,w,h,color='#22d3ee'):
    return f"<path d='M{x},{y} L{x+w-h/2},{y} A{h/2},{h/2} 0 0 1 {x+w-h/2},{y+h} L{x},{y+h} Z' stroke='{color}'/>"
def g_or(x,y,w,h,color='#34d399'):
    return f"<path d='M{x},{y} Q{x+w*0.55},{y} {x+w},{y+h/2} Q{x+w*0.55},{y+h} {x},{y+h} Q{x+w*0.32},{y+h/2} {x},{y} Z' stroke='{color}'/>"
def bubble(cx,cy,color='#e2e8f0'):
    return f"<circle cx='{cx}' cy='{cy}' r='4' stroke='{color}'/>"
def g_not(x,y,w,h,color='#a78bfa'):
    return f"<path d='M{x},{y} L{x},{y+h} L{x+w},{y+h/2} Z' stroke='{color}'/>"

# =================================================================== FIGURAS

# --- Estructura (enunciado q4 a) ---
def fig_estructura():
    s = svg_open('360 300', 340)
    # pared con rayado
    s += line(46,30,46,282,'#64748b')
    for yy in range(36,282,16):
        s += line(30,yy+10,46,yy,'#475569')
    # barra a 45 grados, escala 24 px/m ; A(48,270) ; comp = 24*cos45=16.97
    Ax,Ay=48,270
    Bx,By=int(Ax+8*16.97), int(Ay-8*16.97)   # 8 m
    Cx,Cy=int(Ax+6*16.97), int(Ay-6*16.97)   # 6 m
    s += f"<line x1='{Ax}' y1='{Ay}' x2='{Bx}' y2='{By}' stroke='#94a3b8' stroke-width='6'/>"
    # cable horizontal de C a la pared
    s += line(Cx,Cy,46,Cy,'#22d3ee')
    s += txt((46+Cx)//2, Cy-8, 'cable', '#22d3ee', 12, 'middle')
    # apoyo A (pasador)
    s += f"<circle cx='{Ax}' cy='{Ay}' r='5' fill='none' stroke='#e2e8f0'/>"
    # carga en B
    s += arrow(Bx,By,Bx,By+52,'#fbbf24')
    s += f"<rect x='{Bx-9}' y='{By+52}' width='18' height='22' stroke='#fbbf24'/>"
    s += txt(Bx+14, By+70, '15 000 N', '#fbbf24', 12)
    # etiquetas
    s += txt(Ax-4, Ay+18, 'A', '#e2e8f0', 15, 'middle')
    s += txt(Bx+8, By-4, 'B', '#e2e8f0', 15)
    s += txt(Cx+6, Cy-6, 'C', '#e2e8f0', 15)
    s += txt((Ax+Cx)//2-16, (Ay+Cy)//2+2, '6 m', '#94a3b8', 12)
    s += txt((Cx+Bx)//2+4, (Cy+By)//2-6, '2 m', '#94a3b8', 12)
    s += f"<path d='M{Ax+30},{Ay} A30,30 0 0 0 {Ax+21},{Ay-21}' stroke='#94a3b8'/>"
    s += txt(Ax+30, Ay-8, '45°', '#94a3b8', 12)
    return s + "</svg>"

# --- Diagrama de bloques F* (enunciado q4 b) ---
def fig_bloqueF():
    s = svg_open('560 210', 560)
    y=115
    s += arrow(16,y,55,y); s += txt(10,y-8,'F*','#e2e8f0',15)
    s += summer(70,y); s += txt(58,y-6,'+','#4ade80',13); s += txt(58,y+18,'−','#f87171',15)
    # nodo tras sum1
    nx=100
    s += line(85,y,nx,y); s += f"<circle cx='{nx}' cy='{y}' r='3' fill='#cbd5e1'/>"
    # rama G1 (arriba)
    s += line(nx,y,nx,65); s += line(nx,65,140,65)
    s += box(140,48,52,34,'G₁','#22d3ee'); s += line(192,65,250,65); s += arrow(250,65,250,y-15)
    # rama G2 (medio)
    s += line(nx,y,140,y); s += box(140,y-17,52,34,'G₂','#22d3ee'); s += arrow(192,y,235,y)
    # sum2 (+ de G2 izquierda, − de G1 arriba)
    s += summer(250,y); s += txt(238,y+5,'+','#4ade80',13); s += txt(262,y-8,'−','#f87171',13)
    s += arrow(265,y,300,y)
    s += box(300,y-17,52,34,'G₃','#22d3ee'); s += arrow(352,y,392,y)
    s += box(392,y-17,52,34,'G₄','#22d3ee'); s += arrow(444,y,520,y); s += txt(526,y-6,'F','#e2e8f0',15)
    # realimentacion G5
    fx=470
    s += f"<circle cx='{fx}' cy='{y}' r='3' fill='#cbd5e1'/>"
    s += line(fx,y,fx,170); s += line(fx,170,250,170)
    s += box(198,153,52,34,'G₅','#34d399'); s += line(198,170,70,170); s += arrow(70,170,70,y+15)
    return s + "</svg>"

# --- Viga (enunciado q5 a) ---
def fig_viga():
    s = svg_open('560 235', 540)
    x0=60; sc=80.0  # px/m
    def X(m): return int(x0+sc*m)
    yb=92
    # barra
    s += f"<rect x='{x0}' y='{yb-6}' width='{X(5.5)-x0}' height='12' fill='#64748b' stroke='#94a3b8'/>"
    # apoyo A (fijo) en 0,5 m ; carga 1kN encima
    xa=X(0.5)
    s += f"<path d='M{xa-12},{yb+30} L{xa},{yb+6} L{xa+12},{yb+30} Z' stroke='#e2e8f0'/>"
    for k in range(-12,13,6): s += line(xa+k, yb+30, xa+k-6, yb+38,'#64748b')
    s += line(xa-14,yb+30,xa+14,yb+30,'#e2e8f0')
    # apoyo B (movil) en 4,5 m
    xbp=X(4.5)
    s += f"<path d='M{xbp-12},{yb+26} L{xbp},{yb+6} L{xbp+12},{yb+26} Z' stroke='#e2e8f0'/>"
    s += f"<circle cx='{xbp-6}' cy='{yb+31}' r='4' stroke='#e2e8f0'/><circle cx='{xbp+6}' cy='{yb+31}' r='4' stroke='#e2e8f0'/>"
    s += line(xbp-14,yb+36,xbp+14,yb+36,'#e2e8f0')
    # cargas
    s += arrow(xa,40,xa,yb-7,'#fbbf24'); s += txt(xa,32,'1 kN','#fbbf24',13,'middle')
    xr=X(5.5)
    s += arrow(xr,40,xr,yb-7,'#fbbf24'); s += txt(xr,32,'0,5 kN','#fbbf24',13,'middle')
    # cotas
    yd=165
    def cota(xa2,xb2,lab):
        return (arrow(xa2+2,yd,xb2-2,yd,'#94a3b8')+arrow(xb2-2,yd,xa2+2,yd,'#94a3b8')
                +line(xa2,yd-6,xa2,yd+6,'#334155')+line(xb2,yd-6,xb2,yd+6,'#334155')
                +txt((xa2+xb2)//2,yd-8,lab,'#94a3b8',12,'middle'))
    s += cota(X(0),X(0.5),'0,5 m'); s += cota(X(0.5),X(1.5),'1 m')
    s += cota(X(1.5),X(4.5),'3 m'); s += cota(X(4.5),X(5.5),'1 m')
    return s + "</svg>"

# --- Diagrama de bloques invernadero (enunciado q5 b) ---
def fig_inv():
    s = svg_open('600 200', 600)
    y=88
    s += arrow(16,y,58,y); s += txt(12,y-8,'T*','#e2e8f0',15)
    s += box(58,y-17,52,34,'G₁','#22d3ee'); s += line(110,y,150,y); s += txt(128,y-6,'v1','#94a3b8',12)
    s += summer(170,y); s += txt(158,y-6,'+','#4ade80',12); s += txt(158,y+18,'−','#f87171',13)
    s += arrow(185,y,225,y); s += txt(202,y-6,'v3','#94a3b8',12)
    s += box(225,y-17,52,34,'G₂','#22d3ee'); s += line(277,y,317,y); s += txt(292,y-6,'v4','#94a3b8',12)
    s += box(317,y-17,52,34,'G₃','#22d3ee'); s += arrow(369,y,470,y); s += txt(476,y-6,'T','#e2e8f0',15)
    # realimentacion H
    fx=420
    s += f"<circle cx='{fx}' cy='{y}' r='3' fill='#cbd5e1'/>"
    s += line(fx,y,fx,150); s += line(fx,150,330,150)
    s += box(278,133,52,34,'H','#34d399'); s += line(278,150,170,150); s += arrow(170,150,170,y+15)
    s += txt(150,145,'v2','#94a3b8',12)
    return s + "</svg>"

# --- Circuito lógico (enunciado q7) ---
def fig_logic():
    s = svg_open('620 300', 620)
    # entradas
    for lab,yy in [('A',55),('B',95),('C',160),('D',215)]:
        s += txt(30,yy+4,lab,'#e2e8f0',15,'middle')
    # NAND(A,B)
    s += line(40,55,200,55); s += line(40,95,200,85)
    s += g_and(200,40,52,60,'#22d3ee'); s += bubble(258,70)
    n1y=70
    s += line(262,n1y,470,n1y)   # salida NAND al OR final (arriba)
    # rama B hacia abajo
    s += f"<circle cx='150' cy='95' r='3' fill='#cbd5e1'/>"; s += line(150,95,150,205); s += line(150,205,300,205)
    # NOT(C)
    s += line(40,160,150,160); s += g_not(150,146,32,28,'#a78bfa'); s += bubble(188,160)
    s += line(192,160,360,160)   # C' hacia AND (arriba)
    # OR(B,D)
    s += line(40,215,300,235)
    s += g_or(300,190,52,60,'#34d399'); s += line(352,220,360,220)  # OR out -> AND abajo
    # AND(C', OR)
    s += g_and(360,146,52,74,'#f59e0b')
    s += line(412,183,470,183)   # AND out -> OR final abajo
    # OR final
    s += g_or(470,45,56,74,'#4ade80')
    s += arrow(526,82,570,82); s += txt(578,87,'F','#4ade80',16)
    return s + "</svg>"

# --- Solución: DSL de la estructura ---
def fig_dsl():
    s = svg_open('360 300', 340)
    Ax,Ay=60,265
    Bx,By=int(Ax+8*16.97), int(Ay-8*16.97)
    Cx,Cy=int(Ax+6*16.97), int(Ay-6*16.97)
    s += f"<line x1='{Ax}' y1='{Ay}' x2='{Bx}' y2='{By}' stroke='#94a3b8' stroke-width='5'/>"
    # peso en B
    s += arrow(Bx,By,Bx,By+50,'#fbbf24'); s += txt(Bx+8,By+40,'P = 15 000 N','#fbbf24',12)
    # tension cable en C (horizontal hacia la pared, -x)
    s += arrow(Cx,Cy,Cx-60,Cy,'#22d3ee'); s += txt(Cx-58,Cy-8,'T','#22d3ee',14)
    # reaccion en A (componentes)
    s += arrow(Ax,Ay,Ax+46,Ay,'#f87171'); s += txt(Ax+28,Ay+16,'Rx','#f87171',12)
    s += arrow(Ax,Ay,Ax,Ay-46,'#f87171'); s += txt(Ax-24,Ay-30,'Ry','#f87171',12)
    s += txt(Ax-4,Ay+18,'A','#e2e8f0',14,'middle'); s += txt(Bx+8,By-4,'B','#e2e8f0',14); s += txt(Cx+4,Cy-6,'C','#e2e8f0',14)
    return s + "</svg>"

# --- Solución: mapa de Karnaugh (4 var, F=(ABC)') ---
def fig_karnaugh():
    s = svg_open('420 280', 420)
    ox,oy,c=90,60,66
    cols=['00','01','11','10']; rows=['00','01','11','10']
    s += txt(ox+2*c,34,'CD','#94a3b8',13,'middle'); s += txt(50,oy+2*c,'AB','#94a3b8',13,'middle')
    for j,cl in enumerate(cols): s += txt(ox+j*c+c/2,54,cl,'#94a3b8',12,'middle')
    for i,rw in enumerate(rows): s += txt(72,oy+i*c+c/2+4,rw,'#94a3b8',12,'middle')
    # F=0 solo en AB=11 (fila i=2) y C=1 -> CD col '11'(j2) y '10'(j3): celdas (i2,j2),(i2,j3)
    zeros={(2,2),(2,3)}
    for i in range(4):
        for j in range(4):
            val='0' if (i,j) in zeros else '1'
            col = '#f87171' if val=='0' else '#e2e8f0'
            s += f"<rect x='{ox+j*c}' y='{oy+i*c}' width='{c}' height='{c}' stroke='#334155'/>"
            s += txt(ox+j*c+c/2,oy+i*c+c/2+5,val,col,15,'middle')
    s += f"<rect x='{ox}' y='{oy}' width='{4*c}' height='{4*c}' stroke='#64748b'/>"
    # grupo de los dos ceros (A·B·C) rodeado
    s += f"<rect x='{ox+2*c-4}' y='{oy+2*c-4}' width='{2*c+8}' height='{c+8}' rx='16' stroke='#f87171' stroke-width='2'/>"
    s += txt(ox+3*c, oy+3*c+28, "0 → A·B·C", '#f87171', 12, 'middle')
    s += txt(ox, oy+4*c+34, "F = (A·B·C)′ = A′ + B′ + C′", '#e2e8f0', 15)
    return s + "</svg>"

# --- Solución: NAND de 3 entradas ---
def fig_nand3():
    s = svg_open('340 180', 340)
    for lab,yy in [('A',60),('B',90),('C',120)]:
        s += txt(30,yy+4,lab,'#e2e8f0',15,'middle'); s += line(45,yy,150,yy)
    s += g_and(150,50,70,80,'#f59e0b'); s += bubble(226,90)
    s += arrow(230,90,300,90); s += txt(308,95,'F','#4ade80',16)
    s += txt(185,150,'NAND de 3 entradas', '#94a3b8', 12, 'middle')
    return s + "</svg>"

# tarjetas
tj_mec = "<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#f59e0b' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><rect x='16' y='34' width='40' height='18' rx='3'/><path d='M56 43h14M70 38v10'/><circle cx='30' cy='60' r='4'/><path d='M20 34l6-12h20l6 12'/></svg>"
tj_mat = "<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#22d3ee' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><rect x='18' y='16' width='64' height='48' rx='4'/><path d='M30 40h16M50 40h20M30 52h30'/><circle cx='66' cy='28' r='5'/></svg>"
tj_auto = "<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#34d399' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><rect x='14' y='30' width='24' height='20' rx='3'/><rect x='60' y='30' width='24' height='20' rx='3'/><path d='M38 40h22M50 50v14H24M24 64V50'/></svg>"
tj_ele = "<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#a78bfa' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='M20 20h24l-6 24h16l-24 32 8-24H18z'/></svg>"

data = {
  "meta": {
    "titulo": "Tecnología e Ingeniería II",
    "subtitulo": "Andalucía, Ceuta, Melilla y centros en Marruecos · Curso 2025-2026 · Examen resuelto y comentado",
    "cabecera_titulo": "PAU 2026 · <span>Tecnología e Ingeniería II</span> · Andalucía · Modelo suplente",
    "pill": "90 min · 10 puntos",
    "enunciado_pdf": "../../examens/Andalucia/Tecnologia_Andalucia_2026_ordinaria_suplente.pdf",
    "pdf_dir": "pdf_and_2026_suplente",
    "footer": "Dpto. Tecnología · Solucionario PAU 2026 · Andalucía · Tecnología e Ingeniería II (Suplente)",
    "intro_inicio": "Selecciona un apartado o una cuestión en la barra lateral. El examen tiene <b>4 apartados</b>: el apartado 1 es obligatorio y en los apartados 2, 3 y 4 se responde <b>solo una</b> de las dos opciones (A o B). Aquí se resuelven <b>todas</b> para repasar. Cada cuestión incluye el enunciado oficial, una introducción con los conceptos y la solución paso a paso."
  },
  "bloques": []
}

# ----- Bloque 1
data["bloques"].append({
 "id":"b1","titulo":"Apartado 1 · Sistemas mecánicos","color":"#f59e0b",
 "descripcion_tarjeta":"Cilindro neumático de doble efecto y elección de compresor.",
 "svg_tarjeta":tj_mec,
 "cuestiones":[{
   "id":"q1","titulo":"Apartado 1 · Cilindro neumático y elección del compresor",
   "titulo_corto":"A1 · Neumática","etiqueta":"APARTADO 1 · OBLIGATORIO",
   "meta":"Sistemas mecánicos · 2,5 puntos (a: 1,5 · b: 1,0)","menu":"A1 · Cilindro + compresor",
   "enunciado_html":(
     "<p>Una empresa automatiza el marcado de artículos de cuero con un <b>cilindro neumático de doble efecto</b> que presiona un troquel con una <b>fuerza de avance de 4 500 N</b>. "
     "El cilindro realiza <b>150 ciclos completos por hora</b> (avance y retroceso), con <b>émbolo de 100 mm</b>, <b>carrera de 400 mm</b> y <b>vástago de 25 mm</b>. Hay que elegir un compresor (1 bar = 10⁵ Pa):</p>"
     "<table class='dat'><tr><th>Compresor</th><th>Presión máx. (bar)</th><th>Caudal (l/min)</th></tr>"
     "<tr><td>Modelo A</td><td>5</td><td>20</td></tr><tr><td>Modelo B</td><td>7</td><td>12</td></tr><tr><td>Modelo C</td><td>10</td><td>30</td></tr></table>"
     "<ol type='a'><li>Presión mínima de trabajo (Pa) para ejercer la fuerza (despreciando rozamiento) y caudal de aire (l/min) necesario para los ciclos por hora. <span class='pts'>(1,5 puntos)</span></li>"
     "<li>Indicar y justificar qué modelo de compresor es el adecuado. <span class='pts'>(1 punto)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":(
     "<ul><li>Presión necesaria: \\(p=\\dfrac{F}{A_e}\\), con área del émbolo \\(A_e=\\frac{\\pi}{4}D^2\\).</li>"
     "<li>Consumo por ciclo (doble efecto) = volumen de avance + volumen de retroceso; el retroceso usa el área anular \\(A_a=\\frac{\\pi}{4}(D^2-d^2)\\).</li>"
     "<li>Caudal \\(Q=V_{ciclo}\\times(\\text{ciclos/hora})\\), pasado a l/min.</li>"
     "<li>El compresor válido debe cubrir <b>a la vez</b> la presión y el caudal exigidos.</li></ul>"),
   "solucion_html":(
     "<h5>a) Presión mínima y caudal de aire</h5>"
     "<p>Área del émbolo y presión mínima:</p>"
     "<div class='formula'>$$A_e=\\frac{\\pi}{4}(0{,}1)^2=7{,}854\\times10^{-3}\\ \\mathrm{m^2}\\qquad p=\\frac{F}{A_e}=\\frac{4500}{7{,}854\\times10^{-3}}=5{,}73\\times10^{5}\\ \\mathrm{Pa}$$</div>"
     "<p>Es decir, unos <b>5,73 bar</b>. Área anular y volumen por ciclo (carrera 0,4 m):</p>"
     "<div class='formula'>$$A_a=\\frac{\\pi}{4}(0{,}1^2-0{,}025^2)=7{,}363\\times10^{-3}\\ \\mathrm{m^2}$$</div>"
     "<div class='formula'>$$V_{ciclo}=(A_e+A_a)\\,L=(7{,}854+7{,}363)\\times10^{-3}\\times0{,}4=6{,}087\\times10^{-3}\\ \\mathrm{m^3}$$</div>"
     "<div class='formula'>$$Q=V_{ciclo}\\times150\\ \\tfrac{\\text{ciclos}}{\\text{h}}=0{,}913\\ \\tfrac{\\mathrm{m^3}}{\\mathrm h}=15{,}2\\ \\mathrm{l/min}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(p_{min}\\approx 5{,}73\\times10^{5}\\ \\mathrm{Pa}\\) (5,73 bar) y \\(Q\\approx 15{,}2\\ \\mathrm{l/min}\\).</div>"
     "<h5>b) Compresor adecuado</h5>"
     "<p>El compresor debe dar <b>al menos 5,73 bar y 15,2 l/min</b>:</p><ul>"
     "<li><b>Modelo A</b> (5 bar): no alcanza la presión.</li>"
     "<li><b>Modelo B</b> (7 bar, 12 l/min): presión suficiente, pero <b>caudal insuficiente</b> (12 &lt; 15,2).</li>"
     "<li><b>Modelo C</b> (10 bar, 30 l/min): cumple presión y caudal.</li></ul>"
     "<div class='res'><b>Resultado:</b> el adecuado es el <b>Modelo C</b>, único que satisface simultáneamente presión y caudal.</div>")
 }]})

# ----- Bloque 2
data["bloques"].append({
 "id":"b2","titulo":"Apartado 2 · Materiales y fabricación","color":"#22d3ee",
 "descripcion_tarjeta":"Durezas Brinell y Vickers; resiliencia Charpy en dos probetas.",
 "svg_tarjeta":tj_mat,
 "cuestiones":[
  {"id":"q2","titulo":"Apartado 2 · Opción A · Dureza Brinell y Vickers","titulo_corto":"A2·A Durezas",
   "etiqueta":"APARTADO 2 · OPCIÓN A","meta":"Materiales y fabricación · 2,5 puntos (a:1,25 · b:1,25)","menu":"A2·A · Brinell y Vickers",
   "enunciado_html":(
     "<p>Se ensayan dos probetas. En la <b>probeta A</b> se hace un ensayo <b>Brinell</b> con bola de carburo de wolframio de <b>10 mm</b>, fuerza de <b>3 000 kp</b>, obteniendo una huella de <b>4,0 mm</b>. "
     "En la <b>probeta B</b> se hace un ensayo <b>Vickers</b> con punta piramidal y fuerza de <b>160 kp</b>, midiéndose diagonales de <b>0,44 mm</b> y <b>0,46 mm</b>. Determinar:</p>"
     "<ol type='a'><li>La expresión normalizada de la dureza Brinell de A (duración 20 s). <span class='pts'>(1,25 puntos)</span></li>"
     "<li>La expresión normalizada de la dureza Vickers de B (duración 10 s). <span class='pts'>(1,25 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":(
     "<ul><li>Dureza Brinell: \\(HB=\\dfrac{2F}{\\pi D\\left(D-\\sqrt{D^2-d^2}\\right)}\\) (F en kp, longitudes en mm).</li>"
     "<li>Dureza Vickers: \\(HV=1{,}8544\\,\\dfrac{F}{d^2}\\), con \\(d\\) la <b>media de las diagonales</b>.</li>"
     "<li>Notación normalizada: valor + símbolo + condiciones (bola/carga/tiempo).</li></ul>"),
   "solucion_html":(
     "<h5>a) Dureza Brinell de la probeta A</h5>"
     "<div class='formula'>$$HB=\\frac{2\\cdot3000}{\\pi\\cdot10\\left(10-\\sqrt{10^2-4^2}\\right)}=\\frac{6000}{31{,}416\\,(10-9{,}165)}=\\frac{6000}{26{,}23}=228{,}8$$</div>"
     "<div class='res'><b>Resultado:</b> \\(HB\\approx 229\\). Expresión normalizada: <b>229 HB 10 3000 20</b>.</div>"
     "<h5>b) Dureza Vickers de la probeta B</h5>"
     "<p>Diagonal media \\(d=\\frac{0{,}44+0{,}46}{2}=0{,}45\\ \\mathrm{mm}\\):</p>"
     "<div class='formula'>$$HV=1{,}8544\\,\\frac{160}{0{,}45^2}=\\frac{296{,}7}{0{,}2025}=1465$$</div>"
     "<div class='res'><b>Resultado:</b> \\(HV\\approx 1465\\). Expresión normalizada: <b>1465 HV 160 10</b>.</div>")
  },
  {"id":"q3","titulo":"Apartado 2 · Opción B · Resiliencia Charpy (dos probetas)","titulo_corto":"A2·B Charpy",
   "etiqueta":"APARTADO 2 · OPCIÓN B","meta":"Materiales y fabricación · 2,5 puntos (a:1,25 · b:1,25)","menu":"A2·B · Charpy (2 probetas)",
   "enunciado_html":(
     "<p>En el control de un acero <b>S235JR</b> se hace un ensayo Charpy sobre dos probetas de <b>55 × 10 × 10 mm</b> con entalla en V, obteniéndose una energía absorbida de <b>36 J</b> en la primera y <b>32 J</b> en la segunda.</p>"
     "<ol type='a'><li>Determinar la masa del péndulo si la altura inicial es <b>1,6 m</b> en ambos ensayos y la altura final de la segunda probeta es un <b>10 % mayor</b> que la de la primera. <span class='pts'>(1,25 puntos)</span></li>"
     "<li>Determinar la profundidad de la entalla de ambas probetas sabiendo que la de la segunda es el <b>doble</b> que la de la primera. <span class='pts'>(1,25 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":(
     "<ul><li>Energía absorbida = energía potencial perdida por el péndulo: \\(E=mg(h_0-h_f)\\).</li>"
     "<li>Con dos ensayos y la relación \\(h_{f2}=1{,}1\\,h_{f1}\\) se plantea un sistema para hallar \\(m\\).</li>"
     "<li>La <b>resiliencia</b> \\(\\rho=E/S\\) es la misma (mismo material); \\(S=b\\,(b-a)\\) depende de la entalla \\(a\\).</li></ul>"),
   "solucion_html":(
     "<h5>a) Masa del péndulo</h5>"
     "<p>Planteamos las dos ecuaciones de energía, con \\(h_{f2}=1{,}1\\,h_{f1}\\):</p>"
     "<div class='formula'>$$mg(1{,}6-h_{f1})=36\\qquad mg(1{,}6-1{,}1\\,h_{f1})=32$$</div>"
     "<p>Restando ambas: \\(mg\\,(0{,}1\\,h_{f1})=4\\Rightarrow mg\\,h_{f1}=40\\). Sustituyendo en la primera:</p>"
     "<div class='formula'>$$1{,}6\\,mg-40=36\\Rightarrow mg=47{,}5\\Rightarrow m=\\frac{47{,}5}{9{,}81}=4{,}84\\ \\mathrm{kg}$$</div>"
     "<div class='res'><b>Resultado:</b> la masa del péndulo es \\(m\\approx 4{,}84\\ \\mathrm{kg}\\).</div>"
     "<h5>b) Profundidad de las entallas</h5>"
     "<p>Igual resiliencia y \\(a_2=2a_1\\), con sección \\(S=10\\,(10-a)\\ \\mathrm{mm^2}\\):</p>"
     "<div class='formula'>$$\\frac{E_1}{10\\,(10-a_1)}=\\frac{E_2}{10\\,(10-2a_1)}\\Rightarrow\\frac{36}{10-a_1}=\\frac{32}{10-2a_1}$$</div>"
     "<div class='formula'>$$36\\,(10-2a_1)=32\\,(10-a_1)\\Rightarrow 40=40\\,a_1\\Rightarrow a_1=1\\ \\mathrm{mm}$$</div>"
     "<div class='res'><b>Resultado:</b> entalla de la primera \\(a_1=1\\ \\mathrm{mm}\\) y de la segunda \\(a_2=2\\ \\mathrm{mm}\\).</div>")
  }
 ]})

# ----- Bloque 3
data["bloques"].append({
 "id":"b3","titulo":"Apartado 3 · Sistemas mecánicos y automáticos","color":"#34d399",
 "descripcion_tarjeta":"Estructura en equilibrio, viga con apoyos y sistemas de control por bloques.",
 "svg_tarjeta":tj_auto,
 "cuestiones":[
  {"id":"q4","titulo":"Apartado 3 · Opción A · Estructura con cable y control de fuerza","titulo_corto":"A3·A Estructura",
   "etiqueta":"APARTADO 3 · OPCIÓN A","meta":"Sistemas mecánicos (1,5) y automáticos (1) · 2,5 puntos","menu":"A3·A · Estructura + bloques",
   "enunciado_html":(
     "<p><b>a)</b> A partir del esquema de la estructura en equilibrio (barra a 45° articulada en A, cable horizontal en C y carga de 15 000 N colgada en B), se pide:</p>"
     "<ul><li><b>a.1)</b> Representar el diagrama del sólido libre. <span class='pts'>(0,5 puntos)</span></li>"
     "<li><b>a.2)</b> Calcular la fuerza del cable anclado a la pared. <span class='pts'>(1 punto)</span></li></ul>"
     "<p><b>b)</b> Para regular la fuerza de un cilindro hidráulico se usa el sistema de la figura, donde \\(F^\\ast\\) es la fuerza de consigna, \\(F\\) la real, \\(G_1\\) y \\(G_2\\) forman el controlador, \\(G_3\\) es la válvula, \\(G_4\\) el cilindro y \\(G_5\\) el medidor de presión. Se pide:</p>"
     "<ul><li><b>b.1)</b> Función de transferencia del controlador. <span class='pts'>(0,5 puntos)</span></li>"
     "<li><b>b.2)</b> Relación \\(F/F^\\ast\\) de forma desarrollada. <span class='pts'>(0,5 puntos)</span></li></ul>"
     "<figure class='fig'>"+fig_bloqueF()+"<figcaption>Diagrama de bloques del control de fuerza del cilindro hidráulico.</figcaption></figure>"),
   "figura_enunciado_svg":fig_estructura(),
   "aplica_html":(
     "<ul><li>Equilibrio de la barra: \\(\\sum F=0\\) y \\(\\sum M=0\\). Tomando momentos <b>en A</b> se elimina la reacción del apoyo.</li>"
     "<li>El cable es horizontal: su momento respecto de A es \\(T\\cdot y_C\\) (altura de C). La carga es vertical: momento \\(P\\cdot x_B\\).</li>"
     "<li>Álgebra de bloques: el controlador es la combinación de \\(G_1\\) y \\(G_2\\) según los signos del sumador; el lazo cerrado da \\(F/F^\\ast\\).</li></ul>"),
   "solucion_html":(
     "<h5>a.1) Diagrama del sólido libre</h5>"
     "<p>Sobre la barra actúan: el <b>peso</b> P = 15 000 N (vertical, en B), la <b>tensión del cable</b> T (horizontal, en C, hacia la pared) y la <b>reacción</b> en el apoyo A (componentes \\(R_x, R_y\\)):</p>"
     "<figure class='fig'>"+fig_dsl()+"<figcaption>Diagrama del sólido libre de la barra AB.</figcaption></figure>"
     "<h5>a.2) Fuerza del cable</h5>"
     "<p>La barra forma 45°; C está a 6 m de A y B a 8 m. Alturas y distancias horizontales:</p>"
     "<div class='formula'>$$y_C=6\\sin45^\\circ=4{,}243\\ \\mathrm m\\qquad x_B=8\\cos45^\\circ=5{,}657\\ \\mathrm m$$</div>"
     "<p>Tomando momentos respecto de A (el cable tira en horizontal, la carga cuelga en vertical):</p>"
     "<div class='formula'>$$\\sum M_A=0:\\quad T\\cdot y_C=P\\cdot x_B\\Rightarrow T=15000\\cdot\\frac{5{,}657}{4{,}243}=15000\\cdot\\frac{8}{6}$$</div>"
     "<div class='res'><b>Resultado:</b> la fuerza del cable es \\(T=20\\,000\\ \\mathrm N\\).</div>"
     "<h5>b) Sistema de control del cilindro hidráulico</h5>"
     "<p>El error es \\(e=F^\\ast-G_5F\\). El controlador tiene a \\(G_2\\) en la rama directa (signo +) y a \\(G_1\\) restando (signo −) en el segundo sumador, ambos alimentados por \\(e\\):</p>"
     "<p><b>b.1)</b> Función de transferencia del controlador:</p>"
     "<div class='formula'>$$G_c=G_2-G_1$$</div>"
     "<p><b>b.2)</b> La cadena directa es \\((G_2-G_1)G_3G_4\\) y la realimentación \\(G_5\\):</p>"
     "<div class='formula'>$$\\frac{F}{F^\\ast}=\\frac{(G_2-G_1)\\,G_3\\,G_4}{1+(G_2-G_1)\\,G_3\\,G_4\\,G_5}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(G_c=G_2-G_1\\) y \\(\\dfrac{F}{F^\\ast}=\\dfrac{(G_2-G_1)G_3G_4}{1+(G_2-G_1)G_3G_4G_5}\\).</div>")
  },
  {"id":"q5","titulo":"Apartado 3 · Opción B · Viga con apoyos y control de un invernadero","titulo_corto":"A3·B Viga",
   "etiqueta":"APARTADO 3 · OPCIÓN B","meta":"Sistemas mecánicos (1,5) y automáticos (1) · 2,5 puntos","menu":"A3·B · Viga + invernadero",
   "enunciado_html":(
     "<p><b>a)</b> Para la viga de la figura (apoyo fijo A con la carga de 1 kN encima, apoyo móvil B y carga de 0,5 kN en el extremo derecho), calcular:</p>"
     "<ul><li><b>a.1)</b> Las reacciones en ambos apoyos en equilibrio estático. <span class='pts'>(0,5 puntos)</span></li>"
     "<li><b>a.2)</b> El momento flector en el punto medio de la viga. <span class='pts'>(1 punto)</span></li></ul>"
     "<p><b>b)</b> El diagrama de bloques controla la temperatura de un invernadero: \\(G_1\\) (transductor) convierte la temperatura deseada \\(T^\\ast\\) en la tensión \\(V_1\\); el comparador resta \\(V_2\\) (del sensor), la diferencia \\(V_3\\) se amplifica en \\(G_2\\) y actúa sobre el calefactor \\(G_3\\). En régimen permanente \\(G_1=0{,}1\\ \\mathrm{V/{}^\\circ C}\\), \\(G_2=10\\ \\mathrm{V/V}\\) y \\(G_3=5\\ \\mathrm{{}^\\circ C/V}\\). Se pide:</p>"
     "<ul><li><b>b.1)</b> La relación \\(T/T^\\ast\\). <span class='pts'>(0,5 puntos)</span></li>"
     "<li><b>b.2)</b> ¿Qué valor debe tomar H para que el error \\(T^\\ast-T=0\\)? <span class='pts'>(0,5 puntos)</span></li></ul>"
     "<figure class='fig'>"+fig_inv()+"<figcaption>Diagrama de bloques del control de temperatura del invernadero.</figcaption></figure>"),
   "figura_enunciado_svg":fig_viga(),
   "aplica_html":(
     "<ul><li>Equilibrio de la viga: \\(\\sum F_y=0\\) y \\(\\sum M=0\\) para hallar las reacciones.</li>"
     "<li>El momento flector en una sección es la suma de momentos de las fuerzas situadas a un lado de ella.</li>"
     "<li>Álgebra de bloques: \\(T/T^\\ast=\\dfrac{G_1G_2G_3}{1+G_2G_3H}\\); el error es nulo si \\(T/T^\\ast=1\\).</li></ul>"),
   "solucion_html":(
     "<h5>a.1) Reacciones en los apoyos</h5>"
     "<p>Tomamos A en x = 0,5 m y B en x = 4,5 m (separación 4 m). La carga de 1 kN cae sobre A; la de 0,5 kN en el extremo (x = 5,5 m). Momentos respecto de A:</p>"
     "<div class='formula'>$$\\sum M_A=0:\\ R_B\\cdot4-0{,}5\\cdot5=0\\Rightarrow R_B=0{,}625\\ \\mathrm{kN}$$</div>"
     "<div class='formula'>$$\\sum F_y=0:\\ R_A+R_B=1+0{,}5\\Rightarrow R_A=0{,}875\\ \\mathrm{kN}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(R_A=0{,}875\\ \\mathrm{kN}\\) y \\(R_B=0{,}625\\ \\mathrm{kN}\\).</div>"
     "<h5>a.2) Momento flector en el punto medio</h5>"
     "<p>La viga mide 5,5 m; su punto medio está en x = 2,75 m. A la izquierda solo actúan (en x = 0,5 m) \\(R_A=0{,}875\\) hacia arriba y la carga de 1 kN hacia abajo:</p>"
     "<div class='formula'>$$M=(R_A-1)\\,(2{,}75-0{,}5)=(-0{,}125)\\,(2{,}25)=-0{,}28\\ \\mathrm{kN\\,m}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(M_{medio}\\approx -0{,}28\\ \\mathrm{kN\\,m}\\) (tracción en la fibra superior).</div>"
     "<h5>b) Control de temperatura del invernadero</h5>"
     "<p><b>b.1)</b> Con \\(V_1=G_1T^\\ast\\), \\(V_3=V_1-H\\,T\\), \\(T=G_3G_2V_3\\):</p>"
     "<div class='formula'>$$\\frac{T}{T^\\ast}=\\frac{G_1G_2G_3}{1+G_2G_3H}=\\frac{0{,}1\\cdot10\\cdot5}{1+50H}=\\frac{5}{1+50H}$$</div>"
     "<p><b>b.2)</b> El error \\(T^\\ast-T=0\\) exige \\(T/T^\\ast=1\\):</p>"
     "<div class='formula'>$$\\frac{5}{1+50H}=1\\Rightarrow 1+50H=5\\Rightarrow H=0{,}08$$</div>"
     "<div class='res'><b>Resultado:</b> \\(T/T^\\ast=\\dfrac{5}{1+50H}\\) y para error nulo \\(H=0{,}08\\ \\mathrm{V/{}^\\circ C}\\).</div>")
  }
 ]})

# ----- Bloque 4
data["bloques"].append({
 "id":"b4","titulo":"Apartado 4 · Sistemas eléctricos y electrónicos","color":"#a78bfa",
 "descripcion_tarjeta":"Instalación monofásica con corrección del factor de potencia y diseño lógico con NAND.",
 "svg_tarjeta":tj_ele,
 "cuestiones":[
  {"id":"q6","titulo":"Apartado 4 · Opción A · Instalación eléctrica monofásica","titulo_corto":"A4·A Instalación",
   "etiqueta":"APARTADO 4 · OPCIÓN A","meta":"Sistemas eléctricos y electrónicos · 2,5 puntos (a:1,5 · b:0,5 · c:0,5)","menu":"A4·A · Instalación eléctrica",
   "enunciado_html":(
     "<p>Una instalación a <b>230 V</b> eficaces y <b>50 Hz</b> alimenta:</p><ul>"
     "<li>2 motores asíncronos de <b>3 kW</b> cada uno, con \\(\\cos\\varphi=0{,}7\\) inductivo.</li>"
     "<li>1 motor asíncrono de <b>5 kW</b>, con \\(\\cos\\varphi=0{,}8\\) inductivo.</li>"
     "<li>50 luminarias LED de <b>40 W</b>, con factor de potencia unidad.</li></ul>"
     "<ol type='a'><li>La corriente total absorbida. <span class='pts'>(1,5 puntos)</span></li>"
     "<li>El factor de potencia total. <span class='pts'>(0,5 puntos)</span></li>"
     "<li>Capacidad del condensador en paralelo para mejorar el factor de potencia a la unidad. <span class='pts'>(0,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":(
     "<ul><li>Para cada receptor: \\(P\\) (dato), \\(Q=P\\tan\\varphi\\). Se suman las potencias activas y reactivas.</li>"
     "<li>Potencia aparente \\(S=\\sqrt{P_t^2+Q_t^2}\\); corriente \\(I=S/V\\); factor de potencia \\(\\cos\\varphi=P_t/S\\).</li>"
     "<li>Para \\(\\cos\\varphi=1\\) el condensador debe aportar \\(Q_C=Q_t\\): \\(C=\\dfrac{Q_C}{V^2\\,\\omega}\\).</li></ul>"),
   "solucion_html":(
     "<h5>a) Corriente total</h5>"
     "<p>Potencias activa y reactiva de cada grupo:</p>"
     "<table class='dat'><tr><th>Receptor</th><th>P (kW)</th><th>cos φ</th><th>Q (kVAr)</th></tr>"
     "<tr><td>2 motores 3 kW</td><td>6</td><td>0,7</td><td>6,12</td></tr>"
     "<tr><td>1 motor 5 kW</td><td>5</td><td>0,8</td><td>3,75</td></tr>"
     "<tr><td>50 LED 40 W</td><td>2</td><td>1</td><td>0</td></tr>"
     "<tr><td><b>Total</b></td><td><b>13</b></td><td></td><td><b>9,87</b></td></tr></table>"
     "<div class='formula'>$$S=\\sqrt{P_t^2+Q_t^2}=\\sqrt{13^2+9{,}87^2}=16{,}32\\ \\mathrm{kVA}\\qquad I=\\frac{S}{V}=\\frac{16\\,320}{230}=71{,}0\\ \\mathrm A$$</div>"
     "<div class='res'><b>Resultado:</b> la corriente total es \\(I\\approx 71{,}0\\ \\mathrm A\\).</div>"
     "<h5>b) Factor de potencia total</h5>"
     "<div class='formula'>$$\\cos\\varphi=\\frac{P_t}{S}=\\frac{13}{16{,}32}=0{,}80\\ \\text{(inductivo)}$$</div>"
     "<h5>c) Condensador para cos φ = 1</h5>"
     "<p>El condensador debe compensar toda la reactiva \\(Q_C=Q_t=9{,}87\\ \\mathrm{kVAr}\\):</p>"
     "<div class='formula'>$$C=\\frac{Q_C}{V^2\\,\\omega}=\\frac{9870}{230^2\\cdot2\\pi\\cdot50}=5{,}94\\times10^{-4}\\ \\mathrm F$$</div>"
     "<div class='res'><b>Resultado:</b> \\(C\\approx 594\\ \\mathrm{\\mu F}\\) en paralelo.</div>")
  },
  {"id":"q7","titulo":"Apartado 4 · Opción B · Análisis y simplificación de un circuito lógico","titulo_corto":"A4·B Lógica",
   "etiqueta":"APARTADO 4 · OPCIÓN B","meta":"Sistemas eléctricos y electrónicos · 2,5 puntos (a:1,5 · b:0,5 · c:0,5)","menu":"A4·B · Circuito lógico",
   "enunciado_html":(
     "<p>Dado el circuito lógico de la figura (entradas A, B, C, D), se pide:</p>"
     "<ol type='a'><li>Obtener la tabla de verdad de F y su función canónica. <span class='pts'>(1,5 puntos)</span></li>"
     "<li>Obtener la función simplificada por el método de Karnaugh. <span class='pts'>(0,5 puntos)</span></li>"
     "<li>Representar el circuito lógico correspondiente con puertas NAND. <span class='pts'>(0,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":fig_logic(),
   "aplica_html":(
     "<p>Recorremos el circuito puerta a puerta para obtener la expresión de F, construimos la tabla de verdad, agrupamos en el mapa de Karnaugh y expresamos el resultado con puertas NAND.</p>"),
   "solucion_html":(
     "<h5>a) Expresión, tabla de verdad y función canónica</h5>"
     "<p>Siguiendo el circuito: la NAND da \\((A\\,B)'\\); la rama inferior da \\(C'(B+D)\\); la puerta OR final las combina:</p>"
     "<div class='formula'>$$F=(A\\,B)'+C'\\,(B+D)$$</div>"
     "<p>Analizando: si \\(A=B=1\\) entonces \\((AB)'=0\\) y \\(F=C'\\); en cualquier otro caso \\((AB)'=1\\) y \\(F=1\\). "
     "Por tanto <b>F = 0 únicamente cuando A = B = C = 1</b> (para cualquier D). La función canónica en maxterms es:</p>"
     "<div class='formula'>$$F=\\prod M(14,15)=(A'+B'+C'+D)(A'+B'+C'+D')$$</div>"
     "<h5>b) Simplificación por Karnaugh</h5>"
     "<p>Los dos únicos ceros (A = B = C = 1) se agrupan; la variable D es indiferente:</p>"
     "<figure class='fig'>"+fig_karnaugh()+"<figcaption>Mapa de Karnaugh: los ceros forman el término A·B·C.</figcaption></figure>"
     "<div class='formula'>$$F=(A\\cdot B\\cdot C)'=A'+B'+C'$$</div>"
     "<h5>c) Implementación con puertas NAND</h5>"
     "<p>La función \\(F=(A\\,B\\,C)'\\) es directamente una <b>puerta NAND de tres entradas</b>:</p>"
     "<figure class='fig'>"+fig_nand3()+"<figcaption>F = (A·B·C)′ con una única NAND de 3 entradas.</figcaption></figure>"
     "<div class='res'><b>Resultado:</b> \\(F=(A\\,B\\,C)'\\); la entrada D es irrelevante y basta una NAND de 3 entradas.</div>")
  }
 ]})

out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "and_2026_suplente.json"))
with open(out,"w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=1)
print("JSON escrito:", out)
