from datetime import datetime
from pytz import timezone
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class Product(db.Model):
    __tablename__ = 'Products'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255))  
    category = db.Column(db.String(100))     
    last_updated = db.Column(db.DateTime, default=datetime.now(timezone('America/Sao_Paulo')), onupdate=datetime.now(timezone('America/Sao_Paulo')))  # Adicione a coluna last_updated com valor padrão
    supplier_id = db.Column(db.Integer)  # Adicione a coluna supplier_id
    product_code = db.Column(db.String(50))  # Adicione a coluna product_code

    def __repr__(self):
        return f'<Product {self.name}>'

    @staticmethod
    def generate_product_code():
        # Chame a stored procedure GenerateProductCode aqui
        pass

    def save(self):
        # Obtém o próximo valor de ProductCode
        self.product_code = self.generate_product_code()

        # Salva o objeto Product no banco de dados
        db.session.add(self)
        db.session.commit()

class Supplier(db.Model):
    __tablename__ = 'Suppliers'
    id = db.Column('Id', db.Integer, primary_key=True)
    name = db.Column('Name', db.String(100), nullable=False)
    contact_name = db.Column('ContactName', db.String(255))
    email = db.Column('Email', db.String(255))
    phone = db.Column('Phone', db.String(20))

    def __repr__(self):
        return f'<Supplier {self.name}>'

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fullname = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(64), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        # Retorna True se a senha armazenada for igual à senha fornecida
        return self.password == password

    # Método para autenticação com hash, usado futuramente
    def check_password_hash(self, password):
        return check_password_hash(self.password, password)