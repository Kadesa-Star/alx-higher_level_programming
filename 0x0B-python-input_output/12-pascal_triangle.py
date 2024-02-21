#!/usr/bin/python3
""" The Pascal's triangle"""


def pascal_triangle(n):
    """ this function returns a list of integers representing 
    the pascal's triangle """

    # returns a n empty list
    if n <= 0:
        return []

    # initialize a triangle for the first row
    triangle = [[1]]
    # iterate over the range from 0 to n-1
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        # calculate the values of the new row based on prev row
        for j in range(1, i + 1):
            if j is i:
                new_row.append(1)
            else:
                new_row.append(prev_row[j - 1] + prev_row[j])

        # calculates the value of the new row based on the prev
        triangle.append(new_row)

    # Pascal's triangle
    return triangle
