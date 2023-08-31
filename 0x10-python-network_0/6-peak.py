#!/usr/bin/python3
"""script for finding peak in list of ints, interview prep
"""

"""
Find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    max_i = None
    for i in list_of_integers:
        if max_i is None or max_i < i:
            max_i = i
    return max_i
