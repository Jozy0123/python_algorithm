from treeABC import BinTreeABC


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
        return self.root.left

    def right(self):
        return self.root.right

    def set_left(self, left_tree):
        self.root.left = left_tree

    def set_right(self, right_tree):
        self.root.right = right_tree

    def traversal(self):
        if self.is_empty():
            print("empty tree")
        elif self.left() is None and self.right() is None:
            print(self.data())
        if self.left() is not None:
            self.left().traversal()
        if self.right() is not None:
            self.right().traversal()

    def forall(self, op):
        pass


if __name__ == "__main__":
    t1 = BinTree(BinTNode(2, BinTree(BinTNode(4)), None))
    t2 = BinTree(BinTNode(8, None, None))
    t3 = BinTree(BinTNode(5, t1, t2))
    t3.traversal()
    # t3.forall(lambda x: x**2)
    # print(t3)
    print(t3.num_nodes())






