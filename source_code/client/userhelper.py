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
    data = {}
    print("\n ********************************************************************************** \n")
    print(" \n Signup")
    print("\n ********************************************************************************** \n")
    # firstname = input("\nEnter your First Name: ")
    # lastname  = input("\nEnter your Last Name:  ")
    # email     = input("\n Enter your Email ID:  ") 
    # username  = input("\n Enter your preferred username: ")
    # password  = getpass("\n Enter your password: ") 
    # confirmpassword = getpass("\n Re-enter the password: ")
    # if password == confirmpassword:
    #     print("\n Password matches")
    # else:
    #     print("\n Password doesnot match")
    # phno = input("\n Enter your phone number: ")
    select_userType = input("\n Please select the type of user: \n1.Tenant \n2.Owner \n3.Staff \n Please type one of the following options(1,2 or 3)")
    userType =''
    if select_userType == '1':
        userType = userTypes[1]
        # data.update({'FirstName':firstname,'LastName':lastname,'email':email,'username':username,'password':password,'userType':userType,'phoneNumber':phno})
        tenant_path(data)
    elif select_userType == '2':
        userType= userTypes[2]
        owner_path()
    elif select_userType == '3':
        userType= userTypes[3]
        staff_path()
    else:
        print("\n Invalid option")
    

def tenant_path(data):
    errorApartment = True
    errorBuilding = True
    clear()
    print("\nHere are the list of buildings available: ") 
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
    while errorBuilding:
        try:
            select_building = int(input("\n Enter the building that you are interested in: "))
            if select_building not in building_list.keys():
                raise KeyError("Building not found please try again")
            elif select_building in building_list.keys():
                q = {}
                q['buildingId'] = ObjectId(building_list[select_building])
                q['isAvailable'] = True
                apartmentlist = apartment.get_multiple_apartmentInfo(q)
                if len(apartmentlist) > 0:
                    errorBuilding = False
                else:
                    raise KeyError("Sorry,No apartments available in this building,try again")
        except KeyError as ke:
            print("\n{0}".format(ke))
            continue  
        errorBuilding = False      
    apartmentid = {}
    print("\n ********************************************************************************** \n")
    for index,item in enumerate(apartmentlist):
        print("\n ****************************** Facilities of Apartment - {0} ********************************************* \n".format(index+1))
        print("\n Furnished :{0}, \n No Of Washrooms : {1}, \n Ensuite Washroom: {2}, \n Ensuite Laundry: {3}, \n Rent Price: {4}".format(item['isFurnished'],item['noOfWashrooms'],item['hasEnsuiteWashroom'],item['hasEnsuiteLaundry'],0))
        apartmentid[index+1] = item['_id']
    print("\n ********************************************************************************** \n")
    print("\n ********************************************************************************** \n")
    while errorApartment:
        try:
            select_apartment = int(input("\n Enter the apartment that you are interested in: "))
            if select_apartment not in apartmentid.keys():
                raise KeyError("Apartment not found please try again")
        except KeyError as e:
            print("\n {0}".format(e))
            continue
        errorApartment = False




def owner_path():
    pass
def staff_path():
    pass
    

    



    
    

    

