# -----------------------------------
# pip install Faker
# https://pypi.org/project/Faker/
# -----------------------------------

from flask import Flask, render_template, redirect
from faker import Faker
import sqlite3

# connect to db and get cursor
connection = sqlite3.connect("data/data.db", check_same_thread=False)
cursor = connection.cursor()

# web application
app = Flask(__name__)

# landing page
@app.route('/')
def home():
    # ---------------
    #    YOUR CODE
    # ---------------
    return 'Hello!'    

# create person
@app.route('/create')
def create():
    fake = Faker()

    # ---------------
    #    YOUR CODE
    # ---------------

    # redict to the landing page
    return redirect('/')

# delete all entries
@app.route('/clear')
def clear():

    # ---------------
    #    YOUR CODE
    # ---------------

    # redict to the landing page
    return redirect('/')


# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)