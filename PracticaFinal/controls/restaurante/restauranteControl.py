from controls.dao.daoAdapter import DaoAdapter
from models.restaurante.restaurante import Restaurante

class RestauranteControl(DaoAdapter):
    def __init__(self):
        super().__init__(Restaurante)
        self.__restaurante = None

    @property
    def _restaurante(self):
        if self.__restaurante == None:
            self.__restaurante = Restaurante()
        return self.__restaurante

    @_restaurante.setter
    def _restaurante(self, value):
        self.__restaurante = value

    def _lista(self):
        return self._list()

    @property
    def save(self):
        #self._restaurante._id = self.lista._length + 1
        self._save(self._restaurante)

    def merge(self, pos):
        self._merge(self._restaurante, pos)

    def delete(self, pos):
        self._delete(self._restaurante, pos)