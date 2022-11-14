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
        tabla_usuarios = 'CREATE TABLE IF NOT EXISTS "usuarios" ("id" INTEGER NOT NULL,"user_name" VARCHAR(100),"email" VARCHAR(50), PRIMARY KEY("id" AUTOINCREMENT))'
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(tabla_usuarios)
            
        


            