from python_algorithm.Tree.BinaryTreeABC import BinTreeABC


class BinaryTreeList(BinTreeABC):

    def __init__(self, data, left=None, right=None):
        if left is not None:
            assert isinstance(left, BinTreeList)
        if right is not None:
            assert isinstance(right, BinTreeList)
        self.root = [data, left, right]

    def is_empty(self):
        if self.root[0] is None:
            return True
        else:
            return False

    def data(self):
        return self.root[0]

    def num_nodes(self):
        if self.data() is None:
            return 0
        elif self.left() is None and self.right() is None:
            return 1
        elif self.left() is not None and self.right() is None:
            return self.left().num_nodes() + 1
        elif self.right() is not None and self.left() is None:
            return self.right().num_nodes() + 1
        else:
            return self.left().num_nodes() + 1 + self.right().num_nodes()

    def left(self):
        return self.root[1]

    def right(self):
        return self.root[2]

    def set_root(self, data):
        self.root[0] = data

    def set_left(self, tree):
        self.root[2] = tree

    def set_right(self, tree):
        self.root[2] = tree

    def traversal(self):
        if self.is_empty() is True:
            return
        if self.left() is None and self.right() is None:
            print(self.data())
        if self.left() is not None:
            self.left().traversal()
            print(self.data())
        if self.right() is not None:
            self.right().traversal()

    def forall(self, op):
        if self.is_empty() is True:
            return
        if self.left() is None and self.right() is None:
            self.set_root(op(self.data()))
        if self.left() is not None:
            self.left().forall(op)
            self.set_root(op(self.data()))
        if self.right() is not None:
            self.right().forall(op)

    def __str__(self):
        return ' '.join(map(str, self.root))


if __name__ == "__main__":
    t1 = BinTreeList(2, BinTreeList(4), None)
    t2 = BinTreeList(8, None, None)
    t3 = BinTreeList(5, t1, t2)
    print(t3)
    t3.traversal()
    t3.forall(lambda x: x**2)
    print(t3)
    print(t3.num_nodes())
