import sys

import numpy

include "../include/numerical_pyrex.pyx"


def dynamic_programming_to_find_the_shortest_path(
    int from_vertex, int to_vertex, Long1D path, int n, Double2D dist, Long2D foot_print
):
    """
    Description:
    A function that performs Floyd-Warshall Algorithm and dynamic programming to find the shortest path
    from one vertex to another.

    Floyd-Warshall + dynamic programming algorithms have been implemented here:
    1, Floyd-Warshall algorithm can find shortest distances between any pair of vertices of
    either a positive-weighted graph or a negative-weighted graph;
    2, The implementation of algorithm is succinct; with the help of dynamic programming approaches,
    the lines of codes can be efficiently reduced, and the process can be refined by referring to previously
    calculated values;
    3, Given the context that this functionality will be used to help two researchers connect with each other
    in a graph, but those two researchers usually come from two different clusters or sub-graphs. Floyd-Warshall
    algorithm can help find the shortest path in such situation, a distributed system, or graph of graphs;
    4, The purpose of this functionality is to compute an array of vertices to show the shortest path from one vertex to another,
    so we need consider the complexity of path re-construction factor. Fortunately, the implementation of path re-construction
    is fairly easy along with the construction of Floyd-Warshall algorithm that we pass an initialised array as an input
    parameter to store "foot prints" while the algorithm execution. Then, it's straight-forward to extract the shortest path
    from this array.

    Input parameters:
    from_vertex: the vertex from which the shortest path starts: source vertex;
    to_vertex: the vertex at which the shortest path ends: destination vertex;
    path: an initialised array to store the shortest path;
    n: the number of vertices in the graph + 1;
    dist: distance matrix;
    foot_print: an initialised array that keeps track of "foot prints" while algorithm execution,
    and used for shortest path reconstruction.

    Return:
    an array of vertex indices that represents the shortest path between the source vertex and the
    destination vertex.
    """
    cdef int k, i, j, next_append_index

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] >= dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    if dist[i][j] < float("inf"):
                        foot_print[i][j] = foot_print[i][k]
    if foot_print[from_vertex][to_vertex] == -1:
        return []
    next_append_index = 0
    path[next_append_index] = from_vertex
    next_append_index += 1
    while from_vertex != to_vertex:
        from_vertex = foot_print[from_vertex][to_vertex]
        path[next_append_index] = from_vertex
        next_append_index += 1
    return path
