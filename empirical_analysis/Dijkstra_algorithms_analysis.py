import os
import time

import matplotlib.pyplot as plt

from gm.main import Dijkstra_to_find_shortest_distances
from gm.utils.graph_construction import GraphConstructor
from gm.utils.repo_path import repoPathManager


def analysis():
    # x axis is different numbers of nodes.
    x = [2400, 4800, 7200, 9600, 12000]
    # y axis is the execution time.
    y = []
    for number_of_nodes in x:
        # get the path of test data sets.
        test_data = repoPathManager().Dijkstra_test_data
        gc = GraphConstructor()
        # invoke graph constructor to read data from text files and construct a graph.
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
        # invoke graph constructor to generate necessary input parameters for func Dijkstra_to_find_shortest_distances
        vertices, dm = gc.dijkstra_input_vertices_and_distance_matrix()
        # specify the source vertex is vertex 0.
        src_vertex = 0
        start_time = time.process_time()
        Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        y.append(time.process_time() - start_time)
    plt.plot(x, y, "ro")
    plt.show()


if __name__ == "__main__":
    analysis()
