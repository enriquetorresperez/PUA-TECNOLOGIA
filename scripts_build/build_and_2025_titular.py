#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Andalucía 2025 (titular-a) para pau-dashboard."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, summer, arrow, line, txt, MARK

def g_and(x,y,w,h,color='#22d3ee'):
    return f"<path d='M{x},{y} L{x+w-h/2},{y} A{h/2},{h/2} 0 0 1 {x+w-h/2},{y+h} L{x},{y+h} Z' stroke='{color}'/>"
def g_or(x,y,w,h,color='#34d399'):
    return f"<path d='M{x},{y} Q{x+w*0.55},{y} {x+w},{y+h/2} Q{x+w*0.55},{y+h} {x},{y+h} Q{x+w*0.32},{y+h/2} {x},{y} Z' stroke='{color}'/>"
def bubble(cx,cy,color='#e2e8f0'):
    return f"<circle cx='{cx}' cy='{cy}' r='4' stroke='{color}'/>"
def g_not(x,y,w,h,color='#a78bfa'):
    return f"<path d='M{x},{y} L{x},{y+h} L{x+w},{y+h/2} Z' stroke='{color}'/>"

# --- Fig Ej1A: curva tensión-deformación ---
def fig_sigma():
    s=svg_open('360 300',360)
    ox,oy=55,255
    s+=arrow(ox,oy,335,oy); s+=arrow(ox,oy,ox,35)
    s+=txt(340,oy+4,'ε','#e2e8f0',14); s+=txt(20,45,'σ(MPa)','#94a3b8',12)
    # ejes marcas
    s+=line(ox,oy-88,ox-5,oy-88); s+=txt(30,oy-84,'100','#94a3b8',11)
    s+=line(ox,oy-176,ox-5,oy-176); s+=txt(30,oy-172,'200','#94a3b8',11)
    ex=ox+220  # ε=0,005
    s+=line(ex,oy,ex,oy+5); s+=txt(ex,oy+18,'0,005','#94a3b8',11,'middle')
    # A en ε=0,0025 -> x=ox+110 ; σ=150 -> y=oy-132
    ax_,ay_=ox+110,oy-132
    # curva: tramo recto O->A, luego curva suave
    s+=f"<path d='M{ox},{oy} L{ax_},{ay_} Q{ox+165},{oy-176} {ox+250},{oy-198}' stroke='#e2e8f0' stroke-width='2.5' fill='none'/>"
    # A y lineas discontinuas
    s+=f"<circle cx='{ax_}' cy='{ay_}' r='3' fill='#fbbf24'/>"
    s+=f"<line x1='{ax_}' y1='{ay_}' x2='{ax_}' y2='{oy}' stroke='#64748b' stroke-dasharray='4 3'/>"
    s+=f"<line x1='{ax_}' y1='{ay_}' x2='{ox}' y2='{ay_}' stroke='#64748b' stroke-dasharray='4 3'/>"
    s+=txt(ax_+8,ay_-2,'A','#fbbf24',14)
    return s+"</svg>"

# --- Fig Ej3A: matriz SOP (reproduce el circuito del examen) ---
def fig_matrix():
    s=svg_open('540 380',540)
    cols={'A':40,"A'":74,'B':120,"B'":154,'C':200,"C'":234,'D':280,"D'":314}
    order=['A',"A'",'B',"B'",'C',"C'",'D',"D'"]
    ytop=30; ybot=360
    # verticales + etiquetas + inversores para las negadas
    for k in order:
        x=cols[k]
        s+=line(x,ytop+22,x,ybot,'#94a3b8')
        s+=txt(x,ytop-2,k,'#e2e8f0',13,'middle')
    for base in ['A','B','C','D']:
        xd=cols[base]; xn=cols[base+"'"]
        s+=line(xd,ytop+8,xn,ytop+8,'#64748b')
        s+=g_not(xn-9,ytop+8,18,16,'#a78bfa'); s+=bubble(xn,ytop+26,'#a78bfa')
    # 6 filas (minterms)
    terms=[["A'","B'","C","D"],["A'","B","C","D"],["A","B'","C'","D"],
           ["A","B'","C","D"],["A","B","C'","D"],["A","B","C","D"]]
    andx=400; ry0=70; dy=48; outs=[]
    for i,t in enumerate(terms):
        y=ry0+i*dy
        s+=g_and(andx,y-14,40,28,'#f59e0b')
        for k in t:
            x=cols[k]
            s+=line(x,y,andx,y)
            s+=f"<circle cx='{x}' cy='{y}' r='3.2' fill='#f59e0b'/>"
        outs.append((andx+40,y))
    # OR final
    orx=470; ory=ry0+2.5*dy-30
    s+=g_or(orx,ory,50,90,'#34d399')
    for (ox2,oy2) in outs:
        s+=line(ox2,oy2,orx,oy2 if ory<=oy2<=ory+90 else ory+45)
    s+=arrow(orx+50,ory+45,orx+70,ory+45); s+=txt(orx+76,ory+50,'S','#4ade80',15)
    return s+"</svg>"

