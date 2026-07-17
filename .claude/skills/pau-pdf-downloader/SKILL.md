---
name: pau-pdf-downloader
description: Busca, descarga y organiza exámenes PAU/EvAU/PCE en PDF de diferentes universidades españolas (UAH, UCM, UPM, UNED, universidades de Castilla-La Mancha, etc.). Úsala siempre que el usuario quiera localizar exámenes de selectividad en la web de una universidad, descargar un PDF de examen desde una URL concreta, u organizar exámenes PAU en su carpeta local. Actívala con frases como "descárgame el examen de física de la UAH", "busca los exámenes PAU de tal universidad", "guarda este PDF de examen", "quiero los modelos de PAU 2026 de Madrid", aunque no diga literalmente "skill" ni "descargar". El resultado es un PDF renombrado con el formato Universidad_asignatura_ord/extr_año.pdf guardado en ~/Downloads/PAU, más un resumen de metadatos (asignatura, fecha, universidad, convocatoria).
---

# PAU PDF Downloader

Skill para localizar, descargar, renombrar y catalogar exámenes de PAU / EvAU / PCE de universidades españolas.

## Configuración fija del usuario

- **Carpeta destino:** `~/Downloads/PAU` (crearla si no existe)
- **Formato de nombre:** `Universidad_asignatura_convocatoria_año.pdf`
  - `Universidad`: sigla o nombre corto (UAH, UCM, UPM, UNED, UCLM…)
  - `asignatura`: en minúsculas, sin tildes ni espacios (fisica, matematicasii, historia, tecnologiaeingenieriaii…)
  - `convocatoria`: `ord` (ordinaria/junio) o `extr` (extraordinaria/julio)
  - `año`: cuatro dígitos
  - Ejemplos: `UAH_fisica_ord_2026.pdf`, `UCM_historia_extr_2025.pdf`
- **Resumen entregado:** solo metadatos → asignatura, fecha/convocatoria, universidad. Nada de análisis del contenido del examen.

## Flujo de trabajo

### Caso A — El usuario da una URL directa a un PDF

1. Verificar que la URL apunta a un PDF (termina en `.pdf` o el `Content-Type` es `application/pdf`).
2. Descargar con el script `scripts/download_pau.py` (usa `curl`/`requests`, no requiere navegador).
3. Extraer metadatos (universidad, asignatura, convocatoria, año) desde la URL, el nombre original y las primeras páginas del PDF.
4. Renombrar según el formato fijo y mover a `~/Downloads/PAU`.
5. Devolver el resumen de metadatos.

### Caso B — El usuario pide "buscar" exámenes de una universidad

1. Usar `web_search` para localizar la página oficial de exámenes/modelos PAU de esa universidad. Consultar `references/fuentes-universidades.md` primero: contiene URLs conocidas de las principales universidades.
2. Con `web_fetch`, entrar en la página de la universidad y listar los enlaces a PDFs disponibles.
3. Mostrar al usuario la lista encontrada (asignatura + convocatoria + año) y **preguntar cuáles quiere descargar** antes de bajar nada.
4. Para cada PDF confirmado, seguir el Caso A.

> Descargar archivos requiere confirmación del usuario. Nunca bajes en lote sin que el usuario elija explícitamente qué exámenes quiere.

## Script de descarga

`scripts/download_pau.py` acepta:

```bash
python scripts/download_pau.py \
  --url "https://.../examen.pdf" \
  --universidad UAH \
  --asignatura fisica \
  --convocatoria ord \
  --anio 2026 \
  --dest ~/Downloads/PAU
```

Descarga el PDF, lo guarda con el nombre `Universidad_asignatura_convocatoria_año.pdf` en `--dest`, evita sobrescribir (añade sufijo `_v2`, `_v3`… si ya existe) e imprime la ruta final y los metadatos básicos (número de páginas, tamaño).

Si algún dato de metadatos no se conoce con certeza, **pregunta al usuario** en vez de inventarlo.

### Sitios protegidos por WAF (error 403)

Algunas universidades (p. ej. **UCLM**) bloquean la descarga automática con `curl`/`requests`, incluso con cabeceras de navegador. Si `download_pau.py` devuelve **ERROR 403**, usar la variante con navegador real:

```bash
python scripts/download_pau_browser.py --url "..." --universidad UCLM \
  --asignatura fisica --convocatoria ord --anio 2025 --dest ~/Downloads/PAU
```

Requiere una vez: `pip3 install playwright && playwright install chromium`.

Si tampoco funciona (WAF muy agresivo o descarga tras clic), pide al usuario que baje el PDF a mano y te pase la ruta local; entonces solo renombras (`mv`) y extraes metadatos, saltándote la descarga.

## Extracción de metadatos

Tras descargar, para confirmar universidad/asignatura/convocatoria/año, leer las 1-2 primeras páginas del PDF (ver `references/metadatos.md` para pistas de reconocimiento y comandos de extracción de texto). Si el PDF es escaneado (sin texto), deducir de la URL y el nombre original, y confirmar con el usuario.

## Referencias

- `references/fuentes-universidades.md` — URLs conocidas de páginas de exámenes PAU por universidad.
- `references/metadatos.md` — Cómo detectar asignatura, convocatoria y año; nomenclatura normalizada de asignaturas.
