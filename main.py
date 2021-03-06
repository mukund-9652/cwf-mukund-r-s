import os
from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'),
            debug=bool(os.environ.get('DEVELOPMENT')))