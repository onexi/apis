import os
import openai
import urllib.request
from flask import Flask, render_template, redirect, request, send_file
from faker import Faker

# web application
app = Flask(__name__)

# abel_user
openai.api_key = "YOUR-KEY"

# landing page
@app.route('/')
def home():
    return render_template('index.html')    

@app.route('/create', methods=['POST'])
def create():
    # ---------------
    #    YOUR CODE
    # ---------------

    # redirect to landing page
    return redirect('/')


# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)