# --- Fig Ej3B: circuito lógico ---
def fig_ej3b():
    s=svg_open('520 250',520)
    for lab,yy in [('A',50),('B',110),('C',170)]:
        s+=txt(24,yy+4,lab,'#e2e8f0',15,'middle')
    # OR(A,B)
    s+=line(38,50,120,50); s+=line(38,110,120,95)
    s+=g_or(120,36,50,44,'#34d399'); s+=line(170,58,250,58)  # P=A+B
    # AND(B,C)
    s+=f"<circle cx='80' cy='110' r='3' fill='#cbd5e1'/>"; s+=line(80,110,120,140)
    s+=line(38,170,120,170)
    s+=g_and(120,126,50,54,'#22d3ee'); s+=line(170,153,250,153)  # Q=B·C
    # NAND(P,Q)
    s+=g_and(250,40,48,60,'#f59e0b'); s+=bubble(302,70)
    s+=line(250,58,250,58); s+=line(250,88,250,153)  # Q sube a NAND? (usamos P y Q)
    s+=line(306,70,380,70)  # NAND out
    # NOT(Q)
    s+=f"<circle cx='220' cy='153' r='3' fill='#cbd5e1'/>"; s+=line(220,153,250,153)
    s+=g_not(250,140,30,26,'#a78bfa'); s+=bubble(284,153); s+=line(288,153,380,153)
    # NOR final
    s+=g_or(380,50,52,74,'#4ade80'); s+=bubble(434,87)
    s+=arrow(438,87,490,87); s+=txt(496,92,'S','#4ade80',16)
    return s+"</svg>"

# --- Fig Ej3B: diagrama de bloques ---
def fig_lazo():
    s=svg_open('460 190',460)
    y=70
    s+=arrow(20,y,66,y); s+=txt(14,y-8,'X','#e2e8f0',15)
    s+=summer(84,y); s+=txt(72,y-6,'+','#4ade80',12); s+=txt(72,y+18,'−','#f87171',13)
    s+=arrow(99,y,150,y); s+=txt(120,y-8,'E','#e2e8f0',14)
    s+=box(150,y-18,60,36,'G₁','#22d3ee'); s+=arrow(210,y,250,y)
    s+=box(250,y-18,60,36,'G₂','#22d3ee'); s+=arrow(310,y,400,y); s+=txt(406,y-6,'Y','#e2e8f0',15)
    fx=360
    s+=f"<circle cx='{fx}' cy='{y}' r='3' fill='#cbd5e1'/>"
    s+=line(fx,y,fx,150); s+=line(fx,150,84,150); s+=arrow(84,150,84,y+15)
    return s+"</svg>"

# --- Fig solución Ej3A: mapa de Karnaugh de S ---
def fig_kmap_s():
    s=svg_open('430 300',430)
    ox,oy,c=95,64,66
    cols=['00','01','11','10']; rows=['00','01','11','10']
    s+=txt(ox+2*c,36,'CD','#94a3b8',13,'middle'); s+=txt(52,oy+2*c,'AB','#94a3b8',13,'middle')
    for j,cl in enumerate(cols): s+=txt(ox+j*c+c/2,56,cl,'#94a3b8',12,'middle')
    for i,rw in enumerate(rows): s+=txt(74,oy+i*c+c/2+4,rw,'#94a3b8',12,'middle')
    ones={(0,2),(1,2),(2,2),(3,2),(2,1),(3,1)}
    for i in range(4):
        for j in range(4):
            v='1' if (i,j) in ones else '0'
            col='#e2e8f0' if v=='1' else '#64748b'
            s+=f"<rect x='{ox+j*c}' y='{oy+i*c}' width='{c}' height='{c}' stroke='#334155'/>"
            s+=txt(ox+j*c+c/2,oy+i*c+c/2+5,v,col,15,'middle')
    s+=f"<rect x='{ox}' y='{oy}' width='{4*c}' height='{4*c}' stroke='#64748b'/>"
    # grupo CD (columna j2 completa)
    s+=f"<rect x='{ox+2*c-5}' y='{oy-5}' width='{c+10}' height='{4*c+10}' rx='16' stroke='#22d3ee' stroke-width='2'/>"
    s+=txt(ox+2*c+c/2,oy-12,'CD','#22d3ee',12,'middle')
    # grupo AD (filas i2,i3 x cols j1,j2)
    s+=f"<rect x='{ox+1*c-8}' y='{oy+2*c-8}' width='{2*c+16}' height='{2*c+16}' rx='16' stroke='#f59e0b' stroke-width='2'/>"
    s+=txt(ox+4*c+8,oy+3*c,'AD','#f59e0b',12)
    s+=txt(ox,oy+4*c+34,'S = A·D + C·D = D·(A + C)','#e2e8f0',15)
    return s+"</svg>"

