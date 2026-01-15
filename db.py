import os
from pymongo import MongoClient

MONGO_HOST = os.getenv("MONGO_HOST", "mongo-0.mongo")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_USERNAME = os.getenv("MONGO_USERNAME", "admin")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "secretpass")
MONGO_DB = os.getenv("MONGO_DB", "threat_db")
MONGO_AUTH_SOURCE = os.getenv("MONGO_AUTH_SOURCE", "admin")


connection = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"

client = MongoClient(connection)
db = client[MONGO_DB]
collection = db["top_threats"] 
