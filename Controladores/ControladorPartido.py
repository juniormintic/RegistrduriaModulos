from Modelos.Partido import Partido
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
class ControladorPartido():
    def __init__(self):
        print('prueba de contolador Partido')
        self.repositorioPartido = RepositorioPartido()
        self.repositorioCandidato = RepositorioCandidato()
    def asignarCandidatos(self, idCandidato, idPartido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(idCandidato))
        partidoActual = Partido(self.repositorioPartido.findById(idPartido))
        partidoActual.candidato= candidatoActual
        return self.repositorioPartido.save(partidoActual)
    def index(self):
        resultado = self.repositorioPartido.findAll()
        return resultado
    def crearPartido(self,infoPartido):
        print('crear al Partido....')
        elPartido = Partido(infoCandidato)
        resultado=self.repositorioPartido.save(elPartido)
        return resultado



    def buscarPartido(self,id):
        print('mostrando Partido con ',id)
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elCandidato.__dict__


    def actualizarPartido(self,id,infoPartido):
            print('actualizar Partido',id)
            elPartido = Partido(infoPartido)
            partidoActual = elPartido(self.repositorioPartido.findById(id))
            partidoActual.nombre = infoCandidato["nombre"]
            partidoActual.lema = infoCandidato["lema"]
            resultado = self.repositorioPartido.save(partidoActual)
            return resultado
    def eliminarPartido(self,id):
        print('eliminando Partido',id)
        resultado = self.repositorioPartido.delete(id)
        return resultado

