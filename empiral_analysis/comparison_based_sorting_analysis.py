import os
import time

import matplotlib.pyplot as plt
import numpy

from gm.main import sort_vertices_based_on_comparison
from gm.utils.io_ import read_vertices_from_txt_files
from gm.utils.repo_path import repoPathManager


def analysis():
    x = [4000 * i for i in range(1, 6)]
    y = []
    for number_of_nodes in x:
        test_data = repoPathManager().comparison_sorting_test_data
        vertices = read_vertices_from_txt_files(
            os.path.join(
                test_data,
                "vertices_testcase{}.txt".format(str(int(number_of_nodes / x[0]))),
            )
        )
        vertices = numpy.array([v.impact for v in vertices]).astype(numpy.int64)
        start_time = time.process_time()
        sort_vertices_based_on_comparison(vertices)
        y.append(time.process_time() - start_time)
    plt.plot(x, y, "ro")
    plt.show()


if __name__ == "__main__":
    analysis()
