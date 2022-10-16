from Proyecto.Modelos.Candidato import Candidato

class ControladorCandidato():
    def __init__(self):
        print('prueba de contolador candidato')

    def index(self):
        print('listar todos los candidatos')
        unCandidato={
            "id":" ",
            "cedula":" ",
            "numeroResolucion":" ",
            "nombre":" ",
            "apellido":" "
        }
        return [unCandidato]
    def crearCandidato(self,infoCandidato):
        print('crear al candidato....')
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def buscarCandidato(self,id):
        print('mostrando candidato con ',id)
        elCandidato={
            "id": id,
            "cedula": " ",
            "numeroResolucion": " ",
            "nombre": " ",
            "apellido": " "
        }
        return elCandidato

    def actualizarCandidato(self,id,infoCandidato):
        print('actualizar candidato...',id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def eliminarCandidato(self,id):
        print('eliminando candidato')
        return {"delete_conunt": 1}
