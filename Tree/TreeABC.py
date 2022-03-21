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
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass

    @abstractmethod
    def set_left(self, btree):
        pass

    @abstractmethod
    def set_right(self, btree):
        pass

    @abstractmethod
    def traversal(self):
        pass

    @abstractmethod
    def forall(self, op):
        pass
