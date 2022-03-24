from abc import abstractmethod, ABC


class TreeABC(ABC):

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def num_nodes(self):
        pass

    @abstractmethod
    def data(self):
        pass

    @abstractmethod
    def first_child(self):
        pass

    @abstractmethod
    def children(self):
        pass

    @abstractmethod
    def set_first(self, tree):
        pass

    @abstractmethod
    def insert_child(self, tree):
        pass

    @abstractmethod
    def traversal(self):
        pass

    @abstractmethod
    def forall(self, op):
        pass
