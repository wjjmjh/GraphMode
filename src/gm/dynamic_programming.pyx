import sys

import numpy

include "../include/numerical_pyrex.pyx"


def dynamic_programming_to_find_the_shortest_path(
    int from_vertex, int to_vertex, Long1D path, int n, Double2D dist, Long2D foot_print
):
    """
    Description:
    A function that takes a generated distance matrix from a Graph object, and applies the
    Floyd-Warshall Algorithm and dynamic programming to find the shortest path.

    Input parameters:
    dist_matrix: A dictionary that represents a distance matrix;
    src_vertex: an Integer ID of a specified vertex as the source;
    dest_vertex: an Integer ID of a specified vertex as the destination;

    Return:
    an array of vertices that represents the shortest path between the source vertex and the
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
