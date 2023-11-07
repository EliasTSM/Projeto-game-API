import sqlite3

#Cria um usuário
def criar_usuario(nome, sobrenome, email, idade, cidade, senha, imagem):
  try:
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    sql_insert = "INSERT INTO usuarios (nome_usuario, sobrenome_usuario, email_usuario, idade_usuario, cidade_usuario, senha_usuario, imagem_usuario) VALUES (?,?,?,?,?,?,?)"
    cursor.execute(sql_insert, (nome, sobrenome, email, idade, cidade, senha, imagem))  
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
    resultado = []
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    sql_select_all = "SELECT * FROM usuarios"
    cursor.execute(sql_select_all)    
    usuarios = cursor.fetchall()
    conn.close()
    for item in usuarios:
      usuario = {
        'id': item[0],
        'nome': item[1],
        'sobrenome': item[2],
        'email': item[3],
        'idade': item[4],
        'cidade': item[5],
        'senha': item[6],
        'imagem': item[7]
      }
      resultado.append(usuario)
    return resultado
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
    return {"id": id, 
            "nome": nome, 
            "sobrenome": sobrenome, 
            "email": email, 
            "idade": idade, 
            "cidade": cidade, 
            "senha": senha, 
            "imagem": imagem}
  except:
    return False

#Atualiza informações de um usuário
def atualizar_usuario(id: int, nome, sobrenome, email, idade, cidade, senha, imagem):
  try:
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    sql_update = "UPDATE usuarios SET nome_usuario = ?, sobrenome_usuario = ?, email_usuario = ?, idade_usuario = ?, cidade_usuario = ?, senha_usuario = ?, imagem_usuario = ?  WHERE id_usuario = ?"
    cursor.execute(sql_update, (nome, sobrenome, email, idade, cidade, senha, imagem, id))
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
