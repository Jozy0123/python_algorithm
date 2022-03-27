from abc import abstractmethod, ABC


class BinTreeABC(ABC):

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
    def left(self):
        raise NotImplementedError

    @abstractmethod
    def right(self):
        raise NotImplementedError

    @abstractmethod
    def set_left(self, btree):
        raise NotImplementedError

    @abstractmethod
    def set_right(self, btree):
        raise NotImplementedError

    @abstractmethod
    def traversal(self):
        raise NotImplementedError

    @abstractmethod
    def forall(self, op):
        raise NotImplementedError
