import os
from flask import Flask, request, render_template, session, redirect
from lib.database_connection import get_flask_database_connection
from lib.users.user_repository import User_Repository
from lib.rooms.room_repository import Room_Repository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


