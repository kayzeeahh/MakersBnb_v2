'''
'''

class Room:
    def __init__(self, title, description, location, host, dates_available):
        self.host = host
        self.title = title
        self.description = description
        self.location = location
        self.dates_available = dates_available
        self.requestees = []
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__