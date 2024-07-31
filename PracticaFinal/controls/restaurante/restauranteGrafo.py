
from controls.tda.graph.graphNoManagedLabel import GraphNoManagedLabel
from controls.restaurante.restauranteControl import RestauranteControl
from controls.restaurante.calculo import Distancia
from models.restaurante.restaurante import Restaurante
import os, re

class RestauranteGrafo():
    def __init__(self):
        self.__grafo = None
        self.__ndao = RestauranteControl()
        self.__dirPhysical = "static/d3/grafo.js"
    

    @property
    def _grafo(self):
        if self.__grafo == None:
            self.create_graph()
        return self.__grafo

    @_grafo.setter
    def _grafo(self, value):
        self.__grafo = value

       
    def create_graph(self, origen=None, destino=None):
        list = self.__ndao._list()
        if list._length > 0:
            self.__grafo = GraphNoManagedLabel(list._length)
            arr = list.toArray
            [self.__grafo.label_vertex(i, negocio._nombre) for i, negocio in enumerate(arr)]

            if os.path.exists(self.__dirPhysical):
                with open(self.__dirPhysical, 'r') as file:
                    for line in file:
                        if "from:" in line:
                            line = line.strip()
                            o, d, w = (re.search(pattern, line).group(1) for pattern in [r'from:\s*(\d+)', r'to:\s*(\d+)', r'label:"([\d.]+)"'])
                            negocioOrigen = self.__ndao._list().binary_search_models_int(int(o), "_id")
                            negocioDestino = self.__ndao._list().binary_search_models_int(int(d), "_id")
                            self.__grafo.insert_edges_weight_E(negocioOrigen._nombre, negocioDestino._nombre, float(w))

            if origen and destino:
                if isinstance(origen, Restaurante) and isinstance(destino, Restaurante):
                    peso = round(Distancia().haversine(origen._lat, origen._lng, destino._lat, destino._lng), 3)
                    self.__grafo.insert_edges_weight_E(origen._nombre, destino._nombre, peso)
                else:
                    print("Error: origen o destino no son del tipo Restaurante")
            self.__grafo.paint_graph()
