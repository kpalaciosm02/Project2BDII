import unittest
from unittest.mock import patch, Mock
import requests

class TestAPI(unittest.TestCase):

    def setUp(self):
        # Configurar la URL base de la API para realizar las pruebas
        self.base_url = "https://main-app.thankfulmeadow-0ffb8b59.eastus.azurecontainerapps.io"



    @patch("app.exec_query")
    def test_add_teacher(self, mock_exec_query):
        data = {
            "Id": 1,
            "SchoolId": 1,
            "Name": "John Doe"
        }
        response = self.app.put(
            "/profesor/agregar", 
            json=data,
            content_type="application/json"
        )
        mock_exec_query.assert_called_once()
        self.assertEqual(response.status_code, 200)

    @patch("app.exec_query")
    def test_add_student(self, mock_exec_query):
        data = {
            "Id": 1,
            "StudentId": "1234",
            "Password": "password123",
            "Name": "John",
            "LastName1": "Doe",
            "LastName2": "Smith",
            "IdPlan": 1
        }
        response = self.app.put(
            "/estudiante/agregar", 
            json=data,
            content_type="application/json"
        )
        mock_exec_query.assert_called_once()
        self.assertEqual(response.status_code, 200)

    @patch("app.exec_query")
    def test_enroll_student(self, mock_exec_query):
        data = {
            "StudentId": "1234",
            "GroupId": 1
        }
        response = self.app.put(
            "/estudiante/matricula", 
            json=data,
            content_type="application/json"
        )
        mock_exec_query.assert_called_once()
        self.assertEqual(response.status_code, 200)

    @patch("app.blob_service_client.get_blob_client")
    def test_post_file(self, mock_get_blob_client):
        file = BytesIO(b"example file contents")
        file.name = "example.txt"
        mock_blob_client = Mock()
        mock_blob_client.upload_blob.return_value = None
        mock_get_blob_client.return_value = mock_blob_client
        response = self.app.post(
            "/files/upload", 
            data={"file": file},
            content_type="multipart/form-data"
        )
        mock_get_blob_client.assert_called_once()
        mock_blob_client.upload_blob.assert_called_once()
        self.assertEqual(response.status_code, 200)

    @patch("app.Cluster.connect")
    def test_cassandra(self, mock_connect):
        message = {
            "user_id": 1,
            "logline": "Example log message"
        }
        response = self.app.post(
            "/Cassandra", 
            json=message,
            content_type="application/json"
        )
        mock_connect.assert_called_once()
        self.assertEqual(response.status_code, 200)
    @patch("app.Cluster.connect")


    def test_get_student_enrollment_courses(self):
        with app.test_client() as client:
            response = client.get('/estudiante/matricula/cursos?Id=1')
            self.assertEqual(response.status_code, 200)
            #Contiene los datos deseados

    def test_get_plans(self):
        with app.test_client() as client:
            response = client.get('/planes?Id=1')
            self.assertEqual(response.status_code, 200)
            #Contiene los datos deseados

    def test_get_careers(self):
        with app.test_client() as client:
            response = client.get('/carreras')
            self.assertEqual(response.status_code, 200)
            #Contiene los datos deseados

    def test_visualize_files(self):
        with app.test_client() as client:
            response = client.get('/files/visualize')
            self.assertEqual(response.status_code, 200)
            #Contiene los datos deseados

    def test_get_files(self):
        with app.test_client() as client:
            response = client.get('/files')
            self.assertEqual(response.status_code, 200)
            #Contiene los datos deseados

    def test_download_file(self):
        with app.test_client() as client:
            response = client.get('/files/download?name=test.txt')
            self.assertEqual(response.status_code, 200)
            #Contiene los datos deseados

if __name__ == '_main_':
   unittest.main()