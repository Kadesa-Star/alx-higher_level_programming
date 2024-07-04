#!/usr/bin/python3
"""
6-peak.py

Module to find a peak in a list of unsorted integers efficiently.

This module implements a function find_peak(list_of_integers) that
returns a peak element from the list. A peak is defined as an element
that is greater than or equal to its neighbors.

Example:
    list_of_integers = [1, 2, 3, 1]
    print(find_peak(list_of_integers))  # Output: 3
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int or None: peak element from list,None if list empty.

    Complexity:
        O(log n)

    Raises:
        ValueError: If the input list is empty.

    Note:
        There may be multiple peak elements in the list, this function
        returns any one of them.
    """
    if not list_of_integers:
        return None
    low, high = 0, len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return list_of_integers[low]