tj_mat="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#f59e0b' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='M20 60V28l14 20 14-20v32'/><path d='M60 60V28h10a8 8 0 0 1 0 16H60'/></svg>"
tj_ter="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#22d3ee' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><rect x='20' y='24' width='40' height='32' rx='3'/><path d='M60 40h18M30 62v6M50 62v6'/></svg>"
tj_log="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#34d399' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='M24 26h20a16 16 0 0 1 0 28H24z'/><path d='M24 26q10 14 0 28'/><path d='M64 40h14'/></svg>"
tj_proj="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#a78bfa' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><rect x='26' y='18' width='42' height='48' rx='3'/><path d='M34 30h26M34 42h26M34 54h16'/></svg>"

data={"meta":{
  "titulo":"Tecnología e Ingeniería II",
  "subtitulo":"Andalucía, Ceuta, Melilla y centros en Marruecos · Curso 2024-2025 · Examen resuelto y comentado",
  "cabecera_titulo":"PEvAU 2025 · <span>Tecnología e Ingeniería II</span> · Andalucía · Titular (A)",
  "pill":"90 min · 10 puntos",
  "enunciado_pdf":"../../examens/Andalucia/Tecnologia_Andalucia_2025_ordinaria_titular-a.pdf",
  "pdf_dir":"pdf_and_2025_titular",
  "footer":"Dpto. Tecnología · Solucionario PEvAU 2025 · Andalucía · Tecnología e Ingeniería II (Titular A)",
  "intro_inicio":"Selecciona un ejercicio o cuestión en la barra lateral. En los <b>ejercicios 1, 2 y 3</b> se responde <b>solo una</b> opción (A o B) y el <b>ejercicio 4</b> es de opción única. Aquí se resuelven <b>todas</b> para repasar."},
 "bloques":[]}

