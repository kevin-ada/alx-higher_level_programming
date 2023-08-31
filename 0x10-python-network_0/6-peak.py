#!usr/bin/python3

"""The function find_peak must be written in a file named 6-peak.py,
    what the function will do is that it will loop through and find
    the highest number in the list and return it.
    """


def find_peak(list_of_integers):
    max_num = None
    for i in list_of_integers:
        if max_num is None:
            max_num = i
        elif i > max_num:
            max_num = i
    return max_num
