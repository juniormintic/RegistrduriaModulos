from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        print('prueba de controlador mesa')

    def index(self):
        print('listar todas las mesas')
        mesa={
            "id":"id",
            "numero":"01",
            "cantidadInscritos":10
        }

        return [mesa]

    def consultaMesa(self,id):
        print('buscando la mesa con id:',id)
        mesa={
            "id":id,
            "numero":"02",
            "candidadInscritos":15
        }
        return mesa

    def crearMesa(self,mesa):
        print('crear una nueva mesa')
        resultado=Mesa(mesa)
        return resultado.__dict__

    def actualizarMesa(self,id,mesa):
        print('actualizar mesa',id)
        resultado= Mesa(mesa)
        return resultado.__dict__

    def eliminarMesa(self,id):
        print('eliminado mesa con id:',id)
        return {"delete_conunt": 1}


