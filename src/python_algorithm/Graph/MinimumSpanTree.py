from python_algorithm.Graph.GraphAL import GraphAL
from collections import namedtuple

edge_tuple = namedtuple('edge_tuple', ['start_edge', 'end_edge', 'weight'])


def kruskal(graph: GraphAL):
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
            if edge[0] > edge[1]:
                edge[0], edge[1] = edge[1], edge[0]
            et = edge_tuple(edge[0], edge[1], int(edge[2]))
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
