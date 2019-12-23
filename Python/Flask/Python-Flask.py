import flask
import sqlite3
import os
import werkzeug.utils
import db_writer
from werkzeug.utils import secure_filename
from flask import Flask, url_for, request, render_template, redirect, make_response, escape, session

folder = "/home/pi/Desktop/Python Flask/uploads"
extensions = set(['txt', 'jpg', 'png', 'py'])
app = Flask(__name__)
app.secret_key = "\xa7o\xce\xe8\x80&\xb7Qc/b\x89TT\xda\x05\xd9\xae\xe50\x06\xcd\xad" 
# Bitte diesen Schlüssel durch einen anderen erstetzen da dieser hier öffentlich ist!!!

def allowed(filename):
    return '.' in filename and filename.rsplit(".", 1)[1].lower() in extensions

@app.route("/")
def index():
    return '<a href="' + url_for("hello", name="World") + '">Lass dich grüßen </a>'

@app.route("/hello/<string:name>")
def hello(name):
    return "Hello " + name + "!"

@app.route("/http")
def http_index():
    return render_template('http.html', fantasie="Geile Tutorials")

@app.route("/login", methods=['POST', 'GET'])
def login():
    name = ""
    cookie = request.cookies.get('username')
    if cookie is not None:
        return "Hallo " + cookie + "!"
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args.get('name')
    resp = make_response("Hello " + name + "!")
    resp.set_cookie("username", name)
    return resp
# Einfacher Demonstration wie einfach man Cookies erstellen kann

@app.route("/werbung")
def werbung():
    return render_template('werbung.html')
# Hier mache ich werbung für jemanden der mir das Programmieren sozusagen beigebracht hat

@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if allowed(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(folder, filename))
            return redirect(request.url)
    return render_template('upload.html')
# Demonstration wie man sachen uploaden kann 

@app.route("/sessions", methods=['GET', 'POST'])
def sessions():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(request.url)
    else:
        if 'name' in session:
            return "Hallo " + escape(session['name'])
        else:
            return render_template('sessions.html')
        
@app.route("/logout")
def logout():
    session.pop('name', None)
    return redirect(url_for('sessions'))

@app.route("/db_reg", methods=['GET', 'POST'])
def reg_db():
    if request.method == 'POST':
        db_writer.write_db(request.form['username'], request.form['passwd'])
        return "Sie sind nun registriert"
    else:
        return render_template('database_login.html')
# Einfacher Login code

@app.route("/credits")
def credits():
    return render_template('thanks.html')
# Diese personen haben mir geholfen beim aufbau dieses scriptes

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=80, debug=True)
# debug = false! Falls diesen Code jemand verwenden will und es nicht mehr nur entwickelt

# Und bitte wenn ihr dies hier verwenden wollt es sicherer machen es gibt eine ganze menge exploits im Internet mit denen man
# diesen Server hacken könnte
