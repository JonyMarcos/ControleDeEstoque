from flask import render_template, jsonify, request
from app import app, db
from app.models import Product, Supplier, User
from sqlalchemy.exc import IntegrityError

@app.route('/')
def index():
    return render_template('index.html')

# Rota para gerar relatório de produtos
@app.route('/gerar-relatorio', methods=['GET'])
def generate_report():
    try:
        products = Product.query.all()
        result = [{"product_Code": product.product_code, "name": product.name, "price": product.price, "quantity": product.quantity, "description": product.description, "category": product.category, "last_updated": product.last_updated} for product in products]
        print(result)  
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": "Erro ao gerar o relatório: " + str(e)}), 500

# Rota para atualizar o estoque de um produto
@app.route('/atualizar-estoque', methods=['POST'])
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

@app.route('/cadastrar-produto', methods=['POST'])
def cadastrar_produto():
    try:
        # Chame o procedimento armazenado para obter o próximo código de produto
        cursor = db.session.connection().connection.cursor()
        cursor.execute("EXEC SPGenerateProductCode")
        next_product_code = cursor.fetchone()[0]

        data = request.form
        name = data.get('name')
        supplier_id = data.get('supplier_id')  
        if not name:
            return jsonify({"error": "O nome do produto é obrigatório"}), 400

        description = data.get('description', '')
        price = float(data.get('price', 0))  
        quantity = int(data.get('quantity', 0))  
        category = data.get('category', '')

        new_product = Product(name=name, description=description, price=price, quantity=quantity, category=category, supplier_id=supplier_id, product_code=next_product_code)
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": f"Produto cadastrado com sucesso! Código do produto: {next_product_code}"}), 201
    except Exception as e:
        return jsonify({"error": "Erro ao cadastrar o produto: " + str(e)}), 500

# Rota para cadastrar um novo fornecedor
@app.route('/cadastrar-fornecedor', methods=['POST'])
def cadastrar_fornecedor():
    try:
        data = request.form
        name = data.get('supplier-name')
        contact_name = data.get('supplier-contact')
        email = data.get('supplier-email')
        phone = data.get('supplier-phone')
        
        if not name or not contact_name:
            return jsonify({"error": "O nome e as informações de contato do fornecedor são obrigatórios"}), 400

        # Crie uma instância do modelo Supplier com os dados fornecidos
        new_supplier = Supplier(name=name, contact_name=contact_name, email=email, phone=phone)
        
        # Adicione o novo fornecedor ao banco de dados
        db.session.add(new_supplier)
        db.session.commit()
        
        return jsonify({"message": "Fornecedor cadastrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": "Erro ao cadastrar o fornecedor: " + str(e)}), 500

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
