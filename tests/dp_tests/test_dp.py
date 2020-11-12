import os
import sys

import numpy

from gm.main import dynamic_programming_to_find_the_shortest_path
from gm.utils.graph_construction import GraphConstructor
from gm.utils.repo_path import repoPathManager
from gm.utils.tester import TestCase


class DynamicProgrammingTests(TestCase):
    def setUp(self) -> None:
        self.test_data = repoPathManager().dp_test_data
        self.number_of_vertices_per_level = 3
        self.offset = 100
        self.gc = GraphConstructor()
        self.inf = float("inf")
        self.nocost = 0.00001

    def _template(self, test_case_number):
        # invoke graph constructor to read input text files, construct a graph and generate necessary inputs
        # for func dynamic_programming_to_find_the_shortest_path
        self.gc.graph_from_input_files(
            os.path.join(
                self.test_data, "vertices_testcase{}.txt".format(str(test_case_number))
            ),
            os.path.join(
                self.test_data, "edges_testcase{}.txt".format(str(test_case_number))
            ),
        )
        # prepare necessary input parameters for func dynamic_programming_to_find_the_shortest_path
        # for specific definitions or meanings of these parameters,
        # please see func dynamic_programming_to_find_the_shortest_path docstrings.
        n = self.number_of_vertices_per_level * self.offset * test_case_number + 1
        dist = numpy.array([[self.inf] * n for _ in range(n)]).astype(numpy.double)
        foot_print = numpy.array([[-1] * n for _ in range(n)]).astype(numpy.int64)
        edges = self.gc.dp_input_edges()
        edges += [(v, v, self.nocost) for v in range(n)]
        for first, second, weight in edges:
            dist[first][second] = weight
            foot_print[first][second] = second
        path = numpy.array([-1 for _ in range(n)]).astype(numpy.int64)
        # call func dynamic_programming_to_find_the_shortest_path
        # to compute the shortest path from vertex 0 to vertex n.
        got = [
            val
            for val in dynamic_programming_to_find_the_shortest_path(
                0,
                self.number_of_vertices_per_level * self.offset * test_case_number,
                path,
                n,
                dist,
                foot_print,
            )
            if val != -1
        ]
        # given the test data sets, every edge of the computed path is supposed to have a cost: 1
        # and we preset such path in the test data sets:
        # 0 -> 1 * number_of_vertices_per_level -> 2 * number_of_vertices_per_level -> ... -> n
        self.assertEqual(
            got,
            [
                i
                for i in range(
                    0,
                    self.number_of_vertices_per_level * self.offset * test_case_number
                    + 1,
                    self.number_of_vertices_per_level,
                )
            ],
        )

    def test_case1(self):
        self._template(1)

    def test_case2(self):
        self._template(2)

    def test_case3(self):
        self._template(3)

    def test_case4(self):
        self._template(4)

    def test_case5(self):
        self._template(5)
