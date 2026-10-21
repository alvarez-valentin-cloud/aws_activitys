# Práctica 4: Generación de Datos Sintéticos con Faker y División Stratified Train-Test

## Descripción
En este laboratorio se genera un dataset sintético estructurado de 1,000 registros de clientes adaptado a México (`es_MX`) utilizando la librería **Faker**. Posteriormente, se realiza una partición probabilística sin sesgo mediante **Stratified Train-Test Split** de `scikit-learn` para preservar exactamente la tasa del 20% de clase positiva (`churn`).

## Archivos de esta Carpeta
- `generar_datos_estratificados.py`: Script principal en Python que genera el dataset, aplica One-Hot Encoding y realiza la división estratificada.
- `dataset_sintetico_clientes.csv`: Dataset generado sintéticamente para análisis y auditoría.

## Instrucciones de Ejecución
1. Activar el entorno virtual e instalar dependencias:
   ```bash
   pip install -r ../requirements.txt
