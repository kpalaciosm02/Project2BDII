import unittest
import requests

class TestAPI(unittest.TestCase):

    def setUp(self):
        # URL of the API
        self.base_url = "http://localhost:5000" #Right Now localhost, needs to be changed

    def test_mongo_search(self):
        #Data that is going to be send
        #Searching for a very specific song
        data = {
            "path": ["Artist", "Genres", "Lyric"],
            "query":["Michael Jackson","Pop", "It's close to midnight\nsomething evil's lurkin' in the dark\nUnder the moonlight\nYou see a sight that almost stops your heart\n\nYou try to scream\nBut terror takes the sound before you make it"],
            "limit": 1,
            "query_type":"text"
        }

        #Create de request to de route
        response = requests.get(self.base_url + '/mongo/search', json= data)
        #Verify the responses are OK
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['_id'],"645da7f1743ac88b8a22dd9d") #Compared Id of the song
        
        #Finish mongo/search test route
        print("mongo/search test completed")

    def test_mongo_search_filters(self):
        #Data that is going to be send
        #Searching for a very specific song
        data = {
            "paths": ["Artist", "Genres","Lyric"],
            "queries":["Shakira","Pop","Tsamina mina zangalewa\nPorqu\u00e9 esto es \u00c1frica\n\nTsamina mina eh, eh\nWaka waka eh, eh\nTsamina mina zangalewa\nAnawa aa\n\nTsamina mina eh, eh\nWaka waka eh, eh\nTsamina mina zangalewa"],
            "limit": 1,
            "query_type":"text"
        }

        #Create de request to de route
        response = requests.get(self.base_url + '/mongo/search/filters', json= data)
        #Verify the responses are OK
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['_id'],"645da81e743ac88b8a237079") #Only compared first item
        
        #Finish mongo/search test route
        print("mongo/search/filters test completed")

if __name__ == '__main__':
    unittest.main()