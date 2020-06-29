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

    param = request.args.get("sort")

    if param is None:

        # Initialize a container array
        toys = []
        for sample in collection.find():
            toys.append({
                "id": str(sample["_id"]),
                "title": sample["title"],
                "price": sample["price"],
                "age": sample["age"],
                "tags": sample["tags"],
                "colors": sample["colors"]
            })

        # Serve serialized container array under toys section in JSON
        return {"toys": toys}
    
    if param == "price":

        # Initialize container array
        toys = []
        # Sort collection by price
        for sample in collection.find().sort("price"):
            toys.append({
                "id": str(sample["_id"]),
                "title": sample["title"],
                "price": sample["price"],
                "age": sample["age"],
                "tags": sample["tags"],
                "colors": sample["colors"]
            })
        
        # Serve sorted container array in JSON
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

@app.route("/tags")
@cross_origin()
def pushTags():

    # Find and push distinct categories/tags for toys
    tags = collection.find().distinct("tags")
    return { "tags": tags }


@app.route("/names")
@cross_origin()
def pushNames():

    # Find and push distinct toy names
    names = collection.find().distinct("title")
    return { "names": names }