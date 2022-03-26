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
query = {}

'''Create function
Purpose: The below function is used to create a rental information 
Params : None
Return value : None
'''
def createRentalInfo():
    try: 
        data = {
        "buildingId": ObjectId("621ef1e586ed827ec8845a12"),
        "userId": ObjectId("621eee8586ed827ec88459be"),
        "rentalPeriod":"3 years",
        "rentPaid":True,
        "advancePaid":True,
        "depositPaid":False,
        "rentDueOn":"06/06/2022"
        } 
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
def get_one_rentalInfo():
    try:
        global query
        userId = ObjectId("621eee8586ed827ec88459ad")
        query['userId'] = userId
        rentalInfo = db.get_one_record(c_name,query)
        query = {}
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
def update_rentalInfo():
    try:
        global query
        data = {
        "buildingId": ObjectId("621ef1e586ed827ec8845a12"),
        "userId": ObjectId("621eee8586ed827ec88459be"),
        "rentalPeriod":"4 years",
        "rentPaid":True,
        "advancePaid":True,
        "depositPaid":True,
        "rentDueOn":"06/06/2022"
        }
        query["userId"] = ObjectId("621eee8586ed827ec88459ad")
        data_updated = db.update_one_record(c_name,data,query)
        print(data_updated)
        query = {}
        return data_updated
    except Exception as  e:
        print("\n Error updating the rental info due to exception {} ".format(e.__name__))
        return None

'''Delete rent information
Purpose: The below function is used to delete rent data
Params : None
Return value : Boolean
'''
def delete_rentInfo():
    try:
        global query
        query["userId"] = ObjectId("621eee8586ed827ec88459ad")
        data_deleted = db.delete_one_record(c_name,query)
        print(data_deleted)
        return data_deleted
    except Exception as e:
        print("\n Error deleting the rent info due to exception {} ".format(e.__name__))
        return None


if __name__ == "__main__":  
    try:
        # data = createRentalInfo()
        # print(data)
        data = get_one_rentalInfo()
        print(data)
        # data = get_multiple_rentalInfos()
        # print(data)
        # data = update_rentalInfo()
        # print(data)
        # data = delete_rentInfo()
        # print(data)
    except Exception as e:
        print(e.__name__)
