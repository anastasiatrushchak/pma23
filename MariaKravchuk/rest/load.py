import pymongo
import json

DB_URL = "mongodb://localhost:27017/"
client = pymongo.MongoClient(DB_URL)
db = client["lessonsdb"]
collection = db["lessons"]

with open('lessons_data.json', 'r') as file:
    lessons_data = json.load(file)


collection.insert_many(lessons_data)

print("Data loaded into MongoDB collection.")
