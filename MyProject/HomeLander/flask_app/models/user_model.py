import datetime
from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:

    def __init__(self, info):
        self.id = info['id']
        self.first_name = info['first_name']
        self.last_name = info['last_name']
        self.dob = info['dob']
        self.email = info['email']
        self.password = info['password']
        self.created_at = info['created_at']
        self.updated_at = info['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,dob,email,password) VALUES(%(first_name)s,%(last_name)s,%(dob)s,%(email)s,%(password)s)"
        return connectToMySQL('properties_schema').query_db(query, data)

    @classmethod
    def select_with_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('properties_schema').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def select_with_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('properties_schema').query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validation(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("properties_schema").query_db(query, user)
        if len(user['first_name']) < 2:
            flash("First name minimum requirement is 2 characters", "register_message")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name minimum requirement is 2 characters", "register_message")
            is_valid = False
        if len(results) >= 1:
            flash("Email is already in use.", "register_message")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Email not valid", "register_message")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password minimum requirement is 8 characters", "register_message")
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Does not match password", "register_message")
            is_valid = False

        age = 0

        try:
            dob = datetime.datetime.strptime(user['dob'], '%Y-%m-%d').date()
        except ValueError:
            try:
                dob = datetime.datetime.strptime(user['dob'], '%m/%d/%Y').date()
            except ValueError:
                flash("Please enter a date of birth", "register_message")
                is_valid = False

        if is_valid:
            today = datetime.date.today()
            age = today.year - dob.year - int(today.strftime('%m%d') < dob.strftime('%m%d'))

        if age < 18:
            flash("You must be at least 18 years old to register", "register_message")
            is_valid = False

        return is_valid

    @classmethod
    def delete_user_account(cls, data):
        user_id = data['id']

        delete_query = "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL('properties_schema').query_db(delete_query, data)

        if 'user_id' in session and session['user_id'] == user_id:
            session.clear()

        return
    
    @staticmethod
    def change_password_validation(user):
        is_valid = True
        query = "SELECT * FROM users WHERE password = %(password)s;"
        results = connectToMySQL("properties_schema").query_db(query, user)
        if user['password'] =='':
            flash("Please enter a password", "register_message")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password minimum requirement is 8 characters", "register_message")
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Does not match password", "register_message")
            is_valid = False

        return is_valid

    @classmethod
    def change_password(cls, data):
        query = "UPDATE users SET password=%(password)s WHERE id = %(id)s;"
        return connectToMySQL('properties_schema').query_db(query, data)