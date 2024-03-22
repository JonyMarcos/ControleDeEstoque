from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_pyfile('config.py')

# Initialize SQLAlchemy database
db = SQLAlchemy(app)

# Import routes module
from app import routes
