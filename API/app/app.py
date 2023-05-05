import os
import pyodbc
import flask
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from flask_cors import CORS
from ssl import PROTOCOL_TLS, SSLContext, CERT_NONE
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from werkzeug.utils import secure_filename
from datetime import datetime
import werkzeug.utils
import time
import pytz

app = flask.Flask(__name__)
CORS(app)


# Setup the blob service client
default_credential = DefaultAzureCredential()
blob_service_client = None
if "ACCOUNT_URL" in os.environ:
    blob_service_client = BlobServiceClient(
        os.environ["ACCOUNT_URL"], credential=default_credential
    )

# Setup Azure Monitor
if "APPINSIGHTS_KEY" in os.environ:
    middleware = FlaskMiddleware(
        app,
        exporter=AzureExporter(
            connection_string="InstrumentationKey={0}".format(
                os.environ["APPINSIGHTS_KEY"]
            )
        ),
        sampler=ProbabilitySampler(rate=1.0),
    )

def connect_to_database():
    print(f"env: {os.environ['SQLAZURECONNSTR_WWIF']}")
    try:
        conn = pyodbc.connect(os.environ["SQLAZURECONNSTR_WWIF"], timeout=10)
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def generate_sp_exec_str(sp_name: str, arguments={}):
    if len(arguments) == 0:
        return f"EXEC dbo.{sp_name};"
    else:
        keys_list = [k for k in arguments.keys()]
        str_ret = f"EXEC dbo.{sp_name}"
        for key in keys_list:
            value = arguments[key]
            if isinstance(value, str):
                str_ret += f" @{key}='{value}',"
            else:
                str_ret += f" @{key}={value},"
        return str_ret[:-1] + ";"


def exec_query_get(query: str):
    conn = connect_to_database()
    print(f"query: {query}")
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        # get the column names
        columns = [column[0] for column in cursor.description]

        # create a dictionary for each row
        data = []
        for row in rows:
            row_dict = {}
            for i, column in enumerate(columns):
                row_dict[column] = row[i]
            data.append(row_dict)

        return flask.jsonify({"data": data})
    else:
        return {"error": "Unable to connect to database"}


def exec_query(query: str):
    conn = connect_to_database()
    print(f"query: {query}")
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return "Successful query"
    else:
        return "Error: unable to connect to database"


# my_query = query_db("select * from majorroadstiger limit %s", (3,))


@app.route("/estudiante/matricula/cursos", methods=["GET"])
def get_student_enrollment_courses():
    student_id=flask.request.args.get("Id")
    query_str = generate_sp_exec_str("SpCursosEstudiante", {"IdEstudiante": student_id})
    return exec_query_get(query_str)

@app.route("/planes", methods=["GET"])
def get_plans():
    career_id=flask.request.args.get("Id")
    query_str = generate_sp_exec_str(
        "SpObtenerPlanesDeEstudio", {"IdCarrera": career_id}
    )
    return exec_query_get(query_str)

@app.route("/carreras", methods=["GET"])
def get_careers():
    query_str = generate_sp_exec_str("SpObtenerCarreras")
    return exec_query_get(query_str)


@app.route("/profesor/agregar", methods=["PUT"])
def add_teacher():
    json_input = flask.request.get_json()
    teacher_id = json_input["Id"]
    school_id = json_input["SchoolId"]
    teacher_name = json_input["Name"]
    dict_query = {"Id": teacher_id, "IdEscuela": school_id, "Nombre": teacher_name}
    query_str = generate_sp_exec_str("SpAgregarProfesor", dict_query)
    return exec_query(query_str)


@app.route("/estudiante/agregar", methods=["PUT"])
def add_student():
    json_input = flask.request.get_json()
    _id = json_input["Id"]
    student_id = json_input["StudentId"]
    password = json_input["Password"]
    student_name = json_input["Name"]
    student_last_name_1 = json_input["LastName1"]
    student_last_name_2 = json_input["LastName2"]
    id_plan = json_input["IdPlan"]
    dict_query = {
        "Id": _id,
        "Carne": student_id,
        "Contrasena": password,
        "Nombre": student_name,
        "Apellido1": student_last_name_1,
        "Apellido2": student_last_name_2,
        "IdPlan": id_plan,
    }
    query_str = generate_sp_exec_str("SpAgregarEstudiante", dict_query)
    return exec_query(query_str)


@app.route("/estudiante/matricula", methods=["PUT"])
def enroll_student():
    json_input = flask.request.get_json()
    student_id = json_input["StudentId"]
    group_id = json_input["GroupId"]
    dict_query = {"IdEstudiante": student_id, "IdGrupo": group_id}
    query_str = generate_sp_exec_str("SpMatricularEstudiante", dict_query)
    return exec_query(query_str)


