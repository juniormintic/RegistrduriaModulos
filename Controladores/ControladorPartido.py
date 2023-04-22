from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
class ControladorPartido():
    def __init__(self):
        print('prueba de contolador Partido')
        self.repositorioPartido = RepositorioPartido()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        resultado = self.repositorioPartido.findAll()
        return resultado
    def crearPartido(self,infoPartido):
        print('crear al Partido....')
        elPartido = Partido(infoPartido)
        resultado=self.repositorioPartido.save(elPartido)
        return resultado



    def buscarPartido(self,id):
        print('mostrando Partido con ',id)
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__


    def actualizarPartido(self,id,infoPartido):
            print('actualizar Partido',id)
            partidoActual = Partido(self.repositorioPartido.findById(id))
            partidoActual.nombre = infoPartido["nombre"]
            partidoActual.lema = infoPartido["lema"]
            resultado = self.repositorioPartido.save(partidoActual)
            return resultado
    def eliminarPartido(self,id):
        print('eliminando Partido',id)
        resultado = self.repositorioPartido.delete(id)
        return resultado

