from python_algorithm.Graph.GraphABC import GraphABC
from typing import List, Union, Dict, Optional
from copy import copy


def out_edge(matrix_row: List[int],
             unconn: Union[int, float] = 0,
             nodes_map: Dict[int, int] = None):
    edge_list = []
    for i in nodes_map.keys():
        if matrix_row[nodes_map[i]] != unconn:
            edge_list.append((i, matrix_row[nodes_map[i]]))
    return edge_list


## undirectional graph
class GraphAL(GraphABC):

    def __init__(self,
                 matrix: Optional[List[List[int]]] = None,
                 unconn: Union[int, float] = 0,
                 nodes_map: Optional[Dict[int, int]] = None
                 ):
        if nodes_map is None:
            nodes_map = {i + 1: i for i in range(len(matrix))}
        else:
            nodes_map = copy(nodes_map)

        if matrix is None:
            matrix = []
        else:
            matrix = list(i[:] for i in matrix)

        vertices_num = len(matrix)
        for i in matrix:
            if len(i) != vertices_num:
                raise ValueError("The input matrix must be square!")

        self._matrix = [out_edge(i, unconn, nodes_map) for i in matrix]
        self._vnum = vertices_num
        self._unconn = unconn
        self._nodes_map = nodes_map

    def is_empty(self):
        return self._vnum == 0

    def vertex_num(self):
        return self._vnum

    def edge_num(self):
        return sum([len(i) for i in self._matrix])

    def vertices(self):
        return list(self._nodes_map.keys())

    def edges(self):
        for i in self._matrix:
            for j in i:
                yield j

    def add_vertex(self, v):
        if self._nodes_map.get(v, None) is not None:
            raise ValueError("Node exists!")
        self._matrix.append([])
        self._vnum = self._vnum + 1
        self._nodes_map[self._vnum] = self._vnum - 1

    def add_edge(self, v1, v2):
        if self._nodes_map.get(v1, None) is None or self._nodes_map.get(v2, None) is None:
            raise ValueError("at least one of the node does not exist, add it first")
        for i in self._matrix[self._nodes_map[v1]]:
            if v2 == i[0]:
                raise ValueError("edge exists!")
        self._matrix[self._nodes_map[v1]].insert(self._nodes_map[v2], (v2, 1))

    def get_edge(self, v1, v2):
        if self._nodes_map.get(v1, None) is None or self._nodes_map.get(v2, None) is None:
            raise ValueError("at least one of the node does not exist, add it first")
        for i in self._matrix[self._nodes_map[v1]]:
            if v2 == i[0]:
                return v1, v2, i[1]
        return v1, v2, 0

    def out_edge(self, v):
        for i in self._matrix[self._nodes_map[v]]:
            yield i

    def degree(self, v):
        degree = 0
        for _ in self._matrix[self._nodes_map[v]]:
            degree += 1
        return degree


if __name__ == "__main__":
    mat = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]
    G = GraphAL(matrix=mat)
    print([i for i in G.out_edge(1)])
    print(G.degree(1))
    print([i for i in G.edges()])
    print(G.vertices())
    print(G.vertex_num())
    print(G.edge_num())
    G.add_vertex(5)
    G.add_edge(5, 4)
    print(G.edge_num())
    print([i for i in G.edges()])
