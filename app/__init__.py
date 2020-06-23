from flask import Flask
from flask_sqlalchemy import SQLAlchemy


application = Flask(__name__)
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost:3306/python_cloud_native_demo?charset=utf8mb4'
db = SQLAlchemy(application)
