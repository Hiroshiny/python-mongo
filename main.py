from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values('.env')

# Determine the environment
environment = config.get('ENV', 'development')

if environment == 'production':
    mongo_uri = config['URI_MONGO_ATLAS']
else:
    mongo_uri = "mongodb://guilhermemorei:aluno@localhost:27017/"

mongo_client = MongoClient(mongo_uri)

database = mongo_client['database_test']
test_collection = database['test_collection']

person = {"name": "Guilherme", "age": 17}
test_collection.insert_one(person)

print(test_collection.find_one({"name": "Guilherme Henrique"}))