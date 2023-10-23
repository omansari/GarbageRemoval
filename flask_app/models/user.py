# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app import DB
from flask import flash
# model the class after the User table from our database
# make friends, user

class User:
    db = 'login'
    def __init__( self , data ):
        self.id = data['iduser']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.occupation = data['occupation']
        # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        user = []
        # Iterate over the db results and create instances of friends with cls.
        for row in results:

            user.append( cls(row) )

        return user

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user(first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s)'
        print(query)
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results[0])
        return cls(results[0])

    @classmethod
    def get_by_name(cls, data):
        query = 'SELECT * FROM user WHERE first_name = %(first_name)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = 'SELECT * FROM user WHERE iduser = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return cls(results[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(User.db).query_db(query, user)

        if len(results) >= 1:
            
            flash('Email already taken.', 'register')
            is_valid = False

        if not EMAIL_REGEX.match(user['email']):
            
            flash('Invaild email.', 'register')
            is_valid = False

        if len(user['first_name']) < 3:
        
            flash('First name should be at least 3 characters.', 'register')
            is_valid = False

        if len(user['last_name']) < 3:
        
            flash('Last name should be at least 3 characters.', 'register')
            is_valid = False

        if len(user['password']) < 6:
        
            flash('Password should be at least 6 characters.', 'register')
            is_valid = False

        if user['password'] != user['confirm']:
        
            flash("Passwords don't match.", 'register')
        
        return is_valid