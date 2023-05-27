# Documentación escrita
Evaluación: Proyecto II
Curso: Bases de datos II
Estudiantes: 
 Kendall Fabián Guzmán Ramírez - 2019076561
 Kenneth Palacios Molina - 2020035407
 Iván Solís Ávila - 2018209698
 Jose Pablo Quesada R. - 2020211670
 Carlos Eduardo Leiva Medaglia - 2021032973

## Explicación Loader
A continuación se proporciona una explicación paso a paso del código:
1.  Importación de bibliotecas: Se importan las bibliotecas necesarias para el funcionamiento del código, incluyendo `os`, `BlobServiceClient` y `DefaultAzureCredential` de Azure Blob Storage, `pandas`, `MongoClient` y `ConfigurationError`, `ServerSelectionTimeoutError` de MongoDB, e `io`.
    
2.  Configuración de credenciales: Se establece el nombre del contenedor de Blob Storage en la variable `blob_container_name`, el nombre del archivo de letras en `lyrics_file_name` y el nombre del archivo de artistas en `artists_file_name`. Estas variables se utilizarán más adelante en el código.
    
3.  Definición de la función `merge_data_frames`: Esta función toma dos dataframes como entrada y realiza una combinación interna basada en la columna "ALink". Renombra la columna "Link" del segundo dataframe a "ALink" y luego realiza la combinación. El resultado es el dataframe combinado.
    
4.  Bloque `try-except-finally`: Este bloque se utiliza para controlar los posibles errores y realizar operaciones específicas en caso de éxito o fallo.
    
a. Carga de los datos de Blob Storage: Se crea una instancia del cliente de Blob Storage utilizando la cadena de conexión almacenada en la variable de entorno `ACCOUNT_URL`. Luego, se obtiene el cliente del contenedor y se descarga el archivo CSV de letras mediante `blob_client`. El archivo se guarda localmente con el mismo nombre. A continuación, se muestra un mensaje indicando que el archivo ha sido descargado. Se repite el mismo proceso para el archivo de artistas.
    
b. Lectura de los datos en dataframes: Se utilizan las funciones `pd.read_csv` para leer los archivos CSV descargados y almacenar los datos en los dataframes `data_frame_Lyrics` y `data_frame_Artists`.
    
c. Manipulación de datos: La columna "Genres" del dataframe `data_frame_Artists` se procesa mediante la función `apply` y se divide en una lista de géneros separados por "; " si la columna es una cadena. Esto se hace para normalizar los datos antes de combinarlos con el dataframe `data_frame_Lyrics`.
    
d. Combinación de dataframes: Se llama a la función `merge_data_frames` pasando `data_frame_Lyrics` y `data_frame_Artists` como argumentos. El resultado se almacena en el dataframe `final_data_frame`, que contiene los datos combinados de letras y artistas.
    
e. Procesamiento por chunks y carga en MongoDB Atlas: El dataframe `final_data_frame` se divide en chunks de tamaño `chunk_size` utilizando el método `groupby` y se itera sobre cada chunk. Dentro del bucle, se crea una instancia del cliente de MongoDB Atlas utilizando la cadena de conexión almacenada en la variable de entorno `MONGO_CONNECTION_STRING`. Luego, se accede a la base de datos y a la colección especificada. El chunk se convierte en una lista de diccionarios mediante el método `to_dict('records')` y se inserta en la colección de MongoDB Atlas utilizando `insert_many`. Una vez completada la inserción, se cierra la conexión con MongoDB Atlas. Se imprime un mensaje indicando el número del chunk insertado.
    
f. Manejo de errores: Si se produce alguna excepción durante el proceso, se captura y se imprime un mensaje de error. La excepción se vuelve a lanzar para que pueda ser manejada en un nivel superior si es necesario.
    
g. Bloque `finally`: En este bloque, se realizan algunas acciones finales. Si se creó una instancia del cliente de MongoDB (`mongo_client`) y no es `None`, se cierra la conexión. Además, se comprueba si los archivos CSV descargados existen en el sistema y, de ser así, se eliminan.
## Creación de índices
El full text searchSi usted se mete a mongo filter search va a  ver como se crea la estructura entonces en el pipeline usted va a ver search, después index, después query type, hay dos tipos de query type, text y phrase, text es para que el mae busque coincidencias por palabra y phrase busca exactamente lo que usted manda, database collection index name, constantes que siempre van a estar, el path es a que tabla o a que columna lo va a revisar, por ejemplo entre paréntesis uno lo puede ingresar que busque en artist_name y en lyrics, con phrase el busca exactamente lo que uno ingrese con text se busca cada una de las palabras que se muestre en el query y se encuentran coincidencias por ejemplo de bandas que tienen un "eye" o un "of" o un "tiger" en la busqueda de "eye of the tiger"
Para los filtros se debe usar compound con must, must not,, en este proyecto solo se uso must, para incluir y excluir elementos de las busquedas, 







