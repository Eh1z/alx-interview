#!/usr/bin/python3
"""
0-pascal_triangle.py
"""

def pascal_triangle(n):
    if n <= 0:
        return []
        
    matrix = []
    for i in range(n):
        rows = []

        for j in range(i + 1):
            result = comb(i, j)
            rows.append(result)
        matrix.append(rows)

    # Return list of list
    return matrix
