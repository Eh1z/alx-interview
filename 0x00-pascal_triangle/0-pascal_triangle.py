#!/usr/bin/python3
"""
0-pascal_triangle.py
"""
n = 4
def pascal_triangle(n):
  main_list = []
  for i in range (n):
    temp_list = []
    for j in range(i + 1):
      if j == 0 or j == i:
        temp_list.append(1)
      else:
        temp_list.append(main_list[i-1][j-1] + main_list[i-1][j])
  main_list.append(temp_list)
print(main_list)

              
