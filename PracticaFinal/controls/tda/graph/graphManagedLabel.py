from controls.tda.graph.graphManaged import GraphManaged
from controls.exception.arrayPositionException import ArrayPositionException
class GraphManagedLebelled(GraphManaged):
    
    def __init__(self, num_vert) -> None:
        super().__init__(num_vert)
        self.__lebelled = [None] * self.num_vertex
        
    @property
    def _lebelled(self):
        return self.__lebelled

    @_lebelled.setter
    def _lebelled(self, value):
        self.__lebelled = value

    def getLabel(self, v):
        if v <= self.num_vertex:
            return self.__lebelled[v]
        else:
            raise ArrayPositionException("Indice fuera de rango")
        
    def getId(self, label):
        if label in self.__lebelled:
            return self.__lebelled.index(label)
        else:
            raise ArrayPositionException("El label no existe")
   
    def addLabel(self, v, objeto):
        if v <= self.num_vertex:
            self.__lebelled[v] = objeto
        else:
            raise ArrayPositionException("Indice fuera de rango")
        
    def add_edge_label(self, objUno, objDos, wieght):
        v1 = self.getId(objUno)
        v2 = self.getId(objDos)
        self.insert_edges_weight(v1, v2, wieght)
    
    
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    