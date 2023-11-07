from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        lista_usuarios = repositorio.retornar_usuarios()
        for id, nome, sobrenome, email, idade, cidade, senha, imagem in lista_usuarios:
            if email == request.form["email"]:
                if senha == request.form["senha"]:
                  repositorio.set_id_atual(id)
                  print(id)
                  return redirect(url_for("perfil", id=id))  
    else:
        return render_template("login.html")

@app.route("/cadastro", methods = ['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        email = request.form["email"]
        idade = request.form["idade"]
        cidade = request.form["cidade"]
        senha = request.form["senha"]       
        repositorio.criar_usuario(nome=nome, sobrenome=sobrenome, email=email, idade=idade, cidade=cidade, senha=senha)
        return redirect(url_for('login'))
    else:
        return render_template("cadastro.html")

@app.route("/perfil/<int:id>", methods = ['GET', 'POST'] )
def perfil(id):
    if request.method == "POST":
        repositorio.remover_usuario(id)
        return redirect(url_for('login'))
    else: 
        id, nome, sobrenome, email, idade, cidade, senha, imagem = repositorio.retornar_usuario(id)
        return render_template("perfil.html", id=id, nome=nome, sobrenome=sobrenome, email=email, idade=idade, cidade=cidade, senha=senha, imagem=imagem)

@app.route("/editar/<int:id>", methods = ['GET', 'POST'] )
def editar(id):
    if request.method == "POST":
        nome = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        email = request.form["email"]
        idade = request.form["idade"]
        cidade = request.form["cidade"]
        senha = request.form["senha"]
        dados_retornados = repositorio.retornar_usuario(id)
        if dados_retornados:
            repositorio.atualizar_usuario(id=id, nome=nome, sobrenome=sobrenome, email=email, idade=idade, cidade=cidade, senha=senha)
        return redirect(url_for("perfil", id=id))
    else: 
        id, nome, sobrenome, email, idade, cidade, senha, imagem = repositorio.retornar_usuario(id)
        return render_template("editar.html", id=id, nome=nome, sobrenome=sobrenome, email=email, idade=idade, cidade=cidade, senha=senha, imagem=imagem)

@app.route("/usuarios")
def usuarios():
    lista_usuarios = repositorio.retornar_usuarios()
    id_atual = repositorio.id_atual
    return render_template("usuarios.html", dados = lista_usuarios, id_atual = id_atual)

@app.route("/usuarios/<int:id>")
def usuario_id(id):
    id, nome, sobrenome, email, idade, cidade, senha, imagem = repositorio.retornar_usuario(id)
    id_atual = repositorio.id_atual
    lista_usuarios = repositorio.retornar_usuarios()
    if lista_usuarios:
        usuario_existe = "True"
    return render_template("usuarios.html", id=id, nome=nome, sobrenome=sobrenome, email=email, idade=idade, cidade=cidade, senha=senha, imagem=imagem, dados = lista_usuarios, usuario_existe = usuario_existe, id_atual = id_atual )

app.run(debug=True)