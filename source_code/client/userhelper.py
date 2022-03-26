"""
Code created by Sylvester Francis
Student ID : 8735728
Created date : 26 March 2022
Last Modified date : 26 February 2022
Last Modified by  : Sylvester Francis
"""
import sys
sys.path.append("..")
import backend.User as user
import backend.Building as building
import backend.apartment as apartment
from getpass import getpass
from helper import clear
from bson.objectid import ObjectId
userTypes = {1:'Tenant',2:'Owner',3:'Staff'}

''' Login helper
Purpose: The below function is used as a helper function for login 
Params : None
Return value : None
'''
def login_helper():
    clear()
    print("\n ********************************************************************************** \n")
    print(" \n Login")
    print("\n ********************************************************************************** \n")
    username = input("\n Enter your username: ")
    password = getpass("\n Enter the password: ")
    print(username,password)

def signup_helper():
    clear()
    print("\n ********************************************************************************** \n")
    print(" \n Signup")
    print("\n ********************************************************************************** \n")
    # firstname = input("\nEnter your First Name: ")
    # lastname  = input("\nEnter your Last Name:  ")
    # email     = input("\n Enter your Email ID:  ") => emailid
    # username  = input("\n Enter your preferred username: ")
    # password  = getpass("\n Enter your password: ") 
    # confirmpassword = getpass("\n Re-enter the password: ")
    # if password == confirmpassword:
    #     print("\n Password matches")
    # else:
    #     print("\n Password doesnot match")
    # select_userType = input("\n Please select the type of user: \n1.Tenant \n2.Owner \n3.Staff \n Please type one of the following options(1,2 or 3)")
    # userType =''
    # if select_userType == '1':
    #     userType = userTypes[1]
    # elif select_userType == '2':
    #     userType= userTypes[2]
    # elif select_userType == '3':
    #     userType= userTypes[3]
    # else:
    #     print("\n Invalid option")
    # phno = input("\n Enter your phone number: ")
    # data = {}
    # # data.update({'FirstName':firstname,'LastName':lastname,'email':email,'username':username,'password':password,'userType':userType,'phoneNumber':phno})
    clear()
    # print("\nHere are the list of buildings available: ")
    buildings = building.get_multiple_buildingInfo()
    building_list = {}
    print("\n ********************************************************************************** \n")
    for index,item in enumerate(buildings):
        print("\n ****************************** General-Details of Building - {0} ********************************************* \n".format(index+1))
        print("\n Name of the building : {0} \n Address: {1} \n City: {2} \n PostalCode: {3} \n Province: {4} ".format(item['buildingName'],item['Address'],item['City'],item['postalCode'],item['province']))
        print("\n ****************************** Facilities of Building - {0} ********************************************* \n".format(index+1))
        print("\n Furnished :{0}, \n Parking : {1}, \n Pet-Friendly: {2}, \n Storage: {3}".format(item['isFurnished'],item['isParkingAvailable'],item['petFriendly'],item['storageAreaAvailable']))
        building_list[index+1] = item['_id']
    print("\n ********************************************************************************** \n")
    noOftries = 0
    remainingTries = 2
    while(noOftries < 3):
        select_building = int(input("\n Enter the building that you are interested in: "))
        if select_building in building_list.keys():
            q = {}
            q['buildingId'] = ObjectId(building_list[select_building])
            q['isAvailable'] = True
            apartmentlist = apartment.get_multiple_apartmentInfo(q)
            if len(apartmentlist) > 0:
                noOftries = 3
            else:
                print("\n Sorry,No apartments available in this building,try again")
                print("\n No of tries remaining {0}".format(remainingTries))
                noOftries += 1
                remainingTries -= 1
                continue
        else:
            if noOftries == 2:
                print("\n Building not found")
            else:
                print("\n Building not found,try again")
                print("\n No of tries remaining {0}".format(remainingTries))    
            noOftries += 1
            remainingTries -= 1
    # for item in apartmentlist:

    

    



    
    

    

