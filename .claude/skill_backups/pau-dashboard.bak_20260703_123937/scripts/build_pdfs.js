/*
 * Genera un PDF por cuestión + un PDF con todas las soluciones, a partir del
 * dashboard HTML ya creado por build_dashboard.py.
 *
 * Uso:
 *   node build_pdfs.js <dashboard.html> <carpeta_salida_pdf/>
 *
 * Reglas incorporadas (aprendidas de iteraciones reales con usuarios):
 *  - El contenido empieza pegado a la cabecera (sin salto inicial que deje la
 *    primera página casi vacía).
 *  - Enunciado y solución van seguidos; solo figuras, tablas, fórmulas y
 *    recuadros de resultado no se parten entre páginas.
 *  - En el PDF completo, cada cuestión a partir de la 2ª empieza en página nueva.
 *  - Tema claro para imprimir; los diagramas SVG conservan su fondo oscuro.
 *  - Chromium se lanza con ignoreHTTPSErrors por si hay proxy corporativo.
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const SRC = process.argv[2];
const OUTDIR = process.argv[3] || './pdf/';
if (!SRC) { console.error('Uso: node build_pdfs.js <dashboard.html> <carpeta_salida/>'); process.exit(1); }
fs.mkdirSync(OUTDIR, { recursive: true });

const footer = `<div style="width:100%;font-size:8px;font-family:Helvetica,Arial;color:#334155;display:flex;justify-content:space-between;padding:0 11mm;"><span>{{FOOT}}</span><span>pág. <span class="pageNumber"></span>/<span class="totalPages"></span></span></div>`;

// CSS de impresión: tema claro, compacto, figuras con fondo oscuro conservado.
const printCss = `
:root{--bg:#fff;--bg2:#fff;--panel:#fff;--panel2:#eef2f7;--line:#c2ccdd;
      --txt:#0f172a;--mut:#475069;--acc:#075985;--ok:#166534;--warn:#92400e}
*{box-sizing:border-box}
body{background:#fff;color:#0f172a;font-family:'Inter',system-ui,sans-serif;margin:0;padding:0;line-height:1.34;font-size:11.2px}
.doc-head{border-bottom:2px solid #0f172a;padding:0 0 4px;margin-bottom:6px}
.doc-head h1{font-family:'Sora',sans-serif;font-size:14px;margin:0 0 2px}
.doc-head h1 span{color:#075985}
.doc-head .sub{font-size:9px;color:#475069}
.doc-head .pill{display:inline-block;margin-top:3px;font-family:'JetBrains Mono',monospace;font-size:8px;background:#0f172a;color:#fff;padding:2px 8px;border-radius:99px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.qtitle{font-size:16px;margin-bottom:2px}
.qmeta{font-size:9px;color:#475069;margin-bottom:7px}
.box{background:#fff;border:1px solid var(--line);border-radius:8px;padding:7px 11px;margin-bottom:6px}
.box h4{font-size:8.6px;text-transform:uppercase;letter-spacing:.08em;color:#475069;margin-bottom:4px}
.sol{display:block!important;border:1px solid var(--line)!important;background:#fff!important;border-radius:9px;padding:9px 13px;margin-bottom:6px}
.sol h5{color:#075985;border-bottom:1px dashed #c2ccdd;font-size:10.4px;margin:8px 0 3px;padding-bottom:3px}
.sol h5:first-child{margin-top:0}
.sol p,.enun p,.enun li,.sol li{font-size:10.5px;margin:3.5px 0}
.sol ul,.sol ol,.enun ol{margin:3.5px 0;padding-left:19px}
.res{background:#f0fdf4;border:1px solid #166534;border-left:4px solid #166534;border-radius:8px;padding:6px 13px;margin:6px 0;font-size:10.4px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.res b{color:#166534}
.pts{color:#92400e;font-size:8.8px;font-weight:600}
.formula{margin:2.5px 0;break-inside:avoid;overflow-x:auto}
.katex-display{margin:5px 0}
.fig{background:#0d1220!important;-webkit-print-color-adjust:exact;print-color-adjust:exact;break-inside:avoid;border-radius:10px;padding:7px;margin:6px 0;text-align:center}
.fig svg{max-width:72%!important;height:auto}
.fig figcaption{color:#8fa0bf;font-size:8px;margin-top:3px}
table.dat{border-collapse:collapse;width:100%;font-size:9.4px;margin:5px 0}
table.dat th,table.dat td{border:1px solid #c2ccdd;padding:4px 9px;text-align:center}
table.dat th{background:#eef2f7;font-size:8.4px}
.tag{-webkit-print-color-adjust:exact;print-color-adjust:exact;color:#fff!important;font-size:8.2px;font-weight:700;padding:2px 9px;border-radius:99px}
.enun .enlace-pdf,.nav-q,.crumb{display:none}
.fig,table.dat,.formula,.res{break-inside:avoid}
.box,.sol{break-inside:auto}
h5,.qtitle{break-after:avoid}
.q-break{break-before:page}
`;

const HEAD = (title, footHtml) => `<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<title>${title}</title><style>${printCss}</style></head><body>`;

(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ ignoreHTTPSErrors: true });
  const page = await ctx.newPage();
  await page.goto('file://' + path.resolve(SRC), { waitUntil: 'networkidle' });
  await page.waitForFunction(() => window.renderMathInElement, { timeout: 30000 });
  // abrir y renderizar TODAS las soluciones
  await page.evaluate(() => {
    document.querySelectorAll('.sol').forEach(s => s.classList.add('open'));
    renderMathInElement(document.body, {delimiters:[{left:'$$',right:'$$',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false,strict:false});
  });
  await page.waitForTimeout(1000);

  // extraer cabecera del documento + HTML renderizado de cada cuestión
  const info = await page.evaluate(() => {
    const h1 = document.querySelector('header h1');
    const sub = document.querySelector('header .sub');
    const pill = document.querySelector('header .pill');
    const foot = document.querySelector('footer span b') ? document.querySelector('footer span b').textContent : '';
    const dochead = `<div class="doc-head"><h1>${h1 ? h1.innerHTML : ''}</h1>`+
      `<div class="sub">${sub ? sub.textContent : ''}</div>`+
      `${pill ? '<span class="pill">'+pill.textContent+'</span>' : ''}</div>`;
    const secs = {};
    document.querySelectorAll('main section.view').forEach(sec => {
      if (sec.id === 'home') return;
      const c = sec.cloneNode(true);
      c.querySelectorAll('.nav-q,.btn-sol,.btn-pdf,.crumb,.enlace-pdf').forEach(e => e.remove());
      c.querySelectorAll('.sol').forEach(s => { s.classList.add('open'); s.style.display='block'; });
      secs[sec.id] = c.innerHTML;
    });
    return { dochead, foot, ids: Object.keys(secs), secs };
  });

  const foot = (info.foot || '').trim();
  const footHtml = footer.replace('{{FOOT}}', foot ? '<b>'+foot+'</b>' : '');
  const opts = { format:'A4', printBackground:true, displayHeaderFooter:true, headerTemplate:'<span></span>', footerTemplate:footHtml, margin:{top:'8mm',bottom:'12mm',left:'10mm',right:'10mm'} };

  // ---- un PDF por cuestión ----
  for (const id of info.ids) {
    const html = HEAD(id, foot) + info.dochead + `<div class="view">${info.secs[id]}</div></body></html>`;
    await page.setContent(html, { waitUntil: 'networkidle' });
    await page.waitForTimeout(250);
    await page.pdf({ path: path.join(OUTDIR, id + '.pdf'), ...opts });
    console.log('OK', id + '.pdf');
  }

  // ---- PDF completo ----
  let body = info.dochead;
  info.ids.forEach((id, i) => {
    body += `<div class="view ${i > 0 ? 'q-break' : ''}">${info.secs[id]}</div>`;
  });
  const full = HEAD('Soluciones completas', foot) + body + '</body></html>';
  await page.setContent(full, { waitUntil: 'networkidle' });
  await page.waitForTimeout(500);
  await page.pdf({ path: path.join(OUTDIR, 'soluciones_completas.pdf'), ...opts });
  console.log('OK soluciones_completas.pdf');

  await b.close();
})();
