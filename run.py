#!/usr/bin/env python3.8

'''
Main file that runs the application

Creating functions to implement behaviours that have been created

Import User Class from user
Import Credential class from credential

'''

from user import User
from credential import Credential

def create_user(name,password):
    '''
    Function to create a new user

    Args:
        name:name user wants to set for the passlocker account
        password:the password user wants for the passlocker account

    '''

    new_user=User(name,password)

    return new_user

def save_user(user):
    '''
    Function to save a new user account

    Arg:
        user:newly created user account to be saved
    '''

    user.save_user()
    
def display_users():
    '''
    Functionn that returns the users using pass_locker
    '''

    return User.display_users()

def user_log_in(name,password):
    '''
    Function that allows a user to log in to their    credential account

    Args:
        name:Name of the user who created the acount
        password:Password the user used to create the account
    '''
    verified_user=User.user_verified(name,password)
    
    return verified_user

def create_credential(user_name,user_password,credential_name,credential_password):
    
    '''
    Function to create a credential

    Args:
        user_name:Name of account holder
        user_password:Password for the pass locker account
        credential_name:Name of the account to save
        credential_password:Password of the account to save
    '''

    new_credential=Credential(user_name,user_password,credential_name,credential_password)

    return new_credential

def save_credential(credential):
    '''
    Function to save a credential

    Args:
        credential:the credential to be saved
    '''

    credential.save_credential()

def generated_password(pass_length):
    '''
    Function that generate a random password for a user's credential

    Args:
        pass_length:Length the user wants the password to be 
    '''
    password=Credential.generate_password(pass_length)

    return password 

def delete_credential(credential):
    '''
    Function that deletes a credential

    Args:
        credential:credential to be deleted
    '''

    credential.delete_credential()

def display_credentials(user_name,user_password):
    '''
    Function that returns all the users saved credentials
    '''

    return Credential.display_credential(user_name,user_password)     

def find_by_name(user_name,user_password,credential_name):
    '''
    Function that find a credential by name and returns the credential
    '''

    return Credential.find_by_name(user_name,user_password,credential_name)



def credential_exists(user_name,user_password,credential_name):
    '''
    Function that find a credential by name and returns the credential
    '''

    return Credential.credential_exists(user_name,user_password,credential_name)

    
    
    
def main():
    '''
    Function running the passlocker app
    '''
    print("-"*33)
    print("Hello!Welcome to PassWord Locker!")
    print("-"*33)
    print("\n")

    while True:
        print('''Use these short codes to get around \n
            ShortCodes: \n
                cu:create new pass locker account \n
                du:display users using pass locker\n
                lg:login to your account \n
                ex:exit the app          ''')
        #take user input
        short_code = input().lower()

        if short_code == "cu":
            '''
            Creates a new user account
            '''
            print("-"*27)
            print("New Password Locker Account")
            print("-"*27)
            print("\n")

            print("Enter User Name")
            user_name = input()

            print("Enter Account Password")
            user_password = input()

            save_user( create_user(user_name,user_password) ) #create and save user
            print('\n')
            print(f"Password Locker Account for {user_name} created succesfully!!")
            print('\n')