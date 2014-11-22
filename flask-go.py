# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

DEBUG = True
MONGO_DBNAME = "mydb"
app.config.from_object(__name__)

mongo = PyMongo(app)

@app.route('/')
def homepage():
    hd_health = mongo.db.hdhealth.find_one_or_404({"status" : "good"})
    #print hd_health

    return render_template('index.html', hd_health=hd_health)

if "__main__" == __name__:
    app.run()
