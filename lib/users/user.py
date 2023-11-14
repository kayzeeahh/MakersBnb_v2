'''

'''
class User:
    def __init__(self, username, email, password):
        self.username = username 
        self.email = email
        self.password = password
        self.logged_in = True
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def logout(self):
        self.logged_in = False