import unittest
import requests

class TestAPI(unittest.TestCase):

    def setUp(self):
        # URL of the API
        self.base_url = "http://localhost:5000" #Right Now localhost, needs to be changed

    def test_mongo_search(self):
        #Data that is going to be send
        data = {
        "path": ["Artist", "Genres"],
        "query":["Michael Jackson","Pop"],
        "limit": 1,
        "query_type":"text"
        }

        #Create de request to de route
        response = requests.get(self.base_url + '/mongo/search', json= data)
        #Verify the responses are OK
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['_id'],"645da7f1743ac88b8a22dca6") #Only compared first item
        
        #Finish mongo/search test route
        print("mongo/search test completed")

    def test_mongo_search_filters(self):
        #Data that is going to be send
        data = {
            "paths": ["Artist", "Genres"],
            "queries":["Shakira","Pop"],
            "limit": 1,
            "query_type":"text"
        }

        #Create de request to de route
        response = requests.get(self.base_url + '/mongo/search/filters', json= data)
        #Verify the responses are OK
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['_id'],"645da81e743ac88b8a237076") #Only compared first item
        
        #Finish mongo/search test route
        print("mongo/search/filters test completed")

if __name__ == '__main__':
    unittest.main()