@app.route("/Cursos", methods=["GET"])
def test_get():
    return [
        {
            "Curso": "Bases de datos",
            "Escuela": "Computación",
            "Grupo": 1,
            "Hora de inicio": "8:00",
            "Hora final": "9:30",
            "Profesor": "Juan",
            "Cupo": 25,
            "Periodo": "Semestre",
            "Estado": "Activo",
        },
        {
            "Curso": "Programación Orientada a Objetos",
            "Escuela": "Ingeniería en Sistemas",
            "Grupo": 2,
            "Hora de inicio": "10:00",
            "Hora final": "11:30",
            "Profesor": "María",
            "Cupo": 30,
            "Periodo": "Cuatrimestre",
            "Estado": "Activo",
        },
        {
            "Curso": "Análisis de Algoritmos",
            "Escuela": "Ciencias de la Computación",
            "Grupo": 3,
            "Hora de inicio": "12:00",
            "Hora final": "13:30",
            "Profesor": "Carlos",
            "Cupo": 20,
            "Periodo": "Trimestre",
            "Estado": "Activo",
        },
    ]


@app.route("/files/upload", methods=["POST"])
def post_file():
    if "file" not in flask.request.files:
        flask.flash("No file part")
        return "<p>Upload File!</p>"
    file = flask.request.files["file"]
    if file.filename == "":
        return "<p>Upload No name!</p>"
    filename = secure_filename(str(datetime.now())+file.filename)
    blob_client = blob_service_client.get_blob_client(
        container="documents", blob=filename
    )
    blob_client.upload_blob(file)
    return "<p>Upload!</p>"


@app.route("/files/visualize", methods=["GET"])
def visualize_files():
    container_client = blob_service_client.get_container_client(container="documents")
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print(blob.name)
    # wip

@app.route("/files", methods=["GET"])
def get_files():
    try:
        container_client = blob_service_client.get_container_client("documents")
        blob_list = container_client.list_blobs()
        files = [{'id': blob.name, 'name': blob.name} for blob in blob_list]
        return jsonify(files), 200
    except Exception as e:
        print(str(e))
        return jsonify({'error': 'Unable to retrieve files.'}), 500

@app.route("/files", methods=["DELETE"])
def delete_file():
    try:
        file_name=flask.request.args.get("name")
        # Obtener una referencia al contenedor
        container_client = blob_service_client.get_container_client(container="documents", blob=file_name)
        
        # Verificar si el archivo existe en el contenedor
        blob_client = container_client.get_blob_client(file_name)
        if not blob_client.exists():
            return jsonify({"error": "El archivo no existe."}), 404

        # Borrar el archivo del contenedor
        blob_client.delete_blob()
        return jsonify({"message": f"El archivo {file_name} se ha borrado exitosamente."}), 200

    except Exception as e:
        print(str(e))
        return jsonify({"error": "No se pudo borrar el archivo."}), 500
    

@app.route('/files/download', methods=['GET'])
def download_file():
    try:
        file_name=flask.request.args.get("name")
        # Obtener una referencia al contenedor
        container_client = blob_service_client.get_container_client(container="documents", blob=file_name)
        blob_client = container_client.get_blob_client()
        data = blob_client.download_blob().readall()
        headers = {
            'Content-Disposition': 'attachment; filename=' + file_name
        }
        return data, 200, headers
    except Exception as e:
        print(str(e))
        return jsonify({'error': 'Unable to download file.'}), 500
    

@app.route("/Cassandra", methods=["POST"])
def cassandra():
    # Get Data
    message = flask.request.get_json()

    # Create authentication info
    # Use username and password provide by Azure Cosmos
    ssl_context = SSLContext(PROTOCOL_TLS)
    ssl_context.verify_mode = CERT_NONE
    auth_provider = PlainTextAuthProvider(username='tfex-cosmos-db-31154', password='C2A2lQkldr8Rx6Uzw6p85GtL5tpBlBx79PB8KShzbQ0q1Zk8xTWzmLisViXYwFagSenr8PoPnEN4ACDbnKKI5g==')
   
    # Create the connection with cassandra
    cluster = Cluster(['tfex-cosmos-db-31154.cassandra.cosmos.azure.com'], port = 10350, auth_provider=auth_provider,ssl_context=ssl_context)

    # Create the session
    session = cluster.connect()

    # Get Timestamp
    timestamp = datetime.now(pytz.utc)

    # Insert data
    query = 'INSERT INTO "tfex-cosmos-cassandra-keyspace".userlogs (user_id, logline, event_timestamp) VALUES (%s, %s, %s)'
    session.execute(query, (message["user_id"], message["logline"], timestamp))
    # Close the session and the connection
    session.shutdown()
    cluster.shutdown()

    return message


if __name__ == "__main__":
    app.debug = True
    app.run()
