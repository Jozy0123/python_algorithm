from python_algorithm.DictAndSet.DictABC import DictABC
from python_algorithm.Sort.record import Record
from python_algorithm.Tree.BinTree import BinTNode
from python_algorithm.StackAndQueue.StackAndQueue import SStack


class DictBinTree(DictABC):

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    @staticmethod
    def nodes_num(top_node):
        if top_node is None:
            return 0
        else:
            return 1 + DictBinTree.nodes_num(top_node.left) + DictBinTree.nodes_num(top_node.right)

    def num(self):
        return self.nodes_num(self._root)

    def search(self, key):
        tree = self._root
        while tree is not None:
            if key > tree.root.data.key:
                tree = tree.right
            elif key < tree.root.data.key:
                tree = tree.left
            else:
                return tree.root.data.key
        return None

    def insert(self, key, value):
        tree = self._root
        if tree is None:
            tree.data = BinTNode(Record(key, value))
            return
        while True:
            if key < tree.left.data.key:
                if tree.left is None:
                    tree.left = BinTNode(Record(key, value))
                    return
                else:
                    tree = tree.left
            elif key > tree.right.data.key:
                if tree.right is None:
                    tree.right = BinTNode(Record(key, value))
                    return
                else:
                    tree = tree.right
            else:
                tree.data.data = value
                return

    def values(self):
        if self._root is None:
            return
        else:
            node = self._root
            stack = SStack()
            while node is not None or not stack.is_empty():
                while node is not None:
                    stack.push(node)
                    node = node.left
                node = stack.pop()
                yield node.data.data
                node = node.right

    def entries(self):
        if self._root is None:
            return
        else:
            node = self._root
            stack = SStack()
            while node is not None or not stack.is_empty():
                while node is not None:
                    stack.push(node)
                    node = node.left
                node = stack.pop()
                yield node.data.key, node.data.data
                node = node.right

    def delete(self, key):
        child, parent = self._root, None
        while child is not None and child.data.key != key:
            parent = child
            if child.data.key > key:
                child = child.left
            else:
                child = child.right
            if child is None:
                return

        if child.left is None:
            if parent is None:
                self._root = None
            elif parent.left is child:
                parent.left = child.right
            else:
                parent.right = child.right
            return

        child_left_node = child.left
        while child_left_node is not None:
            child_left_node = child_left_node.right

        if child.right is not None:
            child_left_node.right = child.right

        if parent is None:
            self._root = None
        elif parent.left is child:
            parent.left = child.left
        else:
            parent.right = child.left
