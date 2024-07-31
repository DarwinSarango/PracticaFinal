from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.graphNoManeged import GraphNoManaged
import os
import re

class GraphLabelNoManaged(GraphNoManaged):
    def __init__(self, num_vert) -> None:
        super().__init__(num_vert)
        self.__vertexLabels = {}

    def set_label(self, vertex, label):
        if vertex < self.num_vertex:
            self.__vertexLabels[vertex] = label
        else:
            raise ArrayPositionException("Delimite out")
        
    def get_label(self, vertex):
        if vertex < self.num_vertex:
            return self.__vertexLabels.get(vertex, str(vertex))
        else:
            raise ArrayPositionException("Delimite out")

    def paint_graph(self):
        url = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), "static/d3/grafo.js")
        existing_nodes = {}
        existing_edges = {}
        if os.path.exists(url):
            with open(url, 'r') as file:
                content = file.read()
                nodes_match = re.search(r'var nodes = new vis.DataSet\(\[(.*?)\]\);', content, re.DOTALL)
                if nodes_match:
                    nodes_str = nodes_match.group(1)
                    nodes_str = nodes_str.strip().rstrip(',')  
                    node_entries = nodes_str.split('},\n{')
                    for entry in node_entries:
                        entry = entry.strip('{}\n ')
                        parts = entry.split(', ')
                        node_id = None
                        label = None
                        for part in parts:
                            key, value = part.split(': ')
                            value = value.strip('"')
                            if key == 'id':
                                node_id = int(value)
                            elif key == 'label':
                                label = value
                        if node_id is not None and label is not None:
                            existing_nodes[node_id] = {'id': node_id, 'label': label}
                edges_match = re.search(r'var edges = new vis.DataSet\(\[(.*?)\]\);', content, re.DOTALL)
                if edges_match:
                    edges_str = edges_match.group(1)
                    edges_str = edges_str.strip().rstrip(',') 
                    edge_entries = edges_str.split('},\n{')
                    for entry in edge_entries:
                        entry = entry.strip('{}\n ')
                        parts = entry.split(', ')
                        from_node = None
                        to_node = None
                        label = None
                        for part in parts:
                            key, value = part.split(': ')
                            value = value.strip('"')
                            if key == 'from':
                                from_node = int(value)
                            elif key == 'to':
                                to_node = int(value)
                            elif key == 'label':
                                label = value
                        if from_node is not None and to_node is not None and label is not None:
                            existing_edges[(from_node, to_node)] = {'from': from_node, 'to': to_node, 'label': label}
        for i in range(self.num_vertex):
            negocio = self.get_label(i)
            id = negocio._id
            nombre = negocio._nombre
            if id not in existing_nodes:
                existing_nodes[id] = {'id': id, 'label': f"{id} {nombre}"}
        for i in range(self.num_vertex):
            adjs = self.adjacent(i)
            if adjs and not adjs.isEmpty:
                for j in range(adjs._length):
                    adj = adjs.getData(j)
                    des = adj._destination + 1
                    if (i + 1, des) not in existing_edges:
                        existing_edges[(i + 1, des)] = {'from': i + 1, 'to': des, 'label': str(adj._weight)}
        nodes_js = ',\n'.join(f'{{id: {node["id"]}, label: "{node["label"]}"}}' for node in existing_nodes.values())
        edges_js = ',\n'.join(f'{{from: {edge["from"]}, to: {edge["to"]}, label: "{edge["label"]}"}}' for edge in existing_edges.values())
        
        js_content = (
            f'var nodes = new vis.DataSet([\n{nodes_js}\n]);\n\n'
            f'var edges = new vis.DataSet([\n{edges_js}\n]);\n\n'
            'var container = document.getElementById("mynetwork");\n'
            'var data = {nodes: nodes, edges: edges};\n'
            'var options = {};\n'
            'var network = new vis.Network(container, data, options);\n'
        )
        with open(url, 'w') as file:
            file.write(js_content)