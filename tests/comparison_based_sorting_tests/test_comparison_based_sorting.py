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
        vertices = numpy.array(
            [
                v.impact
                for v in read_vertices_from_txt_files(
                    os.path.join(
                        self.test_data,
                        "vertices_testcase{}.txt".format(str(test_case_number)),
                    )
                )
            ]
        ).astype(numpy.int64)
        sort_vertices_based_on_comparison(vertices)
        self.assertEqual(vertices[0], 1)
        self.assertEqual(vertices[-1], 10)

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
