#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el JSON del examen Andalucía 2024 (ordinaria, titular-a) para pau-dashboard."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import svg_open, box, arrow, line, txt

def g_and(x,y,w,h,color='#22d3ee'):
    return f"<path d='M{x},{y} L{x+w-h/2},{y} A{h/2},{h/2} 0 0 1 {x+w-h/2},{y+h} L{x},{y+h} Z' stroke='{color}'/>"
def g_or(x,y,w,h,color='#34d399'):
    return f"<path d='M{x},{y} Q{x+w*0.55},{y} {x+w},{y+h/2} Q{x+w*0.55},{y+h} {x},{y+h} Q{x+w*0.32},{y+h/2} {x},{y} Z' stroke='{color}'/>"
def dot(cx,cy,color='#cbd5e1'):
    return f"<circle cx='{cx}' cy='{cy}' r='3' fill='{color}'/>"

# ---------- Fig Ej7: circuito lógico del enunciado ----------
def fig_circuito():
    s=svg_open('520 240',520)
    ya,yb,yc=45,80,195
    # etiquetas de entrada
    s+=txt(20,ya+5,'a','#e2e8f0',16); s+=txt(20,yb+5,'b','#e2e8f0',16); s+=txt(20,yc+5,'c','#e2e8f0',16)
    # AND1 (a,b)
    ax=180; s+=g_and(ax,32,58,64,'#22d3ee')
    s+=line(34,ya,ax,ya); s+=line(34,yb,ax,yb)
    o1x=ax+58; o1y=64
    # OR (b-branch, c)
    orx=180; s+=g_or(orx,130,58,64,'#34d399')
    ory=162; o2x=orx+58
    # b se ramifica hacia abajo
    bnode=95
    s+=dot(bnode,yb)
    s+=line(bnode,yb,bnode,148); s+=line(bnode,148,orx,148)
    s+=line(34,yc,orx,yc); s+=line(orx,yc,orx,176)  # c hasta entrada inferior OR
    # AND final
    fx=350; s+=g_and(fx,72,58,64,'#f59e0b')
    fy=104
    # salida AND1 -> entrada superior AND final (y=88)
    s+=line(o1x,o1y,300,o1y); s+=line(300,o1y,300,88); s+=line(300,88,fx,88)
    # salida OR -> entrada inferior AND final (y=120)
    s+=line(o2x,ory,300,ory); s+=line(300,ory,300,120); s+=line(300,120,fx,120)
    # salida F
    s+=line(fx+58,fy,470,fy); s+=txt(478,fy+5,'F','#fbbf24',16)
    return s+"</svg>"

# ---------- Fig Ej6: fuente de agua (Bernoulli) ----------
def fig_fuente():
    s=svg_open('520 320',520)
    ground=150
    # suelo
    s+=line(40,ground,480,ground,'#94a3b8')
    for gx in range(60,150,14):
        s+=line(gx,ground,gx-6,ground-10,'#64748b')
    # tubería horizontal (profundidad 8 m) y codo hacia tubería vertical fina (5 cm)
    hy=270; vx=360
    s+=line(70,hy,vx+14,hy,'#22d3ee')      # pared inferior (exterior del codo)
    s+=line(70,hy-14,vx,hy-14,'#22d3ee')   # pared superior (interior del codo)
    s+=line(vx,hy-14,vx,60,'#22d3ee')      # pared izquierda del tubo vertical
    s+=line(vx+14,hy,vx+14,60,'#22d3ee')   # pared derecha del tubo vertical
    # bomba
    s+=txt(24,hy+26,'Bomba','#e2e8f0',13)
    s+=arrow(70,hy-7,96,hy-7,'#4ade80')
    # chorro de agua saliente
    s+=f"<path d='M{vx},60 q-18,-34 -40,-14' stroke='#38bdf8' stroke-width='2' fill='none'/>"
    s+=f"<path d='M{vx+14},60 q18,-34 40,-14' stroke='#38bdf8' stroke-width='2' fill='none'/>"
    s+=f"<path d='M{vx+7},60 q0,-40 0,-30' stroke='#38bdf8' stroke-width='2' fill='none'/>"
    # cotas
    # 1,75 m (suelo -> salida)
    s+=line(430,ground,430,72,'#f59e0b')
    s+=txt(438,110,'1,75 m','#f59e0b',12)
    # 8 m (suelo -> tubería horizontal)
    s+=line(410,ground,410,hy-7,'#fbbf24')
    s+=txt(418,215,'8 m','#fbbf24',12)
    # diámetros
    s+=txt(150,hy+24,'15 cm Ø','#94a3b8',12)
    s+=txt(vx+22,110,'5 cm Ø','#94a3b8',12)
    # velocidad salida
    s+=txt(300,30,'v = 12 m/s','#38bdf8',12)
    return s+"</svg>"

# ---------- Fig Ej4c: esquema de máquina frigorífica ----------
def fig_frigorifica():
    s=svg_open('480 320',480)
    # lazo rectangular: condensador arriba, evaporador abajo, compresor dcha, válvula izda
    xl,xr,yt,yb=110,360,90,250
    cyc=yt-2   # centro cajas condensador
    cye=yb     # centro caja evaporador
    s+=box(150,yt-22,180,40,'Condensador','#f87171',13)
    s+=box(150,yb-20,180,40,'Evaporador','#38bdf8',13)
    # compresor (lado derecho)
    s+=f"<circle cx='{xr}' cy='170' r='26' stroke='#f59e0b'/>"
    s+=f"<path d='M{xr-13},156 L{xr-13},184 L{xr+15},170 Z' fill='#f59e0b' stroke='#f59e0b'/>"
    s+=txt(xr+34,166,'Compresor','#f59e0b',12)
    # válvula de expansión (lado izquierdo)
    s+=f"<path d='M{xl-13},156 L{xl+13},184 L{xl+13},156 L{xl-13},184 Z' stroke='#a78bfa'/>"
    s+=txt(xl-30,150,'Válvula de','#a78bfa',12,'end'); s+=txt(xl-30,166,'expansión','#a78bfa',12,'end')
    # tuberías con sentido del refrigerante (compresor->condensador->válvula->evaporador->compresor)
    # 1) evaporador (dcha) -> compresor
    s+=line(330,yb,xr,yb,'#cbd5e1'); s+=arrow(xr,yb,xr,196,'#cbd5e1')
    # 2) compresor -> condensador (dcha)
    s+=line(xr,144,xr,cyc,'#cbd5e1'); s+=arrow(xr,cyc,330,cyc,'#cbd5e1')
    # 3) condensador (izda) -> válvula
    s+=line(150,cyc,xl,cyc,'#cbd5e1'); s+=arrow(xl,cyc,xl,156,'#cbd5e1')
    # 4) válvula -> evaporador (izda)
    s+=line(xl,184,xl,yb,'#cbd5e1'); s+=arrow(xl,yb,150,yb,'#cbd5e1')
    # focos
    s+=txt(240,yt-34,'Foco caliente (cede calor)','#f87171',11,'middle')
    s+=txt(240,yb+38,'Foco frío (absorbe calor)','#38bdf8',11,'middle')
    return s+"</svg>"

