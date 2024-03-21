from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'Products'  # Alterado para corresponder ao nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255))  # Adicionada a coluna description
    category = db.Column(db.String(100))     # Adicionada a coluna category

    def __repr__(self):
        return f'<Product {self.name}>'