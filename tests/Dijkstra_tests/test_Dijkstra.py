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
        self.test_data = repoPathManager().Dijkstra_test_data
        self.offset = 800
        self.gc = GraphConstructor()

    def test_case1(self):
        # invoke graph constructor to construct a graph based on input text files.
        self.gc.graph_from_input_files(
            os.path.join(self.test_data, "vertices_testcase1.txt"),
            os.path.join(self.test_data, "edges_testcase1.txt"),
        )
        # ask graph constructor to generate desired input parameters for func Dijkstra_to_find_shortest_distances.
        vertices, dm = self.gc.dijkstra_input_vertices_and_distance_matrix()
        src_vertex = 0
        # call func Dijkstra_to_find_shortest_distances to get the shortest distances.
        got = Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        # as the test data sets preset the cost for every edge from source vertex to destination vertex is 1
        # and all the other edges have a cost higher than 1, then, the total cost from vertex 0 to vertex n
        # is supposed to be 1 * n = n
        # for this test, n = 1 * self.offset
        self.assertEqual(got[-1], 1 * self.offset)

    def test_case2(self):
        # invoke graph constructor to construct a graph based on input text files.
        self.gc.graph_from_input_files(
            os.path.join(self.test_data, "vertices_testcase2.txt"),
            os.path.join(self.test_data, "edges_testcase2.txt"),
        )
        # ask graph constructor to generate desired input parameters for func Dijkstra_to_find_shortest_distances.
        vertices, dm = self.gc.dijkstra_input_vertices_and_distance_matrix()
        src_vertex = 0
        # call func Dijkstra_to_find_shortest_distances to get the shortest distances.
        got = Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        # as the test data sets preset the cost for every edge from source vertex to destination vertex is 1
        # and all the other edges have a cost higher than 1, then, the total cost from vertex 0 to vertex n
        # is supposed to be 1 * n = n
        # for this test, n = 2 * self.offset
        self.assertEqual(got[-1], 2 * self.offset)

    def test_case3(self):
        # invoke graph constructor to construct a graph based on input text files.
        self.gc.graph_from_input_files(
            os.path.join(self.test_data, "vertices_testcase3.txt"),
            os.path.join(self.test_data, "edges_testcase3.txt"),
        )
        # ask graph constructor to generate desired input parameters for func Dijkstra_to_find_shortest_distances.
        vertices, dm = self.gc.dijkstra_input_vertices_and_distance_matrix()
        src_vertex = 0
        # call func Dijkstra_to_find_shortest_distances to get the shortest distances.
        got = Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        # as the test data sets preset the cost for every edge from source vertex to destination vertex is 1
        # and all the other edges have a cost higher than 1, then, the total cost from vertex 0 to vertex n
        # is supposed to be 1 * n = n
        # for this test, n = 3 * self.offset
        self.assertEqual(got[-1], 3 * self.offset)

    def test_case4(self):
        # invoke graph constructor to construct a graph based on input text files.
        self.gc.graph_from_input_files(
            os.path.join(self.test_data, "vertices_testcase4.txt"),
            os.path.join(self.test_data, "edges_testcase4.txt"),
        )
        # ask graph constructor to generate desired input parameters for func Dijkstra_to_find_shortest_distances.
        vertices, dm = self.gc.dijkstra_input_vertices_and_distance_matrix()
        src_vertex = 0
        # call func Dijkstra_to_find_shortest_distances to get the shortest distances.
        got = Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        # as the test data sets preset the cost for every edge from source vertex to destination vertex is 1
        # and all the other edges have a cost higher than 1, then, the total cost from vertex 0 to vertex n
        # is supposed to be 1 * n = n
        # for this test, n = 4 * self.offset
        self.assertEqual(got[-1], 4 * self.offset)

    def test_case5(self):
        # invoke graph constructor to construct a graph based on input text files.
        self.gc.graph_from_input_files(
            os.path.join(self.test_data, "vertices_testcase5.txt"),
            os.path.join(self.test_data, "edges_testcase5.txt"),
        )
        # ask graph constructor to generate desired input parameters for func Dijkstra_to_find_shortest_distances.
        vertices, dm = self.gc.dijkstra_input_vertices_and_distance_matrix()
        src_vertex = 0
        # call func Dijkstra_to_find_shortest_distances to get the shortest distances.
        got = Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        # as the test data sets preset the cost for every edge from source vertex to destination vertex is 1
        # and all the other edges have a cost higher than 1, then, the total cost from vertex 0 to vertex n
        # is supposed to be 1 * n = n
        # for this test, n = 5 * self.offset
        self.assertEqual(got[-1], 5 * self.offset)
