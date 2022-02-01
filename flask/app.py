from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lyuba'}
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'Beautiful day in Portland!'
            },
            {
                'author': {'username': 'Susan'},
                'body': 'The Avengers movie was so cool!'
            }
        ]    
    return render_template('index.html', title='Home', user=user, posts=posts)

app.run(host="0.0.0.0",port=5000,debug=True)