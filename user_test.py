import unittest
from user import User #importing the User class

class TestUser(unittest.TestCase):
    '''
     Test class that defines test cases for the user class behaviours

 Args:
        unnitest.TestCase:TestCase class that helps in creating test cases
    '''

def setUp(self):
     '''
     Set up method to run before each test case
     '''
     self.new_user=User("Joe","3560")
        
def test_init(self):
    '''
    test init test case to test if the obj is initialized correctly
    '''
    self.assertEqual(self.new_user.name,"Joe")
    self.assertEqual(self.new_user.password,"3560")
    
def test_save_user(self):
    '''
    test save user to test if the user object is saved into the user list
    '''
    self.new_user.save_user() #saving a user
    self.assertEqual(len(User.user_list),1)