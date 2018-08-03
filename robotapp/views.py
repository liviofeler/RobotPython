#/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask,render_template, request

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return "Hello world !"

@app.route('/formulaire/', methods=['GET','POST'])
def formulaire():
    if request.method == 'GET':
        return  render_template ('formulaire.html')
    else:
        return "Vous avez envoyé: {msg}".format(msg=request.form['textarea'])


if __name__ == "__main__":
    app.run(debug=True)
