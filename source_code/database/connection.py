"""
Code created by Sylvester Francis
Student ID : 8735728
Created date : 27 February 2022
Last Modified date : 27 February 2022
Last Modified by  : Sylvester Francis
"""
"""
Import statements
"""
import pymongo
from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    try:
        CONNECTION_STRING = "mongodb+srv://administrator:appsrdsf123@pythonproject.bafek.mongodb.net/rental_system?retryWrites=true&w=majority"
        client = MongoClient(CONNECTION_STRING)
        return client['rental_system']
    except Exception as e:
        return e

if __name__ == "__main__":    
    dbname = get_database()
    print(dbname.list_collection_names())