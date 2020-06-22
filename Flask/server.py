from flask import Flask, redirect, render_template, request, url_for
import json
from worker import *

app = Flask(__name__)
app.register_error_handler(404, lambda error: render_template("notfound.html"))


@app.route('/etilotestinit')
def etilotestsequenceinit():
    InitializeSequence()
    return "done"

@app.route('/distantacartela')
def distance():
    data = GetDistance()
    return str(json.dumps(data))

@app.route('/cronometter/<time>')
def cronometter(time):
    SetTime(time)
    return "time"

@app.route('/detectiealcool')
def alcool():
    alcool = GetAlcool()
    return str(json.dumps(alcool))

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
    return redirect("http://192.168.100.231:7000", code=302)

@app.route('/performante')
def performanteTimpReal():
    return render_template("performante.html")

@app.route('/monitor')
def monitor():
    return render_template("monitor.html")

@app.route('/etilotest')
def etilotest():
    return render_template("etilotest.html")

@app.route('/datesenzortemp')
def DHT11():
    data = GetTempHumidity()
    return str(json.dumps(data))

@app.route('/home')
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

