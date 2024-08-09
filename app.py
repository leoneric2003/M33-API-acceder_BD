from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Datos de conexión a la base de datos
db_config = {
    'host': '195.179.238.58',
    'user': 'u927419088_admin',
    'password': '#Admin12345#',
    'database': 'u927419088_testing_sql'
}

# Ruta para obtener todos los registros de la tabla Curso
@app.route('/cursos', methods=['GET'])
def obtener_cursos():
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # Ejecutar la consulta
        cursor.execute("SELECT * FROM curso")
        cursos = cursor.fetchall()

        # Cerrar la conexión
        cursor.close()
        connection.close()

        # Devolver los registros en formato JSON
        return jsonify(cursos), 200

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
