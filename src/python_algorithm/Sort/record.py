class Record:

    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __eq__(self, another):
        return self.key == another.key

    def __lt__(self, another):
        return self.key < another.key

    def __le__(self, another):
        return self.key <= another.key

    def __gt__(self, another):
        return self.key > another.key

    def __ge__(self, another):
        return self.key >= another.key
