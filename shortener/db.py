from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@arma3italy-eufgo.mongodb.net/test?retryWrites=true&w=majority")
db = client["octafox_shortener"]
links = db["links"]


links.finde({})