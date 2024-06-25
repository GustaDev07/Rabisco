"""
Projeto Papelaria Rabisco
PWBE II - Aula 17
Código refatorado

"""


from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

# Cria a aplicação Flask
app = Flask(__name__)
# Habilita CORS para a aplicação
CORS(app)

# Conexão com o banco de dados MySQL
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'senai',
    'database': 'Papelaria'
}
#FUNÇÃO PARA CONECTAR COM O BANCO DE DADOS
def conecta_bd():
    conexaoDB = mysql.connector.connect(**DB_CONFIG)
    cursorDB = conexaoDB.cursor()
    return conexaoDB, cursorDB

#FUNÇÃO IRÁ FECHAR CONEXÃO COM O DB
def close_db(conexaoDB, cursorDB):
    cursorDB.close()
    conexaoDB.close()


# Rota para cadastro de produtos
@app.route('/produto', methods=['POST'])
def cadastro_produto():
    try:
        # Recebe os dados em formato JSON da requisição
        dados = request.json
        nome = dados.get('nome')
        descricao = dados.get('descricao')
        preco = dados.get('preco')
        quantidade = dados.get('quantidade')

        # Verifica se algum campo está vazio
        if not all([nome, descricao, preco, quantidade]):
            return jsonify({'Error':'Há campos vazios'}), 400

        # Comando SQL para inserir um novo produto
        conexaoDB,cursorDB = conecta_bd()
        comandoSQL = 'INSERT INTO Produto (nome, descricao, preco, quantidade) VALUES (%s,%s,%s,%s)'
        cursorDB.execute(comandoSQL, (nome, descricao, preco, quantidade))
        conexaoDB.commit()
 
        return jsonify({'mensagem':'Cadastro realizado'}), 201
    except Error as erro:
        return jsonify({'erro': f'{erro}'}), 500
    except KeyError:
        return jsonify({'erro':'Faltando informação'}), 500
    finally:
        close_db(conexaoDB, cursorDB)

# Rota para listar todos os produtos
@app.route('/produto', methods=['GET'])
def listar_produtos():
    try:
        # Comando SQL para selecionar todos os produtos
        conexaoDB, cursorDB = conecta_bd()
        comandoSQL = "SELECT * FROM Produto"

        cursorDB.execute(comandoSQL)
        produtos = cursorDB.fetchall()
        

        # Verifica se há produtos na lista
        if not produtos:
            return jsonify({'mensagem':'Não há produtos'}), 200
        
        # Converte os produtos para o formato JSON
        produtosjson = []
        for produto in produtos:
            produto_dic = {
                "idproduto": produto[0],
                "nome": produto[1],
                "descricao": produto[2],
                "preco": produto[3],
                "quantidade": produto[4]
            }
            produtosjson.append(produto_dic)

        return jsonify(produtosjson), 200
    except Error as erro:
        return jsonify({'erro': f'{erro}'}), 500
    finally:
        close_db(conexaoDB, cursorDB)

# Rota para retornar um produto específico pelo ID
@app.route('/produto/<int:id_produto>', methods=['GET'])
def get_produto(id_produto):
    try:
        # Comando SQL para selecionar um produto pelo ID
        conexaoDB,cursorDB = conecta_bd()
        comandoSQL = 'SELECT * FROM Produto WHERE idProduto = %s'
        cursorDB.execute(comandoSQL, (id_produto,))
        produto = cursorDB.fetchone()
       
        # Verifica se o produto foi encontrado
        if not produto:
            return jsonify({'mensagem':'Produto não encontrado'}), 200

        # Converte o produto para o formato JSON
        produtojson = {
            "idproduto": produto[0],
            "nome": produto[1],
            "descricao": produto[2],
            "preco": produto[3],
            "quantidade": produto[4]
        }
        return jsonify(produtojson), 200

    except Error as erro:
        return jsonify({'erro': f'{erro}'}), 500
    finally:
        close_db(conexaoDB, cursorDB)

# Rota para atualizar um produto existente
@app.route('/produto', methods=['PUT'])
def update_produto():
    try:
        # Recebe os dados em formato JSON da requisição
        dados = request.json
        idproduto = dados.get('idproduto')
        nome = dados.get('nome')
        descricao = dados.get('descricao')
        preco = dados.get('preco')
        quantidade = dados.get('quantidade')

        # Verifica se algum campo está vazio
        if not all([idproduto, nome, descricao, preco, quantidade]):
            return jsonify({'Erro':'Dados incompletos'}), 400
        
        # Comando SQL para atualizar o produto
        conexaoDB,cursorDB = conecta_bd()
        comandoSQL = 'UPDATE Produto SET nome = %s, descricao = %s, preco = %s, quantidade = %s WHERE idproduto = %s'
        cursorDB.execute(comandoSQL, (nome, descricao, preco, quantidade, idproduto))
        conexaoDB.commit()
    
        return jsonify({'mensagem':'Alteração realizada'}), 200
    except Error as erro:
        return jsonify({'erro': f'{erro}'}), 500
    except KeyError:
        return jsonify({'erro':'Faltando informação'}), 500
    finally:
        close_db(conexaoDB, cursorDB)      

# Rota para excluir um produto
@app.route('/produto', methods=['DELETE'])
def delete_produto():
    try:
        # Recebe os dados em formato JSON da requisição
        dados = request.json
        id_produto = dados.get('idproduto')

        # Comando SQL para deletar o produto pelo ID
        conexaoDB,cursorDB = conecta_bd()
        comandoSQL = 'DELETE FROM Produto WHERE idProduto = %s'
        cursorDB.execute(comandoSQL, (id_produto,))
        conexaoDB.commit()
      
        return jsonify({'mensagem':'Produto excluído'}), 200
    except Error as erro:
        return jsonify({'erro': f'{erro}'}), 500
    except KeyError:
        return jsonify({'erro':'Faltando informação'}), 500
    finally:
        close_db(conexaoDB, cursorDB)

# ERRO 404
@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return jsonify({'erro':'Página não encontrada'}), 404

# ERRO 405
@app.errorhandler(405)
def metodo_invalido(erro):
    return jsonify({'erro':'Método HTTP inválido'}), 405

# ERRO 500
@app.errorhandler(500)
def erro_servidor(erro):
    return jsonify({'erro':'Erro interno no servidor'}), 500


# Inicia a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)