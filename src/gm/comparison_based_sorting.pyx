import sys

import numpy

include "../include/numerical_pyrex.pyx"


def sort_impacts_based_on_comparison(Long1D impacts):
    """
    Descriptions:
    A function takes an array of vertices as input, and return its sorted version, based on
    comparisons.

    Input parameters:
    vertices: an array of Vertex objects to be sorted;
    order: a string that specifies the comparison-based sorting is ascending or descending;

    Return:
    A sorted array of vertices.
    """
    cdef int i, j
    cdef long k

    for i in range(1, len(impacts)):
        k = impacts[i]
        j = i - 1
        while j >= 0 and k < impacts[j]:
            impacts[j + 1] = impacts[j]
            j -= 1
        impacts[j + 1] = k
