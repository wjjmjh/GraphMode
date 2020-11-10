import os
import sys

import numpy

from gm.main import (Dijkstra_to_find_shortest_distances,
                     compute_influence_of_a_vertex)
from gm.utils.graph_construction import GraphConstructor
from gm.utils.repo_path import repoPathManager
from gm.utils.tester import TestCase


class DijkstraAlgorithmsTests(TestCase):
    def setUp(self) -> None:
        self.test_data = repoPathManager().test_data
        self.offset = 800
        self.gc = GraphConstructor()

    def test_case1(self):
        self.gc.graph_from_input_files(
            os.path.join(self.test_data, "vertices_testcase1.txt"),
            os.path.join(self.test_data, "edges_testcase1.txt"),
        )
        vertices, dm = self.gc.dijkstra_input_vertices_and_distance_matrix()
        src_vertex = 0
        got = Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        self.assertEqual(got[-1], 1 * self.offset)

    def test_case2(self):
        self.gc.graph_from_input_files(
            os.path.join(self.test_data, "vertices_testcase2.txt"),
            os.path.join(self.test_data, "edges_testcase2.txt"),
        )
        vertices, dm = self.gc.dijkstra_input_vertices_and_distance_matrix()
        src_vertex = 0
        got = Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        self.assertEqual(got[-1], 2 * self.offset)

    def test_case3(self):
        self.gc.graph_from_input_files(
            os.path.join(self.test_data, "vertices_testcase3.txt"),
            os.path.join(self.test_data, "edges_testcase3.txt"),
        )
        vertices, dm = self.gc.dijkstra_input_vertices_and_distance_matrix()
        src_vertex = 0
        got = Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        self.assertEqual(got[-1], 3 * self.offset)

    def test_case4(self):
        self.gc.graph_from_input_files(
            os.path.join(self.test_data, "vertices_testcase4.txt"),
            os.path.join(self.test_data, "edges_testcase4.txt"),
        )
        vertices, dm = self.gc.dijkstra_input_vertices_and_distance_matrix()
        src_vertex = 0
        got = Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        self.assertEqual(got[-1], 4 * self.offset)

    def test_case5(self):
        self.gc.graph_from_input_files(
            os.path.join(self.test_data, "vertices_testcase5.txt"),
            os.path.join(self.test_data, "edges_testcase5.txt"),
        )
        vertices, dm = self.gc.dijkstra_input_vertices_and_distance_matrix()
        src_vertex = 0
        got = Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        self.assertEqual(got[-1], 5 * self.offset)
