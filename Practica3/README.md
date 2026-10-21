# Práctica 3: Implementación de Limpieza de Datos Avanzada en Python

## Objetivo
Identificar datos ruidosos o inconsistentes, reemplazar valores atípicos (outliers) identificados mediante el Rango Intercuartílico (**IQR**) con `NaN`, e imputar datos faltantes utilizando el algoritmo multivariado **KNNImputer** ($k=2, 3, 5$) en comparación con métodos tradicionales (Media y Mediana).

## Archivos
- `limpieza_knn_iqr.py`: Script principal de procesamiento, filtrado estadístico y experimentación.
- `figuras/boxplot_antes_despues.png`: Diagrama de caja comparativo generado automáticamente.
- `README.md`: Documentación técnica.

## Ejecución
```bash
python Practica3/limpieza_knn_iqr.py
