import sys

import numpy

include "../include/numerical_pyrex.pyx"


def Dijkstra_to_find_shortest_distances(int src_vertex, Long1D vertices, Long2D graph):
    """
    Description:
    A function that invokes the Heap object as the data structure to perform the
    Dijkstra Algorithm to find the shortest distances from a specified source vertex to other
    vertices on a given graph;

    Input parameters:
    graph: a Graph object that contains essential data and methods;
    src_vertex: an integer ID of a specified source vertex that would be used to calculate
    shortest paths from other vertices to this vertex.•

    Return:
    A dictionary that has "destination_vertex" as its keys and "shortest_distance_from_source"
    as its values.
    """
    cdef int minimum_distance_index
    cdef long minimum_distance, d1, d2, d
    cdef Long1D shortest_distances, shortest_path_tree

    shortest_distances = numpy.array([sys.maxsize for v in vertices]).astype(numpy.int64)
    shortest_path_tree = numpy.array([0 for v in vertices]).astype(numpy.int64)
    shortest_distances[src_vertex] = 0

    for _ in vertices:
        minimum_distance = sys.maxsize
        for v in vertices:
            if shortest_distances[v] < minimum_distance and shortest_path_tree[v] == 0:
                minimum_distance = shortest_distances[v]
        minimum_distance_index = -1
        for i, dist in enumerate(shortest_distances):
            if dist == minimum_distance:
                minimum_distance_index = i
                break
        shortest_path_tree[minimum_distance_index] = 1
        for v in vertices:
            d1 = graph[minimum_distance_index][v]
            d2 = shortest_distances[minimum_distance_index]
            d = d1 + d2
            if d1 > 0 and shortest_distances[v] > d and shortest_path_tree[v] == 0:
                shortest_distances[v] = d
    return shortest_distances


def influence_of_a_vertex(Long2D before_removal, Long2D after_removal):
    """
    Description:
    A function that invokes function Dijkstra_to_find_shortest_distances to
    compute the influence of a vertex to the graph by finding the average of the distances of shortest paths of the graph
    before and after the removal of the vertex.

    Input parameters:
    graph: a Graph object that contains essential data and methods;
    vertex: an Integer ID of a specified vertex as the interested;

    Return: a number that represents the influence of the input vertex.
    """
    cdef float val_before_removal, val_after_removal

    val_before_removal = 0.0
    val_after_removal = 0.0

    for v in before_removal:
        for dist in v:
            val_before_removal += dist
    val_before_removal /= len(before_removal)

    for v in after_removal:
        for dist in v:
            val_after_removal += dist
    val_after_removal /= len(after_removal)

    return val_before_removal - val_after_removal
