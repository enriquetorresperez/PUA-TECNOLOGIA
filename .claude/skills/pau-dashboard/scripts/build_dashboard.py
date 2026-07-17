#!/usr/bin/env python3
"""
Genera un dashboard HTML de examen PAU resuelto a partir de un JSON.

Uso:
    python3 build_dashboard.py examen.json salida.html

El JSON sigue el esquema de references/esquema_json.md.
El HTML resultante es autocontenido (KaTeX y fuentes por CDN) e imita el
dashboard de referencia: cabecera, barra lateral por bloques, tarjetas de
inicio, soluciones desplegables y botones "Ver PDF" que abren en pestaña nueva.
"""
import json
import os
import sys
import re

HERE = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(HERE, "..", "assets", "plantilla_estilos.css")

# Estilos añadidos para botón PDF y modo impresión (heredados del dashboard real)
EXTRA_CSS = """
.btn-pdf{text-decoration:none;display:inline-flex;align-items:center;gap:8px;background:transparent;color:var(--warn);
  border:1.5px solid var(--warn);font-family:'Sora',sans-serif;font-weight:700;font-size:.9rem;
  padding:12px 22px;border-radius:12px;cursor:pointer;margin:4px 0 20px 12px}
.btn-pdf:hover{background:rgba(251,191,36,.12)}
@media print{
  aside,.btn-sol,.btn-pdf,.nav-q,.crumb,.intro-exam,.cards{display:none!important}
}
"""

COLOR_SLOTS = ["--b1", "--b2", "--b3", "--b4", "--b5"]


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def build(data):
    meta = data.get("meta", {})
    bloques = data.get("bloques", [])

    css = open(CSS_PATH, encoding="utf-8").read() + EXTRA_CSS

    # Mapa de color por bloque -> clase c1..c5 / t1..t5 (para heredar los estilos de la plantilla)
    # Si el bloque trae color propio, lo inyectamos como variable inline en el punto.
    parts = []
    parts.append(f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta.get('cabecera_titulo','Examen resuelto')}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<style>{css}</style>
</head>
<body>""")

    # ---- HEADER ----
    pill = meta.get("pill", "")
    parts.append(f"""
<header>
  <svg class="logo" viewBox="0 0 48 48" fill="none" style="width:44px;height:44px;flex:none">
    <rect x="2" y="2" width="44" height="44" rx="10" fill="#16233f" stroke="#38bdf8" stroke-width="2"/>
    <path d="M14 30 L22 16 L27 25 L31 19 L36 30" stroke="#fbbf24" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="24" cy="36" r="2.4" fill="#38bdf8"/>
  </svg>
  <div>
    <h1>{meta.get('cabecera_titulo','Examen resuelto')}</h1>
    <div class="sub">{meta.get('subtitulo','')}</div>
  </div>
  {f'<div class="pill">{pill}</div>' if pill else ''}
</header>
<div class="wrap">""")

    # ---- SIDEBAR ----
    parts.append("""<aside>
  <button class="home-btn" onclick="go('home')">
    <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 10.5 12 3l9 7.5V21H3z"/></svg>
    Pantalla de inicio
  </button>""")
    for i, blk in enumerate(bloques):
        ci = (i % 5) + 1
        color = blk.get("color")
        dot = f'style="background:{color}"' if color else ""
        parts.append(f'<div class="blk c{ci}">')
        parts.append(f'<div class="bt"><span class="dot" {dot}></span> {blk.get("titulo","")}</div>')
        for q in blk.get("cuestiones", []):
            qid = q["id"]
            parts.append(f'<a class="q" href="#{qid}" onclick="go(\'{qid}\');return false;" id="l-{qid}">{q.get("menu", q.get("titulo",""))}</a>')
        parts.append("</div>")
    parts.append("</aside>")

    # ---- MAIN ----
    parts.append("<main>")

    # HOME
    enun_pdf = meta.get("enunciado_pdf", "")
    pdf_dir = meta.get("pdf_dir", "pdf").rstrip("/")
    sol_pdf = f"{pdf_dir}/soluciones_completas.pdf"
    home_links = []
    home_links.append(f'<a class="enlace-pdf" href="{sol_pdf}" target="_blank" rel="noopener" style="color:var(--warn)">📄 Ver examen completo resuelto (PDF)</a>')
    if enun_pdf:
        home_links.append(f'<a class="enlace-pdf" href="{enun_pdf}" target="_blank" rel="noopener">📄 Enunciado oficial (PDF)</a>')
    parts.append(f"""
<section class="view show" id="home">
  <div class="intro-exam">
    <h2>{meta.get('cabecera_titulo','Examen resuelto')}</h2>
    <p>{meta.get('intro_inicio','Selecciona un bloque o una cuestión en la barra lateral.')}</p>
    <div style="display:flex;gap:22px;flex-wrap:wrap;margin-top:10px">{''.join(home_links)}</div>
  </div>
  <div class="cards">""")
    for i, blk in enumerate(bloques):
        ci = (i % 5) + 1
        cls = {1: "h1", 2: "h2", 3: "h3x", 4: "h4", 5: "h5"}[ci]
        svg = blk.get("svg_tarjeta", "")
        qlinks = "".join(
            f'<a class="k{ci}" href="#{q["id"]}" onclick="go(\'{q["id"]}\');return false;">{q.get("titulo_corto", q["id"].upper())}</a>'
            for q in blk.get("cuestiones", [])
        )
        parts.append(f"""    <div class="card {cls}">
      <div class="ico">{svg}</div>
      <h3>{blk.get('titulo','')}</h3>
      <p>{blk.get('descripcion_tarjeta','')}</p>
      <div class="qlinks">{qlinks}</div>
    </div>""")
    parts.append("""  </div>
