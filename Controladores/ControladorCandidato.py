from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
from Repositorios.RepositorioCandidato import RepositorioCandidato
from  Repositorios.RepositorioPartido import RepositorioPartido


class ControladorCandidato():
    def __init__(self):
        print('prueba de contolador candidato')
        self.repositorioCandidato=RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def asignarPartido(self, idCandidato, idPartido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(idCandidato))
        partidoActual = Partido(self.repositorioPartido.findById(idPartido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)

    def index(self):
        print('listar todos los candidatos')
        resultado=self.repositorioCandidato.findAll()
        return  resultado


    def crearCandidato(self,infoCandidato):
        print('crear al candidato....')
        elCandidato = Candidato(infoCandidato)
        resultado=self.repositorioCandidato.save(elCandidato)
        return resultado

    def buscarCandidato(self,id):
        print('mostrando candidato con ',id)
        elCandidato= Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def actualizarCandidato(self,id,infoCandidato):
        print('actualizar candidato...',id)
        candidatoActual =Candidato(self.repositorioCandidato.findById(id))

        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        candidatoActual.numeroResolucion = infoCandidato["numeroResolucion"]
        resultado=self.repositorioCandidato.save(candidatoActual)
        return resultado

    def eliminarCandidato(self, id):
        print('eliminando candidato', id)
        resultado=self.repositorioCandidato.delete(id)
        return resultado
