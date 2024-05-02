import typing
import sqlite3 as sq

def db_connection() -> typing.Tuple[sq.Cursor, sq.Connection]:
    connect = sq.connect('usuarios.db')
    connect.execute("CREATE TABLE IF NOT EXISTS usuarios (cedula INTEGER PRIMARY KEY, clave TEXT, nombre TEXT, apellido TEXT, sexo TEXT)")
    return connect.cursor(), connect

def create_user(cedula: int, clave: str, nombre: str, apellido: str, sexo: str):
    # TODO: Validate data
    try:
        if cedula is None:
            raise ValueError("La cédula no puede estar vacía")
        if not clave:
            raise ValueError("La clave no puede estar vacía")
        if not nombre:
            raise ValueError("Tiene que ingresar su nombre")
        if not apellido:
            raise ValueError("Tiene que ingresar su apellido")
        if not sexo:
            raise ValueError("Tiene que ingresar el sexo")

        cursor, connection = db_connection()
        cursor.execute("INSERT INTO usuarios (cedula, clave, nombre, apellido, sexo) VALUES (?, ?, ?, ?, ?)", (cedula, clave, nombre, apellido, sexo))
        connection.commit()
    except sq.IntegrityError:
        raise ValueError("La cédula ingresada ya está en uso")
    except Exception as e:
        raise ValueError(f"Error al crear el usuario: {e}")
        
def validate_user(cedula: int, clave: str) -> bool:
    #TODO: Validate data
    cursor, _ = db_connection()
    cursor.execute("SELECT * FROM usuarios WHERE cedula = ? AND clave = ?", (cedula, clave))
    user = cursor.fetchone()  
    if user:
        return True 
    else:
        return False   