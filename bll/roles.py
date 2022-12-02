from dal.db import Db

def listar():
    sql = "SELECT RolId, Nombre FROM Roles ORDER BY RolId;"
    result = Db.consultar(sql)
    return result