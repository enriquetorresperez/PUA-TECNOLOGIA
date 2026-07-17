# Detección de metadatos

## Extraer texto de las primeras páginas
```bash
python -c "from pypdf import PdfReader; print(PdfReader('archivo.pdf').pages[0].extract_text()[:1500])"
```
Si no hay texto → PDF escaneado: deducir de la URL/nombre y confirmar con el usuario.

## Convocatoria
- `ord` (ordinaria): junio, "ordinaria", "convocatoria ordinaria".
- `extr` (extraordinaria): julio, "extraordinaria", "julio", "septiembre" (antiguas).
- Coincidentes UAH: suelen ser modelos específicos; preguntar si el usuario quiere marcarlas `ord`/`extr`.

## Año
- Buscar el año académico en la portada. Si aparece "2025/2026", usar el año de la convocatoria (normalmente el segundo: 2026).

## Nomenclatura normalizada de asignaturas
Usar minúsculas, sin tildes ni espacios:

| Asignatura oficial | slug |
|---|---|
| Física | fisica |
| Química | quimica |
| Matemáticas II | matematicasii |
| Matemáticas Aplicadas a las CCSS II | matematicasccss |
| Historia de España | historia |
| Historia de la Filosofía | filosofia |
| Lengua Castellana y Literatura II | lengua |
| Biología | biologia |
| Geología | geologia |
| Dibujo Técnico II | dibujotecnico |
| Tecnología e Ingeniería II | tecnologiaeingenieriaii |
| Economía / Empresa | economia |
| Inglés | ingles |
| Latín II | latin |
| Griego II | griego |

Si aparece una asignatura no listada, generar el slug con la misma regla (minúsculas, sin tildes ni espacios) y confirmar con el usuario.
