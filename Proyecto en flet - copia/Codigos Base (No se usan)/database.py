import typing
import sqlite3 as sq

def db_connection() -> typing.Tuple[sq.Cursor, sq.Connection]:
    connect = sq.connect('usuarios.db')
    connect.execute("CREATE TABLE IF NOT EXISTS usuarios (cedula INTEGER PRIMARY KEY, clave TEXT)")
    return connect.cursor(), connect

def create_user(cedula: int, clave: str):
    # TODO: Validate data
    try:
        if not cedula:
            raise ValueError("La cédula no puede estar vacía")
        if not clave:
            raise ValueError("La clave no puede estar vacía")

        cursor, connection = db_connection()
        cursor.execute("INSERT INTO usuarios (cedula, clave) VALUES (?, ?)", (cedula, clave))
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