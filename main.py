from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

#se importa el controlador candidato
from Controladores.ControladorCandidato import ControladorCandidato


app=Flask(__name__)
cors = CORS(app)

#se asigna la importacion a una variable para ser usado en las ruta
#la variable ctrlCandidato tiene todas  las funciones declardas en ControladorCandidato
ctrlCandidato=ControladorCandidato()

#se crea la ruta del servicio con su methodo
@app.route("/candidato",methods=['GET'])
def listaCandidato():
    #se hace uso de la variable que tiene el ControladorCandidato y se llama a la funcion segun el caso
    json= ctrlCandidato.index()
    #la funcion index lo que hace es retornar una lista de candidatos
    return jsonify(json)

#ruta que recibe un valor para buscar candidato
@app.route("/candidato/<string:cedula>",methods=['GET'])
    #la funcion recibe la cedula del candidato
def consultaCandidato(cedula):
    #pasa  la cedula al methodo del controlador y retorna un valor
    json = ctrlCandidato.buscarCandidato(cedula)
    return jsonify(json)

@app.route("/candidato",methods=['POST'])
def crearCandidato():
    #se pasan los valores que el front envia o postman
    data= request.get_json()
    #se llama la funcion crearCandidato y se le  pasan los valores
    json=ctrlCandidato.crearCandidato(data)
    return jsonify(json)



@app.route("/candidato/<string:cedula>",methods=['PUT'])
def actualizarCandidato(cedula):
    data = request.get_json()
    #para actualizar se requiere cedula y los datos
    #con la cedula se save que candidato es el modificado
    json = ctrlCandidato.actualizarCandidato(cedula,data)
    return jsonify(json)


@app.route("/candidato/<string:cedula>",methods=['DELETE'])
def eliminarCandidato(cedula):
    json= ctrlCandidato.eliminarCandidato(cedula)
    return jsonify(json)
#fin rutas candidato



def loadFileConfig():
    with open('config.json') as f:
         data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])