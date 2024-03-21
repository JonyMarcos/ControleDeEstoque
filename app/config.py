# Configuration options for Flask app
import os

# Define a variável de ambiente SECRET_KEY
SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key_123')

# Define a variável de ambiente SQLALCHEMY_DATABASE_URI
DB_SERVER = 'DESKTOP-SI6G0B7'
DB_NAME = 'MercadoCruz'
DB_USER = 'RBLVOB01'
DB_PASSWORD = 'RPA123'

SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server'

# Configuração para desabilitar o rastreamento de modificações do SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False

