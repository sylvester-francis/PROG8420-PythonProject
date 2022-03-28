"""
Code created by Sylvester Francis
Student ID : 8735728
Created date : 26 March 2022
Last Modified date : 28 March 2022
Last Modified by  : Parvathy Suresh
"""
import re
import sys
sys.path.append("..")
import backend.User as user
import backend.Building as building
import backend.apartment as apartment
from  menuactions import *
from getpass import getpass
from helper import clear,encryptPassword,decryptPassword
from bson.objectid import ObjectId
userTypes = {1:'Tenant',2:'Owner',3:'Staff'}
isloggedin =False

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
    q = {}
    data = {}
    isUser = True

    while isUser:
        try:
            username = input("\n Enter your username: ")
            password = getpass("\n Enter the password: ")
            q['username'] = username
            current_User = user.get_one_user(q)
            if current_User == None:
                raise KeyError("Please enter valid username or password")
            decPassword = decryptPassword(current_User['password'])
            if password!=decPassword:
                raise KeyError("Please enter valid username or password")
        except KeyError as ke:
            print("\n{0}".format(ke))
            continue  
        isUser = False
    data.update({'username':current_User['username'],'_id':current_User['_id'],'password':current_User['password']})
    if current_User['userType'] == userTypes[1]:
        tenant_path(data,'login')
    elif current_User['userType'] == userTypes[2]:
        owner_path(data,'login')
    elif current_User['userType'] == userTypes[3]:
        staff_path(data,'login')

    



''' Signup helper
Purpose: The below function is used as a helper function for signup
Params : None
Return value : issignedup -> Boolean 
'''
def signup_helper():
    clear()
    data = {}
    errorEmail = True
    errorUserName = True
    errorPhone = True
    emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phoneRegex = r"^(\([0-9]{3}\) ?|[0-9]{3}-)[0-9]{3}-[0-9]{4}$"
    print("\n ********************************************************************************** \n")
    print(" \n Signup")
    print("\n ********************************************************************************** \n")
    firstname = input("\nEnter your First Name: ")
    lastname  = input("\nEnter your Last Name:  ")
    while errorEmail:
        try:
            email = input("\nEnter your Email ID:  ")
            if not (re.fullmatch(emailRegex, email)):
                raise KeyError("Please enter valid email address in format abc@abc.com")
        except KeyError as ke:
            print("\n{0}".format(ke))
            continue  
        errorEmail = False
    while errorUserName:
        query = {}
        try:
            username  = input("\nEnter your preferred username: ")
            query['username'] = username
            user_data = user.get_one_user(query)
            if user_data != None:
                raise KeyError("Sorry,Entered UserName is already available, Please choose another username!!!")
        except KeyError as ke:
            print("\n{0}".format(ke))
            continue  
        errorUserName = False
    password  = getpass("\nEnter your password: ") 
    confirmpassword = getpass("\nRe-enter the password: ")
    if password == confirmpassword:
        password = encryptPassword(password)

    else:
        print("\n Password doesnot match")
    while errorPhone:
        try:
            phno = input("\n Enter your phone number: ")
            if not (re.fullmatch(phoneRegex, phno)):
                raise KeyError("Please enter phone number in format xxx-xxx-xxxx")
        except KeyError as ke:
            print("\n{0}".format(ke))
            continue  
        errorPhone = False
    select_userType = input("\n Please select the type of user: \n1.Tenant \n2.Owner \n3.Staff \n Please type one of the following options(1,2 or 3)")
    userType =''
    if select_userType == '1':
        userType = userTypes[1]
        data.update({'FirstName':firstname,'LastName':lastname,'email':email,'username':username,'password':password,'userType':userType,'phoneNumber':phno})
        issignedUp = tenant_path(data,'signup')
    elif select_userType == '2':
        userType= userTypes[2]
        data.update({'FirstName':firstname,'LastName':lastname,'email':email,'username':username,'password':password,'userType':userType,'phoneNumber':phno})
        issignedUp= owner_path(data,'signup')
    elif select_userType == '3':
        userType= userTypes[3]
        data.update({'FirstName':firstname,'LastName':lastname,'email':email,'username':username,'password':password,'userType':userType,'phoneNumber':phno})
        staff_path(data,'signup')
    else:
        print("\n Invalid option")
    return issignedUp



''' Tenant path
Purpose: The below function is used as a added function  for tenant signup 
Params : data -> Dictionary with all user inputs, typeAction -> [login,signup]
Return value : signedup -> Boolean 
'''  

