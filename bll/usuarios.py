from dal.db import Db

def agregar(apellido, nombre, fecha_nacimiento, dni, correo_electronico, usuario, contrasenia, rol_Id):    
    sql = "INSERT INTO Usuarios(Apellido, Nombre, FechaNacimiento, Dni, CorreoElectronico, Usuario, Contrasenia, RolId) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
    parametros = (apellido, nombre, Db.formato_fecha_db(fecha_nacimiento), dni, correo_electronico, usuario, Db.encriptar_contraseña(contrasenia), rol_Id)
    Db.ejecutar(sql, parametros)

def actualizar(id, apellido, nombre, fecha_nacimiento, dni, correo_electronico, contrasenia, rol_Id):    
    sql = "UPDATE Usuarios SET Apellido = ?, Nombre = ?, FechaNacimiento = ?, Dni = ?, CorreoElectronico = ?, Contrasenia = ?, RolId = ? WHERE UsuarioId = ?"
    parametros = (apellido, nombre, Db.formato_fecha_db(fecha_nacimiento), dni, correo_electronico, Db.encriptar_contraseña(contrasenia), rol_Id, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id):    
    sql = "DELETE FROM Usuarios WHERE UsuarioId = ?"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = "SELECT Apellido, Nombre, FechaNacimiento, Dni, CorreoElectronico, Usuario, RolId FROM Usuarios"
    result = Db.consultar(sql)
    return result

def filtrar(usuario):    
    sql = "SELECT Apellido, Nombre, FechaNacimiento, Dni, CorreoElectronico, Usuario, RolId FROM Usuarios WHERE Usuario LIKE ?"
    parametros = ('%{}%'.format(usuario),)    
    result = Db.consultar(sql, parametros)
    return result

def validar(usuario, contrasenia):    
    sql = "SELECT Usuario FROM Usuarios WHERE Usuario = ? AND Contrasenia = ?"
    parametros = (usuario, Db.encriptar_contraseña(contrasenia))
    result = Db.consultar(sql, parametros, False)
    return result != None