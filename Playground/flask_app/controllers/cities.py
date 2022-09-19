from flask_app import app
from flask import render_template

@app.route('/play')
def start():
    return render_template("index.html", num=3 , color="cyan")

@app.route('/play/<int:num>')
def makeMore(num):
    return render_template("index.html" , num=num , color = "cyan")

@app.route('/play/<int:num>/<string:color>')
def changeColor(num , color):
    return render_template("index.html" , num=num, color= color)