Un índice de búsqueda de texto completo (Full Text Search) en MongoDB Atlas es una característica poderosa que permite realizar búsquedas avanzadas de texto dentro de los documentos almacenados en una base de datos MongoDB. Aquí tienes una descripción detallada de cómo funciona y cómo se puede utilizar.
Para utilizar Full Text Search en MongoDB Atlas, primero se debe asegurar que se está utilizando una versión de MongoDB igual o superior a la versión 4.0.
Se debe tener una cuenta de MongoDB Atlas y un clúster configurado en la nube.
2.  Creación de un índice de búsqueda de texto completo:
- Para habilitar el índice de búsqueda de texto completo en una colección, se debe crear un índice de texto en uno o más campos de esa colección. Se puede hacer utilizando el comando `song-lyrics-search.Artists-Lyrics.createIndex()` en la consola de MongoDB o a través de una interfaz gráfica como MongoDB Compass.
  -   Por ejemplo, para crear un índice de texto en el campo "ALink" de la colección  "Artists-Lyrics",  se puede ejecutar el siguiente comando en la consola de MongoDB:
               
        `song-lyrics-search.Artists-Lyrics.createIndex({ ALink: "eye of the tiger" })` 
        
 Hay dos tipos de consulta: "text" y "phrase".

-   "text" se utiliza cuando se desea buscar coincidencias por palabra clave. Por ejemplo, si se busca la frase "eye of the tiger", se realizará una búsqueda de cada una de las palabras individuales ("eye", "of", "the", "tiger") y se encontrarán coincidencias en las bandas que contengan alguna de esas palabras.
    
-   "phrase" se utiliza cuando se desea buscar una frase exacta. En este caso, la búsqueda se realiza exactamente como se ingresa, sin dividir las palabras en términos individuales. Por ejemplo, si se busca la frase "eye of the tiger", se encontrará una coincidencia solo si hay una banda que tenga esa frase exacta en los campos indexados.    

Una vez creado el índice, MongoDB comenzará a indexar los términos de texto en el campo especificado.
4.  Realización de consultas de búsqueda de texto completo:
    
  -   Para realizar una búsqueda de texto completo, puedes utilizar el operador `$text` en combinación con el operador `$search`. Puedes realizar consultas en la consola de MongoDB o mediante el uso de un controlador de MongoDB en tu lenguaje de programación preferido.
    -   Por ejemplo, para buscar documentos que contengan la palabra "ejemplo", puedes ejecutar el siguiente comando en la consola de MongoDB:
        

        `lyrics-search.Artists-Lyrics.find({ $text: { $search: "eye of the tiger" } })` 
        
    -   MongoDB buscará en el campo indexando los documentos que contengan la palabra "ejemplo" y devolverá los resultados según su relevancia.
5.  Opciones de consulta adicionales:
    
  -   Se puede ajustar la relevancia de los resultados utilizando la opción `score` en la proyección de la consulta. Por ejemplo:

        `lyrics-search.Artists-Lyrics.find(
          { $text: { $search: "eye of the tiger" } },
          { score: { $meta: "textScore" } }
        ).sort({ score: { $meta: "textScore" } })` 
        
    -   También puedes realizar búsquedas más avanzadas utilizando operadores de texto como `$language`, `$caseSensitive`, `$diacriticSensitive`, entre otros. Estos operadores permiten controlar aspectos como el idioma de la búsqueda, la sensibilidad a mayúsculas y minúsculas, y la sensibilidad a los diacríticos.
## 	Explicación API
En primer lugar, se importan las bibliotecas necesarias, como `os` para acceder a variables de entorno, `flask` para crear la aplicación web, `pymongo` para interactuar con MongoDB, `json` para trabajar con datos en formato JSON, `bson` para manejar los ObjectId de MongoDB y `flask_cors` para habilitar CORS (Cross-Origin Resource Sharing) en la aplicación.

A continuación, se define una clase `JSONEncoder` que extiende `json.JSONEncoder` y se utiliza para serializar objetos de tipo `ObjectId` de MongoDB como cadenas.

La función `verify_connection_to_mongo` se encarga de verificar la conexión con MongoDB. Obtiene la cadena de conexión de la variable de entorno `CONNECTION_STRING`, crea un cliente `MongoClient` utilizando la API estable "1" y envía un ping al servidor para confirmar una conexión exitosa.

