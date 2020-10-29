# Under construction


def Dijkstra_to_find_shortest_distances(src_vertex, vertices, graph):
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
    shortest_distances = [float("inf") for v in vertices]
    shortest_path_tree = [False for v in vertices]
    shortest_distances[src_vertex] = 0

    for _ in vertices:
        minimum_distance = float("inf")
        for v in vertices:
            if shortest_distances[v] < minimum_distance and not shortest_path_tree[v]:
                minimum_distance = shortest_distances[v]
        minimum_distance_index = shortest_distances.index(minimum_distance)
        shortest_path_tree[minimum_distance_index] = True
        for v in vertices:
            d1 = graph[minimum_distance_index][v]
            d2 = shortest_distances[minimum_distance_index]
            d = d1 + d2
            if d1 > 0 and shortest_distances[v] > d and not shortest_path_tree[v]:
                shortest_distances[v] = d
    return shortest_distances


def influence_of_a_vertex():
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
    print("func influence_of_a_vertex is under construction.")
