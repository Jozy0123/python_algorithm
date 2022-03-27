from python_algorithm.Graph.GraphABC import GraphABC
from typing import List, Iterator, Set, Optional
from copy import copy

### non directional graph
class Graph(GraphABC):

    def __init__(self, matrix=None, unconn=0, nodes_map=None):
        if nodes_map is None and matrix is not None:
            nodes_map = {i+1: i for i in range(len(matrix))}
        elif nodes_map is None and matrix is None:
            nodes_map = {}
        else:
            nodes_map = copy(nodes_map)
        nodes_count = len(matrix)
        for i in matrix:
            if len(i) != nodes_count:
                raise ValueError("matrix should be square matrix!")
        self._matrix = [matrix[i][:] for i in range(nodes_count)]
        self._unconn = unconn
        self._num_nodes = nodes_count
        self._nodes_map = nodes_map

    def vertex_num(self) -> int:
        return self._num_nodes

    def edge_num(self) -> int:
        return int(sum([1 for i in self._matrix for j in i if j != self._unconn])/2)

    def is_empty(self) -> bool:
        if self._matrix is None or self._num_nodes == 0:
            return True
        else:
            return False

    def vertices(self) -> List[int]:
        return [i for i in self._nodes_map.keys()]

    def edges(self) -> Set[str]:
        edges_set = set()
        for i in range(self._num_nodes):
            for j in range(i, self._num_nodes):
                if self._matrix[i][j] != self._unconn:
                    edges_set.add(f"{i+1}<->{j+1}")
        return edges_set

    def add_vertex(self, vertex):
        if self._nodes_map.get(vertex) is not None:
            raise ValueError("vertex has already been added!")
        self._num_nodes += 1
        self._nodes_map[vertex] = self._num_nodes - 1

        for i in self._matrix:
            i.append(self._unconn)

        self._matrix.append([self._unconn] * self._num_nodes)

    def add_edge(self, node_1, node_2):
        if self._nodes_map.get(node_1) is None or self._nodes_map.get(node_2) is None:
            raise ValueError("wrong nodes")
        else:
            self._matrix[self._nodes_map[node_1]][self._nodes_map[node_2]] = 1
            self._matrix[self._nodes_map[node_2]][self._nodes_map[node_1]] = 1

    def get_edge(self, node_1, node_2) -> Optional[int]:
        conn = self._matrix[self._nodes_map[node_1]][self._nodes_map[node_2]]
        if conn == self._unconn:
            return None
        else:
            return conn

    def out_edge(self, node) -> Iterator[str]:
        for i in range(len(self._matrix[self._nodes_map[node]])):
            if self._matrix[self._nodes_map[node]][i] == 1:
                yield f"{node} <-> {i+1}"

    def degree(self, node) -> int:
        degree = 0
        for _ in self.out_edge(node):
            degree += 1

        return degree


if __name__ == "__main__":
    mat = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]
    G = Graph(matrix=mat)
    print([i for i in G.out_edge(1)])
    print(G.degree(1))
    print(G.edges())
    print(G.vertices())
    print(G.vertex_num())
    print(G.edge_num())
    G.add_vertex(5)
    G.add_edge(5, 4)
    print(G.edge_num())
    print(G.edges())
