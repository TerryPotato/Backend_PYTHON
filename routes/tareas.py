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
    return jsonify({"mensaje" : "ʕ•́ᴥ•̀ʔっ Estas son su tareas: "})

def validar_campos_requeridos(data, campos):
    faltantes = [campo for campo in campos if not data.get(campo)]
    if faltantes:
        return False, f"ʕ•́ᴥ•̀ʔっ Faltan los siguientes campos: {', '.join(faltantes)}"
    return True, None

#creamos un endpoint POST, recibe datos desde el body
@tareas_bp.route('/crear', methods = ['POST'])
def crear():
    #Obtenemos los datos del body
    data = request.get_json()
    campos_requeridos = ["descripcion", "id_usuario"]
    valido, mensaje = validar_campos_requeridos(data, campos_requeridos)
    if not valido:
        return jsonify({"error": mensaje}), 400

    descripcion = data.get('descripcion')
    id_usuario = data.get('id_usuario')  # Nuevo: obtener id_usuario

    cursor = get_db_connection()
    try:
        cursor.execute(
            'INSERT INTO tareas (descripcion, id_usuario) VALUES (%s, %s)',
            (descripcion, id_usuario))
        cursor.connection.commit()
        return jsonify({"mensaje" : f"ʕ•́ᴥ•̀ʔっ Tu tarea: {descripcion}, ha sido creada"}), 200
    except Exception as error:
        return jsonify({"error" : f"ʕ•́ᴥ•̀ʔっ No se pudo crear la tarea: {str(error)}"})
    finally:
        cursor.close()
