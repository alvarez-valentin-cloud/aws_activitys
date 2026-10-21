# Práctica 1: Perfilamiento e Ingesta Multi-Fuente en AWS S3 con Python

## Descripción
Script de ingesta directa desde memoria (**sin guardar en disco local**) mediante el SDK de AWS (`boto3`) y `io.BytesIO`. Permite procesar datos estructurados (`.csv`) y semiestructurados (`.json`), realizando perfilamiento de esquema, detección de nulos y estadísticos descriptivos.

## Archivos
- `ingesta_perfilamiento_s3.py`: Script principal de conexión, descarga en memoria y perfilamiento.
- `README.md`: Documentación de la práctica.

## Ejecución
```bash
python Practica1/ingesta_perfilamiento_s3.py
