from flask import Flask, request
from deta import Deta

# flask app
app = Flask(__name__)

# contact form base
form_db = Deta().Base("contact-form")

@app.route("/", methods=["POST"])
def save_form_data():
    form_db.put({
        # flask sends a 400 automatically if there is a KeyError 
        "name": request.form["name"],
        "email": request.form["email"],
        "message": request.form["message"]
    })
    return "ok", 201