# ---- Ejercicio 1
data["bloques"].append({"id":"b1","titulo":"Ejercicio 1 · Materiales","color":"#f59e0b",
 "descripcion_tarjeta":"Ensayo de tracción (módulo elástico) y durezas Brinell/Vickers.",
 "svg_tarjeta":tj_mat,"cuestiones":[
  {"id":"q1","titulo":"Ejercicio 1 · Opción A · Ensayo de tracción","titulo_corto":"E1·A Tracción",
   "etiqueta":"EJERCICIO 1 · OPCIÓN A","meta":"Materiales · 2,5 puntos (a:0,75 · b:1 · c:0,75)","menu":"E1·A · Ensayo de tracción",
   "enunciado_html":("<p>En un ensayo de tracción a una probeta cilíndrica se obtiene el diagrama tensión-deformación de la figura, donde el punto <b>A</b> es el límite elástico. Determinar:</p>"
     "<ol type='a'><li>El módulo de elasticidad. <span class='pts'>(0,75 puntos)</span></li>"
     "<li>El alargamiento si se aplica una carga de 20 000 N, con diámetro 25 mm y longitud 75 mm. <span class='pts'>(1 punto)</span></li>"
     "<li>La carga máxima que soporta sin deformarse permanentemente. <span class='pts'>(0,75 puntos)</span></li></ol>"),
   "figura_enunciado_svg":fig_sigma(),
   "aplica_html":("<ul><li>En la zona elástica se cumple la ley de Hooke: \\(E=\\dfrac{\\sigma}{\\varepsilon}\\).</li>"
     "<li>Tensión \\(\\sigma=F/A\\) con \\(A=\\frac{\\pi}{4}D^2\\); deformación \\(\\varepsilon=\\sigma/E\\); alargamiento \\(\\Delta L=\\varepsilon L\\).</li>"
     "<li>El límite elástico \\(\\sigma_A\\) marca la máxima tensión sin deformación permanente: \\(F_{max}=\\sigma_A\\,A\\).</li></ul>"),
   "solucion_html":("<h5>a) Módulo de elasticidad</h5>"
     "<p>Del diagrama, el punto A (límite elástico) está en \\(\\sigma_A=150\\ \\mathrm{MPa}\\) y \\(\\varepsilon_A=0{,}0025\\):</p>"
     "<div class='formula'>$$E=\\frac{\\sigma_A}{\\varepsilon_A}=\\frac{150\\ \\mathrm{MPa}}{0{,}0025}=60\\,000\\ \\mathrm{MPa}=60\\ \\mathrm{GPa}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(E\\approx 60\\ \\mathrm{GPa}\\).</div>"
     "<h5>b) Alargamiento con 20 000 N</h5>"
     "<div class='formula'>$$A=\\frac{\\pi}{4}(0{,}025)^2=4{,}909\\times10^{-4}\\ \\mathrm{m^2}\\qquad \\sigma=\\frac{20000}{4{,}909\\times10^{-4}}=40{,}7\\ \\mathrm{MPa}$$</div>"
     "<p>Como \\(40{,}7<150\\) MPa, la probeta trabaja en régimen elástico:</p>"
     "<div class='formula'>$$\\varepsilon=\\frac{\\sigma}{E}=\\frac{40{,}7}{60000}=6{,}79\\times10^{-4}\\qquad \\Delta L=\\varepsilon L=6{,}79\\times10^{-4}\\times75=0{,}051\\ \\mathrm{mm}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(\\Delta L\\approx 0{,}051\\ \\mathrm{mm}\\).</div>"
     "<h5>c) Carga máxima sin deformación permanente</h5>"
     "<div class='formula'>$$F_{max}=\\sigma_A\\,A=150\\times10^{6}\\times4{,}909\\times10^{-4}=7{,}36\\times10^{4}\\ \\mathrm N$$</div>"
     "<div class='res'><b>Resultado:</b> \\(F_{max}\\approx 73{,}6\\ \\mathrm{kN}\\).</div>")
  },
  {"id":"q2","titulo":"Ejercicio 1 · Opción B · Dureza Brinell y Vickers","titulo_corto":"E1·B Durezas",
   "etiqueta":"EJERCICIO 1 · OPCIÓN B","meta":"Materiales · 2,5 puntos (a:1,25 · b:1,25)","menu":"E1·B · Brinell y Vickers",
   "enunciado_html":("<p>Para una misma muestra de acero:</p>"
     "<ol type='a'><li>Expresión normalizada de la dureza <b>Brinell</b> si la huella es de 2,5 mm con carga de 725 kp, penetrador de 5 mm y 20 s. <span class='pts'>(1,25 puntos)</span></li>"
     "<li>Expresión normalizada de la dureza <b>Vickers</b> con punta piramidal, carga de 120 kp, 10 s y diagonales de 1,25 mm y 1,23 mm. <span class='pts'>(1,25 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Brinell: \\(HB=\\dfrac{2F}{\\pi D\\left(D-\\sqrt{D^2-d^2}\\right)}\\).</li>"
     "<li>Vickers: \\(HV=1{,}8544\\,\\dfrac{F}{d^2}\\), con \\(d\\) la media de las diagonales.</li></ul>"),
   "solucion_html":("<h5>a) Dureza Brinell</h5>"
     "<div class='formula'>$$HB=\\frac{2\\cdot725}{\\pi\\cdot5\\left(5-\\sqrt{25-2{,}5^2}\\right)}=\\frac{1450}{15{,}708\\,(5-4{,}330)}=\\frac{1450}{10{,}52}=137{,}8$$</div>"
     "<div class='res'><b>Resultado:</b> \\(HB\\approx 138\\). Expresión normalizada: <b>138 HB 5 725 20</b>.</div>"
     "<h5>b) Dureza Vickers</h5>"
     "<p>Diagonal media \\(d=\\frac{1{,}25+1{,}23}{2}=1{,}24\\ \\mathrm{mm}\\):</p>"
     "<div class='formula'>$$HV=1{,}8544\\,\\frac{120}{1{,}24^2}=\\frac{222{,}5}{1{,}538}=144{,}7$$</div>"
     "<div class='res'><b>Resultado:</b> \\(HV\\approx 145\\). Expresión normalizada: <b>145 HV 120 10</b>.</div>")
  }
 ]})

