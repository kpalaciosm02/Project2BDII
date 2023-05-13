import os
import flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
import json
from bson import ObjectId

app = flask.Flask(__name__)
os.environ[
    "CONNECTION_STRING"
] = "mongodb+srv://admin:YRklqMOH3ZMA85GU@song-lyrics-search.zpp8xfd.mongodb.net/?retryWrites=true&w=majority"


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)


def verify_connection_to_mongo():
    # Replace the placeholder with your Atlas connection string
    url = os.environ["CONNECTION_STRING"]
    # Set the Stable API version when creating a new client
    client = MongoClient(url, server_api=ServerApi("1"))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return True
    except Exception as e:
        print(e)
        return False


def mongo_search(query: str, path: str, limit: int):
    if not verify_connection_to_mongo():
        return "no"
    else:
        # Connect to MongoDB Atlas
        url = os.environ["CONNECTION_STRING"]
        client = MongoClient(url)

        # Access the desired database and collection
        database = "song-lyrics-search"
        collection = "Artists-Lyrics"
        index_name = "lyrics-search"

        results = client[database][collection].aggregate(
            [
                {
                    "$search": {
                        "index": index_name,
                        "text": {
                            "path": path,
                            "query": query,
                        },
                    }
                },
                {"$limit": limit},
            ]
        )

        documents = [doc for doc in results]

        json_data = json.dumps(documents, cls=JSONEncoder)

        # Close the MongoDB connection
        client.close()
        return json_data


@app.route("/mongo/search", methods=["GET"])
def get_mongo_search():
    json_input = flask.request.get_json()
    path = json_input["path"]
    query = json_input["query"]
    limit = json_input["limit"]
    return mongo_search(query, path, limit)


if __name__ == "__main__":
    app.debug = True
    app.run()
