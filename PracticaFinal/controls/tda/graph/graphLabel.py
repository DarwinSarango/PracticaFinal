from math import nan
import os.path
import json
import os
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.graphManaged import GraphManaged

class GraphLabel(GraphManaged):
    def __init__(self, num_vert) -> None:
        super().__init__(num_vert)
        self.labels = {} # guarda los labels de los vertices

    def addLabel(self, vertex, obj): # para agregar un label a un vertice
        if vertex < self.num_vertex: # si el vertice es menor al numero de vertices se agrega el label al vertice
            self.labels[vertex] = obj   
        else:
            raise ArrayPositionException("Delimite out")

    def getLabel(self, vertex): #es para obtener el label del vertice
        if vertex in self.labels:
            return self.labels[vertex]
        else:
            return None

    def add_edges_label(self, obj1, obj2, weight): #sive paa agregar una arista con el labels
        v1 = self.get_vertexlabel(obj1)
        v2 = self.get_vertexlabel(obj2)
        if v1 is not None and v2 is not None:
            self.insert_edges_weight(v1, v2, weight)
        else:
           raise ArrayPositionException("Delimite out")

    def get_vertexlabel(self, obj): #es para obtener el vertice con el label
        for vertex, label in self.labels.items():
            if label == obj:
                return vertex
        return None

    def paint_graph(self):
        url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"/static/d3/grafo.js"
        js = 'var nodes = new vis.DataSet(['
        #vertices
        for i in range(0, self.num_vertex):
            label = self.labels[i] if i in self.labels else str(i+1)
            js += '{id: ' + str(i+1) + ',label:"' + str(label)+'"},'+ "\n"
        js += ']);'
        js += "\n"
        #edges
        js += 'var edges = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            ini = str(i+1)
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    des = str(adj._destination + 1)
                    js += '{from: '+str(i+1) +',to:'+str(des) + ',label:"'+str(adj._weight)+'"},'+ "\n"
        js += ']);'
        js += "\n"
        js += 'var container = document.getElementById("mynetwork"); var data = {nodes: nodes,edges: edges,};var options = {};var network = new vis.Network(container, data, options);'
        a = open(url, 'w')
        a.write(js)
        a.close()
