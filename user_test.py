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
    
def test_save_multiple_user(self):
    '''
    test save multiple to check if we can save multiple user obj to our user_list
    '''

    self.new_user.save_user()
    test_user=User("Mbugua","2021")
    test_user.save_user()
    self.asserEqual(len(User.user_list),2)
    
    def tearDown(self):
        '''
        tearDown method that cleans up after each test has run
        '''
        User.user_list=[] 
        
    def test_display_users(self):
        '''
        test_display_users returns list of password locker users
        ''' 

        self.assertEqual(User.display_users(),User.user_list)
        
    def test_login_user(self):
        '''
        test_login_ to login a user
        '''
        #confirms if as valid credentials are entered
        self.new_user.save_user() 
        test_user=User("Henry","2019")
        test_user.save_user()
        logged_in=User.user_verified("Henry","2019")
        
        self.assertTrue(logged_in)  
        
        
        
        
        
        
if __name__=='__main__':
    unittest.main()    