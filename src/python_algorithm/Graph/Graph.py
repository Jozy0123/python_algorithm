from python_algorithm.Graph.GraphABC import GraphABC


### non directional graph
class Graph(GraphABC):

    def __init__(self, matrix=None, unconn=0, nodes_map=None):
        if nodes_map is None:
            nodes_map = {i+1: i for i in range(len(matrix))}
        nodes_count = len(matrix)
        for i in matrix:
            if len(i) != nodes_count:
                raise ValueError("matrix should be square matrix!")
        self._matrix = [matrix[i][:] for i in range(nodes_count)]
        self._unconn = unconn
        self._num_nodes = nodes_count
        self._nodes_map = nodes_map

    def vertex_num(self):
        return self._num_nodes

    def edge_num(self):
        return sum([1 for i in self._matrix for j in i if j != self._unconn])/2

    def is_empty(self):
        if self._matrix is None or self._num_nodes == 0:
            return True
        else:
            return False

    def vertices(self):
        return [i for i in self._nodes_map.keys()]

    def edges(self):
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

    def get_edge(self, node_1, node_2):
        return self._matrix[node_1][node_2]

    def out_edge(self, node):
        for i in range(len(self._matrix[self._nodes_map[node]])):
            if self._matrix[self._nodes_map[node]][i] == 1:
                yield f"{node} <-> {i+1}"

    def degree(self, node):
        degree = 0
        for _ in self.out_edge(node):
            degree += 1

        return degree


def traversal_graph(graph: Graph, visited):
    init_node = graph.vertices()[0]
    visited[init_node] = 1
    out_nodes = []
    for out in graph.out_edge(init_node):
        out_node = out.split(" <-> ")[1]
        if out_node not in visited:
            traversal_graph()


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


