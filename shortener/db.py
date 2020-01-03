from pymongo import MongoClient
from shortener.base64converter import convert

client = MongoClient("mongodb+srv://admin:admin@arma3italy-eufgo.mongodb.net/test?retryWrites=true&w=majority")
db = client["octafox_shortener"]
links = db["links"]

def getOriginalLink(id_link):
    link = links.find_one({"id": id_link})

    return link


def getShortLink(original_url):
    links_counter = links.count_documents({}) + 1
    id_base64 = convert(decNum=links_counter, base=64)

    link = {
        "id": id_base64,
        "original": original_url
    }

    links.insert_one(link)

    return link