</section>""")

    # CUESTIONES
    flat = [(bi, q) for bi, blk in enumerate(bloques) for q in blk.get("cuestiones", [])]
    for idx, (bi, q) in enumerate(flat):
        ci = (bi % 5) + 1
        qid = q["id"]
        prev_id = flat[idx - 1][1]["id"] if idx > 0 else "home"
        next_id = flat[idx + 1][1]["id"] if idx < len(flat) - 1 else "home"
        prev_label = "← Inicio" if idx == 0 else "← Anterior"
        next_label = "Inicio →" if idx == len(flat) - 1 else "Siguiente →"

        fig = q.get("figura_enunciado_svg", "")
        fig_html = f'<figure class="fig">{fig}</figure>' if fig else ""
        pdf_name = q.get("pdf", f"{pdf_dir}/{qid}.pdf")
        enlace_enun = (f'<a class="enlace-pdf" href="{pdf_name}" target="_blank" rel="noopener">📄 Ver esta pregunta resuelta (PDF)</a>')

        parts.append(f"""
<section class="view" id="{qid}">
  <div class="crumb">Inicio / {q.get('etiqueta','')}</div>
  <div class="qtitle"><span class="tag t{ci}">{q.get('etiqueta','')}</span> {q.get('titulo','')}</div>
  <div class="qmeta">{q.get('meta','')}</div>

  <div class="box enun">
    <h4>📄 Enunciado</h4>
    {q.get('enunciado_html','')}
    {fig_html}
    {enlace_enun}
  </div>

  <div class="box aplica">
    <h4>💡 ¿Qué vamos a aplicar?</h4>
    {q.get('aplica_html','')}
  </div>

  <button class="btn-sol" onclick="tg(this,'s-{qid}')">▶ Ver solución detallada</button>
  <a class="btn-pdf" href="{pdf_name}" target="_blank" rel="noopener">📄 Ver PDF (pregunta + solución)</a>
  <div class="sol" id="s-{qid}">
    {q.get('solucion_html','')}
  </div>
  <div class="nav-q">
    <a href="#{prev_id}" onclick="go('{prev_id}');return false;">{prev_label}</a>
    <a href="#{next_id}" onclick="go('{next_id}');return false;">{next_label}</a>
  </div>
</section>""")

    parts.append("</main></div>")

    # FOOTER
    parts.append(f"""
<footer>
  <svg class="gear" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .34 1.87l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.7 1.7 0 0 0-1.87-.34 1.7 1.7 0 0 0-1 1.55V21a2 2 0 1 1-4 0v-.09a1.7 1.7 0 0 0-1-1.55 1.7 1.7 0 0 0-1.87.34l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.7 1.7 0 0 0 4.6 15a1.7 1.7 0 0 0-1.55-1H3a2 2 0 1 1 0-4h.09a1.7 1.7 0 0 0 1.55-1z"/></svg>
  <span><b>{meta.get('footer','')}</b></span>
</footer>""")

    # SCRIPT
    parts.append(r"""
<script>
function go(id){
  document.querySelectorAll('.view').forEach(function(v){v.classList.remove('show')});
  var t=document.getElementById(id); if(t){t.classList.add('show')}
  document.querySelectorAll('aside a.q').forEach(function(a){a.classList.remove('active')});
  var l=document.getElementById('l-'+id); if(l){l.classList.add('active')}
  window.scrollTo({top:0,behavior:'smooth'});
  if(history.replaceState){history.replaceState(null,'','#'+id)}
}
function tg(btn,id){
  var s=document.getElementById(id);
  var open=s.classList.toggle('open');
  btn.innerHTML=open?'▼ Ocultar solución':'▶ Ver solución detallada';
  if(open && window.renderMathInElement && !s.dataset.katex){
    renderMathInElement(s,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false,strict:false});
    s.dataset.katex='1';
  }
}
document.addEventListener('DOMContentLoaded',function(){
  var h=(location.hash||'').replace('#','');
  if(h && document.getElementById(h)){go(h)}
  var iv=setInterval(function(){
    if(window.renderMathInElement){
      clearInterval(iv);
      renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false,strict:false});
      document.querySelectorAll('.sol').forEach(function(x){x.dataset.katex='1'});
    }
  },200);
});
</script>
</body>
</html>""")

    return "\n".join(parts)


def main():
    if len(sys.argv) < 3:
        print("Uso: python3 build_dashboard.py examen.json salida.html", file=sys.stderr)
        sys.exit(1)
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    html = build(data)
    os.makedirs(os.path.dirname(os.path.abspath(sys.argv[2])), exist_ok=True)
    open(sys.argv[2], "w", encoding="utf-8").write(html)
    n = sum(len(b.get("cuestiones", [])) for b in data.get("bloques", []))
    print(f"Dashboard generado: {sys.argv[2]} ({len(data.get('bloques',[]))} bloques, {n} cuestiones)")


if __name__ == "__main__":
    main()
