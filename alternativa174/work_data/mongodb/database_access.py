import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["alternativa_174"]
col = db["individual_lesson"]