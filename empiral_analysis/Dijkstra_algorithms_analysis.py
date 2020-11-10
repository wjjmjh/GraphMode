import os
import time

import matplotlib.pyplot as plt

from gm.main import Dijkstra_to_find_shortest_distances
from gm.utils.graph_construction import GraphConstructor
from gm.utils.repo_path import repoPathManager


def analysis():
    x = [2400, 4800, 7200, 9600, 12000]
    y = []
    for number_of_nodes in x:
        test_data = repoPathManager().Dijkstra_test_data
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
        vertices, dm = gc.dijkstra_input_vertices_and_distance_matrix()
        src_vertex = 0
        start_time = time.process_time()
        Dijkstra_to_find_shortest_distances(src_vertex, vertices, dm)
        y.append(time.process_time() - start_time)
    plt.plot(x, y, "ro")
    plt.show()


if __name__ == "__main__":
    analysis()
