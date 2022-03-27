from abc import abstractmethod, ABC


class TreeABC(ABC):

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @abstractmethod
    def num_nodes(self):
        raise NotImplementedError

    @abstractmethod
    def data(self):
        raise NotImplementedError

    @abstractmethod
    def first_child(self):
        raise NotImplementedError

    @abstractmethod
    def children(self):
        raise NotImplementedError

    @abstractmethod
    def set_first(self, tree):
        raise NotImplementedError

    @abstractmethod
    def insert_child(self, tree):
        raise NotImplementedError

    @abstractmethod
    def traversal(self):
        raise NotImplementedError

    @abstractmethod
    def forall(self, op):
        raise NotImplementedError
