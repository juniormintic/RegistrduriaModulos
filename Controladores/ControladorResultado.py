from Modelos.Resultado import Resultado

class ControladorResultado():
    def __init__(self):
        print('prueba de contolador resultado')

    def index(self):
        print('listar todos los resultados')
        unResultado={
            "id":"1",
            "numero_mesa":"22",
            "cedula_candidato":"1090445818",
            "numero_votos":115
        }
        return [unResultado]
    def crearResultado(self,infoResultado):
        print('crear un resultado')
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def buscarResultado(self,id):
        print('mostrando resultado con ',id)
        elResultado={
            "id":id,
            "numero_mesa":"22",
            "cedula_candidato":"1090445818",
            "numero_votos":115
        }
        return elResultado

    def actualizarResultado(self,id,infoResultado):
        print('actualizar resultado',id)
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def eliminarResultado(self,id):
        print('eliminando resultado')
        return {"delete_conunt": 1}
