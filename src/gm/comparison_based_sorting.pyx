import sys

import numpy

include "../include/numerical_pyrex.pyx"


def sort_vertices_based_on_comparison(Long1D vertices):
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

    for i in range(1, len(vertices)):
        k = vertices[i]
        j = i - 1
        while j >= 0 and k < vertices[j]:
            vertices[j + 1] = vertices[j]
            j -= 1
        vertices[j + 1] = k
