import pymongo
from pymongo import MongoClient
import random

# Establish connection to local mongo collection
client = MongoClient('mongodb://localhost:27017')
db = client.stark
collection = db.samples

# A function to generate random filler words
def gen(category=False, color=False, image=False):

    if color is True:
        shades = ["Light", "Dark", "Grey", "Tinted", "Matte", "Glossy"]
        colors = ["Purple", "Orange", "Grey", "Black", "Violet", "Yellow", "Green", "Pink", "Taupe", "Beige", "Neon"]
        return([shades[random.randrange(len(shades) - 1)] + " " + colors[random.randrange(len(colors) - 1)], shades[random.randrange(len(shades) - 1)] + " " + colors[random.randrange(len(colors) - 1)]])

    
    if category is True:
        # Return a category from some random assorted words
        typeA = ["Action Figure", "Model", "Casual", "Mobile", "RC", "Electronic", "Armoured"]
        typeB = ["Collectible", "Accessory", "Starter-Kit", "Portable"]
        
        return([typeA[random.randrange(len(typeA) - 1)], typeB[random.randrange(len(typeB) - 1)]])

    if image is True:
        image_array = [
            "https://i.pinimg.com/564x/1b/de/cb/1bdecb030e88f393e6b57c1341550274.jpg",
            "https://i.pinimg.com/236x/10/db/14/10db1438481381232441b217a43f4175.jpg",
            "https://i.pinimg.com/236x/75/30/55/753055b82d07c48a2ec0db6156295361.jpg",
            "https://i.pinimg.com/236x/09/69/5e/09695e93f7187f61e914d3fa577a8e08.jpg",
            "https://i.pinimg.com/236x/8f/ad/ae/8fadae061f1d8b6f1637e0caf26c783c.jpg",
            "https://i.pinimg.com/236x/d7/3b/34/d73b342502a414f90d039e7bf7c743de.jpg",
            "https://i.pinimg.com/236x/85/2a/ea/852aea423cca599212cfc45466461fb6.jpg",
            "https://i.pinimg.com/236x/6c/3a/e4/6c3ae4431c6d3720f3a9406b8f930e0c.jpg",
            "https://i.pinimg.com/236x/63/8f/ff/638fffdc33b6ea4760bbda199da77093.jpg",
            "https://i.pinimg.com/236x/dc/3b/b4/dc3bb46d4075ac9614f8b7acb3ed2ee7.jpg",
            "https://i.pinimg.com/236x/06/73/8d/06738d86182a7bcc09d58f72a563f697.jpg",
            "https://i.pinimg.com/564x/63/dc/4e/63dc4ed93bc2864df5f8d0fc6a693112.jpg",
            "https://i.pinimg.com/564x/ce/8f/b6/ce8fb68c3a2dfec300ec768f585fffdd.jpg"
        ]

        return(image_array[random.randrange(len(image_array) - 1)])
        
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
        # Generate prices in the range 10 - 50 usd with a step count of 2 usd
        "price": random.randrange(7, 29, 2),
        "desc": "Lorem ipsum dolor sit amet, prompta minimum urbanitas usu no. Agam vocibus forensibus ad nam. Putent aperiam in sea, eum placerat dissentiunt definitiones ne. Pri nibh omnis voluptua an. Nulla consectetuer eos ex, possit denique quo eu, id eum scripta numquam. Mea in alii esse causae, eam ea graece graeco.",
        "age": random.randrange(3, 13),
        "tags": gen(category=True),
        "colors": gen(color=True),
        "image": gen(image=True)
    }

    return sample


# Populate the DB
for i in range(50):

    collection.insert_one(toygen())