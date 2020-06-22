import pymongo
from pymongo import MongoClient
import random

# Establish connection to local mongo collection
client = MongoClient('mongodb://localhost:27017')
db = client.stark
collection = db.samples

# A function to generate random filler words
def gen(category=False, color=False):

    if color is True:
        shades = ["Light", "Dark", "Grey", "Tinted", "Matte", "Glossy"]
        colors = ["Purple", "Orange", "Grey", "Black", "Violet", "Yellow", "Green", "Pink", "Taupe", "Beige", "Neon"]
        return([shades[random.randrange(len(shades) - 1)], colors[random.randrange(len(colors) - 1)]])

    
    if category is True:
        # Return a category from some random assorted words
        typeA = ["Action Figure", "Model", "Casual", "Mobile", "RC", "Electronic", "Armoured"]
        typeB = ["Collectible", "Accessory", "Starter-Kit", "Portable"]
        
        return([typeA[random.randrange(len(typeA) - 1)], typeB[random.randrange(len(typeB) - 1)]])
        
    else:
        # Return a random two syllable name for the toy
        # a = ["Purple", "Orange", "Grey", "Black", "Violet", "Yellow", "Green", "Pink", "Taupe", "Beige", "Neon"]
        # b = ["Stark", "HulkBuster", "P90", "B91", "Slimeback", "Ridge", "Pinethrush", "Ice", "Parker", "Damian", "Porter", "Simulator", "Pascal", "Thermometer", "Torchlight", "Pedro", "Simpson", "Pastor", "Hat", "Boat", "Roofer", "Jet", "Scraper", "Crawler", "Laser", "Chopper", "Zeppelin", "C83"]

        a = ["Vagrant", "Valorant", "Vengeful", "Scaled", "Transit", "Mounted"]
        b = ["Stark", "Hulkbuster", "P90", "B91", "C92", "Ridge", "Pinethrusher", "Knuckle", "Parker", "Damian", "Porter", "Simulator", "Pascal", "Thermometer", "Torchlight", "Pedro", "Simpson", "Pastor", "Hat", "Boat", "Roofer", "Jet", "Scraper", "Crawler", "Laser", "Chopper", "Zeppelin", "C83"]

        
        return(a[random.randrange(len(a) - 1)] + " " + b[random.randrange(len(b) - 1)])


def toygen():

    # Set up some basic attributes to be inserted
    sample = {
        "title": gen(),
        "price": random.randrange(300, 1500, 50),
        "desc": "Lorem ipsum dolor sit amet, prompta minimum urbanitas usu no. Agam vocibus forensibus ad nam. Putent aperiam in sea, eum placerat dissentiunt definitiones ne. Pri nibh omnis voluptua an. Nulla consectetuer eos ex, possit denique quo eu, id eum scripta numquam. Mea in alii esse causae, eam ea graece graeco.",
        "age": random.randrange(3, 13),
        "tags": gen(category=True),
        "color": gen(color=True)
    }

    return sample

for i in range(50):

    # Populate the DB
    collection.insert_one(toygen())