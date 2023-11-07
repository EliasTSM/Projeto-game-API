import sqlite3

#Dicionário com todos os usários do jogo
usuarios = {

  1: {
    "id": 1,
    "nome": "Tiago",
    "sobrenome": "Santos",
    "email": "tiago@gmail.com",
    "idade": 23,
    "cidade": "Salvador",
    "senha": "1234",
    "imagem": "/static/img/perfil_6.png"
  },

  2:{
    "id": 2,
    "nome": "Ana",
    "sobrenome": "Oliveira",
    "email": "ana@gmail.com",
    "idade": 25,
    "cidade": "Fortaleza",
    "senha": "1234",
    "imagem": "/static/img/perfil_2.png"
  },

  3:{
    "id": 3,
    "nome": "Ester",
    "sobrenome": "Santana",
    "email": "ester@gmail.com",
    "idade": 27,
    "cidade": "Belo Horizonte",
    "senha": "1234",
    "imagem": "/static/img/perfil_5.png"
  },

  4:{
    "id": 4,
    "nome": "Luiza",
    "sobrenome": "Andrade",
    "email": "luiza@gmail.com",
    "idade": 38,
    "cidade": "Rio de Janeiro",
    "senha": "1234",
    "imagem": "/static/img/perfil_4.png"
  },

  5:{
    "id": 5,
    "nome": "Carlos",
    "sobrenome": "Miranda",
    "email": "carlos@gmail.com",
    "idade": 37,
    "cidade": "São Paulo",
    "senha": "1234",
    "imagem": "/static/img/perfil_7.png"
  }

}

#Conectar com o banco de dados
conn = sqlite3.connect('game.db')

#Manipular dados no banco
cursor = conn.cursor()

sql_insert = "INSERT INTO usuarios (nome_usuario, sobrenome_usuario, email_usuario, idade_usuario, cidade_usuario, senha_usuario, imagem_usuario) VALUES (?,?,?,?,?,?,?)"
cursor.execute(sql_insert, ("nome_usuario", "sobrenome_usuario", "email_usuario", "idade_usuario", "cidade_usuario", "senha_usuario", "imagem_usuario"))

sql_select = "SELECT * FROM usuarios WHERE id_usuario = ?"
cursor.execute(sql_select, (1, ))
cursor.fetchone()

sql_select_all = "SELECT * FROM usuarios"
cursor.execute(sql_select_all)
cursor.fetchall()

sql_update = "UPDATE usuarios SET nome_usuario = ?  WHERE id_usuario = ?"
cursor.execute(sql_update, ("nome_usuario", 1))

sql_delete = "DELETE from usuarios WHERE id_usuario = ?"
cursor.execute(sql_delete, (1, ))

conn.commit()
conn.close()