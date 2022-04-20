"""
Code created by Sylvester Francis
Student ID : 8735728
Created date : 01 March 2022
Last Modified date : 01 March 2022
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
c_name = client["users"] # c_name => Collection Name
user_list = []

'''Signup function
Purpose: The below function is used to create a user 
Params : None
Return value : None
'''
def signup(data):
    try:  
        data_inserted = db.insert_into_collection(c_name,data)
        return data_inserted
    except Exception as e:
        print("\n Error signing up to the system due to exception {} ".format(e))
        return None

'''Login function
Purpose: The below function is used to login a user 
Params : None
Return value : Boolean
'''
def login(query):
    try:
        user = db.get_one_record(c_name,query)
        return user
    except Exception as e:
        print("\n Error logging in to the system due to exception {} ".format(e))
        return None



''' Add function isloggedin '''
'''Add function  issignedup'''

'''Get one user information
Purpose: The below function is used to return a  single user data 
Params : None
Return value : None
'''
def get_one_user(query):
    try:
        user = db.get_one_record(c_name,query)
        return user
    except Exception as e:
        print("\n User not found in collection {}, exception {}".format(c_name,e))

'''Get multiple user information
Purpose: The below function is used to return multiple user data
Params : None
Return value : user_list -> List of all the users present in the collection
'''
def get_multiple_users(query = {}):
    global user_list
    users = db.get_many_records(c_name,query)
    for user in users:
        user_list.append(user)
    return user_list

'''Update user information
Purpose: The below function is used to update user data
Params : None
Return value : Boolean
'''
def update_user(query,data):
    try:
        data_updated = db.update_one_record(c_name,data,query)
        print(data_updated)
        return data_updated
    except Exception as  e:
        print("\n Error updating the user due to exception {} ".format(e))
        return None

'''Delete user information
Purpose: The below function is used to update user data
Params : None
Return value : Boolean
'''
def delete_user(query):
    try:
        data_deleted = db.delete_one_record(c_name,query)
        print(data_deleted)
        return data_deleted
    except Exception as e:
        print("\n Error deleting the user due to exception {} ".format(e))
        return None

