from flask import render_template
from app import app
from systeminfo.main import main
@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'Tom'
    returnDict['title'] = 'Home'
    returnDict['platform'] = main()
    return render_template("index.html", **returnDict)