# ---------- Fig Ej7b: mapa de Karnaugh de F (3 variables) ----------
def fig_kmap_f():
    s=svg_open('360 240',360)
    ox,oy,c=95,60,64
    cols=['0','1']; rows=['00','01','11','10']
    s+=txt(ox+c,40,'c','#94a3b8',13,'middle'); s+=txt(52,oy+2*c,'ab','#94a3b8',13,'middle')
    for j,cl in enumerate(cols): s+=txt(ox+j*c+c/2,54,cl,'#94a3b8',12,'middle')
    for i,rw in enumerate(rows): s+=txt(74,oy+i*c+c/2+4,rw,'#94a3b8',12,'middle')
    ones={(2,0),(2,1)}  # ab=11 -> filas i=2, ambas columnas
    for i in range(4):
        for j in range(2):
            v='1' if (i,j) in ones else '0'
            col='#e2e8f0' if v=='1' else '#64748b'
            s+=f"<rect x='{ox+j*c}' y='{oy+i*c}' width='{c}' height='{c}' stroke='#334155'/>"
            s+=txt(ox+j*c+c/2,oy+i*c+c/2+5,v,col,15,'middle')
    s+=f"<rect x='{ox}' y='{oy}' width='{2*c}' height='{4*c}' stroke='#64748b'/>"
    # grupo ab=11 (fila i=2 completa)
    s+=f"<rect x='{ox-5}' y='{oy+2*c-5}' width='{2*c+10}' height='{c+10}' rx='14' stroke='#22d3ee' stroke-width='2'/>"
    s+=txt(ox+2*c+14,oy+2*c+c/2,'a·b','#22d3ee',13)
    s+=txt(ox,oy+4*c+30,'F = a·b','#e2e8f0',15)
    return s+"</svg>"

# ---------- Fig Ej7b: implementación simplificada (una AND) ----------
def fig_and_simple():
    s=svg_open('300 140',300)
    s+=txt(24,55,'a','#e2e8f0',16); s+=txt(24,95,'b','#e2e8f0',16)
    s+=g_and(110,35,60,70,'#22d3ee')
    s+=line(38,50,110,50); s+=line(38,90,110,90)
    s+=line(170,70,250,70); s+=txt(258,75,'F','#fbbf24',16)
    return s+"</svg>"

# ---------- Fig Ej8b: mapa de Karnaugh de S (4 variables) ----------
def fig_kmap_s():
    s=svg_open('430 390',430)
    ox,oy,c=95,64,66
    cols=['00','01','11','10']; rows=['00','01','11','10']
    s+=txt(ox+2*c,36,'CD','#94a3b8',13,'middle'); s+=txt(52,oy+2*c,'AB','#94a3b8',13,'middle')
    for j,cl in enumerate(cols): s+=txt(ox+j*c+c/2,56,cl,'#94a3b8',12,'middle')
    for i,rw in enumerate(rows): s+=txt(74,oy+i*c+c/2+4,rw,'#94a3b8',12,'middle')
    # S=1 en minterms 7,9,10,11,12,13,14,15  (orden AB filas 00,01,11,10; CD cols 00,01,11,10)
    def cell(m):
        A=(m>>3)&1;B=(m>>2)&1;C=(m>>1)&1;D=m&1
        ri={ (0,0):0,(0,1):1,(1,1):2,(1,0):3 }[(A,B)]
        cj={ (0,0):0,(0,1):1,(1,1):2,(1,0):3 }[(C,D)]
        return (ri,cj)
    ones={cell(m) for m in [7,9,10,11,12,13,14,15]}
    for i in range(4):
        for j in range(4):
            v='1' if (i,j) in ones else '0'
            col='#e2e8f0' if v=='1' else '#64748b'
            s+=f"<rect x='{ox+j*c}' y='{oy+i*c}' width='{c}' height='{c}' stroke='#334155'/>"
            s+=txt(ox+j*c+c/2,oy+i*c+c/2+5,v,col,15,'middle')
    s+=f"<rect x='{ox}' y='{oy}' width='{4*c}' height='{4*c}' stroke='#64748b'/>"
    s+=txt(ox,oy+4*c+30,'S = A·B + A·C + A·D + B·C·D','#e2e8f0',15)
    return s+"</svg>"

# ---------- Fig Ej5c: símbolos de compresor y manómetro ----------
def fig_neumatica_ce():
    s=svg_open('460 180',460)
    # compresor: círculo con triángulo relleno apuntando hacia dentro
    cx,cy=110,80
    s+=f"<circle cx='{cx}' cy='{cy}' r='40' stroke='#f59e0b'/>"
    s+=f"<path d='M{cx-16},{cy-16} L{cx-16},{cy+16} L{cx+18},{cy} Z' fill='#f59e0b' stroke='#f59e0b'/>"
    s+=line(cx,cy-40,cx,cy-58,'#cbd5e1')  # toma de aire
    s+=txt(cx,cy+64,'Compresor','#f59e0b',13,'middle')
    # manómetro: círculo con aguja
    mx,my=330,80
    s+=f"<circle cx='{mx}' cy='{my}' r='40' stroke='#22d3ee'/>"
    s+=line(mx,my,mx+22,my-22,'#e2e8f0')
    s+=f"<circle cx='{mx}' cy='{my}' r='4' fill='#e2e8f0'/>"
    s+=line(mx,my+40,mx,my+58,'#cbd5e1')  # conexión
    s+=txt(mx,my+64,'Manómetro','#22d3ee',13,'middle')
    return s+"</svg>"

