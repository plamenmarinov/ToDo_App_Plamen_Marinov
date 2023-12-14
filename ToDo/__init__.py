import psycopg2
from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gfjfgtretrehfggh245354342d'

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="TodoApp",
    user="postgres",
    password="Plamikoteto123"
)

# Login Manager
LoginManager = LoginManager(app)
LoginManager.login_view = 'Login.login'
LoginManager.login_message_category = 'info'

from ToDo.Views.routes import Views
from ToDo.Login.routes import Login

app.register_blueprint(Views)
app.register_blueprint(Login)

# import psycopg2
# from flask import Flask, g
# from flask_login import LoginManager
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'gfjfgtretrehfggh245354342d'
#
# # Database configuration
# app.config['DATABASE'] = {
#     'host': 'localhost',
#     'database': 'TodoApp',
#     'user': 'postgres',
#     'password': 'Plamikoteto123'
# }
#
# # Login Manager
# login_manager = LoginManager(app)
# login_manager.login_view = 'Login.login'
# login_manager.login_message_category = 'info'
#
# # Database connection functions
# def get_db():
#     if 'db' not in g:
#         g.db = psycopg2.connect(
#             host=app.config['DATABASE']['host'],
#             database=app.config['DATABASE']['database'],
#             user=app.config['DATABASE']['user'],
#             password=app.config['DATABASE']['password']
#         )
#     return g.db
#
# @app.teardown_appcontext
# def close_db(error):
#     db = g.pop('db', None)
#     if db is not None:
#         db.close()
#
# # Import your views and login routes after configuring the app
# from ToDo.Views.routes import Views
# from ToDo.Login.routes import Login
#
# app.register_blueprint(Views)
# app.register_blueprint(Login)
