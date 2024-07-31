import os.path
import json
import os
from controls.tda.graph.adjacent import Adjacent

class Graph():
    
    @property
    def num_vertex(self): #saber cuantos vertices hay
        raise NotImplementedError("Please implement this method")
    
    @property
    def num_edges(self): #saber cuantas aristas hay
        raise NotImplementedError("Please implement this method")
    
    def exist_edges(self,v1, v2): #para ver si existe una arista entre dos vertices
        raise NotImplementedError("Please implement this method")
    
    
    def weight_edges(self,v1, v2): #para ver el peso de una arista
        raise NotImplementedError("Please implement this method")
    
    def insert_edges(self,v1, v2): #para insertar una arista sin peso
        raise NotImplementedError("Please implement this method")
    
    def insert_edges_weight(self, v1, v2, weight): #para insertar una arista con peso
        raise NotImplementedError("Please implement this method")
    
    def adjacent(self,v1): #para ver los vertices adyacentes
        raise NotImplementedError("Please implement this method")
    
    def __str__(self) -> str:
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" +str(i+1) + "\n"
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out+= "ady" + "V" + str(adj._destination +1) + " weight: " + str(adj._weight) + "\n"
        return out
    
    def paint_graph(self):
        url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"/static/d3/grafo.js"
        js = 'var nodes = new vis.DataSet(['
        #vertices
        for i in range(0, self.num_vertex):
            #js+= '{id: ' + str(i+1) + ',label:"' + str(i+1)+'"},'+ "\n"
            js+= '{id: ' + str(i+1) + ',label:"' + str(self.getLabel(i))+'"},'+ "\n"
        js+= ']);'
        js+= "\n"
        #edges
        js+= 'var edges = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            #ini = str(i+1)
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.getNode(j)
                    des = str(adj._destination+1) 
                    js+= '{from: '+str(i+1) +',to:'+str(des) + ',label:"'+str(adj._weight)+'"},'+ "\n"
                    #+ " weight: " + str(adj._weight) + "\n"
    
        #codigo de aristas
        js+= ']);'
        js+= "\n"
        js+= 'var container = document.getElementById("mynetwork"); var data = {nodes: nodes,edges: edges,};var options = {};var network = new vis.Network(container, data, options);'
        a = open(url, 'w')
        a.write(js)
        a.close()