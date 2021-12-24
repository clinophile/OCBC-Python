import re
from flask import Flask
from markupsafe import escape
from flask import request
app = Flask(__name__) #__name__ adalah atribut

@app.route('/')
def hello_world() :
    return 'Hello, World!'

##############ROUTING##################
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World <br> <h1>(Home)</h1>'

@app.route('/user/<username>')
def show_user_profile(username):    
    # show the user profile for that user    
    return f'Hi, this is user {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):    
    # show the post with the given id, the id is an integer    
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):    
    # show the subpath after /path/    
    return f'Subpath {escape(subpath)}'



if __name__ == '__main__' :
    app.run()