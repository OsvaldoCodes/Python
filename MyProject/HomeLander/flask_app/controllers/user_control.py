from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.property_model import Property
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/register_page')
def registration_page():
    return render_template("register.html")


@app.route('/register', methods=['POST'])
def register():
    if not User.validation(request.form):
        return render_template('register.html')
    info = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "dob": request.form['dob'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }

    id = User.save(info)
    session['user_id'] = id

    return redirect('/register_success')


@app.route('/register_success')
def register_success():
    if "user_id" not in session:
        return redirect('/register_page')
    info = {
        'id': session['user_id']
    }
    return render_template("home.html", user=User.select_with_id(info), properties=Property.select_all_properties())


@app.route('/login_page')
def login_page():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    user = User.select_with_email(request.form)

    if not user:
        flash("Email not valid", "login_message")
        return redirect('/login_page')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Password not valid", "login_message")
        return redirect('/login_page')
    session['user_id'] = user.id
    return redirect('/login_success')


@app.route('/login_success')
def login_success():
    if "user_id" not in session:
        return redirect('/login_page')
    info = {
        'id': session['user_id']
    }
    return render_template("home.html", user=User.select_with_id(info), properties=Property.select_all_properties())


@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/logout')
    info = {
        'id': session['user_id']
    }
    return render_template("home.html", user=User.select_with_id(info), properties=Property.select_all_properties())


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/delete_account')
def delete_user_account():
    if 'user_id' not in session:
        return redirect('/logout')

    user_id = session['user_id']
    User.delete_user_account({'id': user_id})
    session.clear()

    return redirect('/')


@app.route('/change_password_page')
def change_password_change():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('change_password.html')


@app.route('/change_password', methods=['POST'])
def change_password():
    if 'user_id' not in session:
        return redirect('/logout')

    password = request.form['password']
    if password == '':
        flash("Please enter a password", "register_message")
        return render_template('change_password.html', user=User.select_with_id({'id': session['user_id']}))
    if not User.change_password_validation(request.form):
        data = {"id": session['user_id']}
        return render_template('change_password.html', user=User.select_with_id(data))
    info = {
        "id": session['user_id'],
        "password": bcrypt.generate_password_hash(password)
    }

    User.change_password(info)

    return redirect('/home')
