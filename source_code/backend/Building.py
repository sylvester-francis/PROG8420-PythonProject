"""
Code created by Rachel Denzil
Student ID : 8806655
Created date : 03 March 2022
Last Modified date : 15 March 2022
Last Modified by  : Rachel Denzil
"""
import sys
sys.path.append("..")
import database.connection as db
from bson.objectid import ObjectId
client = db.get_database()
c_name = client["buildings"] #c_name => Collection Name
c_user = client["users"]
building_list = []
query = {}

'''Get one building information
Purpose: The below function is used to return a single building data 
Params : None
Return value : None
'''
def get_apartment_info():
    try:
        userquery = {}
        userquery['LastName'] = "Summerlee"
        userdata = db.get_one_record(c_user,userquery)
        global query
        query['userId'] = ObjectId(userdata['_id'])
        # building = "Marq"
        # query['isFurnished'] = True
        # query['buildingName'] = building
        apartment = db.get_one_record(c_name,query)
        query = {}
        return apartment
    except Exception as e:
        print("\n Building info not found in collection {}, exception {}".format(c_name,e.__name__))

'''Get multiple building information
Purpose: The below function is used to return multiple building data
Params : None
Return value : building_list -> List of all the users present in the collection
'''
def get_multiple_buildingInfo():
    global building_list
    buildings = db.get_many_records(c_name)
    for i in buildings:
        building_list.append(i)
    return building_list

'''Create building information
Purpose: The below function is used to create building information 
Params : None
Return value : Boolean
'''
def create_buildingInfo():
    try:
        data = {
        "buildingName":"BlueTwo",
        "Address":"665544 Scott Lane",
        "City":"Bowmanville",
        "postalCode":"L1K",
        "province":"ON",
        "isFurnished":False,
        "isParkingAvailable":True,
        "storageAreaAvailable":True,
        "petFriendly":True,
        "noOfWashrooms":"2",
        "userId": ObjectId("621ef1e586ed827ec8845a12")
        }
        data_inserted = db.insert_into_collection(c_name,data)
        print(data_inserted)
        return data_inserted
    except Exception as e:
        print("\n Error creating new record to rental info collection due to exception {} ".format(e.__name__))
        return None

'''Update building information
Purpose: The below function is used to update building data
Params : None
Return value : Boolean
'''
def update_buildingInfo():
    try:
        global query
        data = {
        "buildingName":"BlueTwo",
        "Address":"665544 Scott Lane",
        "City":"Whitby",  #update city
        "postalCode":"L1K",
        "province":"ON",
        "isFurnished":False,
        "isParkingAvailable":True,
        "storageAreaAvailable":True,
        "petFriendly":True,
        "noOfWashrooms":"2",
        "userId": ObjectId("621ef1e586ed827ec8845a12")
        }
        query["userId"] = ObjectId("621ef1e586ed827ec8845a12")
        data_updated = db.update_one_record(c_name,data,query)
        print(data_updated)
        query = {}
        return data_updated
    except Exception as  e:
        print("\n Error updating the user due to exception {} ".format(e.__name__))
        return None


'''Delete building information
Purpose: The below function is used to delete building data
Params : None
Return value : Boolean
'''
def delete_buildingInfo():
    try:
        global query
        query["userId"] = ObjectId("621ef1e586ed827ec8845a12")
        data_deleted = db.delete_one_record(c_name,query)
        print(data_deleted)
        return data_deleted
    except Exception as e:
        print("\n Error deleting the rent info due to exception {} ".format(e.__name__))
        return None


if __name__ == "__main__":  

    try:
        # data = get_apartment_info()
        # print(data)
        # data = get_multiple_buildingInfo()
        # print(data)
        # data = create_buildingInfo()
        # print(data)
        # data = update_buildingInfo()
        # print(data)
        # data = delete_buildingInfo()
        # print(data)
    except Exception as e:
        print(e)