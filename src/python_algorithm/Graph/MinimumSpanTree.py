from python_algorithm.Graph.GraphAL import GraphAL
from collections import namedtuple
from typing import Tuple, List, Dict
from python_algorithm.Tree.PriorityQueue import PriorityQueueHeap


class EdgeTuple(namedtuple('EdgeTuple', ['start_edge', 'end_edge', 'weight'])):
    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __hash__(self):
        return hash(self.start_edge + self.end_edge)


def kruskal(graph: GraphAL) -> List[Tuple[str, str, int]]:
    if graph.is_directed:
        split_sign = ' -> '
    else:
        split_sign = ' <-> '
    vnum = graph.vertex_num()
    reps = graph.nodes_rep
    mst, edges = [], set()

    for vi in graph.vertices():
        for edge in graph.out_edge(vi):
            edge = edge.split(split_sign)
            if edge[0] > edge[1] and not graph.is_directed:
                edge[0], edge[1] = edge[1], edge[0]
            et = EdgeTuple(edge[0], edge[1], int(edge[2]))
            edges.add(et)

    edges = list(edges)
    edges.sort(key=lambda x: x.weight)

    for individual_edge in edges:
        if reps[individual_edge.start_edge] != reps[individual_edge.end_edge]:
            mst.append((individual_edge.start_edge, individual_edge.end_edge, individual_edge.weight))
            if len(mst) == vnum - 1:
                break
            rep, orep = reps[individual_edge.start_edge], reps[individual_edge.end_edge]
            for i in graph.vertices():
                if reps[i] == orep:
                    reps[i] = rep
    return mst


def prim(graph: GraphAL) -> Dict[str, EdgeTuple]:
    if graph.is_directed:
        split_sign = ' -> '
    else:
        split_sign = ' <-> '
    vnum = graph.vertex_num()
    reps = graph.nodes_rep
    mst = {}

    edges_set = set()

    start_node = list(reps.keys())[0]
    candidates = PriorityQueueHeap([EdgeTuple(start_node, start_node, 0)])

    while len(edges_set) < vnum and not candidates.is_empty():
        edge_tuple = candidates.dequeue()
        if mst.get(edge_tuple.end_node, None) is not None:
            continue
        mst[edge_tuple.end_node] = EdgeTuple(edge_tuple.start_node, edge_tuple.end_node, -1 * edge_tuple.weight)
        edges_set.add(edge_tuple.end_node)
        for edge_ in graph.out_edge(edge_tuple.end_node):

            edge = edge_.split(split_sign)
            end_node = edge_.split(split_sign)[1]
            et = EdgeTuple(edge[0], edge[1], int(edge[2])*(-1))
            if mst.get(end_node, None) is None:
                candidates.enqueue(et)

    return mst


if __name__ == "__main__":
    graph = GraphAL()
    for i in "abcdefg":
        graph.add_vertex(i)
    graph.add_edge("a", "b", 5)
    graph.add_edge("a", "c", 11)
    graph.add_edge("a", "d", 5)
    graph.add_edge("b", "d", 3)
    graph.add_edge("b", "g", 7)
    graph.add_edge("b", "e", 9)
    graph.add_edge("c", "d", 7)
    graph.add_edge("c", "f", 6)
    graph.add_edge("d", "g", 20)
    graph.add_edge("e", "g", 8)
    graph.add_edge("f", "g", 8)
    print(kruskal(graph))
    print(prim(graph))
