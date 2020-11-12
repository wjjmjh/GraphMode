import os
import sys

import numpy

from gm.main import sort_vertices_based_on_comparison
from gm.utils.graph_construction import GraphConstructor
from gm.utils.io_ import read_vertices_from_txt_files
from gm.utils.repo_path import repoPathManager
from gm.utils.tester import TestCase


class ComparisonBasedSortingTests(TestCase):
    def setUp(self) -> None:
        self.test_data = repoPathManager().comparison_sorting_test_data
        self.offset = 4000
        self.gc = GraphConstructor()

    def _template(self, test_case_number):
        # read vertices data from text file.
        got = read_vertices_from_txt_files(
            os.path.join(
                self.test_data,
                "vertices_testcase{}.txt".format(str(test_case_number)),
            )
        )
        # extract impacts from vertices.
        impacts = numpy.array([v.impact for v in got]).astype(numpy.int64)
        # construct a dictionary: {impact: an array of vertices that have this impact}
        vertices = dict()
        for vertex in got:
            if vertex.impact not in vertices.keys():
                vertices[vertex.impact] = [vertex]
            else:
                vertices[vertex.impact].append(vertex)
        # invoke func sort_vertices_based_on_comparison to sort the vertices based on impacts.
        sorted_vertices = sort_vertices_based_on_comparison(vertices, impacts)
        # the first vertex of sorted vertices is supposed to have a minimum impact: 1
        self.assertEqual(sorted_vertices[0].impact, 1)
        # the last vertex of sorted vertices is supposed to have a maximum impact: 10
        self.assertEqual(sorted_vertices[-1].impact, 10)

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
