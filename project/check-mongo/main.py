import os
from pymongo import MongoClient
import sys


def check_mongo_connection(uri):
    try:
        client = MongoClient(uri)

        client.admin.command("ismaster")

        print("MongoDB connection successful.")
    except Exception as e:
        print("MongoDB connection failed:", e)
        sys.exit(1)


if __name__ == "__main__":
    uri = os.getenv("MONGODB")

    check_mongo_connection(uri)
