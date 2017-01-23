#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dean:dean@localhost/task4'


db = SQLAlchemy(app)
db.create_all()


class Task4(db.Model):

    __tablename__ = "task4"

    id = db.Column(db.Integer, primary_key=True)
    process_id = db.Column(db.Integer)
    message = db.Column(db.String(50))




@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", task4=Task4.query.all())

    task4 = Task4(content=request.form["contents"])
    db.session.add(task4)
    db.session.commit()
    return redirect(url_for('index'))




app.run(debug=True, port=8000, host='localhost')