import re
from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__) #__name__ adalah atribut

@app.route('/')
def hello_world() :
    return 'Hello, World!'

@app.route('/login', methods=['GET'])
def login():    
    if request.method == 'GET':        
        return do_the_login()

def do_the_login() :
    return f"Do the login:: used HTTP request is {request.method}"

if __name__ == '__main__' :
    app.run()