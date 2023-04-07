from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo_model import Dojo


@app.route('/')
def start():
    return redirect('/home')

@app.route('/home')
def home():
    dojos = Dojo.select_all_from_dojos()
    return render_template("home.html",dojo_list = dojos)


@app.route('/create_dojo',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/home')

@app.route('/show_dojo/<int:id>')
def show_dojo(id):
    info = {
        "id": id
    }
    return render_template('show_dojo.html', dojo=Dojo.ninjas_in_dojo(info))