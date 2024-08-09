from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Datos de conexión a la base de datos
db_config = {
    'host': '195.179.238.58',
    'user': 'u927419088_admin',
    'password': '#Admin12345#',
    'database': 'u927419088_testing_sql'
}

# Ruta para obtener un curso por idCurso
@app.route('/cursos/<int:idCurso>', methods=['GET'])
def obtener_curso_por_id(idCurso):
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # Ejecutar la consulta para obtener el curso con el id proporcionado
        cursor.execute("SELECT * FROM curso WHERE idCurso = %s", (idCurso,))
        curso = cursor.fetchone()

        # Cerrar la conexión
        cursor.close()
        connection.close()

        if curso:
            # Devolver el registro en formato JSON
            return jsonify(curso), 200
        else:
            # Si no se encuentra el curso, devolver un error 404
            return jsonify({'error': 'Curso no encontrado'}), 404

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
