#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if not list_of_integers:  # Check if list is empty
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = size // 2  # Use integer division for midpoint calculation
    peak = list_of_integers[mid]

    # Check if peak is greater than its neighbors
    if (mid == 0 or peak >= list_of_integers[mid - 1]) and \
            (mid == size - 1 or peak >= list_of_integers[mid + 1]):
        return peak
    elif mid > 0 and list_of_integers[mid - 1] > peak:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
