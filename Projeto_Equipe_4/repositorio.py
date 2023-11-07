import sqlite3

#Gera um ID
def gerar_id():
  conn = sqlite3.connect('game.db')
  cursor = conn.cursor()
  cursor.execute("SELECT seq FROM sqlite_sequence WHERE name = 'usuarios'")
  next_id = cursor.fetchone()[0]
  return next_id + 1

#Cria um usuário
def criar_usuario(nome, sobrenome, email, idade, cidade, senha):
  try:
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    sql_insert = "INSERT INTO usuarios (nome_usuario, sobrenome_usuario, email_usuario, idade_usuario, cidade_usuario, senha_usuario) VALUES (?,?,?,?,?,?)"
    cursor.execute(sql_insert, (nome, sobrenome, email, idade, cidade, senha))  
    usuario_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return usuario_id
  except Exception as ex:
    print(ex)
    return 0

#Retorna todos os usuários
def retornar_usuarios():
  try:
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    sql_select_all = "SELECT * FROM usuarios"
    cursor.execute(sql_select_all)    
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios
  except:
    return False

#Retorna um usuário unico
def retornar_usuario(id: int):
  try:
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    sql_select = "SELECT * FROM usuarios WHERE id_usuario = ?"
    cursor.execute(sql_select, (id, ))
    id, nome, sobrenome, email, idade, cidade, senha, imagem = cursor.fetchone()
    conn.close()
    return id, nome, sobrenome, email, idade, cidade, senha, imagem
  except:
    return False

#Atualiza informações de um usuário 
def atualizar_usuario(id: int, nome, sobrenome, email, idade, cidade, senha):
  try:
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    sql_update = "UPDATE usuarios SET nome_usuario = ?, sobrenome_usuario = ?, email_usuario = ?, idade_usuario = ?, cidade_usuario = ?, senha_usuario = ?  WHERE id_usuario = ?"
    cursor.execute(sql_update, (nome, sobrenome, email, idade, cidade, senha, id))
    conn.commit()
    conn.close()
    return True
  except Exception as ex:
    print(ex)
    return False

#Exclui um usuário
def remover_usuario(id: int):
  try:
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    sql_delete = "DELETE from usuarios WHERE id_usuario = ?"
    cursor.execute(sql_delete, (id, ))
    conn.commit()
    conn.close()
    return True
  except Exception as ex:
     print(ex)
     return False

#Pega o ID do Atual usuário  
def set_id_atual(id):
    global id_atual
    id_atual = id
