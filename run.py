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
