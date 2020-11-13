import os
import time

import numpy

from gm.utils.graph_construction import GraphConstructor
from gm.utils.io_ import read_vertices_from_txt_files

from . import Dijkstra, comparison_based_sorting, dynamic_programming
from . import hello_world as hw


def hello_world():
    hw.hello_world()


def Dijkstra_to_find_shortest_distances(src_vertex, vertices, graph):
    return Dijkstra.Dijkstra_to_find_shortest_distances(src_vertex, vertices, graph)


def dynamic_programming_to_find_the_shortest_path(
    from_vertex, to_vertex, path, n, dist, foot_print
):
    return dynamic_programming.dynamic_programming_to_find_the_shortest_path(
        from_vertex, to_vertex, path, n, dist, foot_print
    )


def compute_influence_of_a_vertex(before_removal, after_removal):
    return Dijkstra.influence_of_a_vertex(before_removal, after_removal)


def sort_impacts_based_on_comparison(impacts):
    comparison_based_sorting.sort_impacts_based_on_comparison(impacts)


def sort_vertices_based_on_comparison(vertices, impacts):
    sort_impacts_based_on_comparison(impacts)
    sorted_impacts_with_no_duplicates = []
    [
        sorted_impacts_with_no_duplicates.append(x)
        for x in impacts
        if x not in sorted_impacts_with_no_duplicates
    ]
    sorted_vertices = []
    for impact in sorted_impacts_with_no_duplicates:
        sorted_vertices += vertices[impact]
    return sorted_vertices


def functionality_1(path_to_txt):
    """minimum spanning tree + Dijkstra algorithm"""
    print("you are invoking minimum spanning tree + Dijkstra algorithm")
    gc = GraphConstructor()
    gc.graph_from_combined_file(path_to_txt)
    vertices, dm = gc.dijkstra_input_vertices_and_distance_matrix()
    source_vertex = 0
    start_time = time.process_time()
    got = Dijkstra_to_find_shortest_distances(source_vertex, vertices, dm)
    print("the result of minimum spanning tree + Dijkstra algorithm is:")
    print("[{}]".format(", ".join([str(val) for val in got])))
    print("the execution takes time: {}".format(str(time.process_time() - start_time)))


def functionality_2(path_to_txt):
    """Comparison-based algorithm: Insertion Sort"""
    print("Comparison-based algorithm: Insertion Sort")
    got = read_vertices_from_txt_files(path_to_txt)
    impacts = numpy.array([v.impact for v in got]).astype(numpy.int64)
    vertices = dict()
    for vertex in got:
        if vertex.impact not in vertices.keys():
            vertices[vertex.impact] = [vertex]
        else:
            vertices[vertex.impact].append(vertex)
    start_time = time.process_time()
    sorted_vertices = sort_vertices_based_on_comparison(vertices, impacts)
    print(
        "the result of Comparison-based algorithm: Insertion Sort is (sorted vertices):"
    )
    print(
        [
            "{vertex}: has impact {impact}".format(
                vertex=str(v.index), impact=str(v.impact)
            )
            for v in sorted_vertices
        ]
    )
    print("the execution takes time: {}".format(str(time.process_time() - start_time)))


def functionality_3(path_to_txt):
    """Floyd-Warshall Dynamic Programming"""
    print("Floyd-Warshall Dynamic Programming")
    gc = GraphConstructor()
    gc.graph_from_combined_file(path_to_txt)
    n = len(gc.graph.vertices)
    dist = numpy.array([[float("inf")] * n for _ in range(n)]).astype(numpy.double)
    foot_print = numpy.array([[-1] * n for _ in range(n)]).astype(numpy.int64)
    edges = gc.dp_input_edges()
    edges += [(v, v, 0.00001) for v in range(n)]
    for first, second, weight in edges:
        dist[first][second] = weight
        foot_print[first][second] = second
    path = numpy.array([-1 for _ in range(n)]).astype(numpy.int64)
    start_time = time.process_time()
    got = [
        val
        for val in dynamic_programming_to_find_the_shortest_path(
            0,
            n - 1,
            path,
            n,
            dist,
            foot_print,
        )
        if val != -1
    ]
    print(
        "the result of Floyd-Warshall Dynamic Programming is (computed shortest path):"
    )
    print(got)
    print("the execution takes time: {}".format(str(time.process_time() - start_time)))


def test(path_to_txt):
    functionality_number = path_to_txt.split(os.sep)[-1].split(".")[0].split("-")[1]
    switch_dict = {"f1": functionality_1, "f2": functionality_2, "f3": functionality_3}
    try:
        f = switch_dict[functionality_number]
    except KeyError:
        print("Unrecognised path!")
    f(path_to_txt)


_funcs = [
    "hello_world()",
    "sort_vertices_based_on_comparison",
    "Dijkstra_to_find_shortest_distances(src_vertex, vertices, graph)",
    "dynamic_programming_to_find_the_shortest_path(from_vertex, to_vertex, path, n, dist, foot_print)",
    "compute_influence_of_a_vertex(before_removal, after_removal)",
    "sort_vertices_based_on_comparison(vertices)",
]


def show_funcs():
    for func in _funcs:
        print(func)
