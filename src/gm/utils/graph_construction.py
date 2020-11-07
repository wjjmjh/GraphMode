import random

from gm.graph import Edge, Graph, Vertex


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
                            parental_vertex,
                            topological_graph.vertices[-1],
                        ),
                        min_cost,
                    )
                )
            else:
                topological_graph.append_edge(
                    Edge(
                        (
                            parental_vertex,
                            topological_graph.vertices[-(ver + 1)],
                        ),
                        random.randint(min_cost + 1, max_cost),
                    )
                )
    return topological_graph


class GraphConstructor:
    def __init__(self, graph=None):
        self.graph = graph

    def graph_from_input_files(self):
        pass

    def dijkstra_input_graph(self):
        pass

    def dp_input_graph(self):
        pass

    def comparison_sorting_input_vertices(self):
        pass
