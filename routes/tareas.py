from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv

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
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    user_id = data.get('id')
    return jsonify({"saludo": f" ʕ•́ᴥ•̀ʔっ ¡Hola! {nombre} {apellido} ({user_id}), ¡Bienvenido!"})

#Crear un endpoint usando el PUT y pasando datos por el body y el URL
@tareas_bp.route('/editar/<int:user_id>', methods = ['PUT'])
def editar(user_id):
    #obtenemos los datos de body
    data = request.get_json()
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    mensaje = f" ʕ•́ᴥ•̀ʔっ El usuario {nombre} {apellido} con ID: {user_id} ha sido modificado correctamente."
    return  jsonify({"mensaje": mensaje})