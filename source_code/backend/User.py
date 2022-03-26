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
query = {}

'''Signup function
Purpose: The below function is used to create a user 
Params : None
Return value : None
'''

#An example of create function
def signup():
    try: 
        data = {
        "FirstName": "Sylvester",
        "LastName": "Francis",
        "email": "sylvester@phoca.cz",
        "username": "sylvester",
        "password": "ABCDEFG",
        "userType": "Tenant",
        "phoneNumber": "548-333-1624",
        "buildingId": ObjectId("621ef1e586ed827ec8845a12")
        } 
        data_inserted = db.insert_into_collection(c_name,data)
        print(data_inserted)
        return data_inserted
    except Exception as e:
        print("\n Error signing up to the system due to exception {} ".format(e.__name__))
        return None

'''Login function
Purpose: The below function is used to login a user 
Params : None
Return value : Boolean
'''
def login():
    try:
        global query
        username = input("\n Enter the username:") 
        password = getpass("\n Enter the password:")
        query["username"] = username
        query["password"] = password
        user = db.get_one_record(c_name,query)
        return user
    except Exception as e:
        print("\n Error logging in to the system due to exception {} ".format(e.__name__))
        return None



''' Add function isloggedin '''
'''Add function  issignedup'''

'''Get one user information
Purpose: The below function is used to return a  single user data 
Params : None
Return value : None
'''
def get_one_user():
    try:
        global query
        lname = "Summerlee"
        query['LastName'] = lname
        user = db.get_one_record(c_name,query)
        query = {}
        return user
    except Exception as e:
        print("\n User not found in collection {}, exception {}".format(c_name,e.__name__))

'''Get multiple user information
Purpose: The below function is used to return multiple user data
Params : None
Return value : user_list -> List of all the users present in the collection
'''
def get_multiple_users():
    global user_list
    users = db.get_many_records(c_name)
    for user in users:
        user_list.append(user)
    return user_list

'''Update user information
Purpose: The below function is used to update user data
Params : None
Return value : Boolean
'''
def update_user():
    try:
        global query
        data = {
        "FirstName": "Sylvester",
        "LastName": "Francis",
        "email": "sylvester@gmail.com",
        "username": "sylvester",
        "password": "ABCDEFG",
        "userType": "Owner",
        "phoneNumber": "548-333-1624",
        "buildingId": ObjectId("621ef1e586ed827ec8845a12")
        }  
        query["FirstName"] = "Sylvester"
        data_updated = db.update_one_record(c_name,data,query)
        print(data_updated)
        query = {}
        return data_updated
    except Exception as  e:
        print("\n Error updating the user due to exception {} ".format(e.__name__))
        return None

'''Delete user information
Purpose: The below function is used to update user data
Params : None
Return value : Boolean
'''
def delete_user():
    try:
        global query
        query["FirstName"] = "Sylvester"
        data_deleted = db.delete_one_record(c_name,query)
        print(data_deleted)
        return data_deleted
    except Exception as e:
        print("\n Error deleting the user due to exception {} ".format(e.__name__))
        return None


if __name__ == "__main__":  
    try:
        data = get_one_user()
        print(data)
        # data = login()
        # if data != None:
            # print(data)
        # else:
            # print(" \n No record found")
        # data = signup()
        # print(data)
        # data = update_user()
        # print(data)
        # data = delete_user()
        # print(data)
    except Exception as e:
        print(e.__name__)
