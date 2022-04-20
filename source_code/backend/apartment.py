"""
Code created by Pradeep Asokan
Student ID : 8807488
Created date : 14 March 2022
Last Modified date : 26 March 2022
Last Modified by  : Sylvester Francis
"""
import sys
sys.path.append("..")
import database.connection as db
from bson.objectid import ObjectId
client = db.get_database()
c_name = client["apartments"] 
c_user = client["users"]
apartment_list = []

'''Get one apartment information
Purpose: The below function is used to return a single apartment data 
Params : query
Return value : apartment information
'''
def get_apartment_info(query):
    try:
        #query['buildingId'] = '621ef1e586ed827ec8845a16'
        apartment = db.get_one_record(c_name,query)
        return apartment
    except Exception as e:
        print("\n Apartment info not found in collection {}, exception {}".format(c_name,e))

'''Get multiple apartment information
Purpose: The below function is used to return multiple apartment data
Params : None
Return value : apartment_list -> List of all the apartments present in the collection
'''
def get_multiple_apartmentInfo(query = {}):
    global apartment_list
    apartments = db.get_many_records(c_name,query)
    for i in apartments:
        apartment_list.append(i)
    return apartment_list




'''Create apartment information
Purpose: The below function is used to create apartment information 
Params : None
Return value : Boolean
'''
def create_apartmentInfo(data):
    try:
        data_inserted = db.insert_into_collection(c_name,data)
        print(data_inserted)
        return data_inserted
    except Exception as e:
        print("\n Error creating new record to rental info collection due to exception {} ".format(e))
        return None

'''Update apartment information
Purpose: The below function is used to update apartment data
Params : None
Return value : Boolean
'''
def update_apartmentInfo(query,data):
    try:
        data_updated = db.update_one_record(c_name,data,query)
        print(data_updated)
        query = {}
        return data_updated
    except Exception as  e:
        print("\n Error updating the apartment due to exception {} ".format(e))
        return None


'''Delete apartment information
Purpose: The below function is used to delete apartment data
Params : None
Return value : Boolean
'''
def delete_apartmentInfo(query):
    try:
        data_deleted = db.delete_one_record(c_name,query)
        print(data_deleted)
        return data_deleted
    except Exception as e:
        print("\n Error deleting the Apartment info due to exception {} ".format(e))
        return None

