'''

'''
class User:
    def __init__(self, username, email, password):
        self.username = username 
        self.email = email
        self.password = password
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__