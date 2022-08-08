from flask import Flask, redirect, request, render_template, url_for
from flask import session as login_session
import pyrebase



config = {
  "apiKey": "AIzaSyD1rctb8fdxnTAq_MM4m010BaZKk4NR4Go",
  "authDomain": "personal-project-seddit-y2s.firebaseapp.com",
  "databaseURL": "https://personal-project-seddit-y2s-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "personal-project-seddit-y2s",
  "storageBucket": "personal-project-seddit-y2s.appspot.com",
  "messagingSenderId": "552845203678",
  "appId": "1:552845203678:web:3e4f353775f5bd3e398a4f",
  "measurementId": "G-M9L3JDSZ5D",
  "databaseURL" : "https://personal-project-seddit-y2s-default-rtdb.europe-west1.firebasedatabase.app"
}

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)


app.config["SECRET_KEY"] = "awekfhnqwepiou"
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


@app.route('/')
def home():
  return render_template("index.html")

@app.route('/Q&A')
def QnA():
  return render_template("about.html")

@app.route('/media')
def media():
  return render_template("contact.html")

@app.route('/sign')
def sign():
  return render_template("post.html")

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)