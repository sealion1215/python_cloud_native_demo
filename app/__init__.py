from config import db_host, db_port, db_user, db_password, db_schema
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


application = Flask(__name__)
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234567@localhost:3306/python_cloud_native_demo?charset=utf8mb4'
# application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
#     db_user, db_password, db_host, db_port, db_schema
# )
print(application.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(application)
