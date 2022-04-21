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
c_name = client["buildings"] 
c_user = client["users"]
building_list = []

'''Get one building information
Purpose: The below function is used to return a single building data 
Params : query
Return value : buildinginfo
'''
def get_building_info(query):
    try:
        building = db.get_one_record(c_name,query)
        return building
    except Exception as e:
        print("\n Building info not found in collection {}, exception {}".format(c_name,e))

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
def create_buildingInfo(data):
    try:
        data_inserted = db.insert_into_collection(c_name,data)
        print(data_inserted)
        return data_inserted
    except Exception as e:
        print("\n Error creating new record to rental info collection due to exception {} ".format(e))
        return None

'''Update building information
Purpose: The below function is used to update building data
Params : None
Return value : Boolean
'''
def update_buildingInfo(query,data):
    try:
        data_updated = db.update_one_record(c_name,data,query)
        print(data_updated)
        query = {}
        return data_updated
    except Exception as  e:
        print("\n Error updating the user due to exception {} ".format(e))
        return None


'''Delete building information
Purpose: The below function is used to delete building data
Params : None
Return value : Boolean
'''
def delete_buildingInfo(query):
    try:
        data_deleted = db.delete_one_record(c_name,query)
        print(data_deleted)
        return data_deleted
    except Exception as e:
        print("\n Error deleting the rent info due to exception {} ".format(e))
        return None


'''Aggregating the apartments collection
Purpose: The below function is used to aggregate building data with apartment data
Params : None
Return value : Boolean
'''

def agg_apartments():
    report_data = []
    agg_data = {}
    try:
        result = c_name.aggregate([
            {
                '$lookup': {
                    'from': 'apartments', 
                    'localField': '_id', 
                    'foreignField': 'buildingId', 
                    'as': 'apartments'
                }
            }, {
                '$unwind': {
                    'path': '$apartments'
                }
            }, {
                '$project': {
                    '_id': 0, 
                    'buildingName': 1, 
                    'Address':1,
                    'City':1,
                    'province': 1, 
                    'apartments.isAvailable': 1
                }
            }
        ])
        for data in result:
            agg_data.update({'buildingName':data['buildingName'],'province':data['province'],'isAvailable':data['apartments']['isAvailable'],'City':data['City'],'Address':data['Address']})
            report_data.append(agg_data)
            agg_data = {}
        return report_data
    except Exception as e:
        print("\n Error in aggregation due to exception {} ".format(e))
        return None
    
def agg_rental_info():
    report_data = []
    agg_data = {}
    try:
        result = c_name.aggregate([
            {
                '$lookup': {
                    'from': 'apartments', 
                    'localField': '_id', 
                    'foreignField': 'buildingId', 
                    'as': 'apartments'
                }
            }, {
                '$unwind': {
                    'path': '$apartments'
                }
            }, {
                '$project': {
                    '_id': 0, 
                    'buildingName': 1, 
                    'City':1,
                    'apartments.rentalPrice':1
                }
            }
        ])
        for data in result:
            agg_data.update({'buildingName':data['buildingName'],'City':data['City'],'rentalPrice':data['apartments']['rentalPrice']})
            report_data.append(agg_data)
            agg_data = {}
        return report_data
    except Exception as e:
        print("\n Error in aggregation due to exception {} ".format(e))
        return None
