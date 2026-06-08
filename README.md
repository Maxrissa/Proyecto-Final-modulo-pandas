# Proyecto Final — Análisis de Datos con Pandas
## Caso: Mundial FIFA 2026 — Estrategias de Marketing para una Marca de Snacks

**Instituto Nacional San Luis**  
**Módulo:** Limpieza, Transformación y Análisis de Datos con Pandas

---

## Descripción

Este proyecto implementa un proceso ETL completo utilizando Pandas sobre una encuesta
de mercado de 2,500 respuestas recolectadas en Guatemala, con el objetivo de generar
recomendaciones estratégicas para una marca de snacks durante el Mundial FIFA 2026.

## Estructura del Repositorio

```
Proyecto_Final/
├── data/
│   └── encuesta_snacks_mundial_2026_guatemala_2500_respuestas.csv
├── notebooks/
│   └── analisis_snacks_mundial_2026.ipynb
├── reports/
│   ├── dataset_limpio_transformado.csv
│   ├── ranking_snacks.csv
│   ├── ranking_jugadores.csv
│   └── kpis_resumen.csv
├── images/
│   ├── reporte_01_perfil_demografico.png
│   ├── reporte_02_frecuencia_consumo.png
│   ├── reporte_03_ranking_snacks.png
│   ├── reporte_04_analisis_precios.png
│   ├── reporte_05_selecciones_influencia.png
│   ├── reporte_06_jugadores_influencia.png
│   ├── reporte_07_tipo_publicidad.png
│   ├── reporte_08_promociones_preferidas.png
│   ├── reporte_09_intencion_compra_campania.png
│   └── reporte_10_dashboard_ejecutivo.png
├── README.md
└── requirements.txt
```

## Fases del Proyecto

| Fase | Descripción |
|------|-------------|
| 1 | Carga de datos desde CSV |
| 2 | Exploración inicial (shape, dtypes, nulos, duplicados) |
| 3 | Limpieza (duplicados, nulos, errores tipográficos) |
| 4 | Transformación (segmentos, categorías, variables derivadas) |
| 5 | Análisis y construcción de KPIs |
| 6 | Generación de 10 reportes visuales |
| 7 | Interpretación y respuestas a preguntas de negocio |
| 8 | Documentación y exportación de resultados |

## KPIs Principales

| KPI | Valor |
|-----|-------|
| Intención de compra positiva | 59.1% |
| Planea ver el Mundial 2026 | 87.9% |
| Acepta precio premium edición Mundial | 62.1% |
| Interés en tarjetas coleccionables | 61.7% |

## Recomendación Estratégica Final

- **Producto a promover:** Mundialitos Queso Picante + CrunchMax BBQ
- **Embajador:** Lionel Messi (863 menciones — #1 en influencia)
- **Selección:** Argentina (497 — mayor influencia en compra)
- **Promoción:** 2x1 + Tarjetas coleccionables
- **Precio ideal:** Q16 – Q20 por unidad
- **Canal:** Publicidad con jugador famoso + medios digitales

## Cómo Ejecutar

```bash
pip install -r requirements.txt
jupyter notebook notebooks/analisis_snacks_mundial_2026.ipynb
```

## Tecnologías Utilizadas

- Python 3.11
- pandas 2.x
- matplotlib 3.x
- numpy
- Jupyter Notebook
