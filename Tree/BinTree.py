from Tree.BinaryTreeABC import BinTreeABC


class BinTNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinTree(BinTreeABC):

    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def num_nodes(self):
        if self.is_empty():
            return 0
        else:
            return 1 + self.left().num_nodes() + self.right().num_nodes()

    def data(self):
        return self.root.data

    def left(self):
        if self.root is not None:
            return BinTree(self.root.left)
        else:
            return BinTree()

    def right(self):
        if self.root is not None:
            return BinTree(self.root.right)
        else:
            return BinTree()

    def set_left(self, left_node):
        self.root.left = left_node

    def set_right(self, right_node):
        self.root.right = right_node

    def traversal(self):
        if self.is_empty():
            return
        self.left().traversal()
        print(self.data())
        self.right().traversal()

    def forall(self, op):
        if self.is_empty():
            return
        self.root.data = op(self.root.data)
        if self.left() is not None:
            self.left().forall(op)
        if self.right() is not None:
            self.right().forall(op)


if __name__ == "__main__":
    t1 = BinTNode(2, BinTNode(4))
    t2 = BinTNode(8)
    t3 = BinTree(BinTNode(5, t1, t2))
    t3.traversal()
    # t3.forall(lambda x: x**2)
    # print(t3)
    # print(t3.num_nodes())
    # t3.forall(lambda x: x**2)
    # t3.traversal()
