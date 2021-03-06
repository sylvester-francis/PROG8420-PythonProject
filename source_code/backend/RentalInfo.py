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
c_name = client["rentalInfo"] # c_name => Collection Name
info_list = []


'''Create function
Purpose: The below function is used to create a rental information 
Params : None
Return value : None
'''
def createRentalInfo(data):
    try: 
        data_inserted = db.insert_into_collection(c_name,data)
        print(data_inserted)
        return data_inserted
    except Exception as e:
        print("\n Error creating new record to rental info collection due to exception {} ".format(e.__name__))
        return None



'''Get one user information
Purpose: The below function is used to return a  single rental info data 
Params : None
Return value : None
'''
def get_one_rentalInfo(query):
    try:
        rentalInfo = db.get_one_record(c_name,query)
        return rentalInfo
    except Exception as e:
        print("\n Info not found in collection {}, exception {}".format(c_name,e.__name__))

'''Get multiple user information
Purpose: The below function is used to return multiple rental info data
Params : None
Return value : info_list -> List of all the info present in the rentalInfo collection
'''
def get_multiple_rentalInfos():
    global info_list
    info = db.get_many_records(c_name)
    for rentalInfo in info:
        info_list.append(rentalInfo)
    return info_list

'''Update user information
Purpose: The below function is used to update rental info data
Params : None
Return value : Boolean
'''
def update_rentalInfo(data,query):
    try:
        data_updated = db.update_one_record(c_name,data,query)
        print(data_updated)
        return data_updated
    except Exception as  e:
        print("\n Error updating the rental info due to exception {} ".format(e.__name__))
        return None

'''Delete rent information
Purpose: The below function is used to delete rent data
Params : None
Return value : Boolean
'''
def delete_rentInfo(query):
    try:
        data_deleted = db.delete_one_record(c_name,query)
        print(data_deleted)
        return data_deleted
    except Exception as e:
        print("\n Error deleting the rent info due to exception {} ".format(e.__name__))
        return None

