#!/usr/bin/python3
"""Defines a Pascal’s triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle
    of n size
    """
    if n <= 0:
        return []

    p_triangles = [[1]]
    while len(p_triangles) != n:
        p_tri = p_triangles[-1]
        temp = [1]
        for i in range(len(p_tri) - 1):
            temp.append(p_tri[i] + p_tri[i + 1])
        temp.append(1)
        p_triangles.append(temp)
    return p_triangles
