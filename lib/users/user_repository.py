from lib.users import User
from flask import request
class User_Repository:
    def __init__(self, connection):
        self._connection = connection
        
    def create(self, request):
        """
        checks for uniquness, throws error code for username or email already exists
        """
        if len(self._connection.execute(
            "SELECT * FROM users WHERE username=%s", [request.form.get("username")])) > 0:
            return "User already exists", 409
        else:
            user = User(
            request.form.get("username"),
            request.form.get("email"),
            request.form.get("password"),
        )
            self._connection.execute(
            "INSERT INTO users "
            + "(username, email, password) "
            + "VALUES (%s, %s, %s,)",
            [user.username, user.email, user.password],
        )
        
    def verify(self, username, password):
        print(
            self._connection.execute(
                "SELECT * FROM users WHERE username=%s AND password=%s",
                [username, password],
            )
        )
        return self._connection.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            [username, password],
        )
        
    def login(self, request):
        username = request.form.get("username")
        password = request.form.get("password")

        userReturn = self.verify(username, password)

        if len(userReturn) > 0:
            userRow = userReturn[0]
            user = User(
                userRow["username"], userRow["email"], userRow["password"]
            )
            user.id = userRow["id"]
            return user.id
        else:
            # user does not exist, return error
            return "error"
    
    def logout(user):
        user.logout()