import sys

import numpy

from gm.main import Dijkstra_to_find_shortest_paths
from gm.utils.tester import TestCase


class DijkstraAlgorithmsTests(TestCase):
    def test_basic(self):
        src_vertex = 0
        vertices = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8]).astype(numpy.int64)
        graph = numpy.array(
            [
                [0, 4, 0, 0, 0, 0, 0, 8, 0],
                [4, 0, 8, 0, 0, 0, 0, 11, 0],
                [0, 8, 0, 7, 0, 4, 0, 0, 2],
                [0, 0, 7, 0, 9, 14, 0, 0, 0],
                [0, 0, 0, 9, 0, 10, 0, 0, 0],
                [0, 0, 4, 14, 10, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 6],
                [8, 11, 0, 0, 0, 0, 1, 0, 7],
                [0, 0, 2, 0, 0, 0, 6, 7, 0],
            ]
        ).astype(numpy.int64)
        got = Dijkstra_to_find_shortest_paths(src_vertex, vertices, graph)
