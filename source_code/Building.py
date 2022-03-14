"""
Code created by Rachel Denzil
Student ID : 8806655
Created date : 03 March 2022
Last Modified date : 03 March 2022
Last Modified by  : Rachel Denzil
"""
import database.connection as db
from bson.objectid import ObjectId


client = db.get_database()
c_name = client["buildings"] #c_name => Collection Name
c_user = client["users"]
building_list = []
query = {}

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


def get_multiple_buildingInfo():
    global building_list
    buildings = db.get_many_records(c_name)
    for i in buildings:
        building_list.append(i)
    return building_list

#Delete,update,save - Building info  - #TODO

if __name__ == "__main__":  

    try:
        data = get_apartment_info()
        print(data)
    # data = get_multiple_buildingInfo()
    # print(data)
    except Exception as e:
        print(e)