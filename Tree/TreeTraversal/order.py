import sys
sys.path.append('/Users/joeyzhou/Documents/projects/PycharmProjects/python_algorithm')

from Tree.BinTree import BinTree, BinTNode
from enum import Enum
from StackAndQueue.StackAndQueue import SQueue


class TraversalType(Enum):
    ROOT_FIRST_ORDER = 0
    ROOT_MIDDLE_ORDER = 1
    ROOT_LAST_ORDER = 2


def tree_pre_order(tree: BinTree,
                   traversal: TraversalType = TraversalType.ROOT_FIRST_ORDER):
    while tree.data() is None:
        return
    if traversal == TraversalType.ROOT_FIRST_ORDER:
        print(tree.data())
        tree_pre_order(tree.left())
        tree_pre_order(tree.right())
    elif traversal == TraversalType.ROOT_MIDDLE_ORDER:
        tree_pre_order(tree.left())
        print(tree.data())
        tree_pre_order(tree.right())
    elif traversal == TraversalType.ROOT_LAST_ORDER:
        tree_pre_order(tree.left())
        tree_pre_order(tree.right())
        print(tree.data())


def tree_level_order(tree: BinTree):
    queue = SQueue()
    if not tree.is_empty():
        queue.enqueue(tree)
    else:
        raise ValueError("Tree is empty!")
    while not queue.is_empty():
        tree = queue.dequeue()
        if tree.is_empty():
            continue
        print(tree.data())
        if not tree.left().is_empty():
            queue.enqueue(tree.left())
        if not tree.right().is_empty():
            queue.enqueue(tree.right())


if __name__ == "__main__":
    t1 = BinTNode("D", None, BinTNode("H"))
    t2 = BinTNode("E", None, BinTNode("I"))
    t3 = BinTNode("B", t1, t2)
    t4 = BinTNode("F", BinTNode("J"), BinTNode("K"))
    t5 = BinTNode("C", t4, BinTNode("G"))
    t6 = BinTNode(t3, t5)

    tree_pre_order(BinTree(t6), TraversalType.ROOT_FIRST_ORDER)
    tree_pre_order(BinTree(t6), TraversalType.ROOT_MIDDLE_ORDER)
    tree_pre_order(BinTree(t6), TraversalType.ROOT_LAST_ORDER)
    tree_pre_order(BinTree(t6))



