from flask import Flask, redirect, render_template, request, url_for
import time
import json
from worker import *

app = Flask(__name__)
app.register_error_handler(404, lambda error: "Page not fucking found!")

'''
@app.route('/<name>', methods = ["POST", "GET"])
def home(name):
    if request.method == "POST":
        print("post")
        user = request.form["nm" name din form]
        return redirect(url_for("user", usr=user))
'''

@app.route('/style.css')
def styles():
    return render_template('css/style.css')

@app.route('/sysdata')
def systemdata():
    data = GetSystemData()
    return str(json.dumps(data))

@app.route('/websitehost')
def websitehost():
    return render_template("websitehost.html")

@app.route('/peakyblinders')
def peakyblindersredirect():
    return redirect("http://192.168.43.43:7000", code=302)

@app.route('/performante')
def performanteTimpReal():
    return render_template("performante.html", temp = 10)


@app.route('/home')
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

