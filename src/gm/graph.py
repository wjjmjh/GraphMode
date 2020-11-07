class vertex:
    """
    An object having an ID and a weight to define a vertex in a graph.
    """

    def __init__(self, index, name, impact):
        self.index = index
        self.name = name
        self.impact = impact


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
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, new_edges):
        self._edges = new_edges

    def compute_distance_matrix(self):
        raise NotImplementedError
