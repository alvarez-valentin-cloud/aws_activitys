# Práctica 2: Generación y Estructuración de un Esquema Estrella en PostgreSQL (EC2) / Pandas

## Objetivo
Diseñar y estructurar un modelo multidimensional (**Star Schema**) en Python con `pandas` para transformar datos transaccionales operacionales (OLTP) en un Data Warehouse (OLAP), generando llaves subrogadas (*Surrogate Keys*), atributos temporales extendidos (`dia_semana`, `es_fin_semana`) y métricas financieras (`monto_bruto`, `impuesto_iva`, `monto_neto`).

## Estructura del Proyecto
- `esquema_estrella_etl.py`: Script ETL en Python de separación dimensional, construcción de surrogate keys y merges.
- `schema.sql`: Script DDL para la creación de tablas en PostgreSQL en AWS EC2.
- `datos/`: Archivos CSV exportados con las dimensiones (`dim_cliente.csv`, `dim_producto.csv`, `dim_tiempo.csv`) y la tabla de hechos (`fact_ventas.csv`).
- `README.md`: Documentación de la práctica.

## Ejecución
```bash
python Practica2/esquema_estrella_etl.py
