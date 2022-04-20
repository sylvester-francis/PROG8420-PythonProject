"""
Code created by Parvathy Suresh
Student ID : 8764553
Created date : 03 March 2022
Last Modified date : 03 March 2022
Last Modified by  : Parvathy Suresh
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
c_name = client["subleases"] # c_name => Collection Name
info_list = []


'''Create function
Purpose: The below function is used to create sublet information
Params : None
Return value : None
'''
def createSubletInfo(data):
    try: 
        data_inserted = db.insert_into_collection(c_name,data)
        print(data_inserted)
        return data_inserted
    except Exception as e:
        print("\n Error creating new record to  collection due to exception {} ".format(e))
        return None



'''Get one user information
Purpose: The below function is used to return a  single rental info data 
Params : None
Return value : None
'''
def get_one_subletInfo(query):
    try:
        subletInfo = db.get_one_record(c_name,query)
        return subletInfo
    except Exception as e:
        print("\n Info not found in collection {}, exception {}".format(c_name,e))

'''Get multiple sublet information
Purpose: The below function is used to return multiple rental info data
Params : None
Return value : info_list -> List of all the info present in the rentalInfo collection
'''
def get_multiple_subletInfos(query = {}):
    global info_list
    info = db.get_many_records(c_name,query)
    for subletInfo in info:
        info_list.append(subletInfo)
    return info_list

'''Update user information
Purpose: The below function is used to update sublet info data
Params : None
Return value : Boolean
'''
def update_subletInfo(data,query):
    try:
        data_updated = db.update_one_record(c_name,data,query)
        print(data_updated)
        return data_updated
    except Exception as  e:
        print("\n Error updating the rental info due to exception {} ".format(e))
        return None

'''Delete rent information
Purpose: The below function is used to delete rent data
Params : None
Return value : Boolean
'''
def delete_subletInfo(query):
    try:
        data_deleted = db.delete_one_record(c_name,query)
        print(data_deleted)
        return data_deleted
    except Exception as e:
        print("\n Error deleting the rent info due to exception {} ".format(e))
        return None
