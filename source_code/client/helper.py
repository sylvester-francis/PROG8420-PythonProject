"""
Code created by Sylvester Francis
Student ID : 8735728
Created date : 26 March 2022
Last Modified date : 26 February 2022
Last Modified by  : Sylvester Francis
"""

from os import system, name
from cryptography.fernet import Fernet
key = b'stVG3hXK3GXlz-mgzzru-BmcMcNyH27TtO4HryqWC-M='
fernet = Fernet(key)

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def encryptPassword(password):
    encMessage = fernet.encrypt(password.encode())
    return encMessage
def decryptPassword(password):
    decMessage = fernet.decrypt(password).decode()
    return decMessage

    
  