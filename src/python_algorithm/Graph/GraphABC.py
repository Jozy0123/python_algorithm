from abc import abstractmethod, ABC


class GraphABC(ABC):

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def vertex_num(self):
        pass

    @abstractmethod
    def edge_num(self):
        pass

    @abstractmethod
    def vertices(self):
        pass

    @abstractmethod
    def edges(self):
        pass

    @abstractmethod
    def add_vertex(self, vertex):
        pass

    @abstractmethod
    def add_edge(self, v1, v2):
        pass

    @abstractmethod
    def get_edge(self, v1, v2):
        pass

    @abstractmethod
    def out_edge(self, v):
        pass

    @abstractmethod
    def degree(self, v):
        pass
