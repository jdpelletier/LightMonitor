import os
import datetime

from werkzeug.urls import url_parse
from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap

from config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app)

from home import home
from history import history

@app.route('/',methods=['POST', 'GET'])
def home_():
    parent_directory = "/home/pi/Desktop/Apps/FireBeetleTesting/LightMonitor/TestData/"
    today = datetime.date.today()
    todaystr = today.isoformat()
    path = os.path.join(parent_directory, todaystr)
    filepath = os.path.join(str(path), "dataFile.txt")
    return home(filepath)

@app.route('/history',methods=['POST', 'GET'])
def history_():
    parent_directory = "/home/pi/Desktop/Apps/FireBeetleTesting/LightMonitor/TestData/"
    today = datetime.date.today()
    day = request.form.get("day", str(today.day))
    if len(day) == 1:
        day = "0" + day
    month = request.form.get("month", str(today.month))
    if len(month) == 1:
        month = "0" + month
    year = request.form.get("year", str(today.year))
    daystring = f"{year}-{month}-{day}"
    path = parent_directory + daystring
    filepath = os.path.join(str(path), "dataFile.txt")
    submit = request.form.get("submit")
    if submit:
        return history(filepath, daystring, submit)
    return history(filepath, daystring, submit)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=50009)