# ---- Ejercicio 2
data["bloques"].append({"id":"b2","titulo":"Ejercicio 2 · Máquinas y sistemas mecánicos","color":"#22d3ee",
 "descripcion_tarjeta":"Motor Otto y bomba de calor; cilindro neumático de doble efecto.",
 "svg_tarjeta":tj_ter,"cuestiones":[
  {"id":"q3","titulo":"Ejercicio 2 · Opción A · Motor Otto y bomba de calor","titulo_corto":"E2·A Térmica",
   "etiqueta":"EJERCICIO 2 · OPCIÓN A","meta":"Máquinas térmicas · 2,5 puntos (a:1,5 · b:1)","menu":"E2·A · Motor Otto + bomba de calor",
   "enunciado_html":("<p><b>a)</b> Un motor Otto de 4T y 4 cilindros consume 9 litros/hora de un combustible con poder calorífico 41 000 kJ/kg y densidad 0,850 kg/l, con rendimiento del 40 %. El diámetro de cada pistón es 70 mm y la carrera 90 mm. Obtener la potencia desarrollada y la cilindrada. <span class='pts'>(1,5 puntos)</span></p>"
     "<p><b>b)</b> Una bomba de calor reversible climatiza una nave a 23 °C en invierno. Su eficiencia real es 5 y equivale al 30 % de la ideal. Calcular la temperatura media en el exterior. <span class='pts'>(1 punto)</span></p>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Potencia calorífica del combustible: \\(\\dot Q=\\dot m\\,PCI\\) con \\(\\dot m=\\rho\\,\\dot V\\); potencia útil \\(P=\\eta\\,\\dot Q\\).</li>"
     "<li>Cilindrada: \\(V_T=z\\,\\frac{\\pi}{4}D^2 S\\).</li>"
     "<li>Bomba de calor (calefacción): \\(COP_{ideal}=\\dfrac{T_c}{T_c-T_f}\\), con temperaturas en kelvin.</li></ul>"),
   "solucion_html":("<h5>a) Potencia y cilindrada</h5>"
     "<div class='formula'>$$\\dot m=\\rho\\,\\dot V=0{,}850\\times9=7{,}65\\ \\mathrm{kg/h}\\qquad \\dot Q=\\frac{7{,}65\\times41000}{3600}=87{,}1\\ \\mathrm{kW}$$</div>"
     "<div class='formula'>$$P=\\eta\\,\\dot Q=0{,}40\\times87{,}1=34{,}9\\ \\mathrm{kW}$$</div>"
     "<div class='formula'>$$V_T=4\\cdot\\frac{\\pi}{4}(0{,}07)^2(0{,}09)=1{,}385\\times10^{-3}\\ \\mathrm{m^3}=1385\\ \\mathrm{cm^3}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(P\\approx 34{,}9\\ \\mathrm{kW}\\) y cilindrada \\(\\approx 1{,}39\\ \\mathrm L\\) (1385 cm³).</div>"
     "<h5>b) Temperatura exterior</h5>"
     "<p>La eficiencia ideal es \\(COP_{ideal}=5/0{,}30=16{,}67\\). Para bomba de calor con foco caliente \\(T_c=23+273=296\\ \\mathrm K\\):</p>"
     "<div class='formula'>$$COP_{ideal}=\\frac{T_c}{T_c-T_f}\\Rightarrow 16{,}67=\\frac{296}{296-T_f}\\Rightarrow 296-T_f=17{,}76$$</div>"
     "<div class='formula'>$$T_f=278{,}2\\ \\mathrm K=5{,}1\\ \\mathrm{^\\circ C}$$</div>"
     "<div class='res'><b>Resultado:</b> la temperatura media exterior es \\(\\approx 5{,}1\\ \\mathrm{^\\circ C}\\).</div>")
  },
  {"id":"q4","titulo":"Ejercicio 2 · Opción B · Cilindro neumático de un brazo robótico","titulo_corto":"E2·B Neumática",
   "etiqueta":"EJERCICIO 2 · OPCIÓN B","meta":"Sistemas neumáticos · 2,5 puntos (a:1 · b:1,5)","menu":"E2·B · Cilindro neumático",
   "enunciado_html":("<p>Un brazo robótico usa un cilindro neumático de doble efecto con émbolo de <b>20 mm</b>, vástago de <b>8 mm</b> y carrera de <b>40 mm</b>. El compresor suministra aire a <b>9 bar</b> y realiza <b>12 ciclos por minuto</b>. Calcular:</p>"
     "<ol type='a'><li>La fuerza que ejerce el vástago en la carrera de avance. <span class='pts'>(1 punto)</span></li>"
     "<li>El consumo de aire en condiciones normales, en l/min. <span class='pts'>(1,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Fuerza de avance: \\(F=p\\,A_e\\) con \\(A_e=\\frac{\\pi}{4}D^2\\) (presión manométrica).</li>"
     "<li>Volumen por ciclo (doble efecto): \\((A_e+A_a)\\,L\\), con área anular \\(A_a=\\frac{\\pi}{4}(D^2-d^2)\\).</li>"
     "<li>A condiciones normales se multiplica por la relación de presiones absolutas: \\(V_N=V\\cdot\\dfrac{p_{abs}}{p_{atm}}\\).</li></ul>"),
   "solucion_html":("<h5>a) Fuerza en el avance</h5>"
     "<div class='formula'>$$A_e=\\frac{\\pi}{4}(0{,}02)^2=3{,}142\\times10^{-4}\\ \\mathrm{m^2}\\qquad F=p\\,A_e=9\\times10^{5}\\times3{,}142\\times10^{-4}=282{,}7\\ \\mathrm N$$</div>"
     "<div class='res'><b>Resultado:</b> \\(F\\approx 283\\ \\mathrm N\\).</div>"
     "<h5>b) Consumo de aire en condiciones normales</h5>"
     "<div class='formula'>$$A_a=\\frac{\\pi}{4}(0{,}02^2-0{,}008^2)=2{,}639\\times10^{-4}\\ \\mathrm{m^2}$$</div>"
     "<div class='formula'>$$V_{ciclo}=(A_e+A_a)L=(3{,}142+2{,}639)\\times10^{-4}\\times0{,}04=2{,}312\\times10^{-5}\\ \\mathrm{m^3}$$</div>"
     "<div class='formula'>$$Q_{trab}=V_{ciclo}\\times12=2{,}77\\times10^{-4}\\ \\mathrm{m^3/min}$$</div>"
     "<p>A condiciones normales (tomando \\(p_{abs}=9+1=10\\ \\mathrm{bar}\\), \\(p_{atm}\\approx1\\ \\mathrm{bar}\\)):</p>"
     "<div class='formula'>$$Q_N=Q_{trab}\\cdot\\frac{p_{abs}}{p_{atm}}=2{,}77\\times10^{-4}\\times10=2{,}77\\times10^{-3}\\ \\mathrm{m^3/min}=2{,}77\\ \\mathrm{l/min}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(Q_N\\approx 2{,}8\\ \\mathrm{l/min}\\) (a condiciones normales).</div>")
  }
 ]})

