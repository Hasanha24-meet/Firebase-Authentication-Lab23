from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

firebaseConfig = {
  "piKey": "AIzaSyCaHdk3wWeN9FkjKd9N6lcQGnOzI-xtXk8",
  "authDomain": "example-f07b0.firebaseapp.com",
  "projectId": "example-f07b0",
  "storageBucket": "example-f07b0.appspot.com",
  "messagingSenderId": "28514512477",
  "appId": "1:28514512477:web:0e247450036923752f27b4",
  "measurementId": "G-RQ1FK5CWYY",
  "databaseURL": ""
}

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/signin', methods=['GET', 'POST'])
def signin():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
       except:
           error = "Authentication failed"
   return render_template("add_tweet.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('home'))
       except:
           error = "Authentication failed"
   return render_template("add_tweet.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)