from gm.utils.io_ import write_txt


class Vertex:
    """
    An object having an ID (index) and a weight (impact) to define a vertex in a graph.
    """

    def __init__(self, index, impact):
        self._index = int(index)
        self._impact = int(impact)

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, new_index):
        self._index = new_index

    @property
    def impact(self):
        return self._impact

    @impact.setter
    def impact(self, new_impact):
        self._impact = new_impact

    def to_str(self):
        return "{index} {impact}".format(
            index=str(self._index), impact=str(self._impact)
        )


class Edge:
    """
    An object having two vertices as the ends and a cost to define an edge in a graph.
    """

    def __init__(self, vertices, cost):
        """
        :param vertices: a tuple that has two vertices connected by this edge. e.g. (vertex A, vertex B)
        :param cost: the cost of going from vertex A to vertex B on this edge.
        """
        self._vertices = (int(vertices[0]), int(vertices[1]))
        self._cost = int(cost)

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, new_vertices):
        self._vertices = new_vertices

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, new_cost):
        self._cost = new_cost

    def to_str(self):
        return "{v1} {v2} {cost}".format(
            v1=str(self._vertices[0]),
            v2=str(self._vertices[1]),
            cost=str(self._cost),
        )

    def to_tuple(self):
        return (self._vertices[0], self._vertices[1], self._cost)


class Graph:
    """
    An object having an array of vertices and an array of edges to define the graph.
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
        m = [[0 for _ in range(self.len_vertices)] for _ in range(self.len_vertices)]
        for edge in self._edges:
            m[edge.vertices[0]][edge.vertices[1]] = edge.cost
        return m

    def to_txt(self):
        vertices = [v.to_str() for v in self._vertices]
        edges = [e.to_str() for e in self._edges]
        write_txt(vertices, "vertices")
        write_txt(edges, "edges")

    def to_combined_txt(self, fn):
        vertices = [v.to_str() for v in self._vertices]
        edges = [e.to_str() for e in self._edges]
        lines = vertices + edges
        write_txt(lines, fn)