# ---- Ejercicio 3
data["bloques"].append({"id":"b3","titulo":"Ejercicio 3 · Sistemas eléctricos, electrónicos y de control","color":"#34d399",
 "descripcion_tarjeta":"Sensores inductivos y diseño lógico; simplificación de circuitos y lazo de control.",
 "svg_tarjeta":tj_log,"cuestiones":[
  {"id":"q5","titulo":"Ejercicio 3 · Opción A · Sensores inductivos y circuito digital","titulo_corto":"E3·A Lógica",
   "etiqueta":"EJERCICIO 3 · OPCIÓN A","meta":"Electrónica digital · 2,5 puntos (a:0,5 · b:2)","menu":"E3·A · Sensores + circuito digital",
   "enunciado_html":("<p><b>a)</b> Indicar el principio de funcionamiento y las aplicaciones principales de los <b>sensores inductivos</b>. <span class='pts'>(0,5 puntos)</span></p>"
     "<p><b>b)</b> Del circuito digital de la figura (entradas A, B, C, D):</p>"
     "<ul><li><b>b.1)</b> Obtener la tabla de verdad y la función lógica S. <span class='pts'>(1 punto)</span></li>"
     "<li><b>b.2)</b> Simplificar S por Karnaugh e implementarla con puertas lógicas. <span class='pts'>(1 punto)</span></li></ul>"),
   "figura_enunciado_svg":fig_matrix(),
   "aplica_html":("<p>El circuito es una matriz suma de productos: cada puerta AND forma un <b>producto</b> (minterm) con las variables directas o negadas conectadas (los puntos), y la puerta OR final <b>suma</b> los seis productos. Leyendo las conexiones se obtiene S, que luego se simplifica con el mapa de Karnaugh.</p>"),
   "solucion_html":("<h5>a) Sensores inductivos</h5>"
     "<p>Un <b>sensor inductivo</b> detecta la presencia de objetos <b>metálicos</b> sin contacto. Genera un campo magnético alterno mediante una bobina en un oscilador; cuando un metal entra en el campo, se inducen <b>corrientes de Foucault</b> que amortiguan la oscilación, y un circuito detector conmuta la salida. "
     "Aplicaciones: detección de posición y fin de carrera, conteo de piezas metálicas, control de velocidad (ruedas dentadas), automatización industrial y robótica.</p>"
     "<h5>b.1) Función lógica S</h5>"
     "<p>Leyendo los seis productos de la matriz:</p>"
     "<div class='formula'>$$S=A'B'CD+A'BCD+AB'C'D+AB'CD+ABC'D+ABCD$$</div>"
     "<div class='formula'>$$S=\\sum m(3,7,9,11,13,15)$$</div>"
     "<p>Es decir, S = 1 en las combinaciones (ABCD) 0011, 0111, 1001, 1011, 1101 y 1111.</p>"
     "<h5>b.2) Simplificación por Karnaugh e implementación</h5>"
     "<p>Todos los unos tienen <b>D = 1</b>; entre ellos faltan 0001 y 0101 (que comparten \\(A'C'\\)). Agrupando:</p>"
     "<div class='formula'>$$S=A\\,D+C\\,D=D\\,(A+C)$$</div>"
     "<figure class='fig'>"+fig_kmap_s()+"<figcaption>Mapa de Karnaugh de S: dos grupos AD y CD.</figcaption></figure>"
     "<div class='res'><b>Resultado:</b> \\(S=D(A+C)\\); se implementa con una puerta OR (A + C) y una AND con D (o dos AND y una OR).</div>")
  },
  {"id":"q6","titulo":"Ejercicio 3 · Opción B · Simplificación de un circuito y lazo de control","titulo_corto":"E3·B Control",
   "etiqueta":"EJERCICIO 3 · OPCIÓN B","meta":"Electrónica y control · 2,5 puntos (a:1,5 · b:1)","menu":"E3·B · Circuito + lazo de control",
   "enunciado_html":("<p><b>a)</b> Dado el circuito digital de la figura, obtener otro que realice la misma función con puertas de dos entradas. <span class='pts'>(1,5 puntos)</span></p>"
     "<figure class='fig'>"+fig_ej3b()+"<figcaption>Circuito lógico dado (Opción B).</figcaption></figure>"
     "<p><b>b)</b> El sistema de control de lazo cerrado de la figura tiene un regulador \\(G_1\\) y una planta \\(G_2=50\\). Determinar \\(G_1\\) para que el error E sea inferior a 0,1 cuando la entrada X = 1. <span class='pts'>(1 punto)</span></p>"
     "<figure class='fig'>"+fig_lazo()+"<figcaption>Sistema de control en lazo cerrado (realimentación unitaria).</figcaption></figure>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Se recorre el circuito puerta a puerta y se simplifica el álgebra de Boole (absorción, De Morgan).</li>"
     "<li>Con realimentación unitaria: \\(E=X-Y\\) y \\(Y=G_1G_2E\\), de donde \\(E=\\dfrac{X}{1+G_1G_2}\\).</li></ul>"),
   "solucion_html":("<h5>a) Función del circuito y equivalente</h5>"
     "<p>Puerta a puerta: \\(P=A+B\\) (OR), \\(Q=B\\,C\\) (AND). La NAND da \\((P\\,Q)'\\) y el inversor \\(Q'\\); la NOR final:</p>"
     "<div class='formula'>$$S=\\big((P Q)'+Q'\\big)'=(P Q)\\cdot Q=P\\,Q=(A+B)\\,B\\,C$$</div>"
     "<p>Por absorción \\((A+B)\\,B=B\\), luego:</p>"
     "<div class='formula'>$$S=B\\cdot C$$</div>"
     "<div class='res'><b>Resultado:</b> la función es \\(S=B\\cdot C\\); el circuito equivalente con puertas de dos entradas es una <b>única puerta AND</b> de entradas B y C.</div>"
     "<h5>b) Valor del regulador G₁</h5>"
     "<p>Con realimentación unitaria y \\(G_2=50\\):</p>"
     "<div class='formula'>$$E=\\frac{X}{1+G_1 G_2}=\\frac{1}{1+50\\,G_1}<0{,}1$$</div>"
     "<div class='formula'>$$1+50\\,G_1>10\\Rightarrow 50\\,G_1>9\\Rightarrow G_1>0{,}18$$</div>"
     "<div class='res'><b>Resultado:</b> el error es menor que 0,1 si \\(G_1>0{,}18\\).</div>")
  }
 ]})

