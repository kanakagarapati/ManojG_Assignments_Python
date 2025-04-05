import json
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

db_uri = os.getenv("db_connection_uri")
client = MongoClient(db_uri)
db = client["config_db"]
collection = db["configs"]

def save_config(data):
    collection.delete_many({})  # clear old config
    collection.insert_one({"_id": "latest_config", "data": data})

def get_config():
    doc = collection.find_one({"_id": "latest_config"})
    return doc["data"] if doc else {}