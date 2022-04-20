"""
Code created by Sylvester Francis
Student ID : 8735728
Created date : 17 April 2022
Last Modified date : 17 April 2022
Last Modified by  : Sylvester Francis
"""
"""
Import statements
"""
import sys
sys.path.append("..")
import database.connection as db
from bson.objectid import ObjectId #Added for objectID type -> Mongo Specific type
from getpass import getpass #Added for password hiding

"""
Global Variables
"""
client = db.get_database()
c_name = client["service"] # c_name => Collection Name
info_list = []


'''Create function
Purpose: The below function is used to create a service request 
Params : data
Return value : None
'''
def createService(data):
    try: 
        data_inserted = db.insert_into_collection(c_name,data)
        print(data_inserted)
        return data_inserted
    except Exception as e:
        print("\n Error creating new record to service info collection due to exception {} ".format(e))
        return None



'''Get one service information
Purpose: The below function is used to return a  single service data 
Params : Query
Return value : None
'''
def get_one_serviceInfo(query):
    try:
        serviceInfo = db.get_one_record(c_name,query)
        return serviceInfo
    except Exception as e:
        print("\n Info not found in collection {}, exception {}".format(c_name,e))

'''Get multiple service information
Purpose: The below function is used to return multiple service information data
Params : None
Return value : info_list -> List of all the info present in the rentalInfo collection
'''
def get_multiple_serviceInfos():
    global info_list
    info = db.get_many_records(c_name)
    for serviceInfo in info:
        info_list.append(serviceInfo)
    return info_list

'''Update user information
Purpose: The below function is used to update rental info data
Params : None
Return value : Boolean
'''
def update_serviceInfo(data,query):
    try:
        data_updated = db.update_one_record(c_name,data,query)
        print(data_updated)
        return data_updated
    except Exception as  e:
        print("\n Error updating the service Info due to exception {} ".format(e))
        return None

'''Delete rent information
Purpose: The below function is used to delete service data
Params : None
Return value : Boolean
'''
def delete_serviceInfo(query):
    try:
        data_deleted = db.delete_one_record(c_name,query)
        print(data_deleted)
        return data_deleted
    except Exception as e:
        print("\n Error deleting the service due to exception {} ".format(e))
        return None
