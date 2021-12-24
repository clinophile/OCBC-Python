from flask import request
import re
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__) #__name__ adalah atribut


@app.route('/')
def hello_world() :
    return 'Hello, World!'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):    
    return render_template('hello.html', name=name)

if __name__ == '__main__' :
    app.run(debug=True)