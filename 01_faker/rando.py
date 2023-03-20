# -------------------------------
# you can great a person at
#   https://randomuser.me/api/
# -------------------------------

# import package
from flask import Flask, jsonify
import urllib.request

# create application instance
app = Flask(__name__)

# root route - create and return user
@app.route('/')
def hello_world():
    # ---------------
    #    YOUR CODE   
    # ---------------
    return "Hello!"

# start server - note the port is 3000
if __name__ == '__main__':
    app.run(debug=True, port=3000)


# -----------------------------------------------
# Requesting Multiple Users
# https://randomuser.me/api/?results=5

# Specifying a gender
# https://randomuser.me/api/?gender=female
# -----------------------------------------------