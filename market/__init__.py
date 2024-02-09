from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'e6d9bf80fc62756603601c62'
app.app_context().push()
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
