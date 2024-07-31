from typing import TypeVar, Generic, Type
from controls.tda.linked.linkedList import Linked_List
import os.path

import json
import os

T = TypeVar('T')
class DaoAdapter(Generic[T]):
    atype: Type[T]

    def __init__(self, atype: Type[T]):
        self.atype = atype
        self.lista = Linked_List()
        self.file = atype.__name__.lower()+".json"
        self.URL = os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))) + "/data/"

    def _list(self):
        if os.path.isfile(self.URL+self.file):
            f = open(self.URL+self.file, "r")
            datos = json.load(f)
            self.lista.clear   
            for data in datos:
                a = self.atype.deserializar(data) 
                self.lista.addNode(a, self.lista._length)
        return self.lista
    
    def __transform__(self):
        aux = "["
        for i in range(0, self.lista._length):
            if i < self.lista._length - 1:
                aux += str(json.dumps(self.lista.getNode(i).serializable)) + ","
            else:
                aux += str(json.dumps(self.lista.getNode(i).serializable))
        aux += "]"

        return aux
    
    def to_dic_lista(self, lista):
        aux = []
        arreglo = lista.toArray
        for i in range(0, lista._length):
            aux.append(arreglo[i].serializable)

        return aux
    
    def to_dic(self):
        aux = []
        self._list()
        for i in range(0, self.lista._length):
            aux.append(self.lista.getNode(i).serializable)

        return aux
    
    def _get(self, id):
        list = self._list()
        array = list.toArray()
        for i in range(0, len(array)):
            if array[i]._id == id:
                return array[i]
        return None
        
    
    def _save_json(self, data):
        name = self.atype.__name__
        with open("../files/"+ name + ".json", "w") as outfile:
            json.dump(data, outfile, indent=4)

    def read_json(self):
        if os.path.exists("../files/persona.json"): #si existe el archivo
            with open("../files/persona.json") as file: #abrir archivo
                data = json.load(file)
                self.lista = None
                return self.lista.dicToList(data)
        else:
           return self.__lista

    

    def _save(self, data) -> T:
        self._list()
        self.lista.addNode(data, self.lista._length) 
        data._id = self.lista._length
        a = open(self.URL+self.file, "w")
        a.write(self.__transform__())
        a.close()

    def _merge(self, data: T, pos) -> T:
        data = self.lista.getNode(pos)  #para obtener el id

        self._list()
        self.lista.edit(data, pos)
        a = open(self.URL+self.file, "w")
        a.write(self.__transform__())
        a.close()

    def _delete(self, data: T, pos) -> T:
        self._list()
        self.lista.delete(pos)
        a = open(self.URL+self.file, "w")
        a.write(self.__transform__())
        a.close()
     