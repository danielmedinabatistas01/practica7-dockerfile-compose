
from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST", "mysql"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "123456"),
            database=os.getenv("DB_NAME", "hola_mundo")
        )
        return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar con MySQL: {error}")
        return None

@app.route("/")
def inicio():
    conexion = conectar_db()

    if conexion:
        conexion.close()
        return """
            <h1>¡Hola Mundo!</h1>
            <p>Aplicación conectada correctamente a MySQL.</p>
        """

    return """
        <h1>¡Hola Mundo!</h1>
        <p>No se pudo conectar a la base de datos.</p>
    """, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
