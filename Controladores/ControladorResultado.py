from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
class ControladorResultado():
    def __init__(self):
        print('prueba de contolador resultado')
        self.repositorioResultado=RepositorioResultado()
        self.repositorioCandidato=RepositorioCandidato()
        self.repositorioMesa=RepositorioMesa()
    def index(self):
        print('listar todos los resultados')
        resultado=self.repositorioResultado.findAll()
        return resultado
    def crearResultado(self,infoResultado, id_candidato, id_mesa):
        print('crear un resultado')
        nuevoResultado=Resultado(infoResultado)
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa=Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        resultado=self.repositorioResultado.save(nuevoResultado)
        return resultado

    def buscarResultado(self,id):
        print('mostrando resultado con ',id)
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    def actualizarResultado(self,id,infoResultado, id_candidato, id_mesa):
        print('actualizar resultado',id)
        resultadoActual=Resultado(self.repositorioResultado.findById(id))
        resultadoActual.numero_mesa=infoResultado["numero_mesa"]
        resultadoActual.cedula_candidato=infoResultado["cedula_candidato"]
        resultadoActual.numero_votos=infoResultado["numero_votos"]
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa=Mesa(self.repositorioMesa.findById(id_mesa))
        resultadoActual.candidato = elCandidato
        resultadoActual.mesa = laMesa
        resultado=self.repositorioResultado.save(resultadoActual)
        return resultado

    def eliminarResultado(self,id):
        print('eliminando resultado',id)
        resultado=self.repositorioResultado.delete(id)
        return resultado