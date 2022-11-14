from dal.db import Db

def agregar(user_name, email):    
    sql = "INSERT INTO usuarios(user_name, email) VALUES(?, ?)"    
    parametros = (user_name, email)
    Db.ejecutar(sql, parametros)

def actualizar(id, user_name, email):    
    sql = "UPDATE usuarios SET user_name=?, email=? WHERE id=?"    
    parametros = (user_name, email, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id):    
    sql = "DELETE FROM usuarios WHERE id=?"       
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = "SELECT id, user_name, email FROM usuarios"    
    result = Db.consultar(sql)
    return result

def filtrar(user_name):    
    sql = "SELECT id, user_name, email FROM usuarios WHERE user_name LIKE ?"
    parametros = ('%{}%'.format(user_name),)    
    result = Db.consultar(sql, parametros)
    return result