# from pymongo import MongoClient
from flask import Flask, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from bson import json_util, ObjectId

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
            "id": str(sample["_id"]),
            "title": sample["title"],
            "price": sample["price"],
            "desc": sample["desc"],
            "age": sample["age"],
            "tags": sample["tags"],
            "colors": sample["colors"]
        })

    # Serve serialized container array under toys section in JSON
    return {"toys": toys}

@app.route("/product")
@cross_origin()
def pushToy():

    # Get url id string from incoming request
    _id = request.args.get("id")
    # Find product by id in the collection
    search = collection.find_one({ "_id": ObjectId(_id) })
    product = {
        "title": search["title"],
        "price": search["price"],
        "desc": search["desc"],
        "age": search["age"],
        "tags": search["tags"],
        "colors": search["colors"]
    }

    # Serve product info
    return product