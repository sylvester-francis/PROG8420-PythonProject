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
from bson.objectid import ObjectId
def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    try:
        #For Atlas connect
        #CONNECTION_STRING = "mongodb+srv://administrator:appsrdsf123@pythonproject.bafek.mongodb.net/rental_system?retryWrites=true&w=majority"
        #client = MongoClient(CONNECTION_STRING)

        # Local Connect
        hostname = 'localhost'
        port = 27017
        client =MongoClient(hostname,port)
        
        # print("\n Client {}".format(str(client)))
        database_obj =  client['rental_system']
        return database_obj
    except Exception as e:
        print("\n An exception occured in connecting to db")
        return e

''' Insert one record into collection 
Purpose: The below function is used to insert a record into a specific collection
Params : Collection name & data to be inserted
'''
#Parvathy's case: c_name = rentalInfo data: {}
def insert_into_collection(c_name,data):
    dataInserted = False
    try:
        c_name.insert_one(data)
        dataInserted = True
        return dataInserted
    except Exception as e:
        print("\n Error in inserting data in collection {}".format(c_name))
        dataInserted = False
        return dataInserted
    

''' Get one record 
Purpose : The below function is used to retrieve one record from the database
Params : Collection name & query field
'''

# Rachel's case : query : {userid:_id usercollection}
def get_one_record(c_name,query):
    try:
       data = c_name.find_one(query)
       return data
    except Exception as e:
        print("\n Could not find the record in collection {}".format(c_name))
        return None

'''Get many records
Purpose: The below function is used to get many records from  a specific collection
Params : Collection name 
'''
def get_many_records(c_name,query={}):
    try:
        data = c_name.find(query)
        return data
    except Exception as e:
        print("\n Could not find any record in collection {}".format(c_name))
        return None

'''Update one record
Purpose: The below function is used to edit a record from a specific collection
Params : Collection name,data to be inserted,query
'''
def update_one_record(c_name,data,query):
    recordUpdated = False
    try:
        current_record = c_name.find_one(query)
        updated_data = {'$set':data}
        c_name.update_one(current_record,updated_data)
        recordUpdated = True
        return recordUpdated
    except Exception as e:
        print("\n Could not update the record in collection {}".format(c_name))
        recordUpdated = False
        return recordUpdated


'''Delete one record
Purpose: The below function is used to delete a record from a specific collection
Params : Collection name and query
'''
def delete_one_record(c_name,query):
    recordDeleted = False
    try:
        c_name.delete_one(query)
        recordDeleted = True
        return recordDeleted
    except Exception as e:
        print("\n Could not delete the record in collection {}".format(c_name))
        recordDeleted = False
        return recordDeleted



if __name__ == "__main__":    
    dbname = get_database()
    print(dbname)