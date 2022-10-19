from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        print('prueba de contolador Partido')

    def index(self):
        print('listar todos los Partidos')
        unPartido={
            "id":"1",
            "nombre":"Falcon",
            "Lema":"The best Group"
        }
        return [unPartido]
    def crearPartido(self,infoPartido):
        print('crear un Partido')
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def buscarPartido(self,id):
        print('mostrando Partido con ',id)
        elPartido={
            "id":"1",
            "nombre":"Falcon",
            "Lema":"The best Group"
        }
        return elPartido

    def actualizarPartido(self,id,infoPartido):
        print('actualizar Partido',id)
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def eliminarPartido(self,id):
        print('eliminando Partido')
        return {"delete_conunt": 1}