La función `mongo_search` realiza una búsqueda en la base de datos MongoDB. Recibe como parámetros una consulta `query`, una ruta `path` en la estructura de datos de MongoDB, un límite `limit` para el número de resultados y un tipo de consulta `query_type`. Utiliza el cliente `MongoClient` para conectarse a la base de datos, construye una tubería de agregación para realizar la búsqueda utilizando el operador `$search` de MongoDB, y limita la cantidad de resultados utilizando el operador `$limit`. Luego, serializa los resultados en formato JSON y cierra la conexión con la base de datos.

La función `mongo_filter_search` realiza una búsqueda filtrada en la base de datos MongoDB. Recibe como parámetros una lista de rutas `paths`, una lista de consultas `queries`, un límite `limit` y un tipo de consulta `query_type`. Verifica que las listas de rutas y consultas tengan la misma longitud y luego realiza una búsqueda utilizando el operador `$search` de MongoDB junto con el operador `$must` para combinar las consultas en una búsqueda compuesta. Al igual que en `mongo_search`, se limita la cantidad de resultados y se serializan en formato JSON.

Las rutas de la aplicación Flask están definidas para manejar las solicitudes HTTP. La ruta "/mongo/connection" responde a una solicitud GET y verifica la conexión con MongoDB. La ruta "/mongo/search" responde a una solicitud POST y realiza una búsqueda simple en la base de datos utilizando los parámetros proporcionados en formato JSON. La ruta "/mongo/search/filters" responde a una solicitud POST y realiza una búsqueda filtrada utilizando los parámetros proporcionados en formato JSON.

Finalmente, se configura la aplicación Flask y se inicia el servidor si el script se ejecuta directamente.

## Node JS App

Para el desarrollo de la página web solicitada se optó por el Framework Vue ya que este es sumamente versátil y posee muchas funcionalidades prehechas, además de ser más sencillo de utilizar que frameworks grandes como Angular. 
Ya que Vue está diseñado para que las aplicaciones que se desarrollen acá sean modularizadas y con componentes reutilizables, optamos por crear un conjunto de componentes y vistas que son las que utilizarán numerosas veces en el sistema.
En cuanto a componentes tenemos LogIn, SignUp, SongInfo y SongPreview.
 - **LogIn:** este componente simplemente pide los datos de inicio de sesión al usuario y posee un botón para realizar dicha acción. Esta acción va a Firebase y verifica los datos y si son correctos redirige a la página principal del sistema, si no lo son envía un mensaje de error al usuario.
 - **SignUp:** este componente también es muy simple. Pide los datos para registrar un usuario y una vez se indica que el usuario está listo, los verifica y los envía a Firebase para registrar un usuario.
 - **SongInfo:** este componente muestra todos los datos de una canción, desde su nombre y autor, hasta su letra. Ya que estos datos son variantes, están guardados en el documento dentro de variables que pueden ser cambiadas según sea necesario enseñar distinta información.
 - **SongPreview** este componente se utiliza para mostrar una previsualización de las canciones y que, así, el usuario pueda elegir sobre qué canción ver más detalles. Igualmente recibe por parámetro los datos de la canción a mostrar.

## Pruebas Unitarias
La clase `TestAPI` hereda de `unittest.TestCase`, lo que indica que es una clase de prueba que contiene varios métodos de prueba.

El método `setUp` se ejecuta antes de cada prueba y se encarga de establecer la URL base de la API que se va a probar.

El método `test_mongo_connection` verifica si la conexión con la base de datos MongoDB es exitosa. Envía una solicitud GET a la ruta `/mongo/connection` de la API y verifica que la respuesta tenga un código de estado 200 y un texto que dice "Succesful Connection!".

El método `test_mongo_search` realiza una búsqueda en la base de datos MongoDB utilizando una solicitud POST a la ruta `/mongo/search`. Envía datos de búsqueda específicos y luego verifica que la respuesta tenga un código de estado 200 y el ID del primer resultado coincida con el valor esperado.

El método `test_mongo_search_filters` realiza una búsqueda con filtros en la base de datos MongoDB utilizando una solicitud POST a la ruta `/mongo/search/filters`. Envía datos de búsqueda con varios filtros y luego verifica que la respuesta tenga un código de estado 200 y el ID del primer resultado coincida con el valor esperado.

Cada método de prueba utiliza el método `assertEqual` para verificar si los valores esperados coinciden con los valores reales obtenidos de la API.

Al final del código, se utiliza `unittest.main()` para ejecutar todas las pruebas definidas en la clase `TestAPI`.