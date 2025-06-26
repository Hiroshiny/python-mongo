from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

if (config['ENV'] == "development"):
    mongo_uri = config["URI_MONGO_DOCKER"]
else:
    mongo_uri = config["URI_MONGO_ATLAS"]
    
mongo_client = MongoClient(mongo_uri)

database = mongo_client['test_database']
test_collection = database['test_collection']


person = {"name": "Guilherme Henrique", "age": 18}
test_collection.insert_one(person)

print(test_collection.find_one({"name": "Guilherme Henrique"}))