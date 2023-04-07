from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.sighting_model import Sighting
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def start():
    return redirect('/home')


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/register', methods=['POST'])
def register():
    if not User.validation(request.form):
        return redirect('/')

    info = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(info)
    session['user_id'] = id

    return redirect('/success')


@app.route('/success')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    info = {
        'id': session['user_id']
    }
    return render_template("sightings.html", user=User.select_with_id(info), sightings=Sighting.select_all_sightings())


@app.route('/login', methods=['POST'])
def login():
    user = User.select_with_email(request.form)

    if not user:
        flash("Email not valid", "login_message")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Password not valid", "login_message")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/success')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
