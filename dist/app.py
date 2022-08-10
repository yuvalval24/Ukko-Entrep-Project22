from flask import Flask, redirect, request, render_template, url_for
from flask import session as login_session
import pyrebase



config = {
  "apiKey": "AIzaSyBIY-LB6X66OoVFNi27eZcVPCpreDN7C-Y",
  "authDomain": "entrep-site-summer-2022.firebaseapp.com",
  "databaseURL": "https://entrep-site-summer-2022-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "entrep-site-summer-2022",
  "storageBucket": "entrep-site-summer-2022.appspot.com",
  "messagingSenderId": "1077886875371",
  "appId": "1:1077886875371:web:2b56572f5a95868b6730ae",
  "measurementId": "G-XE5XPTY1JD",
  "databaseURL" : "https://entrep-site-summer-2022-default-rtdb.europe-west1.firebasedatabase.app"
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


@app.route('/', methods = ["get", "post"])
def home():
    print(request.method)
    if request.method == "POST":
        try:
            email = request.form["email"]
            password = request.form["password"]
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
        except:
            print("not sign in")
        try:
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            message = request.form["message"]
            admin = (request.form["code"] == "Ukko2022")
            # print(name+"\n"+email+"\n"+password+"\n"+message)
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            db.child('Users').child(login_session["user"]["localId"]).set({"email":email, "password":password, "name":name, "message":message, "admin":admin})
        except:
            print("not sign up")
    return render_template("post.html", logged = (len(login_session)>0))

@app.route('/Q&A', methods = ["get", "post"])
def QnA():
    if request.method == "POST":
        try:
            print("post")
            name = request.form["name"]
            print("name")
            email = request.form["email"]
            print("email")
            question = request.form["question"]
            print("question")
            db.child("Requests").push({"name":name, "email":email,"question":question, "status":"unresolved"})
            print("submitted")
        except:
            print("something went wrong")
    return render_template("about.html", logged = (len(login_session)>0))

@app.route('/media', methods = ["get", "post"])
def media():
    return render_template("index.html", logged = (len(login_session)>0))

@app.route('/client-questions', methods = ["get", "post"])
def sign():
    questions = dict(db.child("Requests").get().val())
    print(questions)
    return render_template("contact.html", logged = (len(login_session)>0), questions =questions, keys=list(questions.keys()))

@app.route('/out', methods = ["get", "post"])
def out():
    login_session.clear()
    return redirect("/")

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)