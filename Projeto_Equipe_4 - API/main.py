from flask import Flask, jsonify, request
import repositorio

app = Flask(__name__)

#RETORNAR TODOS OS USUÁRIOS
@app.route("/usuarios", methods = ['GET'])
def get_usuarios():
    lista_usuarios = repositorio.retornar_usuarios()
    return jsonify(lista_usuarios)
    
#RETORNAR APENAS UM USUÁRIOS
@app.route("/usuario/<int:id>", methods = ['GET'])
def get_usuario(id):
    usuario = repositorio.retornar_usuario(id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"message": "Usuário não encontrado."}), 404
    
#CADASTRAR UM USUÁRIO
@app.route("/usuario", methods = ['POST'])
def create_usuario():
    usuario = request.json
    id_usuario = repositorio.criar_usuario(**usuario)
    usuario["id"] = id_usuario
    return jsonify(usuario), 201

#ALTERAR UM USUÁRIO
@app.route("/usuario/<int:id>", methods = ['PUT'])
def atualize_usuario(id):
    usuario = repositorio.retornar_usuario(id)
    if usuario:
        dados_atualizados = request.json
        dados_atualizados ["id"] = id
        repositorio.atualizar_usuario(**dados_atualizados)
        return jsonify(dados_atualizados)
    else:
        return jsonify({"message": "Personagem não encontrado."}), 404   

#DELETAR UM USUÁRIO
@app.route("/usuario/<int:id>", methods = ['DELETE'])
def remove_usuario(id):
    usuario = repositorio.retornar_usuario(id)
    if usuario:
        repositorio.remover_usuario(id)
        return jsonify({"message": "Personagem removido com sucesso."})
    else:
        return jsonify({"message": "Personagem não encontrado."}), 404  

app.run(debug=True)