# ---------- Fig Ej6c: unidad de mantenimiento (FRL) ----------
def fig_unidad_mant():
    s=svg_open('520 200',520)
    y0,y1=50,150
    # recuadro discontinuo de conjunto
    s+=f"<rect x='40' y='{y0-14}' width='440' height='{y1-y0+40}' rx='8' stroke='#64748b' stroke-dasharray='6 4'/>"
    # línea de aire
    s+=line(20,100,40,100,'#cbd5e1'); s+=line(480,100,500,100,'#cbd5e1')
    # filtro (rombo con V)
    fx=100
    s+=f"<path d='M{fx-26},{y0} L{fx+26},{y0} L{fx+26},{y1} L{fx-26},{y1} Z' stroke='#34d399'/>"
    s+=line(fx,y0,fx,y1,'#34d399')
    s+=f"<path d='M{fx-14},95 L{fx+14},95 L{fx},112 Z' stroke='#34d399'/>"
    s+=txt(fx,y1+22,'Filtro','#34d399',12,'middle')
    # regulador (rectángulo con flecha diagonal) + manómetro
    rx=260
    s+=f"<rect x='{rx-30}' y='{y0}' width='60' height='{y1-y0}' stroke='#a78bfa'/>"
    s+=f"<line x1='{rx-18}' y1='{y1-8}' x2='{rx+18}' y2='{y0+8}' stroke='#a78bfa' marker-end='url(#ar)'/>"
    s+=f"<circle cx='{rx}' cy='{y0-30}' r='14' stroke='#22d3ee'/>"; s+=line(rx,y0-16,rx,y0,'#22d3ee')
    s+=line(rx,y0-30,rx+8,y0-38,'#e2e8f0')
    s+=txt(rx,y1+22,'Regulador + manómetro','#a78bfa',12,'middle')
    # lubricador (rombo con gota)
    lx=420
    s+=f"<path d='M{lx-26},{y0} L{lx+26},{y0} L{lx+26},{y1} L{lx-26},{y1} Z' stroke='#fbbf24'/>"
    s+=line(lx,y0,lx,y1,'#fbbf24')
    s+=f"<path d='M{lx},92 q8,12 0,16 q-8,-4 0,-16z' fill='#fbbf24' stroke='#fbbf24'/>"
    s+=txt(lx,y1+22,'Lubricador','#fbbf24',12,'middle')
    return s+"</svg>"

# iconos de tarjeta
tj_mat="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#f59e0b' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='M20 60V28l14 20 14-20v32'/><path d='M60 60V28h10a8 8 0 0 1 0 16H60'/></svg>"
tj_ter="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#22d3ee' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><rect x='20' y='24' width='40' height='32' rx='3'/><path d='M60 40h18M30 62v6M50 62v6'/></svg>"
tj_flu="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#34d399' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='M50 16c14 18 20 30 20 40a20 20 0 0 1-40 0c0-10 6-22 20-40z'/></svg>"
tj_log="<svg viewBox='0 0 100 80' width='84' height='66' fill='none' stroke='#a78bfa' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='M24 26h20a16 16 0 0 1 0 28H24z'/><path d='M24 26q10 14 0 28'/><path d='M64 40h14M14 32h10M14 48h10'/></svg>"

data={"meta":{
  "titulo":"Tecnología e Ingeniería II",
  "subtitulo":"Andalucía, Ceuta, Melilla y centros en Marruecos · Curso 2023-2024 · Examen resuelto y comentado",
  "cabecera_titulo":"PEvAU 2024 · <span>Tecnología e Ingeniería II</span> · Andalucía · Titular (A)",
  "pill":"90 min · se eligen 4 de 8",
  "enunciado_pdf":"../../examens/Andalucia/Tecnologia_Andalucia_2024_ordinaria_titular-a.pdf",
  "pdf_dir":"pdf_and_2024_titular",
  "footer":"Dpto. Tecnología · Solucionario PEvAU 2024 · Andalucía · Tecnología e Ingeniería II (Titular A)",
  "intro_inicio":"De los <b>ocho ejercicios</b> propuestos el alumnado debe responder <b>cuatro</b>, elegidos libremente. Aquí se resuelven <b>todos</b> para repasar. Selecciona un ejercicio en la barra lateral."},
 "bloques":[]}

