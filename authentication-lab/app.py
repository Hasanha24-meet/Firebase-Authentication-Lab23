from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyCaHdk3wWeN9FkjKd9N6lcQGnOzI-xtXk8",
  "authDomain": "example-f07b0.firebaseapp.com",
  "projectId": "example-f07b0",
  "storageBucket": "example-f07b0.appspot.com",
  "messagingSenderId": "28514512477",
  "appId": "1:28514512477:web:0e247450036923752f27b4",
  "measurementId": "G-RQ1FK5CWYY",
  "databaseURL": "https://example-f07b0-default-rtdb.europe-west1.firebasedatabase.app/"
}

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


@app.route('/', methods=['GET', 'POST'])
def signin():  
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url('add_tweet'))
        except:
            error = "Authentication Failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        fullname = request.form['fullname']
        password = request.form['password']
        username = request.form['username']
        bio = request.form['bio']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user = {"fullname": fullname, "email": email, "username": username, "bio": bio}
            db.child("Users").child(UID).set(user)
            return redirect(url('add_tweet'))

        except:
            error = "Authentication Failed"
    return render_template("signup.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        try:
            UID = login_session['user']['localId']
            tweet = {"title": title, "text": text, "UID": UID}
            db.child("Tweets").push(tweet)
            return redirect(url('all_tweets'))
        except:
            return "You must be logged in to add a tweet."
    return render_template("add_tweet.html")




if __name__ == '__main__':
    app.run(debug=True)