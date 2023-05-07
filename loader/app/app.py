import os
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential
import pandas as pd
from pymongo import MongoClient
from pymongo.errors import ConfigurationError, ServerSelectionTimeoutError

# Configura tus credenciales de Azure Blob Storage y MongoDB Atlas
account_url = 'DefaultEndpointsProtocol=https;AccountName=filesmanagerdbiip2;AccountKey=c4bVZdzevTHK/G5P7Gb/aLD4syQ/0kA8jAiB0/a3kvBU090dyMUMk9PL30Z85gK5fXd64bB+Qgoo+AStpiMqkA==;EndpointSuffix=core.windows.net'
mongo_connection_string = 'mongodb+srv://kendallguzmanramirez:banderocool0000@cluster0.vvtvtzo.mongodb.net/?retryWrites=true&w=majority'

# Configura la información de los archivos que deseas descargar
blob_container_name = 'documents'

def loadFiles(blob_file_names):
    # Crea una instancia del cliente de Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(account_url)
    blob_container_client = blob_service_client.get_container_client(blob_container_name)
    counter = 0
    # Descarga los archivos CSV de Blob Storage y los inserta en MongoDB Atlas
    for blob_file_name in blob_file_names:
        # Descarga el archivo CSV de Blob Storage
        blob_client = blob_container_client.get_blob_client(blob_file_name)
        with open(blob_file_name, 'wb') as f:
            f.write(blob_client.download_blob().readall())

        print(f'Downloaded {blob_file_name}')

        # Lee el archivo CSV con pandas en chunks
        chunk_size = 4000  # Número de filas por chunk
        for chunk in pd.read_csv(blob_file_name, chunksize=chunk_size):
            # Crea una instancia del cliente de MongoDB Atlas y accede a la base de datos y la colección que deseas usar
            mongo_client = MongoClient(mongo_connection_string, serverSelectionTimeoutMS=30000)
            try:
                mongo_client.server_info()  # Prueba la conexión
            except ConnectionError:
                print("No se pudo conectar a MongoDB Atlas")
                continue  # Continúa con el siguiente archivo

            mongo_db = mongo_client['dbii-p2']
            mongo_collection = mongo_db[blob_file_name]

            # Convierte el dataframe a una lista de diccionarios
            data = chunk.to_dict('records')

            # Inserta los documentos en la colección de MongoDB Atlas
            mongo_collection.insert_many(data)

            # Cierra la conexión con MongoDB Atlas
            mongo_client.close()

            print(f'Insertando {len(data)} documentos del chunk {counter}')
            counter += 1

        # Borra el archivo CSV descargado
        os.remove(blob_file_name)

        print(f'Deleted {blob_file_name}')


loadFiles(["artists-data.csv", "lyrics-data.csv"])
