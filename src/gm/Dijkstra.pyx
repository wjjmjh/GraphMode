import sys

import numpy

include "../include/numerical_pyrex.pyx"


def Dijkstra_to_find_shortest_distances(int src_vertex, Long1D vertices, Long2D graph):
    """
    Description:
    A function that uses minimum spanning tree to perform the Dijkstra Algorithm
    to find the shortest distances from a specified source vertex to other
    vertices on a given graph;

    Minimum spanning tree + Dijkstra algorithm has been implemented here,
    1, Dijkstra algorithm is optimal and it finds all shortest distances from a vertex to all the other vertices;
    2, Dijkstra algorithm does not investigate all edges, in the implementation of the algorithm,
    a minimum spanning tree is generated and the root of tree is the source vertex. It maintains two sets when performing the
    algorithm, one set has all the vertices included in the minimum spanning tree and the other set has all the vertices
    not included in the minimum spanning tree;
    3, The efficiency of the algorithm is sound, after the analysis (both theoretical analysis and empirical analysis),
    the implementation of minimum spanning tree + Dijkstra algorithm below has the time complexity O(n^2);
    4, Since the return of this function is very informative: An array of numbers showing the shortest distances
    between any two reachable vertices of the graph, we can then compute the influence of a vertex to the graph by finding
    the average of the distances of shortest paths of the graph before and after the removal of a vertex
    (actual implementation please see function below: influence_of_a_vertex).

    Input parameters:
    src_vertex: an integer index of a specified source vertex that would be used to calculate
    shortest distances from this vertex to other vertices;
    vertices: an array of indices of vertices;
    graph: a two dimensional distance matrix computed by the Graph constructor that suits Dijkstra algorithm.

    Return:
    An array of distances, each distance's index in the array maps to the vertex which has the index.
    for example:
    if src_vertex is 0 and [0, 1] returned, this means:
    the shortest distance from vertex 0 to vertex 0 is 0;
    the shortest distance from vertex 0 to vertex 1 is 1.
    """
    cdef int minimum_distance_index
    cdef long minimum_distance, d1, d2, d
    cdef Long1D shortest_distances, shortest_path_tree

    shortest_distances = numpy.array([sys.maxsize for v in vertices]).astype(numpy.int64)
    shortest_path_tree = numpy.array([0 for v in vertices]).astype(numpy.int64)
    shortest_distances[src_vertex] = 0

    for _ in vertices:
        minimum_distance = sys.maxsize
        for i, v in enumerate(vertices):
            if shortest_distances[v] < minimum_distance and shortest_path_tree[v] == 0:
                minimum_distance = shortest_distances[v]
                minimum_distance_index = i
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
    A function that computes the influence of a vertex to the graph by finding the average of the distances
    of shortest paths of the graph before and after the removal of a vertex.

    Input parameters:
    before_removal: returned from func Dijkstra_to_find_shortest_distances, an array of shortest distances before the removal;
    after_removal: returned from func Dijkstra_to_find_shortest_distances, an array of shortest distances after the removal;

    Return: a number that represents the influence of the removed vertex.
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
