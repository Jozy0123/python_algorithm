from abc import abstractmethod, ABC


class GraphABC(ABC):

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @abstractmethod
    def vertex_num(self):
        raise NotImplementedError

    @abstractmethod
    def edge_num(self):
        raise NotImplementedError

    @abstractmethod
    def vertices(self):
        raise NotImplementedError

    @abstractmethod
    def edges(self):
        raise NotImplementedError

    @abstractmethod
    def add_vertex(self, vertex):
        raise NotImplementedError

    @abstractmethod
    def add_edge(self, v1, v2):
        raise NotImplementedError

    @abstractmethod
    def get_edge(self, v1, v2):
        raise NotImplementedError

    @abstractmethod
    def out_edge(self, v):
        raise NotImplementedError

    @abstractmethod
    def degree(self, v):
        raise NotImplementedError
