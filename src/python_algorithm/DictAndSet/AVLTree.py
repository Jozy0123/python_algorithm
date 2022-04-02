from python_algorithm.Tree.BinTree import BinTNode
from python_algorithm.DictAndSet.DictBinTree import DictBinTree


class AVLNode:

    def __init__(self, data, left=None, right=None):
        super().__init__(left, right)
        self.balance_factor = 0


class AVLTree(DictBinTree):

    def __init__(self):
        super().__init__()

    @staticmethod
    def right_rotation(root_node):
        left_node = root_node.left
        root_node.left = left_node.right
        left_node.right = root_node

        root_node = left_node

        root_node.balance_factor = 0
        left_node.balance_factor = 0
        return root_node

    @staticmethod
    def left_rotation(root_node):
        right_node = root_node.right
        root_node.right = right_node.left
        right_node.left = root_node

        root_node = right_node

        root_node.balance_factor = 0
        right_node.balance_factor = 0

        return  root_node

    @staticmethod
    def left_right_rotation(root_node):
        left_node = root_node.left
        root_node.left = root_node.left.right
        left_node.right = None
        root_node.left.left = left_node

        left_node = root_node.left

        root_node.left = left_node.right
        left_node.right = None

        root_node = left_node
        return root_node

    @staticmethod
    def right_left_rotation(root_node):







    def insert(self, key, value):


