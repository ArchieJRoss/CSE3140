from flask import Flask

app = Flask(__name__)

@app.route("/")
def basic_website():
    return "<p>Team 2: Ross Archie and Jiang Tommy</p>"

