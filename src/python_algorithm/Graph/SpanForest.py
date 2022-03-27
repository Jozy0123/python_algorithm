from typing import Dict, Any
from python_algorithm.Graph.GraphAL import GraphAL
from python_algorithm.StackAndQueue.StackAndQueue import LStack, LQueue


def DSF_span_forest(graph: GraphAL) -> Dict[Any, Any]:
    nodes = graph.vertices()
    span_forest = {}

    def dfs(graph_in, v):
        nonlocal span_forest
        for neighbor in sorted(graph_in.out_edge(v)):
            node = neighbor.split(' <-> ')[1]
            if span_forest.get(node, None) is None:
                span_forest[node] = v
                dfs(graph_in, node)
            else:
                continue

    for i in nodes:
        if span_forest.get(i) is None:
            span_forest[i] = 0
            dfs(graph, i)

    return span_forest


def DFS_span_forest_non_recursive(graph: GraphAL) -> Dict[str, Any]:
    nodes = graph.vertices()
    span_forest = {}

    def non_recursive_dfs(graph_in: GraphAL, node):
        nonlocal span_forest

        stack = LStack()
        stack.push(node)
        last_traverse = node

        while not stack.is_empty():
            top_node = stack.pop()
            if span_forest.get(top_node, None) is not None and span_forest.get(top_node, None) != '0':
                continue
            if span_forest.get(top_node, None) is None:
                span_forest[top_node] = last_traverse
                last_traverse = top_node
            neighbors = sorted([neighbor.split(" <-> ")[1] for neighbor in graph_in.out_edge(top_node)])[::-1]
            for neighbor in neighbors:
                if span_forest.get(neighbor, None) is None:
                    stack.push(neighbor)

    for i in nodes:
        if span_forest.get(str(i)) is None:
            span_forest[str(i)] = '0'
            non_recursive_dfs(graph, i)

    return span_forest


def BFS_span_forest_non_recursive(graph: GraphAL) -> Dict[Any, Any]:

    nodes = graph.vertices()
    span_forest = {}

    def bfs(graph_in: GraphAL, node):
        nonlocal span_forest
        queue = LQueue()
        queue.append(node)
        while not queue.is_empty():
            top_node = queue.pop()
            neighbors = sorted([neighbor.split(" <-> ")[1] for neighbor in graph_in.out_edge(top_node)])
            for neighbor in neighbors:
                if span_forest.get(neighbor, None) is None:
                    queue.append(neighbor)
                    span_forest[neighbor] = top_node

    span_forest['b'] = '0'
    bfs(graph, 'b')

    return span_forest


if __name__ == '__main__':
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
    print(DSF_span_forest(G))
    print("=======non-recursive-DFS-tree============")
    print(DFS_span_forest_non_recursive(G))
    print("=======non-recursive-BFS-tree============")
    print(BFS_span_forest_non_recursive(G))