# ==================== Bloque 1 · Materiales ====================
data["bloques"].append({"id":"b1","titulo":"Ejercicios 1 y 2 · Materiales","color":"#f59e0b",
 "descripcion_tarjeta":"Ensayo de dureza Vickers y ensayo de tracción; propiedades y tratamientos térmicos.",
 "svg_tarjeta":tj_mat,"cuestiones":[
  {"id":"q1","titulo":"Ejercicio 1 · Ensayo de dureza Vickers","titulo_corto":"E1 Vickers",
   "etiqueta":"EJERCICIO 1","meta":"Materiales · 2,5 puntos (a:1 · b:1 · c:0,5)","menu":"E1 · Dureza Vickers",
   "enunciado_html":("<p>Una probeta de un determinado material se somete a un ensayo de dureza Vickers. Al aplicar al penetrador una carga de <b>120 kp</b> se produce una huella cuya diagonal es <b>0,773 mm</b>.</p>"
     "<ol type='a'><li>Obtener la dureza Vickers y su expresión normalizada. <span class='pts'>(1 punto)</span></li>"
     "<li>Determinar la carga, expresada en N, que se ha aplicado al penetrador si la diagonal de la huella es 0,1 mm. <span class='pts'>(1 punto)</span></li>"
     "<li>Definir las siguientes propiedades de los materiales: maleabilidad y ductilidad. <span class='pts'>(0,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Dureza Vickers: \\(HV=1{,}8544\\,\\dfrac{F}{d^2}\\), con \\(F\\) en kp y \\(d\\) (diagonal media) en mm.</li>"
     "<li>Para un mismo material la dureza es constante, de modo que de la misma expresión se despeja la carga: \\(F=\\dfrac{HV\\,d^2}{1{,}8544}\\).</li>"
     "<li>Conversión de unidades: \\(1\\ \\mathrm{kp}=9{,}81\\ \\mathrm N\\).</li></ul>"),
   "solucion_html":("<h5>a) Dureza Vickers y expresión normalizada</h5>"
     "<div class='formula'>$$HV=1{,}8544\\,\\frac{F}{d^2}=1{,}8544\\cdot\\frac{120}{0{,}773^2}=\\frac{222{,}53}{0{,}5975}=372{,}4$$</div>"
     "<div class='res'><b>Resultado:</b> \\(HV\\approx 372\\). Expresión normalizada: <b>372 HV 120</b> (dureza · símbolo · carga en kp).</div>"
     "<h5>b) Carga para una diagonal de 0,1 mm</h5>"
     "<p>El material es el mismo, así que conserva su dureza \\(HV=372{,}4\\). Despejando la carga:</p>"
     "<div class='formula'>$$F=\\frac{HV\\,d^2}{1{,}8544}=\\frac{372{,}4\\cdot 0{,}1^2}{1{,}8544}=\\frac{3{,}724}{1{,}8544}=2{,}008\\ \\mathrm{kp}$$</div>"
     "<div class='formula'>$$F=2{,}008\\times 9{,}81=19{,}7\\ \\mathrm N$$</div>"
     "<div class='res'><b>Resultado:</b> \\(F\\approx 19{,}7\\ \\mathrm N\\).</div>"
     "<h5>c) Maleabilidad y ductilidad</h5>"
     "<ul><li><b>Maleabilidad:</b> capacidad de un material para deformarse plásticamente en <b>láminas</b> u hojas delgadas sin romperse (p. ej. el oro o el aluminio).</li>"
     "<li><b>Ductilidad:</b> capacidad de un material para deformarse plásticamente en forma de <b>hilos</b> o alambres sin romperse (p. ej. el cobre).</li></ul>")
  },
  {"id":"q2","titulo":"Ejercicio 2 · Ensayo de tracción","titulo_corto":"E2 Tracción",
   "etiqueta":"EJERCICIO 2","meta":"Materiales · 2,5 puntos (a:1 · b:1 · c:0,5)","menu":"E2 · Ensayo de tracción",
   "enunciado_html":("<p>Se realiza un ensayo de tracción sobre una probeta normalizada de <b>100 mm</b> de longitud y <b>13,8 mm</b> de diámetro. Al aplicar una carga de <b>20000 N</b>, la longitud de la probeta aumenta hasta <b>105 mm</b>.</p>"
     "<ol type='a'><li>Calcular la tensión. <span class='pts'>(1 punto)</span></li>"
     "<li>Calcular el alargamiento y la deformación unitaria. <span class='pts'>(1 punto)</span></li>"
     "<li>Describir en qué consisten los tratamientos térmicos de los metales. Indicar dos ejemplos. <span class='pts'>(0,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Tensión normal: \\(\\sigma=\\dfrac{F}{A}\\), con sección \\(A=\\dfrac{\\pi}{4}D^2\\).</li>"
     "<li>Alargamiento: \\(\\Delta L=L_f-L_0\\); deformación unitaria: \\(\\varepsilon=\\dfrac{\\Delta L}{L_0}\\).</li></ul>"),
   "solucion_html":("<h5>a) Tensión</h5>"
     "<div class='formula'>$$A=\\frac{\\pi}{4}D^2=\\frac{\\pi}{4}(0{,}0138)^2=1{,}496\\times10^{-4}\\ \\mathrm{m^2}$$</div>"
     "<div class='formula'>$$\\sigma=\\frac{F}{A}=\\frac{20000}{1{,}496\\times10^{-4}}=1{,}337\\times10^{8}\\ \\mathrm{Pa}=133{,}7\\ \\mathrm{MPa}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(\\sigma\\approx 133{,}7\\ \\mathrm{MPa}\\).</div>"
     "<h5>b) Alargamiento y deformación unitaria</h5>"
     "<div class='formula'>$$\\Delta L=L_f-L_0=105-100=5\\ \\mathrm{mm}$$</div>"
     "<div class='formula'>$$\\varepsilon=\\frac{\\Delta L}{L_0}=\\frac{5}{100}=0{,}05\\ (5\\,\\%)$$</div>"
     "<div class='res'><b>Resultado:</b> \\(\\Delta L=5\\ \\mathrm{mm}\\) y \\(\\varepsilon=0{,}05\\).</div>"
     "<h5>c) Tratamientos térmicos</h5>"
     "<p>Los <b>tratamientos térmicos</b> son procesos de calentamiento y enfriamiento controlados a los que se somete un metal (sin variar su composición química) para modificar su <b>estructura interna</b> y, con ello, sus propiedades mecánicas (dureza, tenacidad, resistencia, mecanizabilidad). Dos ejemplos:</p>"
     "<ul><li><b>Temple:</b> calentamiento y enfriamiento rápido para aumentar la dureza y la resistencia.</li>"
     "<li><b>Recocido:</b> calentamiento y enfriamiento lento para ablandar el material y eliminar tensiones internas.</li></ul>"
     "<p>(También el revenido y el normalizado.)</p>")
  }
 ]})

