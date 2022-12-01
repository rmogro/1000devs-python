from dal.db import Db

def listar():
    sql = "SELECT RolId, Nombre FROM Roles"
    result = Db.consultar(sql)
    return result