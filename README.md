Controle de Estoque - MercadoCruz
Descrição do Projeto:
Este é um sistema de controle de estoque desenvolvido para a empresa MercadoCruz. Ele permite o cadastro de produtos e fornecedores além de oferecer funcionalidades para atualizar produtos e gerar relatórios sobre o estoque.

Pré-requisitos:
Python 3.x
Flask
SQLAlchemy
Banco de dados SQL Server

Configuração do Ambiente:
Clone este repositório para o seu ambiente de desenvolvimento:
git clone https://github.com/JonyMarcos/ControleDeEstoque.git

Instale as dependências do projeto utilizando o pip:
pip install Flask==2.0.1
pip install SQLAlchemy==1.4.22

Configuração do Banco de Dados:
Execute os scripts SQL localizados na pasta sql na seguinte ordem:
Create_database.sql: Este script cria o banco de dados MercadoCruz.
Create_tables.sql: Este script cria as tabelas no banco de dados.
Create_procedures.sql: Este script cria o procedimento armazenado responsável por gerar o código do produto.

Executando a Aplicação
Configure as informações do banco de dados no arquivo config.py, incluindo o nome do banco de dados, usuário e senha, se necessário.

Execute o arquivo run.py para iniciar o servidor Flask:
python run.py

Acesse a aplicação no seu navegador web, utilizando o endereço http://localhost:5000.

Como Utilizar:
Ao acessar a aplicação, você encontrará as opções de navegação para cadastrar produtos e fornecedores, além de atualizar produtos e gerar relatórios sobre o estoque.
Preencha os formulários conforme necessário e clique em "Cadastrar" ou "Atualizar" para salvar as informações no banco de dados.
O relatório de estoque será exibido na página inicial, mostrando os produtos cadastrados, seus preços, quantidades e outras informações relevantes.