# ---- Ejercicio 4 (opción única)
data["bloques"].append({"id":"b4","titulo":"Ejercicio 4 · Proyectos, seguridad, IA y medio ambiente","color":"#a78bfa",
 "descripcion_tarjeta":"Documentos de un proyecto, ciberseguridad, inteligencia artificial y estudio de impacto ambiental.",
 "svg_tarjeta":tj_proj,"cuestiones":[
  {"id":"q7","titulo":"Ejercicio 4 · Opción única · Cuestiones teóricas","titulo_corto":"E4 · Teoría",
   "etiqueta":"EJERCICIO 4 · OPCIÓN ÚNICA","meta":"Cuestiones cortas · 2,5 puntos (a:0,75 · b:0,5 · c:0,5 · d:0,75)","menu":"E4 · Cuestiones teóricas",
   "enunciado_html":("<ol type='a'><li>Enumerar y definir los documentos básicos de un proyecto técnico. <span class='pts'>(0,75 puntos)</span></li>"
     "<li>Se recibe un correo de un desconocido diciendo que la IP del ordenador ha ganado un premio y que, para recibirlo, hay que entrar en una web e indicar datos personales. Identificar y justificar el ataque. <span class='pts'>(0,5 puntos)</span></li>"
     "<li>En inteligencia artificial, ¿qué es una máquina reactiva? Indicar un ejemplo. <span class='pts'>(0,5 puntos)</span></li>"
     "<li>¿Cuándo y por qué es necesario un estudio de impacto ambiental? <span class='pts'>(0,75 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<p>Cuestiones conceptuales sobre proyectos técnicos, ciberseguridad, tipos de inteligencia artificial y legislación medioambiental.</p>"),
   "solucion_html":("<h5>a) Documentos básicos de un proyecto técnico</h5><ul>"
     "<li><b>Memoria:</b> describe y justifica las soluciones adoptadas, objetivos y necesidades.</li>"
     "<li><b>Planos:</b> representación gráfica acotada que define el producto o instalación para su fabricación/construcción.</li>"
     "<li><b>Pliego de condiciones:</b> condiciones técnicas, legales y económicas de ejecución (materiales, normativa, garantías).</li>"
     "<li><b>Presupuesto:</b> valoración económica basada en el estado de mediciones y los precios unitarios.</li>"
     "<li><b>Estado de mediciones</b> (a menudo dentro del presupuesto): cuantifica materiales y unidades de obra.</li></ul>"
     "<h5>b) Tipo de ataque</h5>"
     "<p>Es un caso de <b>phishing</b> (suplantación de identidad mediante ingeniería social): un mensaje fraudulento con un cebo (premio) induce a la víctima a entrar en una web falsa y ceder <b>datos personales y credenciales</b>, que los atacantes usarán para fraude o robo de identidad. Se justifica por: remitente desconocido, premio no solicitado, urgencia y petición de datos personales en un enlace externo.</p>"
     "<h5>c) Máquina reactiva (IA)</h5>"
     "<p>Una <b>máquina reactiva</b> es el tipo de IA más básico: <b>no tiene memoria</b> ni aprende de experiencias pasadas; simplemente reacciona ante los estímulos presentes con una respuesta determinada. "
     "Ejemplo: <b>Deep Blue</b>, el ordenador de ajedrez de IBM, que elige la jugada evaluando el estado actual del tablero sin recordar partidas anteriores.</p>"
     "<h5>d) Estudio de impacto ambiental</h5>"
     "<p>Es necesario <b>antes de ejecutar</b> proyectos, obras o actividades que pueden producir efectos <b>significativos sobre el medio ambiente</b> (grandes infraestructuras, industrias, etc.), tal como <b>exige la legislación</b>. "
     "Su finalidad es <b>identificar, evaluar y prevenir o minimizar</b> los efectos ambientales, proponiendo medidas correctoras y alternativas para un desarrollo sostenible.</p>")
  }
 ]})

out=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","and_2025_titular.json"))
with open(out,"w",encoding="utf-8") as f: json.dump(data,f,ensure_ascii=False,indent=1)
print("JSON escrito:",out)
