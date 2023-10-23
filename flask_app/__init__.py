from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'SECRET_KEY'

DB = 'login' #database name


