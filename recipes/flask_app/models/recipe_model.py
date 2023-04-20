from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model


class Recipe:

    def __init__(self, info):
        self.id = info['id']
        self.name = info['name']
        self.under_30_min = info['under_30_min']
        self.instruction = info['instruction']
        self.description = info['description']
        self.date_made = info['date_made']
        self.created_at = info['created_at']
        self.updated_at = info['updated_at']
        self.user_id = info['user_id']
        self.chef = None

    @staticmethod
    def validation(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name length minimum requirement is 3 characters", "recipe_message")
            is_valid = False
        if len(recipe['instruction']) < 3:
            flash("Instruction length minimum requirement is 3 characters", "recipe_message")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description length minimum requirement is 3 characters", "recipe_message")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name,under_30_min,instruction,description,date_made,user_id) VALUES(%(name)s,%(under_30_min)s,%(instruction)s,%(description)s,%(date_made)s,%(user_id)s);"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def select_all_recipes(cls):
        query = """SELECT * FROM recipes JOIN users on recipes.user_id = users.id;"""

        result = connectToMySQL('recipes_schema').query_db(query)
        recipes = []
        for count in result:
            select_recipe = cls(count)
            user_info = {
                "id": count['users.id'],
                "first_name": count['first_name'],
                "last_name": count['last_name'],
                "email": count['email'],
                "password": "",
                "created_at": count['users.created_at'],
                "updated_at": count['users.updated_at']
            }
            select_recipe.chef = user_model.User(user_info)
            recipes.append(select_recipe)
        return recipes

    @classmethod
    def select_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s,under_30_min=%(under_30_min)s,instruction=%(instruction)s,description=%(description)s,date_made=%(date_made)s,user_id=%(user_id)s WHERE id = %(id)s;"

        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"

        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def select_with_id(cls, data):
        query = """
                SELECT * FROM recipes
                JOIN users on recipes.user_id = users.id
                WHERE recipes.id = %(id)s;
                """
        result = connectToMySQL('recipes_schema').query_db(query, data)
        if not result:
            return False

        result = result[0]
        select_recipe = cls(result)
        user_data = {
            "id": result['users.id'],
            "first_name": result['first_name'],
            "last_name": result['last_name'],
            "email": result['email'],
            "password": "",
            "created_at": result['users.created_at'],
            "updated_at": result['users.updated_at']
        }
        select_recipe.chef = user_model.User(user_data)
        return select_recipe
