from . import Dijkstra, comparison_based_sorting, dynamic_programming
from . import hello_world as hw


def hello_world():
    hw.hello_world()


def sort_vertices_based_on_comparison():
    comparison_based_sorting.sort_vertices_based_on_comparison()


def Dijkstra_to_find_shortest_distances(src_vertex, vertices, graph):
    return Dijkstra.Dijkstra_to_find_shortest_distances(src_vertex, vertices, graph)


def dynamic_programming_to_find_the_shortest_path():
    dynamic_programming.dynamic_programming_to_find_the_shortest_path()


def compute_influence_of_a_vertex(before_removal, after_removal):
    return Dijkstra.influence_of_a_vertex(before_removal, after_removal)


_funcs = [
    "hello_world",
    "sort_vertices_based_on_comparison",
    "Dijkstra_to_find_shortest_distances",
    "dynamic_programming_to_find_the_shortest_path",
    "compute_influence_of_a_vertex",
]


def show_funcs():
    for func in _funcs:
        print(func)
