import random

import numpy

from gm.main_objects.graph import Edge, Graph, Vertex
from gm.utils.io_ import read_graph_from_txt_files


def generate_topological_graph(
    topological_graph,
    number_of_vertices_per_layer,
    graph_depth,
    min_impact,
    max_impact,
    min_cost,
    max_cost,
):
    assert graph_depth >= 1, "the depth of a topological graph at least 1"
    id = 0
    topological_graph.append_vertex(Vertex(id, random.randint(min_impact, max_impact)))
    id += 1
    for dep in range(graph_depth):
        for ver in range(number_of_vertices_per_layer):
            new_vertex = Vertex(id, random.randint(min_impact, max_impact))
            topological_graph.append_vertex(new_vertex)
            id += 1

        for ver in range(number_of_vertices_per_layer):
            parental_vertex = topological_graph.vertices[
                -(number_of_vertices_per_layer + 1)
            ]

            if ver == 0:
                topological_graph.append_edge(
                    Edge(
                        (
                            parental_vertex.index,
                            topological_graph.vertices[-1].index,
                        ),
                        min_cost,
                    )
                )
            else:
                topological_graph.append_edge(
                    Edge(
                        (
                            parental_vertex.index,
                            topological_graph.vertices[-(ver + 1)].index,
                        ),
                        random.randint(min_cost + 1, max_cost),
                    )
                )
    return topological_graph


class GraphConstructor:
    def __init__(self, graph=None):
        self.graph = graph

    def graph_from_input_files(self, vertices_input_txt, edges_input_txt):
        got = read_graph_from_txt_files(vertices_input_txt, edges_input_txt)
        self.graph = got
        return got

    def dijkstra_input_vertices_and_distance_matrix(self):
        if self.graph is None:
            raise ValueError(
                "Please properly construct Graph object, the current graph is None."
            )
        vertices = numpy.array([v.index for v in self.graph.vertices]).astype(
            numpy.int64
        )
        dm = numpy.array(self.graph.compute_distance_matrix()).astype(numpy.int64)
        return vertices, dm

    def dp_input_edges(self):
        if self.graph is None:
            raise ValueError(
                "Please properly construct Graph object, the current graph is None."
            )
        return [edge.to_tuple() for edge in self.graph.edges]

    def comparison_sorting_input_vertices(self):
        if self.graph is None:
            raise ValueError(
                "Please properly construct Graph object, the current graph is None."
            )
        return self.graph.vertices
