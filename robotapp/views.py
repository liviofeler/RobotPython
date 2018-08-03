#/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask,render_template, request
from torndb import Connection

app = Flask(__name__)
app.config.from_object('config')

db = Connection('127.0.0.1', app.config['DATABASE_NAME'], app.config['DATABASE_USER'], app.config['DATABASE_PASS'])

@app.route('/')
def index():
    return "Hello world !"

@app.route('/formulaire/', methods=['GET','POST'])
def formulaire():
    if request.method == 'GET':
        return  render_template ('formulaire.html')
    else:
        msg = request.form['textarea']
        db.execute("INSERT INTO Test (test) VALUES (%s)",msg)
        return "Vous avez envoyé: {msg}".format(msg=request.form['textarea'])

@app.route('/SQLHelloWorld')
def SQLHelloWorld():
    post = db.get("Select test From Test")
    return post.test


if __name__ == "__main__":
    app.run(debug=True)
