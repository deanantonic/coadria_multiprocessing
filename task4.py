#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
db = SQLAlchemy(app)



class Task4(db.Model):

    __tablename__ = "task4"

    id = db.Column(db.Integer, primary_key=True)
    process_id = db.Column(db.Integer)
    message = db.Column(db.String(50))


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://dean:dean@localhost/task4'
db.create_all()


@app.route('/')
def index():
    if request.method == "GET":
        return render_template("main_page.html", task4=Task4.query.all())
    return redirect(url_for('index'))




app.run(debug=True, port=8000, host='localhost')


