# ==================== Bloque 2 · Máquinas y sistemas térmicos ====================
data["bloques"].append({"id":"b2","titulo":"Ejercicios 3 y 4 · Máquinas térmicas","color":"#22d3ee",
 "descripcion_tarjeta":"Bomba de calor y rendimiento térmico; motor Diésel de cuatro tiempos y ciclo frigorífico.",
 "svg_tarjeta":tj_ter,"cuestiones":[
  {"id":"q3","titulo":"Ejercicio 3 · Bomba de calor","titulo_corto":"E3 Bomba de calor",
   "etiqueta":"EJERCICIO 3","meta":"Termodinámica · 2,5 puntos (a:1 · b:1 · c:0,5)","menu":"E3 · Bomba de calor",
   "enunciado_html":("<p>La calefacción de un hotel en invierno funciona con un sistema con <b>bomba de calor</b>. La temperatura de las habitaciones se mantiene a <b>24 °C</b> mientras que en el exterior la temperatura es de <b>6 °C</b>. La eficiencia de la máquina es la <b>tercera parte de la ideal</b> y la máquina aporta al foco caliente <b>1500 J</b>.</p>"
     "<ol type='a'><li>Calcular la eficiencia real de la bomba de calor y el trabajo aplicado al sistema para su funcionamiento. <span class='pts'>(1 punto)</span></li>"
     "<li>Calcular la cantidad de calor que se extrae del foco frío. <span class='pts'>(1 punto)</span></li>"
     "<li>Definir el rendimiento térmico de un motor. Explicar razonadamente si puede ser superior a la unidad. <span class='pts'>(0,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Eficiencia ideal de una bomba de calor (Carnot): \\(COP_{id}=\\dfrac{T_c}{T_c-T_f}\\), con temperaturas en kelvin.</li>"
     "<li>Definición: \\(COP=\\dfrac{Q_c}{W}\\Rightarrow W=\\dfrac{Q_c}{COP}\\).</li>"
     "<li>Balance de energía: \\(Q_c=Q_f+W\\Rightarrow Q_f=Q_c-W\\).</li></ul>"),
   "solucion_html":("<h5>a) Eficiencia real y trabajo</h5>"
     "<p>Con \\(T_c=24+273=297\\ \\mathrm K\\) y \\(T_f=6+273=279\\ \\mathrm K\\):</p>"
     "<div class='formula'>$$COP_{id}=\\frac{T_c}{T_c-T_f}=\\frac{297}{297-279}=\\frac{297}{18}=16{,}5$$</div>"
     "<div class='formula'>$$COP_{real}=\\frac{1}{3}\\,COP_{id}=\\frac{16{,}5}{3}=5{,}5$$</div>"
     "<div class='formula'>$$W=\\frac{Q_c}{COP_{real}}=\\frac{1500}{5{,}5}=272{,}7\\ \\mathrm J$$</div>"
     "<div class='res'><b>Resultado:</b> \\(COP_{real}=5{,}5\\) y \\(W\\approx 272{,}7\\ \\mathrm J\\).</div>"
     "<h5>b) Calor extraído del foco frío</h5>"
     "<div class='formula'>$$Q_f=Q_c-W=1500-272{,}7=1227{,}3\\ \\mathrm J$$</div>"
     "<div class='res'><b>Resultado:</b> \\(Q_f\\approx 1227{,}3\\ \\mathrm J\\).</div>"
     "<h5>c) Rendimiento térmico de un motor</h5>"
     "<p>El <b>rendimiento térmico</b> de un motor es el cociente entre el trabajo útil obtenido y el calor absorbido del foco caliente: \\(\\eta=\\dfrac{W}{Q_c}\\). "
     "<b>No puede ser superior a la unidad</b>: por el segundo principio de la termodinámica siempre se cede una parte del calor al foco frío \\((Q_f>0)\\), de modo que \\(W=Q_c-Q_f<Q_c\\) y por tanto \\(\\eta<1\\). Un rendimiento igual a 1 exigiría \\(Q_f=0\\), lo que es imposible.</p>")
  },
  {"id":"q4","titulo":"Ejercicio 4 · Motor Diésel de cuatro tiempos","titulo_corto":"E4 Motor Diésel",
   "etiqueta":"EJERCICIO 4","meta":"Máquinas térmicas · 2,5 puntos (a:1 · b:1 · c:0,5)","menu":"E4 · Motor Diésel",
   "enunciado_html":("<p>De un motor <b>Diésel</b> de cuatro cilindros y cuatro tiempos se sabe que el diámetro de sus cilindros es <b>60 mm</b>, la carrera <b>90 mm</b> y la relación volumétrica de compresión <b>20:1</b>. El motor desarrolla un par de <b>53 N·m</b> para una potencia de <b>20 kW</b>.</p>"
     "<ol type='a'><li>Calcular el volumen de la cámara de combustión y la cilindrada del motor. <span class='pts'>(1 punto)</span></li>"
     "<li>Calcular el régimen de giro en rpm cuando desarrolla un par motor de 53 N·m. <span class='pts'>(1 punto)</span></li>"
     "<li>Representar el esquema de una máquina frigorífica indicando sus elementos fundamentales. <span class='pts'>(0,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Cilindrada unitaria (volumen desplazado por pistón): \\(V_d=\\dfrac{\\pi}{4}D^2\\,S\\); cilindrada total: \\(V_T=z\\,V_d\\).</li>"
     "<li>Relación de compresión: \\(r=\\dfrac{V_d+V_c}{V_c}\\Rightarrow V_c=\\dfrac{V_d}{r-1}\\).</li>"
     "<li>Potencia y par: \\(P=M\\,\\omega\\), con \\(\\omega=\\dfrac{2\\pi n}{60}\\) y \\(n\\) en rpm.</li></ul>"),
   "solucion_html":("<h5>a) Cámara de combustión y cilindrada</h5>"
     "<p>Cilindrada de cada cilindro (volumen desplazado):</p>"
     "<div class='formula'>$$V_d=\\frac{\\pi}{4}D^2 S=\\frac{\\pi}{4}(0{,}06)^2(0{,}09)=2{,}545\\times10^{-4}\\ \\mathrm{m^3}=254{,}5\\ \\mathrm{cm^3}$$</div>"
     "<p>De la relación de compresión \\(r=20\\):</p>"
     "<div class='formula'>$$V_c=\\frac{V_d}{r-1}=\\frac{254{,}5}{19}=13{,}4\\ \\mathrm{cm^3}$$</div>"
     "<p>Cilindrada total (4 cilindros):</p>"
     "<div class='formula'>$$V_T=z\\,V_d=4\\times254{,}5=1018\\ \\mathrm{cm^3}\\approx 1{,}02\\ \\mathrm L$$</div>"
     "<div class='res'><b>Resultado:</b> cámara de combustión \\(V_c\\approx 13{,}4\\ \\mathrm{cm^3}\\) por cilindro; cilindrada \\(V_T\\approx 1018\\ \\mathrm{cm^3}\\).</div>"
     "<h5>b) Régimen de giro</h5>"
     "<div class='formula'>$$\\omega=\\frac{P}{M}=\\frac{20000}{53}=377{,}4\\ \\mathrm{rad/s}$$</div>"
     "<div class='formula'>$$n=\\frac{60\\,\\omega}{2\\pi}=\\frac{60\\times377{,}4}{2\\pi}=3604\\ \\mathrm{rpm}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(n\\approx 3600\\ \\mathrm{rpm}\\).</div>"
     "<h5>c) Esquema de una máquina frigorífica</h5>"
     "<p>Sus elementos fundamentales son el <b>compresor</b> (aporta trabajo y comprime el refrigerante), el <b>condensador</b> (cede calor al foco caliente), la <b>válvula de expansión</b> (reduce la presión) y el <b>evaporador</b> (absorbe calor del foco frío).</p>"
     "<figure class='fig'>"+fig_frigorifica()+"<figcaption>Ciclo de una máquina frigorífica: compresor, condensador, válvula de expansión y evaporador.</figcaption></figure>")
  }
 ]})

