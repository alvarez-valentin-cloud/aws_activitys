import io
import boto3
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sqlalchemy import create_engine

# --- Configuración PostgreSQL Local (Ubuntu) ---
DB_USER = "postgres"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "etldb"

# --- Configuración AWS S3 ---
# REEMPLAZA ESTE VALOR con tu bucket real de AWS Academy
BUCKET_NAME = "aws-academy-datacenter-bucket-23-02-025"
S3_KEY = "processed/etl_output.parquet"

def pipeline_etl_completo():
    print("=== 1. FASE DE EXTRACCIÓN (PostgreSQL Local) ===")
    connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_string)

    query = "SELECT cliente, edad, monto_compras FROM clientes;"
    df_raw = pd.read_sql(query, con=engine)
    print("Datos extraídos exitosamente desde PostgreSQL:")
    print(df_raw)

    print("\n=== 2. FASE DE TRANSFORMACIÓN (Transform) ===")
    df_raw['categoria_edad'] = pd.cut(
        df_raw['edad'], 
        bins=[0, 25, 50, 100], 
        labels=['Joven', 'Adulto', 'Senior']
    )
    
    scaler = MinMaxScaler()
    df_raw['monto_normalizado'] = scaler.fit_transform(df_raw[['monto_compras']])
    df_raw['score_promocional'] = df_raw['monto_normalizado'] * 100
    
    print("Dataset Transformado:")
    print(df_raw)

    print("\n=== 3. FASE DE CARGA (AWS S3) ===")
    buffer = io.BytesIO()
    df_raw.to_parquet(buffer, index=False, engine='pyarrow')
    buffer.seek(0)

    s3_client = boto3.client('s3')
    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=S3_KEY,
        Body=buffer.getvalue()
    )
    print(f"-> Éxito: Archivo Parquet cargado correctamente en s3://{BUCKET_NAME}/{S3_KEY}")

if __name__ == "__main__":
    pipeline_etl_completo()