def tenant_path(data,typeAction):
    if typeAction == 'signup':
        signedup = False
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
        clear()
        print("\n ********************************************************************************** \n")
        for index,item in enumerate(apartmentlist):
            print("\n ****************************** Facilities of Apartment - {0} ********************************************* \n".format(index+1))
            print("\n Furnished :{0}, \n No Of Washrooms : {1}, \n Ensuite Washroom: {2}, \n Ensuite Laundry: {3}, \n Rent Price: {4}".format(item['isFurnished'],item['noOfWashrooms'],item['hasEnsuiteWashroom'],item['hasEnsuiteLaundry'],item['rentalPrice']))
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
        data['buildingId'] = building_list[select_building]
        data['apartmentId'] = apartmentid[select_apartment]
        user_obj = user.signup(data)
        if user_obj != None:
            print("\n User signed up successfully")
            signedup = True
            return signedup
        else:
            print("\n Error in signing up User, please try again")
            return signedup
    elif typeAction == 'login':
        tenant_menu(data)



''' Owner path
Purpose: The below function is used as a added function  for owner signup path/login path
Params : data -> Dictionary with all user inputs,typeAction -> [login,signup]
Return value : signedup -> Boolean 
'''  
def owner_path(data,typeAction):
    print("\n Owner path called")
    errorBuilding = True
    if typeAction == 'signup':
        print("\n Owner signup path")
        print("\nHere are the list of buildings available: ") 
        buildings = building.get_multiple_buildingInfo()
        building_list = {}
        print("\n ********************************************************************************** \n")
        for index,item in enumerate(buildings):
            print("\n ****************************** General-Details of Building - {0} ********************************************* \n".format(index+1))
            print("\n Name of the building : {0} \n Address: {1} \n City: {2} \n PostalCode: {3} \n Province: {4} ".format(item['buildingName'],item['Address'],item['City'],item['postalCode'],item['province']))
            building_list[index+1] = item['_id'] 
        print("\n ********************************************************************************** \n")
        while errorBuilding:
            try:
                select_building = int(input("\n Enter the building that you own: "))
                if select_building not in building_list.keys():
                    raise KeyError("Building not found please try again")
                else:
                    data['buildingId'] = building_list[select_building]
            except KeyError as ke:
                print("\n{0}".format(ke))
                continue  
            errorBuilding = False
        user_obj = user.signup(data)
        if user_obj != None:
            print("\n Owner signed up successfully")
            signedup = True
            return signedup
        else:
            print("\n Error in signing up Owner, please try again")
            return signedup
        
                

        
    elif typeAction =='login':
        owner_menu()


''' Staff path
Purpose: The below function is used as a added function  for staff signup 
Params : data -> Dictionary with all user inputs,typeAction -> [login,signup]
Return value : signedup -> Boolean 
'''  
def staff_path(data,typeAction):
    print("\n Staff path called")
    if typeAction == 'signup':
        print("\n Staff signup path")
    elif typeAction == 'login':
        staff_menu()
    

def tenant_menu(data):
    clear()
    menu_selection = True
    print("\n ********************************************************************************** \n")
    print("\n 1. View profile ")
    print("\n 2. View apartment detail ")
    print("\n 3. Raise service request ")
    print("\n 4. Raise sublet request")
    print("\n 5. Pay rent")
    print(" \n Please choose one of the following options to continue")
    while menu_selection:
        try:
            selection = input("\n Enter your choice:")
            if selection == '1':
                viewProfile(data)
            elif selection == '2':
                viewapartment()
            elif selection == '3':
                raise_service_req()
            elif selection == '4':
                raise_sublet_req()
            elif selection == '5':
                pay_rent()
            else:
                raise KeyError('\n Invalid option, try again')
        except KeyError as ke:
            print('\n{0}'.format(ke))
            continue
        menu_selection = False
    
def owner_menu():
    clear()
    menu_selection = True
    print("\n ********************************************************************************** \n")
    print("\n 1. Check building information ")
    print("\n 2. Generate reports ")
    print("\n 3. Check employee information ")
    print("\n 4. Display rent info")
    print("\n 5. Display Apartment Information")
    print(" \n Please choose one of the following options to continue")
    while menu_selection:
        try:
            selection = input("\n Enter your choice:")
            if selection == '1':
                BuildingInfo()
            elif selection == '2':
                GenReport()
            elif selection == '3':
                CheckEmpInfo()
            elif selection == '4':
                DisplayRentInfo()
            elif selection == '5':
                DisplayApartmentInformation()
            else:
                raise KeyError('\n Invalid option, try again')
        except KeyError as ke:
            print('\n{0}'.format(ke))
            continue
        menu_selection = False


def staff_menu():
    clear()
    menu_selection = True
    print("\n ********************************************************************************** \n")
    print("\n 1. Check for sublease requests ")
    print("\n 2. Check for service requests ")
    print("\n 3. Display Apartment information ")
    print(" \n Please choose one of the following options to continue")
    while menu_selection:
        try:
            selection = input("\n Enter your choice:")
            if selection == '1':
                check_sublease()
            elif selection == '2':
                check_service()
            elif selection == '3':
                display_apartment()
            else:
                raise KeyError('\n Invalid option, try again')
        except KeyError as ke:
            print('\n{0}'.format(ke))
            continue
        menu_selection = False




    
    

    

