# ConnectaTel: análisis de clientes y calidad de datos

Caso académico de telecomunicaciones para un portafolio de Python y análisis de datos. Explora calidad de datos, consumo de llamadas/mensajes y segmentación mediante reglas. **No acredita un encargo comercial ni resultados obtenidos para una empresa real.**

## Estado de reproducción

El código está disponible, pero **los CSV del curso no se distribuyen**. No se ha reejecutado el análisis completo con los datos originales. Las cifras y conclusiones conservadas en el notebook son históricas, no resultados verificados del código corregido. No deben citarse como métricas actuales.

La revisión corrige rutas locales, suma de minutos exclusivamente de llamadas, filtro de eventos de 2024 y clasificación de usuarios sin eventos. Las salidas antiguas se limpiaron porque estos cambios pueden alterar resultados.

## Pregunta de negocio

¿Cómo varía el uso observado de llamadas y mensajes, qué problemas de calidad afectan sus métricas y qué segmentos conviene investigar para diseñar ofertas?

El notebook incluye exploración, nulos y sentinels, fechas, perfiles por usuario, histogramas, IQR y segmentos por edad/uso. No incluye un modelo predictivo de abandono ni demuestra incremento de ventas o rentabilidad.

## Datos necesarios

Coloca archivos autorizados en `data/raw/`:

| Archivo | Columnas utilizadas |
|---|---|
| `plans.csv` | Se inspecciona la tabla de planes; no se calculan ingresos. |
| `users_latam.csv` | `user_id, age, city, plan, reg_date, churn_date` |
| `usage.csv` | `id, user_id, type, date, duration, length` |

`user_id` en usuarios e `id` en eventos deben ser únicos y no nulos. Los eventos deben pertenecer a un usuario y tener tipo `call` o `text`. La duración de llamadas debe ser numérica, no negativa y no nula. La unidad de minutos se asume del ejercicio: confírmala antes de usar otra fuente.

No publiques archivos de clientes ni materiales de curso sin derechos de redistribución. La licencia del código no concede derechos sobre los datasets.

## Ejecución

Recomendado: Python 3.11 o 3.12 y un entorno virtual.

```bash
git clone https://github.com/Sacuervo26/connectatel-telecom-analysis.git
cd connectatel-telecom-analysis
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
jupyter notebook notebooks/connectatel_analysis.ipynb
```

Ejecuta las celdas en orden desde un kernel limpio. Se resuelve la carpeta de datos desde la raíz o desde `notebooks/`. Para otra ubicación configura `CONNECTATEL_DATA_DIR` antes de iniciar Jupyter; por ejemplo en PowerShell:

```powershell
$env:CONNECTATEL_DATA_DIR = "C:\datos\connectatel"
```

El error de archivos faltantes muestra los nombres y la ruta que debes revisar. Instalar dependencias no descarga datos.

## Pruebas sin los datos del curso

```bash
python -m unittest discover -s tests -v
```

Las cuatro pruebas usan datos artificiales mínimos en memoria, nunca como resultados de negocio. Comprueban sintaxis de las celdas, mensaje por archivos faltantes, exclusión de mensajes del total de minutos, filtro de fechas, usuarios sin uso, edad faltante y rechazo de llamadas sin duración. Se verificaron con pandas 2.2.3 y NumPy 2.3.5. **No sustituyen una ejecución completa ni validan gráficos o conclusiones originales.**

## Decisiones y límites

- Perfil anual: solo eventos con fecha válida de 2024. Se reporta el número excluido.
- Sin eventos observados se asigna cero uso; esto no prueba inactividad real.
- Sentinel de edad `-999`: mediana según la regla del ejercicio. La imputación puede sesgar segmentos; edad ausente residual se clasifica como `Sin dato`.
- Uso bajo: llamadas < 5 y mensajes < 5; medio: ambos < 10; alto: resto. Son reglas exploratorias, no umbrales comerciales validados.
- Los nulos que no aplican al tipo de evento son estructurales; una tabla cruzada no demuestra por sí sola MAR.
- Una fecha de cancelación vacía no confirma cliente activo sin validar la fuente.
- Las recomendaciones son hipótesis por contrastar, no efectos medidos.

## Próximo paso

Recuperar datos autorizados, ejecutar desde cero y actualizar cifras, gráficos y conclusiones. No es necesario ni está autorizado redistribuir los datos originales para hacer esa validación.

**Autor:** Sebastián Cuervo
