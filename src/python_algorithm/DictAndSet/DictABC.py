from abc import abstractmethod, ABC


class DictABC(ABC):

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @abstractmethod
    def num(self):
        raise NotImplementedError

    @abstractmethod
    def search(self, key):
        raise NotImplementedError

    @abstractmethod
    def insert(self, key, value):
        raise NotImplementedError

    @abstractmethod
    def delete(self, key):
        raise NotImplementedError

    @abstractmethod
    def values(self):
        raise NotImplementedError

    @abstractmethod
    def entries(self):
        raise NotImplementedError

