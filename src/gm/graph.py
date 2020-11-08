from gm.utils.io_ import write_txt


class Vertex:
    """
    An object having an ID and a weight to define a vertex in a graph.
    """

    def __init__(self, index, impact):
        self.index = index
        self.impact = impact

    def to_str(self):
        return "{index} {impact}".format(index=self.index, impact=self.impact)


class Edge:
    """
    An object having two vertices as the ends and a weight to define an edge in a graph.
    """

    def __init__(self, vertices, cost):
        """
        :param vertices: a tuple that has two vertices connected by this edge. e.g. (vertex A, vertex B)
        :param cost: the cost of going from vertex A to vertex B on this edge.
        """
        self.vertices = vertices
        self.cost = cost

    def to_str(self):
        return "{v1} {v2} {cost}".format(
            v1=self.vertices[0].to_str().split(" ")[0],
            v2=self.vertices[1].to_str().split(" ")[0],
            cost=self.cost,
        )

    def to_tuple(self):
        return (self.vertices[0].index, self.vertices[1].index, self.cost)


class Graph:
    """
    An object having an array of vertices and an array of edges to define the graph. Graph
    object also contains basic methods.

    potential methods to be implemented:
    func compute_distance_matrix: returns a distance matrix based on existing vertices and edges on the
    graph.
    """

    def __init__(self):
        self._vertices = []
        self._edges = []

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, new_vertices):
        self._vertices = new_vertices

    @property
    def len_vertices(self):
        return len(self._vertices)

    @property
    def len_edges(self):
        return len(self._edges)

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, new_edges):
        self._edges = new_edges

    def append_vertex(self, v):
        self._vertices.append(v)

    def append_edge(self, e):
        self._edges.append(e)

    def compute_distance_matrix(self):
        raise NotImplementedError

    def to_txt(self):
        vertices = [v.to_str() for v in self._vertices]
        edges = [e.to_str() for e in self._edges]
        write_txt(vertices, "vertices")
        write_txt(edges, "edges")
