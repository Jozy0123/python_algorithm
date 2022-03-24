from GraphABC import GraphABC

### non directional graph
class Graph(GraphABC):

    def __init__(self, matrix=None, conn=0, nodes_map=None):
        if nodes_map is None:
            nodes_map = {i: i for i in range(len(matrix))}
        nodes_count = len(matrix)
        for i in matrix:
            if len(i) != nodes_count:
                raise ValueError("matrix should be square matrix!")
        self._matrix = [matrix[i][:] for i in range(nodes_count)]
        self._conn = conn
        self._num_nodes = nodes_count
        self._nodes_map = nodes_map

    def vertex_num(self):
        return self._num_nodes

    def edge_num(self):
        if self._conn == 0:
            return sum([j for i in self._matrix for j in i])

    def is_empty(self):
        if self._matrix is None or self._num_nodes == 0:
            return True
        else:
            return False

    def vertices(self):
        return {i for i in range(self._num_nodes)}

    def edges(self):
        edges_set = set()
        for i in range(self._num_nodes):
            for j in range(self._num_nodes):
                if self._matrix[i][j] != self._conn:
                    edges_set.add("{i}->{j}")
        return edges_set

    def add_vertex(self, vertex):
        if self._nodes_map.get(vertex) is not None:
            raise ValueError("vertex has already been added!")
        self._num_nodes += 1
        self._nodes_map[vertex] = self._num_nodes

        for i in self._matrix:
            i.append(self._conn)

        self._matrix.append([self._conn] * self._num_nodes)

    def add_edge(self, node_1, node_2):
        if self._nodes_map.get(node_1) is None or self._nodes_map.get(node_2) is None:
            raise ValueError("wrong nodes")
        else:
            self._matrix[node_1][node_2] = 1

    def get_edge(self, node_1, node_2):
        return self._matrix[node_1][node_2]

    def out_edge(self, node):

    def degree(self, node):





