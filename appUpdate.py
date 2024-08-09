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

# Ruta para actualizar un curso por idCurso
@app.route('/cursos/<int:idCurso>', methods=['PUT'])
def actualizar_curso(idCurso):
    try:
        # Obtener los datos del cuerpo de la solicitud
        datos = request.json
        nombre = datos.get('nombre')
        descripcion = datos.get('descripcion')

        # Validar datos
        if not nombre or not descripcion:
            return jsonify({'error': 'Faltan datos'}), 400

        # Conectar a la base de datos
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Ejecutar la consulta de actualización
        query = "UPDATE curso SET nombre = %s, descripcion = %s WHERE idCurso = %s"
        cursor.execute(query, (nombre, descripcion, idCurso))
        connection.commit()

        # Cerrar la conexión
        cursor.close()
        connection.close()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Curso actualizado con éxito'}), 200
        else:
            return jsonify({'error': 'Curso no encontrado'}), 404

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
