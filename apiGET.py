from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuración de la base de datos
DB_CONFIG = {
    'host': '195.179.238.58',
    'user': 'u927419088_admin',
    'password': '#Admin12345#',
    'database': 'u927419088_testing_sql'
}

# Función para obtener la conexión a la base de datos
def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Ruta para obtener los registros de la tabla "Curso"
@app.route('/cursos', methods=['GET'])
def obtener_cursos():
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Curso")
        cursos = cursor.fetchall()
        return jsonify(cursos), 200
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return jsonify({'error': 'Error al obtener los cursos'}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
