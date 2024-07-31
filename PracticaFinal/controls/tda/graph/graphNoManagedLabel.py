from controls.tda.graph.graphNoManeged import GraphNoManaged
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.linked.linkedList import Linked_List
from math import nan
import heapq
from math import inf
import time

class GraphNoManagedLabel(GraphNoManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        self.__labels = []
        self.__labelsVertex = {}
        for i in range(0, self.num_vertex):
            self.__labels.append(None)
        
    def getVertex(self, label):
        try:
            return self.__labelsVertex[str(label)]
        except Exception as error:
            return -1    
    
    def label_vertex(self, v, label):
        self.__labels[v] = label
        self.__labelsVertex[str(label)] = v
        
    def getLabel(self, v):
        return self.__labels[v]
    
    def exist_edge_E(self, label1, label2):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            return self.exist_edges(v1, v2)
        else:
            return False
        
    def insert_edges_weight_E(self, label1, label2, weight):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            self.insert_edges_weight(v1, v2, weight)
        else:
            raise ArrayPositionException("Vertex not found") 
        
    def insert_edges_E(self, label1, label2):
        self.insert_edges_weight_E(label1, label2, nan)
    
    def weight_edges_E(self, label1, label2):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            return self.weight_edges(v1, v2)
        else:
            raise ArrayPositionException("Vertex not found") 
        
    def adjacent_E(self, label1):
        v1 = self.getVertex(label1)
        if v1 != -1:
            return self.adjacent(v1)
        else:
            raise ArrayPositionException("Vertex not found")
    
    ### Dijkstra
    def dijkstra(self, start_label):
        start = self.getVertex(start_label)
        distances = {v: float('infinity') for v in range(self.num_vertex)}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue

            list_adj = self.adjacent(current_vertex).toArray
            for adj in list_adj:
                neighbor = adj._destination
                weight = adj._weight
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    def shortest_path_dijkstra(self, start_label, end_label):
        start = self.getVertex(start_label)
        end = self.getVertex(end_label)
        if start == -1 or end == -1:
            raise ArrayPositionException("Start or end vertex not found")

        start_time = time.time()  

        distances = {vertex: float('infinity') for vertex in range(self.num_vertex)}
        previous_vertices = {vertex: None for vertex in range(self.num_vertex)}
        distances[start] = 0
        vertices = set(range(self.num_vertex))

        while vertices:
            current = min(vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current)

            if distances[current] == float('infinity'):
                break

            for adj in self.adjacent(current).toArray:
                neighbor = adj._destination
                cost = adj._weight
                alternative_route = distances[current] + cost
                if alternative_route < distances[neighbor]:
                    distances[neighbor] = alternative_route
                    previous_vertices[neighbor] = current

        path, current = [], end
        while previous_vertices[current] is not None:
            path.insert(0, current)
            current = previous_vertices[current]
        if path:
            path.insert(0, current)

        end_time = time.time()  
        elapsed_time = end_time - start_time  

        return [self.getLabel(v) for v in path], distances[end], elapsed_time


    ### Floyd-Warshall
    def floyd_warshall(self):
        num_v = self.num_vertex
        distances = [[inf] * num_v for _ in range(num_v)]
        next_node = [[None] * num_v for _ in range(num_v)]

        for v in range(num_v):
            distances[v][v] = 0

        for v in range(num_v):
            list_adj = self.adjacent_E(self.getLabel(v)).toArray
            for adj in list_adj:
                u = adj._destination
                weight = adj._weight
                distances[v][u] = weight
                next_node[v][u] = u

        for k in range(num_v):
            for i in range(num_v):
                for j in range(num_v):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
                        next_node[i][j] = next_node[i][k]

        return distances, next_node

    def shortest_path_floyd(self, start_label, end_label):
        start = self.getVertex(start_label)
        end = self.getVertex(end_label)
        if start == -1 or end == -1:
            raise ArrayPositionException("Start or end vertex not found")

        start_time = time.time()

        distances, next_node = self.floyd_warshall()
        if next_node[start][end] is None:
            end_time = time.time()
            elapsed_time = end_time - start_time 
            return [], float('infinity'), elapsed_time

        path = [start]
        while start != end:
            start = next_node[start][end]
            path.append(start)

        end_time = time.time()  
        elapsed_time = end_time - start_time  

        return [self.getLabel(v) for v in path], distances[self.getVertex(start_label)][self.getVertex(end_label)], elapsed_time


    ### Saber si esta connectado
    def siEstaConectado(self):
        visited = set()
        
        def dfs(v):
            visited.add(v)
            for neighbor in self.adjacent(v).toArray:
                if neighbor._destination not in visited:
                    dfs(neighbor._destination)
        dfs(0)
        return len(visited) == self.num_vertex

    # ## Usando Lista

    # def dijkstra(self, start_label):
    #     start = self.getVertex(start_label)
    #     distances = Linked_List()
    #     for _ in range(self.num_vertex):
    #         distances.append(float('infinity'))
    #     distances.update(start, 0)
    #     pq = [(0, start)]

    #     while pq:
    #         current_distance, current_vertex = heapq.heappop(pq)

    #         if current_distance > distances.get(current_vertex):
    #             continue

    #         list_adj = self.adjacent(current_vertex).toArray
    #         for adj in list_adj:
    #             neighbor = adj._destination
    #             weight = adj._weight
    #             distance = current_distance + weight

    #             if distance < distances.get(neighbor):
    #                 distances.update(neighbor, distance)
    #                 heapq.heappush(pq, (distance, neighbor))

    #     return distances

    # def shortest_path_dijkstra(self, start_label, end_label):
    #     start = self.getVertex(start_label)
    #     end = self.getVertex(end_label)
    #     if start == -1 or end == -1:
    #         raise ArrayPositionException("Start or end vertex not found")

    #     start_time = time.time()

    #     distances = Linked_List()
    #     previous_vertices = Linked_List()
    #     for _ in range(self.num_vertex):
    #         distances.append(float('infinity'))
    #         previous_vertices.append(None)
    #     distances.update(start, 0)
    #     vertices = set(range(self.num_vertex))

    #     while vertices:
    #         current = min(vertices, key=lambda vertex: distances.get(vertex))
    #         vertices.remove(current)

    #         if distances.get(current) == float('infinity'):
    #             break

    #         for adj in self.adjacent(current).toArray:
    #             neighbor = adj._destination
    #             cost = adj._weight
    #             alternative_route = distances.get(current) + cost
    #             if alternative_route < distances.get(neighbor):
    #                 distances.update(neighbor, alternative_route)
    #                 previous_vertices.update(neighbor, current)

    #     path, current = [], end
    #     while previous_vertices.get(current) is not None:
    #         path.insert(0, current)
    #         current = previous_vertices.get(current)
    #     if path:
    #         path.insert(0, current)

    #     end_time = time.time()
    #     elapsed_time = end_time - start_time

    #     return [self.getLabel(v) for v in path], distances.get(end), elapsed_time
    
    # ### Floyd-Warshall

    # def floyd_warshall(self):
    #     num_v = self.num_vertex
    #     distances = [Linked_List() for _ in range(num_v)]
    #     next_node = [Linked_List() for _ in range(num_v)]

    #     for v in range(num_v):
    #         for _ in range(num_v):
    #             distances[v].append(inf)
    #             next_node[v].append(None)
    #         distances[v].update(v, 0)

    #     for v in range(num_v):
    #         list_adj = self.adjacent_E(self.getLabel(v)).toArray
    #         for adj in list_adj:
    #             u = adj._destination
    #             weight = adj._weight
    #             distances[v].update(u, weight)
    #             next_node[v].update(u, u)

    #     for k in range(num_v):
    #         for i in range(num_v):
    #             for j in range(num_v):
    #                 if distances[i].get(j) > distances[i].get(k) + distances[k].get(j):
    #                     distances[i].update(j, distances[i].get(k) + distances[k].get(j))
    #                     next_node[i].update(j, next_node[i].get(k))

    #     return distances, next_node

    # def shortest_path_floyd(self, start_label, end_label):
    #     start = self.getVertex(start_label)
    #     end = self.getVertex(end_label)
    #     if start == -1 or end == -1:
    #         raise ArrayPositionException("Start or end vertex not found")

    #     start_time = time.time()

    #     distances, next_node = self.floyd_warshall()
    #     if next_node[start].getNode(end) is None:
    #         end_time = time.time()
    #         elapsed_time = end_time - start_time 
    #         return [], float('infinity'), elapsed_time

    #     path = [start]
    #     while start != end:
    #         start = next_node[start].get(end)
    #         path.append(start)

    #     end_time = time.time()  
    #     elapsed_time = end_time - start_time  

    #     return [self.getLabel(v) for v in path], distances[self.getVertex(start_label)].get(self.getVertex(end_label)), elapsed_time