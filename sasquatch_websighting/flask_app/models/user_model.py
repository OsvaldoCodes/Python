from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:

    def __init__(self, info):
        self.id = info['id']
        self.first_name = info['first_name']
        self.last_name = info['last_name']
        self.email = info['email']
        self.password = info['password']
        self.created_at = info['created_at']
        self.updated_at = info['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL('sightings_schema').query_db(query, data)

    @classmethod
    def select_with_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('sightings_schema').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def select_with_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('sightings_schema').query_db(query, data)
        return cls(results[0])


    @staticmethod
    def validation(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("sightings_schema").query_db(query, user)
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
        return is_valid
