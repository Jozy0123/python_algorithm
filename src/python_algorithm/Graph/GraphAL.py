from python_algorithm.Graph.GraphABC import GraphABC
from typing import List, Union, Dict, Optional, Iterator, Tuple, Any
from copy import copy, deepcopy


def out_edge(matrix_row: List[int],
             unconn: Union[int, float] = 0,
             nodes_map: Dict[int, int] = None):
    edge_list = []
    for i in nodes_map.keys():
        if matrix_row[nodes_map[i]] != unconn:
            edge_list.append((i, matrix_row[nodes_map[i]]))
    return edge_list


## for both directional and undirectional graph
class GraphAL(GraphABC):

    def __init__(self,
                 matrix: Optional[List[List[int]]] = None,
                 unconn: Union[int, float] = 0,
                 nodes_map: Optional[Dict[int, int]] = None,
                 directional: bool = False
                 ):
        if nodes_map is None and matrix is not None:
            nodes_map = {i+1: i for i in range(len(matrix))}
        elif nodes_map is None and matrix is None:
            nodes_map = {}
        else:
            nodes_map = copy(nodes_map)

        if matrix is None and nodes_map is not None:
            matrix = []
        else:
            matrix = list(i[:] for i in matrix)

        vertices_num = len(matrix)
        for i in matrix:
            if len(i) != vertices_num:
                raise ValueError("The input matrix must be square!")

        if vertices_num == 0:
            for _ in nodes_map.keys():
                matrix.append([])
        else:
            matrix = [out_edge(i, unconn, nodes_map) for i in matrix]

        self._matrix = matrix
        self._vnum = vertices_num
        self._unconn = unconn
        self._nodes_map = nodes_map
        self._directional = directional

    @property
    def is_directed(self) -> bool:
        return self._directional

    @property
    def nodes_rep(self) -> Dict[Any, int]:
        return deepcopy(self._nodes_map)

    def is_empty(self) -> bool:
        return self._vnum == 0

    def vertex_num(self) -> int:
        return self._vnum

    def edge_num(self) -> int:
        if self._directional:
            return sum([len(i) for i in self._matrix])
        else:
            return int(sum([len(i) for i in self._matrix]) / 2)

    def vertices(self) -> List[int]:
        return list(self._nodes_map.keys())

    def edges(self) -> Iterator[str]:
        if self._directional:
            for i in self._nodes_map.keys():
                for j in self._matrix[self._nodes_map[i]]:
                    yield f"{j[0]} -> {i} -> {j[1]}"
        else:
            for i in self._nodes_map.keys():
                for j in self._matrix[self._nodes_map[i]]:
                    if j[0] > i:
                        yield f"{j[0]} <-> {i} <-> {j[1]}"

    def add_vertex(self, v):
        if self._nodes_map.get(v, None) is not None:
            raise ValueError("Node exists!")
        self._matrix.append([])
        self._vnum += 1
        self._nodes_map[v] = self._vnum - 1

    def add_edge(self, v1, v2, weight=1):
        if self._nodes_map.get(v1, None) is None or self._nodes_map.get(v2, None) is None:
            raise ValueError("at least one of the node does not exist, add it first")
        edge_list_len = len(self._matrix[self._nodes_map[v1]])
        if self._directional:
            i = 0
            while i < edge_list_len:
                if v2 == self._matrix[i][0]:
                    raise ValueError("edge exists!")
                i += 1
            self._matrix[self._nodes_map[v1]].insert(i, (v2, weight))
        else:
            i = 0
            while i < edge_list_len:
                if v2 == self._matrix[i][0]:
                    raise ValueError("edge exists!")
                i += 1
            self._matrix[self._nodes_map[v1]].insert(i, (v2, weight))
            self._matrix[self._nodes_map[v2]].insert(i, (v1, weight))

    def get_edge(self, v1, v2) -> Tuple[int, int, int]:
        if self._nodes_map.get(v1, None) is None or self._nodes_map.get(v2, None) is None:
            raise ValueError("at least one of the node does not exist, add it first")
        for i in self._matrix[self._nodes_map[v1]]:
            if v2 == i[0]:
                return v1, v2, i[1]
        return v1, v2, self._unconn

    def out_edge(self, v) -> Iterator[str]:
        if self._directional:
            for i in self._matrix[self._nodes_map[v]]:
                yield f"{v} -> {i[0]} -> {i[1]}"
        else:
            for i in self._matrix[self._nodes_map[v]]:
                yield f"{v} <-> {i[0]} <-> {i[1]}"

    def degree(self, v) -> int:
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
    print(G.vertex_num())
    print(G.edge_num())
    print([i for i in G.edges()])
