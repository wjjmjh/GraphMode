import sys

import numpy

include "../include/numerical_pyrex.pyx"


def sort_impacts_based_on_comparison(Long1D impacts):
    """
    Descriptions:
    A function takes an array of impacts (int[]) as input, and return its sorted version, based on
    insertion sort algorithm.

    Insertion sort algorithm has been implemented here,
    1. Insertion sort algorithm is an in-place algorithm that requires less space or server resources
    compared against other sorting algorithms; it has a low overhead and a succinct implementation;
    2. Based on real-world working experience serving researchers, the impacts (can be reflected by the number of publications, etc.)
    of them do not have a large randomness or differences, this makes insertion sort run fairly stable and fast;
    3. The use cases of this function usually do not deal with large data sets since users may only interested in
    ranking of impacts of a specific group or cluster of researchers (e.g. Computer Science), therefore, considering the
    simple implementations of elegant properties of Insertion sort algorithm, it has been implemented here.

    Input parameters:
    impacts: an array of integers to be sorted;

    Return:
    A sorted array of impacts.
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
