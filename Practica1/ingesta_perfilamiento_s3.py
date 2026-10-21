import os
import io
import json
import pandas as pd
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

# 1. Configuración de cliente Boto3 para conexión con AWS S3
s3_client = boto3.client('s3', region_name='us-east-1')
BUCKET_NAME = 'aws-academy-datacenter-bucket'

def cargar_y_perfilar_s3(file_key, is_json=False):
    """
    Descarga archivos directamente a memoria (io.BytesIO) desde AWS S3 
    y genera un perfilamiento estadístico y de calidad de datos.
    """
    print(f"\n==================================================")
    print(f"=== Procesando Objeto S3: {file_key} ===")
    print(f"==================================================")

    try:
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_key)
        body = response['Body'].read()

        if is_json:
            data_json = json.loads(body.decode('utf-8'))
            df = pd.json_normalize(data_json)
        else:
            df = pd.read_csv(io.BytesIO(body))

        # Perfilamiento de Datos Extendido
        print(f"\n Dimensions: {df.shape[0]} filas x {df.shape[1]} columnas")
        
        print("\n Tipos de Datos e Identificación de Esquema:")
        print(df.dtypes)

        print("\n Conteo de Valores Nulos por Columna:")
        print(df.isnull().sum())

        print("\n Resumen de Estadísticos Descriptivos (Cuantitativos):")
        print(df.describe().T)

        return df

    except NoCredentialsError:
        print("\n [ERROR]: No se encontraron credenciales válidas de AWS Academy (~/.aws/credentials).")
        return None
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'NoSuchBucket':
            print(f"\n [ERROR]: El bucket '{BUCKET_NAME}' no existe.")
        elif error_code == 'NoSuchKey':
            print(f"\n [ERROR]: El archivo '{file_key}' no fue encontrado en S3.")
        else:
            print(f"\n [ERROR de AWS S3]: {e}")
        return None
    except Exception as e:
        print(f"\n [ERROR Inesperado]: {e}")
        return None

if __name__ == "__main__":
    # Ingesta en memoria y perfilamiento
    df_transacciones = cargar_y_perfilar_s3('raw/transacciones.csv')
    df_logs = cargar_y_perfilar_s3('raw/logs_m2m.json', is_json=True)
