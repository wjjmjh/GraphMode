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
    [sorted_impacts_with_no_duplicates.append(x) for x in impacts if x not in sorted_impacts_with_no_duplicates]
    sorted_vertices = []
    for impact in sorted_impacts_with_no_duplicates:
        sorted_vertices += vertices[impact]
    return sorted_vertices


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
