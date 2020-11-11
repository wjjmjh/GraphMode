import os
import time

import matplotlib.pyplot as plt
import numpy

from gm.main import (Dijkstra_to_find_shortest_distances,
                     dynamic_programming_to_find_the_shortest_path)
from gm.utils.graph_construction import GraphConstructor
from gm.utils.repo_path import repoPathManager


def analysis():
    # x axis is different numbers of nodes.
    x = [300, 600, 900, 1200, 1500]
    # y axis is the execution time.
    y = []
    for number_of_nodes in x:
        # get the path to test data sets.
        test_data = repoPathManager().dp_test_data
        # prepare some input parameters for func dynamic_programming_to_find_the_shortest_path
        number_of_vertices_per_level = 3
        offset = 100
        inf = float("inf")
        nocost = 0.00001
        n = number_of_vertices_per_level * offset * int(number_of_nodes / x[0]) + 1
        path = numpy.array([-1 for _ in range(n)]).astype(numpy.int64)
        dist = numpy.array([[inf] * n for _ in range(n)]).astype(numpy.double)
        foot_print = numpy.array([[-1] * n for _ in range(n)]).astype(numpy.int64)
        # invoke graph constructor to read inputs, construct a graph and generate necessary inputs
        # for func dynamic_programming_to_find_the_shortest_path
        gc = GraphConstructor()
        gc.graph_from_input_files(
            os.path.join(
                test_data,
                "vertices_testcase{}.txt".format(str(int(number_of_nodes / x[0]))),
            ),
            os.path.join(
                test_data,
                "edges_testcase{}.txt".format(str(int(number_of_nodes / x[0]))),
            ),
        )
        edges = gc.dp_input_edges()
        edges += [(v, v, nocost) for v in range(n)]
        for first, second, weight in edges:
            dist[first][second] = weight
            foot_print[first][second] = second
        # empirically assess the algorithm.
        start_time = time.process_time()
        dynamic_programming_to_find_the_shortest_path(
            0,
            number_of_vertices_per_level * offset * int(number_of_nodes / x[0]),
            path,
            n,
            dist,
            foot_print,
        )
        y.append(time.process_time() - start_time)
    plt.plot(x, y, "ro")
    plt.show()


if __name__ == "__main__":
    analysis()
