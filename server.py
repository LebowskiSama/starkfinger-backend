# from pymongo import MongoClient
from flask import Flask
from flask_cors import CORS, cross_origin
from pymongo import MongoClient

# Establish a connection for CRUD ops on the samples collection under the stark DB
client = MongoClient('mongodb://localhost:27017')
db = client.stark
collection = db.samples

# Configure flask and Cross Origin Requests
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/toys')
@cross_origin()
def pushToys():

    # Initialize a container array
    toys = []
    for sample in collection.find():
        toys.append({
            # "id": sample["_id"],
            "title": sample["title"],
            "price": sample["price"],
            "desc": sample["desc"],
            "age": sample["age"],
            "tags": sample["tags"],
            "color": sample["color"]
        })

    # Serve serialized container array under toys section in JSON
    return ({"toys": toys})