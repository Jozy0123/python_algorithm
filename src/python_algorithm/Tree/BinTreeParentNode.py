from python_algorithm.Tree.BinTree import BinTNode, BinTree


class BinTNodeWithParent(BinTNode):

    def __init__(self, data, left=None, right=None, parent=None):
        super().__init__(data, left, right)
        self.parent = parent

