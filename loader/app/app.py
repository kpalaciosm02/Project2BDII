import os
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential
import pandas as pd
from pymongo import MongoClient
from pymongo.errors import ConfigurationError, ServerSelectionTimeoutError
import io

# Configura tus credenciales de Azure Blob Storage y MongoDB Atlas
blob_container_name = 'documents'
lyrics_file_name='lyrics-data.csv'
artists_file_name='artists-data.csv'
def merge_data_frames(data_frame1, data_frame2):
    # Renombra la columna "Link" en df2 a "ALink"
    data_frame2 = data_frame2.rename(columns={"Link": "ALink"})
    
    # Combina los dos dataframes usando la columna "ALink" como clave
    merged_df = pd.merge(data_frame1, data_frame2, on="ALink", how="inner")
    
    return merged_df

try:
    # Crea una instancia del cliente de Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(os.environ['ACCOUNT_URL'])
    blob_container_client = blob_service_client.get_container_client(blob_container_name)

    # Descarga el archivo CSV de Blob Storage para las letras
    blob_client = blob_container_client.get_blob_client(lyrics_file_name)
    with open(lyrics_file_name, 'wb') as f:
        f.write(blob_client.download_blob().readall())

    print(f'Descargado {lyrics_file_name}')

    data_frame_Lyrics = pd.read_csv(lyrics_file_name)

    #Y para el archivo de artistas igual
    blob_client = blob_container_client.get_blob_client(artists_file_name)
    with open(artists_file_name, 'wb') as f:
        f.write(blob_client.download_blob().readall())

    print(f'Descargado {artists_file_name}')

    data_frame_Artists = pd.read_csv(artists_file_name)
    data_frame_Artists['Genres'] = data_frame_Artists['Genres'].apply(lambda x: x.split('; ') if isinstance(x, str) else [x])
    final_data_frame=merge_data_frames(data_frame_Lyrics,data_frame_Artists)
    # Leer la cadena como un objeto DataFrame
    # Lee el archivo CSV con pandas en chunks
    chunk_size = 25000  # Número de filas por chunk
    for i,chunk in final_data_frame.groupby(final_data_frame.index // chunk_size) :
        # Crea una instancia del cliente de MongoDB Atlas y accede a la base de datos y la colección que deseas usar
        mongo_client = MongoClient(os.environ['MONGO_CONNECTION_STRING'])
        mongo_db = mongo_client['song-lyrics-search']
        mongo_collection = mongo_db['Artists-Lyrics']

        # Convierte el dataframe a una lista de diccionarios
        data = chunk.to_dict('records')
        # Inserta los documentos en la colección de MongoDB Atlas
        mongo_collection.insert_many(data)

        # Cierra la conexión con MongoDB Atlas
        mongo_client.close()

        print(f'Insertados datos del chunk {i+1}')

except Exception as e:
    print(f'Se ha producido un error: {str(e)}')
    raise e

finally:
    if 'mongo_client' in locals() and mongo_client is not None:
        mongo_client.close()

    # Borra el archivo CSV descargado
    if os.path.exists(lyrics_file_name):
        os.remove(lyrics_file_name)
        print(f'Borrado {lyrics_file_name}')

    if os.path.exists(artists_file_name):
        os.remove(artists_file_name)
        print(f'Borrado {artists_file_name}')