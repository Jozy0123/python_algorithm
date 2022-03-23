import sys
sys.path.append('/Users/joeyzhou/Documents/projects/PycharmProjects/python_algorithm')

from Tree.BinTree import BinTree, BinTNode
from enum import Enum
from StackAndQueue.StackAndQueue import LQueue, SStack


class TraversalType(Enum):
    ROOT_FIRST_ORDER = 0
    ROOT_MIDDLE_ORDER = 1
    ROOT_LAST_ORDER = 2


def tree_pre_order(tree: BinTree,
                   traversal: TraversalType = TraversalType.ROOT_FIRST_ORDER):
    while tree.is_empty():
        return
    if traversal == TraversalType.ROOT_FIRST_ORDER:
        print(tree.data())
        tree_pre_order(tree.left(), traversal)
        tree_pre_order(tree.right(), traversal)
    elif traversal == TraversalType.ROOT_MIDDLE_ORDER:
        tree_pre_order(tree.left(), traversal)
        print(tree.data())
        tree_pre_order(tree.right(), traversal)
    elif traversal == TraversalType.ROOT_LAST_ORDER:
        tree_pre_order(tree.left(), traversal)
        tree_pre_order(tree.right(), traversal)
        print(tree.data())


def tree_level_order(tree: BinTree):
    queue = LQueue()
    if not tree.is_empty():
        queue.enqueue(tree)
    else:
        raise ValueError("Tree is empty!")
    while not queue.is_empty():
        tree = queue.dequeue()
        if tree.is_empty():
            continue
        print(tree.data())
        if tree.left().is_empty() is False:
            queue.enqueue(tree.left())
        if tree.right().is_empty() is False:
            queue.enqueue(tree.right())


def tree_pre_order_nonrecur(tree: BinTree):
    stack = SStack()
    if not tree.is_empty():
        stack.push(tree)
    while not stack.is_empty():
        sub_tree = stack.pop()
        print(sub_tree.data())
        if not sub_tree.right().is_empty():
            stack.push(sub_tree.right())
        if not sub_tree.left().is_empty():
            stack.push(sub_tree.left())


def tree_middle_order_nonrecur(tree: BinTree):
    stack = SStack()
    while not tree.is_empty() or not stack.is_empty():
        while not tree.is_empty():
            stack.push(tree)
            tree = tree.left()
        tree = stack.pop()
        print(tree.data())
        tree = tree.right()


def tree_last_order_nonrecur(tree: BinTree):
    stack = SStack()
    while not tree.is_empty() or not stack.is_empty():
        while not tree.is_empty():
            stack.push(tree)
            if not tree.right().is_empty():
                stack.push(tree.right())
            tree = tree.left()
        tree = stack.pop()
        print(tree.data())
        if tree == stack.top().right():
            tree = stack.pop()
            print(tree.data())
            tree = stack.pop()


if __name__ == "__main__":
    t1 = BinTNode("D", None, BinTNode("H"))
    t2 = BinTNode("E", None, BinTNode("I"))
    t3 = BinTNode("B", t1, t2)
    t4 = BinTNode("F", BinTNode("J"), BinTNode("K"))
    t5 = BinTNode("C", t4, BinTNode("G"))
    t6 = BinTNode("A", t3, t5)
    print("=======root first=======")
    tree_pre_order(BinTree(t6), TraversalType.ROOT_FIRST_ORDER)
    print("=======root middle======")
    tree_pre_order(BinTree(t6), TraversalType.ROOT_MIDDLE_ORDER)
    print("=======root last========")
    tree_pre_order(BinTree(t6), TraversalType.ROOT_LAST_ORDER)
    print("=======depth first======")
    tree_level_order(BinTree(t6))
    print("=======non recursive root first======")
    tree_pre_order_nonrecur(BinTree(t6))
    print("=======non recursive root middle======")
    tree_middle_order_nonrecur(BinTree(t6))
    print("=======non recursive root last======")
    tree_last_order_nonrecur(BinTree(t6))
