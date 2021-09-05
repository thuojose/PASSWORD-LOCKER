

class User:
    
    '''
     Class that generates a new instance of a passlocker user
    
    __init__method that helps us to define properties for our objects

    Args:
        name:New user name
        password:New user password
    '''
    user_list=[]

    def __init__(self,name,password):
        
        self.name=name
        self.password=password 
        
    def save_user(self):
        '''
        save user method that saves user obj into user list
        '''
        User.user_list.append(self)
        
    @classmethod
    def display_users(cls):
        '''
        Method that returns users using the password locker app
        '''
        return cls.user_list  
