from flask import render_template, jsonify, request
from app import app, db
from app.models import Product
from sqlalchemy.exc import IntegrityError

@app.route('/')
def index():
    return render_template('index.html')

# Rota para gerar relatório de produtos
@app.route('/generate-report', methods=['GET'])
def generate_report():
    try:
        products = Product.query.all()
        result = [{"id": product.id, "name": product.name, "quantity": product.quantity} for product in products]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": "Erro ao gerar o relatório: " + str(e)}), 500

# Rota para atualizar o estoque de um produto
@app.route('/update-stock', methods=['POST'])
def update_stock():
    try:
        data = request.json
        product_id = data.get('id')
        new_quantity = data.get('quantity')
        if not product_id or not new_quantity:
            return jsonify({"error": "ID do produto e nova quantidade são obrigatórios"}), 400

        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": "Produto não encontrado"}), 404

        product.quantity = new_quantity
        db.session.commit()
        return jsonify({"message": "Estoque atualizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": "Erro ao atualizar o estoque: " + str(e)}), 500

# Rota para adicionar um novo produto
@app.route('/add-product', methods=['POST'])
def add_product():
    try:
        data = request.json
        name = data.get('name')
        if not name:
            return jsonify({"error": "O nome do produto é obrigatório"}), 400

        description = data.get('description', '')  # Descrição é opcional
        price = data.get('price')
        if not price or not isinstance(price, (int, float)):
            return jsonify({"error": "O preço do produto é obrigatório e deve ser um número"}), 400

        quantity = data.get('quantity')
        if not quantity or not isinstance(quantity, int):
            return jsonify({"error": "A quantidade do produto é obrigatória e deve ser um número inteiro"}), 400

        category = data.get('category', '')  # Categoria é opcional

        # Criando um novo produto
        new_product = Product(name=name, description=description, price=price, quantity=quantity, category=category)
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Produto cadastrado com sucesso!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Erro ao cadastrar o produto: nome duplicado"}), 400
    except Exception as e:
        return jsonify({"error": "Erro ao cadastrar o produto: " + str(e)}), 500

# Rota para lidar com erros 404 (recurso não encontrado)
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Recurso não encontrado"}), 404

# Rota para lidar com outros erros
@app.errorhandler(Exception)
def internal_error(error):
    return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)
