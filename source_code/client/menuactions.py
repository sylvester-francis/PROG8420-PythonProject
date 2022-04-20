"""
Code created by Sylvester Francis
Student ID : 8735728
Created date : 26 March 2022
Last Modified date : 04 April 2022
Last Modified by  : Parvathy Suresh
"""

import backend.User as user
import backend.apartment as apartment
import backend.Building as building
import backend.RentalInfo as rental
from bson.objectid import ObjectId


'''Tenant Actions'''
def viewProfile(data):
    q = {}
    q['username'] = data['username']
    q['password'] = data['password']
    current_User = user.get_one_user(q)
    print("\n ******************************User Details***************************************** \n")
    print("\n First Name : {0} \n Last Name: {1} \n Email: {2} \n User name: {3} \n Phone Number: {4} ".format(current_User['FirstName'],current_User['LastName'],current_User['email'],current_User['username'],current_User['phoneNumber']))
    print("\n ********************************************************************************** \n")
def viewapartment(data):
    q = {}
    q['userId'] = ObjectId(data['_id'])
    current_Apartment = apartment.get_apartment_info(q)
    if current_Apartment!= None:
        print("\n ******************************Apartment Details***************************************** \n")
        print("\n UnitType : {0} \n rentalPrice: {1} \n NoOfWashrooms: {2} \n IsFurnished: {3} \n Has Ensuite Laundry: {4} ".format(current_Apartment['unitType'],current_Apartment['rentalPrice'],current_Apartment['noOfWashrooms'],current_Apartment['isFurnished'],current_Apartment['hasEnsuiteLaundry']))
        print("\n ********************************************************************************** \n")
    else:
        print("\n Apartment Not Found \n")

#TODO : For Parvathy
def raise_service_req():
    print("\n raise service req called")

#TODO : For Parvathy
def raise_sublet_req():
    print("\n raise sublet req called")

def pay_rent(data):
    error_entry = True
    while error_entry:
        try:
            amount = input("Enter the rent amount to pay: ")
            amount = int(amount)
        except ValueError:
            continue
        else:
            error_entry = False
            q = {}
            q['userId'] = ObjectId(data['_id'])
            current_Apartment = apartment.get_apartment_info(q)
            if current_Apartment!= None:
                rent_Price = current_Apartment['rentalPrice']
                res = [int(i) for i in rent_Price.split() if i.isdigit()]
                if (amount < res[0] or amount > res[0]):
                    print("Please pay the rent amount ${0}".format(res[0]))
                    error_entry = True
                else:
                    print("Rent amount paid successfully!!")
                    error_entry = False
            else:
                print("\n Apartment Not Found \n")

'''Owner Actions'''
# TODO : FOR RACHEL
def BuildingInfo():
    print("\n Building info called")


def GenReport():
    print("\n Gen report called")


def CheckEmpInfo(data):
    q = {}
    q['_id'] = ObjectId(data['_id'])
    current_User = user.get_one_user(q)
    query = {}
    query['buildingId'] = current_User['buildingId']
    query['userType'] = "Staff"
    staff_info = user.get_multiple_users(query)
    for index,item in enumerate(staff_info):
        print("\n ******************************Details of Staff - {0} ********************************************* \n".format(index+1))
        print("\n FirstName : {0} \n LastName: {1} \n Email: {2} \n PhoneNumber: {3} \n ".format(item['FirstName'],item['LastName'],item['email'],item['phoneNumber']))
    print("\n ********************************************************************************** \n")


def DisplayRentInfo(data):
    q = {}
    query_building = {}
    query_rental = {}
    q['_id'] = ObjectId(data['_id'])
    current_User = user.get_one_user(q)
    query_building['_id'] = current_User['buildingId']
    current_Building = building.get_building_info(query_building)
    query_rental['buildingId'] =  current_User['buildingId']
    current_rental = rental.get_one_rentalInfo(query_rental)
    print("\n ******************************Rental information ********************************************* \n")
    print("\n Building Name : {0} \n Rental Period : {1} \n Rent Paid: {2} \n Advance Paid: {3} \n Deposit Paid: {4} \n Rent due on: {5} \n".format(current_Building['buildingName'],current_rental['rentalPeriod'],current_rental['rentPaid'],current_rental['advancePaid'],current_rental['depositPaid'],current_rental['rentDueOn']))


#TODO : Print statement to be modified - Rachel
def DisplayApartmentInformation(data):
    print("\n DisplayApartmentInfomation called")
    q = {}
    query_building = {}
    query_apartment = {}
    q['_id'] = ObjectId(data['_id'])
    current_User = user.get_one_user(q)
    query_building['_id'] = current_User['buildingId']
    query_apartment['buildingId'] = current_User['buildingId']
    current_Building = building.get_building_info(query_building)
    current_apartment = apartment.get_multiple_apartmentInfo(query_apartment)
    print("\n ******************************Apartment information ********************************************* \n")
    print("\n Building Name : {0} \n Rental Period : {1} \n Rent Paid: {2} \n Advance Paid: {3} \n Deposit Paid: {4} \n Rent due on: {5} \n".format(current_Building['buildingName'],current_rental['rentalPeriod'],current_rental['rentPaid'],current_rental['advancePaid'],current_rental['depositPaid'],current_rental['rentDueOn']))


    
'''Staff Actions'''
#TODO : For Parvathy
def check_sublease():
    print("\n Check sublease called")
#TODO : For Parvathy
def check_service():
    print("\n Check service called")

#TODO : For Rachel  
def display_apartment(data):
    print("\n DisplayApartmentInfomation called")
    q = {}
    query_building = {}
    query_apartment = {}
    q['_id'] = ObjectId(data['_id'])
    current_User = user.get_one_user(q)
    query_building['_id'] = current_User['buildingId']
    query_apartment['buildingId'] = current_User['buildingId']
    current_Building = building.get_building_info(query_building)
    current_apartment = apartment.get_multiple_apartmentInfo(query_apartment)
    print("\n ******************************Apartment information ********************************************* \n")
    print("\n Building Name : {0} \n Rental Period : {1} \n Rent Paid: {2} \n Advance Paid: {3} \n Deposit Paid: {4} \n Rent due on: {5} \n".format(current_Building['buildingName'],current_rental['rentalPeriod'],current_rental['rentPaid'],current_rental['advancePaid'],current_rental['depositPaid'],current_rental['rentDueOn']))



