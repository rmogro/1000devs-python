import sqlite3

database = "super.db" # todo: por ahora ponemos el nombre de la base aqui, ver mejor opcion

class Db:
    @staticmethod
    def ejecutar(consulta, parametros = ()):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, parametros)
            cnn.commit()            
    
    @staticmethod
    def consultar(consulta, pametros = (), fetchAll = True):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, pametros)
            if fetchAll:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
            return result
    
    @staticmethod
    def crear():
        tabla_usuarios = '''CREATE TABLE IF NOT EXISTS "Usuarios" (
                            "UsuarioId"	INTEGER NOT NULL,
                            "Apellido"	VARCHAR(50),
                            "Nombre"	VARCHAR(30),
                            "FechaNacimiento"	VARCHAR(23),
                            "Dni"	INTEGER,
                            "CorreoElectronico"	VARCHAR(30),
                            "Usuario"	VARCHAR(15) UNIQUE,
                            "Contrasenia"	VARCHAR(100),
                            "RolId"	INTEGER,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("UsuarioId" AUTOINCREMENT)
                         );'''
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(tabla_usuarios)
            
        


            