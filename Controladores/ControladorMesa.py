from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa


class ControladorMesa():
    def __init__(self):
        print('prueba de controlador mesa')
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        print('listar todas las mesas')
        resultado = self.repositorioMesa.findAll()
        return resultado

    def consultaMesa(self,id):
        print('buscando la mesa con id:',id)
        adherirMesa = Mesa(self.repositorioMesa.findById(id))
        return adherirMesa.__dict__
    def crearMesa(self,mesa):
        print('crear una nueva mesa')
        nuevaMesa= Mesa(mesa)
        return self.repositorioMesa.save(nuevaMesa)

    def actualizarMesa(self,id,mesa):
        print("actualizando mesa con id ",id)
        refrescarMesa = Mesa(self.repositorioMesa.findById(id))
        refrescarMesa.numero= mesa["numero"]
        refrescarMesa.cantidad_inscritos = mesa["cantidad_inscritos"]
        return self.repositorioMesa.save(refrescarMesa)


    def eliminarMesa(self,id):
        print('eliminado mesa con id:',id)
        return self.repositorioMesa.delete(id)


