import os
import flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
import json
from bson import ObjectId

app = flask.Flask(__name__)


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


def mongo_search(query: str, path: str, limit: int, query_type: str):
    try:
        # Connect to MongoDB Atlas
        url = os.environ["CONNECTION_STRING"]
        client = MongoClient(url)

        # Access the desired database and collection
        database = "song-lyrics-search"
        collection = "Artists-Lyrics"
        index_name = "lyrics-search"

        pipeline = [
            {
                "$search": {
                    "index": index_name,
                    query_type: {
                        "path": path,
                        "query": query,
                    },
                }
            },
            {"$limit": limit},
        ]

        results = client[database][collection].aggregate(pipeline)

        documents = [doc for doc in results]

        json_data = json.dumps(documents, cls=JSONEncoder)

        # Close the MongoDB connection
        client.close()
        return json_data
    except Exception as e:
        return e


def mongo_filter_search(paths: list, queries: list, limit: int, query_type: str):
    if len(paths) != len(queries):
        return "Error: paths and queries length don't match"
    try:
        # Connect to MongoDB Atlas
        url = os.environ["CONNECTION_STRING"]
        client = MongoClient(url)

        # Access the desired database and collection
        database = "song-lyrics-search"
        collection = "Artists-Lyrics"
        index_name = "lyrics-search"

        pipeline = [
            {
                "$search": {
                    "index": index_name,
                    "compound": {
                        "must": [
                            {query_type: {"query": query, "path": path}}
                            for path, query in zip(paths, queries)
                        ]
                    },
                }
            },
            {"$limit": limit},
        ]

        results = client[database][collection].aggregate(pipeline)

        documents = [doc for doc in results]

        print(len(documents))

        json_data = json.dumps(documents, cls=JSONEncoder)

        # Close the MongoDB connection
        client.close()
        return json_data
    except Exception as e:
        return e


@app.route("/mongo/search", methods=["GET"])
def get_mongo_search():
    json_input = flask.request.get_json()
    path = json_input["path"]
    query = json_input["query"]
    limit = json_input["limit"]
    query_type = json_input["query_type"]
    return mongo_search(query, path, limit, query_type)


@app.route("/mongo/search/filters", methods=["GET"])
def get_mongo_search_filters():
    json_input = flask.request.get_json()
    paths = json_input["paths"]
    queries = json_input["queries"]
    limit = json_input["limit"]
    query_type = json_input["query_type"]
    return mongo_filter_search(paths, queries, limit, query_type)


if __name__ == "__main__":
    app.debug = True
    app.run()
