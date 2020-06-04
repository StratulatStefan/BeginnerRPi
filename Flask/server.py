from flask import Flask, redirect, render_template, request, url_for
import json
from worker import *

app = Flask(__name__)
app.register_error_handler(404, lambda error: render_template("notfound.html"))

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
    return render_template("performante.html")

@app.route('/monitor')
def monitor():
    return render_template("monitor.html")

@app.route('/etilotest')
def etilotest():
    return render_template("etilotest.html")

@app.route('/datesenzortempsigaz')
def DHT11MQ2():
    return {"temp" : "Nimic inca" ,"umiditate" : "Nimic inca", "gaz" : "Nimic inca"}


@app.route('/home')
@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