# ==================== Bloque 3 · Neumática e hidráulica ====================
data["bloques"].append({"id":"b3","titulo":"Ejercicios 5 y 6 · Neumática e hidráulica","color":"#34d399",
 "descripcion_tarjeta":"Cilindro neumático de simple efecto con retorno por muelle y diseño hidráulico de una fuente (Bernoulli).",
 "svg_tarjeta":tj_flu,"cuestiones":[
  {"id":"q5","titulo":"Ejercicio 5 · Cilindro de simple efecto","titulo_corto":"E5 Neumática",
   "etiqueta":"EJERCICIO 5","meta":"Sistemas neumáticos · 2,5 puntos (a:1 · b:1 · c:0,5)","menu":"E5 · Cilindro de simple efecto",
   "enunciado_html":("<p>Un cilindro de simple efecto de retorno por muelle está conectado a una red de aire comprimido con <b>1 MPa</b> de presión. El diámetro del émbolo es <b>10 cm</b>, su carrera <b>3 cm</b> y la fuerza de rozamiento se puede considerar un <b>10 %</b> de la teórica.</p>"
     "<ol type='a'><li>¿Cuál será la fuerza ejercida por el vástago al comienzo del ciclo de trabajo si el muelle se encuentra en su longitud natural \\(L_0\\)? <span class='pts'>(1 punto)</span></li>"
     "<li>¿Cuál será la fuerza de rozamiento al comienzo del ciclo de trabajo? <span class='pts'>(1 punto)</span></li>"
     "<li>Dibujar el símbolo de los siguientes elementos neumáticos y comentar su función: compresor y manómetro. <span class='pts'>(0,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Fuerza teórica del émbolo: \\(F_{teo}=p\\,A\\), con \\(A=\\dfrac{\\pi}{4}D^2\\) y \\(p\\) la presión manométrica.</li>"
     "<li>Al comienzo, con el muelle en su longitud natural \\(L_0\\), la fuerza del muelle es nula \\((F_m=0)\\).</li>"
     "<li>Fuerza útil del vástago: \\(F=F_{teo}-F_{roz}-F_m\\).</li></ul>"),
   "solucion_html":("<h5>a) Fuerza del vástago al inicio del ciclo</h5>"
     "<div class='formula'>$$A=\\frac{\\pi}{4}D^2=\\frac{\\pi}{4}(0{,}1)^2=7{,}854\\times10^{-3}\\ \\mathrm{m^2}$$</div>"
     "<div class='formula'>$$F_{teo}=p\\,A=1\\times10^{6}\\times7{,}854\\times10^{-3}=7854\\ \\mathrm N$$</div>"
     "<p>Con el muelle en su longitud natural \\(F_m=0\\) y el rozamiento igual al 10 % de la teórica \\((785{,}4\\ \\mathrm N)\\):</p>"
     "<div class='formula'>$$F=F_{teo}-F_{roz}-F_m=7854-785{,}4-0=7068{,}6\\ \\mathrm N$$</div>"
     "<div class='res'><b>Resultado:</b> \\(F\\approx 7069\\ \\mathrm N\\approx 7{,}07\\ \\mathrm{kN}\\).</div>"
     "<h5>b) Fuerza de rozamiento</h5>"
     "<div class='formula'>$$F_{roz}=0{,}10\\,F_{teo}=0{,}10\\times7854=785{,}4\\ \\mathrm N$$</div>"
     "<div class='res'><b>Resultado:</b> \\(F_{roz}\\approx 785{,}4\\ \\mathrm N\\).</div>"
     "<h5>c) Símbolos neumáticos</h5>"
     "<figure class='fig'>"+fig_neumatica_ce()+"<figcaption>Símbolos normalizados: compresor y manómetro.</figcaption></figure>"
     "<ul><li><b>Compresor:</b> genera el aire comprimido, aumentando la presión del aire aspirado de la atmósfera y suministrándolo a la red.</li>"
     "<li><b>Manómetro:</b> instrumento de medida que indica la presión del aire en un punto de la instalación.</li></ul>")
  },
  {"id":"q6","titulo":"Ejercicio 6 · Fuente de agua (Bernoulli)","titulo_corto":"E6 Hidráulica",
   "etiqueta":"EJERCICIO 6","meta":"Mecánica de fluidos · 2,5 puntos (a:1 · b:1 · c:0,5)","menu":"E6 · Fuente de agua",
   "enunciado_html":("<p>Se desea diseñar una fuente de agua para un hotel, alimentada por una tubería cilíndrica de <b>15 cm</b> de diámetro situada horizontalmente a <b>8 m</b> bajo el nivel del suelo. Esta se conecta a otra tubería de <b>5 cm</b> de diámetro que se curva hacia arriba; el agua se expulsa por su extremo, situado a <b>1,75 m</b> por encima del suelo, con una velocidad de <b>12 m/s</b>.</p>"
     "<p><i>Dato: densidad del agua = 1000 kg/m³.</i></p>"
     "<ol type='a'><li>Calcular el caudal de agua cuando esté en funcionamiento. <span class='pts'>(1 punto)</span></li>"
     "<li>Calcular la presión manométrica necesaria en la tubería horizontal. <span class='pts'>(1 punto)</span></li>"
     "<li>Representar el símbolo de la unidad de mantenimiento en una instalación neumática y citar sus componentes. <span class='pts'>(0,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":fig_fuente(),
   "aplica_html":("<ul><li>Caudal: \\(Q=A_2\\,v_2\\), con \\(A_2=\\dfrac{\\pi}{4}D_2^2\\).</li>"
     "<li>Continuidad: \\(v_1=\\dfrac{Q}{A_1}\\).</li>"
     "<li>Ecuación de Bernoulli entre la tubería horizontal (1) y la salida (2): \\(p_1+\\tfrac12\\rho v_1^2+\\rho g z_1=p_2+\\tfrac12\\rho v_2^2+\\rho g z_2\\), con \\(p_2\\) atmosférica (manométrica nula).</li></ul>"),
   "solucion_html":("<h5>a) Caudal</h5>"
     "<div class='formula'>$$A_2=\\frac{\\pi}{4}(0{,}05)^2=1{,}963\\times10^{-3}\\ \\mathrm{m^2}$$</div>"
     "<div class='formula'>$$Q=A_2\\,v_2=1{,}963\\times10^{-3}\\times12=2{,}356\\times10^{-2}\\ \\mathrm{m^3/s}=23{,}56\\ \\mathrm{L/s}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(Q\\approx 23{,}6\\ \\mathrm{L/s}\\).</div>"
     "<h5>b) Presión manométrica en la tubería horizontal</h5>"
     "<p>Velocidad en la tubería de 15 cm por continuidad:</p>"
     "<div class='formula'>$$A_1=\\frac{\\pi}{4}(0{,}15)^2=1{,}767\\times10^{-2}\\ \\mathrm{m^2}\\qquad v_1=\\frac{Q}{A_1}=\\frac{0{,}02356}{0{,}01767}=1{,}33\\ \\mathrm{m/s}$$</div>"
     "<p>Diferencia de cotas: la salida está a +1,75 m y la tubería a −8 m, luego \\(z_2-z_1=1{,}75-(-8)=9{,}75\\ \\mathrm m\\). Despejando \\(p_1\\) manométrica \\((p_2=0)\\):</p>"
     "<div class='formula'>$$p_1=\\tfrac12\\rho\\,(v_2^2-v_1^2)+\\rho g\\,(z_2-z_1)$$</div>"
     "<div class='formula'>$$p_1=\\tfrac12\\cdot1000\\,(12^2-1{,}33^2)+1000\\cdot9{,}81\\cdot9{,}75=71\\,116+95\\,648=166\\,764\\ \\mathrm{Pa}$$</div>"
     "<div class='res'><b>Resultado:</b> \\(p_1\\approx 1{,}67\\times10^{5}\\ \\mathrm{Pa}\\approx 1{,}67\\ \\mathrm{bar}\\).</div>"
     "<h5>c) Unidad de mantenimiento</h5>"
     "<figure class='fig'>"+fig_unidad_mant()+"<figcaption>Unidad de mantenimiento (FRL): filtro, regulador con manómetro y lubricador.</figcaption></figure>"
     "<p>La <b>unidad de mantenimiento</b> acondiciona el aire comprimido antes de su uso. Sus componentes son: <b>filtro</b> (elimina impurezas y condensados), <b>regulador de presión</b> (con <b>manómetro</b>, fija y estabiliza la presión de trabajo) y <b>lubricador</b> (añade aceite para engrasar los elementos neumáticos).</p>")
  }
 ]})

# ==================== Bloque 4 · Electrónica digital ====================
data["bloques"].append({"id":"b4","titulo":"Ejercicios 7 y 8 · Sistemas electrónicos digitales","color":"#a78bfa",
 "descripcion_tarjeta":"Circuito lógico combinacional y forma canónica; diseño de un sistema de control de acceso con Karnaugh.",
 "svg_tarjeta":tj_log,"cuestiones":[
  {"id":"q7","titulo":"Ejercicio 7 · Circuito lógico combinacional","titulo_corto":"E7 Lógica",
   "etiqueta":"EJERCICIO 7","meta":"Electrónica digital · 2,5 puntos (a:1 · b:1 · c:0,5)","menu":"E7 · Circuito lógico",
   "enunciado_html":("<p>Dado el circuito lógico mostrado en la figura:</p>"
     "<figure class='fig'>"+fig_circuito()+"<figcaption>Circuito lógico combinacional con entradas a, b, c y salida F.</figcaption></figure>"
     "<ol type='a'><li>Obtener la tabla de verdad y expresar la función lógica F en su forma canónica. <span class='pts'>(1 punto)</span></li>"
     "<li>Simplificar la función F mediante el método de Karnaugh e implementarla con puertas lógicas. <span class='pts'>(1 punto)</span></li>"
     "<li>Determinar qué números binarios representan los decimales: 14, 27, 45, 28 y 36. <span class='pts'>(0,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Se recorre el circuito puerta a puerta: la AND superior da \\(a\\cdot b\\), la OR inferior da \\(b+c\\), y la AND final multiplica ambas: \\(F=(a\\cdot b)\\cdot(b+c)\\).</li>"
     "<li>La forma canónica (suma de productos) se obtiene con los minterms en que \\(F=1\\).</li>"
     "<li>Conversión decimal→binario por divisiones sucesivas entre 2.</li></ul>"),
   "solucion_html":("<h5>a) Tabla de verdad y forma canónica</h5>"
     "<p>La salida es \\(F=(a\\cdot b)\\cdot(b+c)\\). Operando: \\((a b)(b+c)=abb+abc=ab+abc=ab\\). Es decir, la función se reduce a \\(F=a\\cdot b\\):</p>"
     "<table class='dat'><tr><th>a</th><th>b</th><th>c</th><th>a·b</th><th>b+c</th><th>F</th></tr>"
     "<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
     "<tr><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>"
     "<tr><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
     "<tr><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>"
     "<tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
     "<tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>"
     "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
     "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>"
     "<p>F = 1 en los minterms 6 y 7. Forma canónica (suma de productos):</p>"
     "<div class='formula'>$$F=a\\,b\\,\\bar c+a\\,b\\,c=\\sum m(6,7)$$</div>"
     "<h5>b) Simplificación por Karnaugh e implementación</h5>"
     "<p>Los dos unos comparten \\(a=1,\\ b=1\\) (la variable \\(c\\) es indiferente). El grupo da:</p>"
     "<div class='formula'>$$F=a\\cdot b$$</div>"
     "<figure class='fig'>"+fig_kmap_f()+"<figcaption>Mapa de Karnaugh de F: un único grupo a·b.</figcaption></figure>"
     "<figure class='fig'>"+fig_and_simple()+"<figcaption>Implementación: una única puerta AND de dos entradas.</figcaption></figure>"
     "<div class='res'><b>Resultado:</b> \\(F=a\\cdot b\\); se implementa con una sola puerta AND de entradas a y b.</div>"
     "<h5>c) Conversión decimal → binario</h5>"
     "<table class='dat'><tr><th>Decimal</th><th>Binario</th></tr>"
     "<tr><td>14</td><td>1110</td></tr><tr><td>27</td><td>11011</td></tr>"
     "<tr><td>45</td><td>101101</td></tr><tr><td>28</td><td>11100</td></tr>"
     "<tr><td>36</td><td>100100</td></tr></table>")
  },
  {"id":"q8","titulo":"Ejercicio 8 · Sistema de apertura de una puerta","titulo_corto":"E8 Control acceso",
   "etiqueta":"EJERCICIO 8","meta":"Electrónica digital · 2,5 puntos (a:1 · b:1 · c:0,5)","menu":"E8 · Puerta de seguridad",
   "enunciado_html":("<p>El sistema de apertura de una puerta de seguridad <b>S</b> se regula con cuatro interruptores: <b>A</b> (cabina de control), <b>B</b> (entrada) y <b>C</b>, <b>D</b> (detrás de la puerta). La puerta se abre:</p>"
     "<ul><li>Cuando se activa el interruptor <b>A</b> y al menos uno de los restantes.</li>"
     "<li>Cuando, sin activar <b>A</b>, se activan simultáneamente los restantes (B, C y D).</li></ul>"
     "<ol type='a'><li>Obtener la tabla de verdad del sistema y la función de salida S. <span class='pts'>(1 punto)</span></li>"
     "<li>Simplificar la función S mediante Karnaugh e implementarla con puertas lógicas. <span class='pts'>(1 punto)</span></li>"
     "<li>Indicar el principio de funcionamiento y las aplicaciones principales de los sensores capacitivos. <span class='pts'>(0,5 puntos)</span></li></ol>"),
   "figura_enunciado_svg":"",
   "aplica_html":("<ul><li>Traducción del enunciado: \\(S=A\\,(B+C+D)+\\bar A\\,(B\\,C\\,D)\\).</li>"
     "<li>La tabla de verdad recorre las 16 combinaciones de A, B, C, D.</li>"
     "<li>Se agrupan los unos en el mapa de Karnaugh de 4 variables para simplificar.</li></ul>"),
   "solucion_html":("<h5>a) Tabla de verdad y función S</h5>"
     "<p>La puerta se abre si \\(A=1\\) y (B o C o D), o bien si \\(A=0\\) y B·C·D. Es decir \\(S=A(B+C+D)+\\bar A\\,BCD\\). S = 1 en los minterms 7, 9, 10, 11, 12, 13, 14 y 15:</p>"
     "<table class='dat'><tr><th>A</th><th>B</th><th>C</th><th>D</th><th>S</th></tr>"
     "<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
     "<tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>"
     "<tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr>"
     "<tr><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr>"
     "<tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>"
     "<tr><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>"
     "<tr><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr>"
     "<tr style='background:rgba(74,222,128,.14)'><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>"
     "<tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
     "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr>"
     "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>"
     "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>"
     "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr>"
     "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>"
     "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr>"
     "<tr style='background:rgba(74,222,128,.14)'><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>"
     "<h5>b) Simplificación por Karnaugh e implementación</h5>"
     "<p>Agrupando los unos se obtienen los grupos AB, AC, AD (todos con A=1) y el grupo BCD (que cubre además el minterm 7):</p>"
     "<div class='formula'>$$S=A\\,B+A\\,C+A\\,D+B\\,C\\,D=A\\,(B+C+D)+B\\,C\\,D$$</div>"
     "<figure class='fig'>"+fig_kmap_s()+"<figcaption>Mapa de Karnaugh de S (4 variables).</figcaption></figure>"
     "<div class='res'><b>Resultado:</b> \\(S=A(B+C+D)+B\\,C\\,D\\); se implementa con una OR de tres entradas (B+C+D) y una AND con A, una AND de tres entradas (B·C·D) y una OR final que une ambas ramas.</div>"
     "<h5>c) Sensores capacitivos</h5>"
     "<p>Un <b>sensor capacitivo</b> detecta la presencia de objetos sin contacto midiendo la <b>variación de capacidad</b> de un condensador: al acercarse un objeto (conductor o dieléctrico) cambia la constante dieléctrica del campo eléctrico del sensor, lo que altera su capacidad y hace conmutar la salida. "
     "A diferencia de los inductivos, detectan <b>tanto metales como no metales</b> (plásticos, líquidos, madera, vidrio). Aplicaciones: control de nivel de líquidos y sólidos en depósitos, detección de piezas no metálicas, conteo, y detección a través de paredes de envases.</p>")
  }
 ]})

out=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","and_2024_titular.json"))
with open(out,"w",encoding="utf-8") as f: json.dump(data,f,ensure_ascii=False,indent=1)
print("JSON escrito:",out)
