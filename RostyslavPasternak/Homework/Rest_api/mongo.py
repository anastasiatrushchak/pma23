import pymongo


DB_URL = "mongodb://localhost:27017/"

client = pymongo.MongoClient(DB_URL)
db = client["students_db"]
collection = db["students"]
