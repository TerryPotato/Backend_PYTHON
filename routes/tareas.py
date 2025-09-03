from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
from flask_mysqldb import MySQL
from config.db import get_db_connection

load_dotenv()
mysql = MySQL()

#creamos el blueprint
tareas_bp = Blueprint('tareas', __name__)

#creamos un endpoint para obtener tareas
@tareas_bp.route('/obtener', methods = ['GET'])
def get():
    return jsonify({"mensaje" : "Estas son su tareas: "})

#creamos un endpoint POST, recibe datos desde el body
@tareas_bp.route('/crear', methods = ['POST'])
def crear():
    #Obtenemos los datos del body
    data = request.get_json()
    descripcion = data.get('descripcion')
    id_usuario = data.get('id_usuario')  # Nuevo: obtener id_usuario

    if not descripcion or not id_usuario:
        return jsonify({"error" : "Proporciona una descripción y un id_usuario"}), 400

    cursor = get_db_connection()
    try:
        cursor.execute(
            'INSERT INTO tareas (descripcion, id_usuario) VALUES (%s, %s)',
            (descripcion, id_usuario))
        cursor.connection.commit()
        return jsonify({"mensaje" : f"ʕ•́ᴥ•̀ʔっ Tu tarea: {descripcion}, ha sido creada"}), 200
    except Exception as error:
        return jsonify({"error" : f"No se pudo crear la tarea: {str(error)}"})
    finally:
        cursor.close()
