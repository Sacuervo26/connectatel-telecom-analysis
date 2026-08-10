# ConnectaTel Telecom Analysis

Proyecto de análisis de datos para **ConnectaTel**, una empresa de telecomunicaciones con operaciones en México y Colombia. El objetivo es entender el comportamiento de los clientes según su uso de llamadas y mensajes, detectar valores atípicos y crear segmentos accionables para apoyar decisiones comerciales.

## Objetivo del proyecto

Analizar tres fuentes de datos de clientes, planes y uso real de servicios móviles para responder preguntas de negocio como:

- ¿Qué segmentos de clientes muestran mayor o menor uso de llamadas y mensajes?
- ¿Qué usuarios presentan comportamientos atípicos?
- ¿Cómo varía el uso según edad y plan contratado?
- ¿Qué oportunidades comerciales pueden ayudar a mejorar la oferta de planes y la retención?

## Datasets utilizados

El proyecto usa tres archivos CSV:

| Archivo | Descripción |
|---|---|
| `plans.csv` | Información de los planes, precio mensual, minutos, GB incluidos y costos extra. |
| `users_latam.csv` | Información de usuarios: edad, ciudad, fecha de registro, plan y fecha de cancelación. |
| `usage.csv` | Detalle de uso real: llamadas, mensajes, duración y longitud. |

> Los datasets originales pertenecen al entorno del curso. Para ejecutar el notebook localmente, coloca los archivos en `data/raw/` con los nombres exactos anteriores.

## Herramientas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Flujo de trabajo

1. Carga y exploración inicial de los datasets.
2. Revisión de estructura, tipos de datos y valores nulos.
3. Identificación de valores inválidos, sentinels y fechas fuera de rango.
4. Limpieza básica de datos.
5. Agregación del uso por usuario.
6. Estadísticas descriptivas por cliente.
7. Visualización de distribuciones.
8. Detección de outliers con boxplots e IQR.
9. Segmentación por edad y nivel de uso.
10. Conclusiones ejecutivas y recomendaciones de negocio.

## Principales hallazgos

- El dataset `plans` contiene 2 planes: Básico y Premium.
- El dataset `users` contiene 4000 usuarios y el dataset `usage` contiene 40000 registros de uso.
- En `users`, la columna `city` presentó valores faltantes y valores inconsistentes como `?`.
- En `age`, se detectó el sentinel `-999`, que fue reemplazado por la mediana.
- En `reg_date`, se encontraron 40 registros del año 2026, fuera del rango del proyecto, por lo que fueron marcados como fechas inválidas.
- En `usage`, los nulos en `duration` y `length` dependen del tipo de evento: llamadas o mensajes.
- La mayoría de usuarios pertenece al plan Básico.
- La mayoría de clientes se ubica en el segmento de uso medio.
- Los minutos de llamada presentan mayor dispersión y posibles usuarios de alto consumo.

## Segmentación creada

### Segmentación por uso

- **Bajo uso:** menos de 5 llamadas y menos de 5 mensajes.
- **Uso medio:** menos de 10 llamadas y menos de 10 mensajes.
- **Alto uso:** resto de casos.

### Segmentación por edad

- **Joven:** edad menor a 30 años.
- **Adulto:** edad menor a 60 años.
- **Adulto Mayor:** edad igual o mayor a 60 años.

## Recomendaciones de negocio

- Diseñar campañas diferenciadas para clientes de bajo, medio y alto uso.
- Ofrecer beneficios especiales o planes Premium a clientes de alto consumo.
- Revisar usuarios con minutos de llamada extremos para diferenciar clientes intensivos de posibles anomalías.
- Mantener los nulos de `churn_date` como posible indicador de clientes activos.
- Imputar o marcar ciudades faltantes como `Unknown` para no perder registros en análisis geográficos.
- Excluir o revisar fechas fuera de rango antes de realizar análisis temporales.

## Estructura del repositorio

```text
connectatel-telecom-analysis/
├── notebooks/
│   └── connectatel_analysis.ipynb
├── data/
│   └── raw/
│       └── README.md
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Cómo ejecutar el proyecto

1. Clona este repositorio o descarga los archivos.
2. Coloca los datasets en la carpeta `data/raw/`:
   - `plans.csv`
   - `users_latam.csv`
   - `usage.csv`
3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Abre el notebook:

```bash
jupyter notebook notebooks/connectatel_analysis.ipynb
```

5. Ejecuta las celdas en orden.

## Autor

Sebastián Cuervo
