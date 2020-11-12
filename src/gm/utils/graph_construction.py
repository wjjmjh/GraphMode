import random

import numpy

from gm.main_objects.graph import Edge, Graph, Vertex
from gm.utils.io_ import (read_graph_from_combined_txt_files,
                          read_graph_from_txt_files)


def generate_vertices_with_impacts(number_of_vertices, min_impact, max_impact):
    """
    A helper function that generates vertices data for testing.
    :param number_of_vertices: the number of vertices that will be generated.
    :param min_impact: minimum impact for a vertex.
    :param max_impact: maximum impact for a vertex.
    :return: an array of Vertex objects.
    """
    return [
        Vertex(i, random.randint(min_impact, max_impact))
        for i in range(number_of_vertices)
    ]


def generate_topological_graph(
    topological_graph,
    number_of_vertices_per_layer,
    graph_depth,
    min_impact,
    max_impact,
    min_cost,
    max_cost,
):
    """
    A helper function that generates a graph (vertices data and edges data) for testing.
    :param topological_graph: A Graph object, could be simply initialised as: Graph().
    :param number_of_vertices_per_layer: the number of vertices for each layer or level of the topological graph.
    :param graph_depth: how many layers or levels in the topological graph.
    :param min_impact: minimum impact for each vertex that will be generated.
    :param max_impact: maximum impact for each vertex that will be generated.
    :param min_cost: minimum cost for each edge that will be generated.
    :param max_cost: maximum cost for each edge that will be generated.
    :return: the Graph object with desired vertices and edges appended.
    """
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
    """
    A constructor that interfaces with Graph objects to construct graphs
    or generates required input parameters for the algorithms.
    """

    def __init__(self, graph=None):
        self.graph = graph

    def graph_from_input_files(self, vertices_input_txt, edges_input_txt):
        """
        construct a graph from text files.
        :param vertices_input_txt: the path to a text file that contains vertex data.
        :param edges_input_txt: the path to a text file that contains edge data.
        :return: a constructed Graph object.
        """
        got = read_graph_from_txt_files(vertices_input_txt, edges_input_txt)
        self.graph = got
        return got

    def graph_from_combined_file(self, combined_txt):
        """
        construct a graph from one single txt file.
        :param combined_txt: a txt file has both vertex data and edge data
        if the row has two columns, it's supposed to e vertex data that first column is the index and second column is impact
        if the row has three columns, it's supposed to be a edge data that the first two columns are indices of two connected
        vertices and the third column is the associated cost.
        :return: a constructed Graph object.
        """
        got = read_graph_from_combined_txt_files(combined_txt)
        self.graph = got
        return got

    # generates input parameters for Dijkstra algorithm.
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

    # generates input parameters for dynamic programming algorithm.
    def dp_input_edges(self):
        if self.graph is None:
            raise ValueError(
                "Please properly construct Graph object, the current graph is None."
            )
        return [edge.to_tuple() for edge in self.graph.edges]

    # generate input parameters for comparison-based sorting algorithm.
    def comparison_sorting_input_vertices(self):
        if self.graph is None:
            raise ValueError(
                "Please properly construct Graph object, the current graph is None."
            )
        return self.graph.vertices
