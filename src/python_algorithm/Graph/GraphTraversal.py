from python_algorithm.Graph.GraphAL import GraphAL
from python_algorithm.StackAndQueue.StackAndQueue import LStack, LQueue
from typing import Set, Any


def traversal_graph(graph: GraphAL):
    seq = []
    visited = set()
    init_node = graph.vertices()[0]

    def traversal_graph_util(node: Any, visited_in: Set[Any], seq):
        visited_in.add(node)
        seq.append(node)

        neighbors = [neighbor.split(" <-> ")[1] for neighbor in graph.out_edge(node)]
        for neighbor in sorted(neighbors):
            if neighbor not in visited_in:
                traversal_graph_util(neighbor, visited_in, seq)

    traversal_graph_util(init_node, visited, seq)
    print(seq)


def DFS_traversal_graph(graph: GraphAL):
    visited = set()

    stack = LStack()
    init_node = graph.vertices()[0]
    stack.push(init_node)

    while not stack.is_empty():
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            yield node
        else:
            continue
        neighbors = sorted([neighbor.split(" <-> ")[1] for neighbor in graph.out_edge(node)])[::-1]
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.push(neighbor)


def BSF_traversal_graph(graph: GraphAL):
    queue = LQueue()
    visited = set()

    init_node = graph.vertices()[0]
    visited.add(init_node)
    yield init_node

    queue.append(init_node)
    while not queue.is_empty():
        node = queue.pop()
        neighbors = [neighbor.split(" <-> ")[1] for neighbor in graph.out_edge(node)]
        for neighbor in sorted(neighbors):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                yield neighbor


if __name__ == "__main__":
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    G = GraphAL()
    for i in nodes:
        G.add_vertex(i)
    G.add_edge('a', 'b')
    G.add_edge('a', 'd')
    G.add_edge('a', 'c')
    G.add_edge('b', 'd')
    G.add_edge('b', 'g')
    G.add_edge('b', 'e')
    G.add_edge('c', 'd')
    G.add_edge('c', 'f')
    G.add_edge('d', 'g')
    G.add_edge('e', 'g')
    G.add_edge('f', 'g')
    traversal_graph(G)
    print("===========DFS-non-recursive==========")
    for i in DFS_traversal_graph(G):
        print(f"current node : {i}")
    print("===========BFS-non-recursive==========")
    for i in BSF_traversal_graph(G):
        print(i)
