import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours

    Arg:
        unittest.TestCase:Test case class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        setUp method to run before each test case
        '''

        #create a credential obj
        self.new_credential=Credential("Keith","eith","Charles","arles")
        
    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        Credential.credential_list=[]


    def test_init(self):
        '''
        test init test case to test if the obj is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"Keith")
        self.assertEqual(self.new_credential.user_password,"eith")
        self.assertEqual(self.new_credential.credential_name,"Charles")
        self.assertEqual(self.new_credential.credential_password,"arles")
        

def test_save_credential(self):
        '''
        test_save_credential to test if the credential obj is saved into the credential list
        '''

        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)
