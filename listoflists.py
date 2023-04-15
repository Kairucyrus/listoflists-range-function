# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:53:09 2023

@author: Kairu Cyrus
Creating a function that accepts a list of lists as a parameter and returns a range 
of values contained in the list of lists, defined as two or more than the difference
between the largest and smallest elements of the list of lists
"""

def range_list(lst):
    flat_list = [item for sublist in lst for item in sublist]
    return max(flat_list) - min(flat_list) + 2

my_list = [[11, 9, 23], [16, 6, 18], [4, 19, 1]]
print(range_list(my_list)) # returns 24
"""
First, we flattened the list of lists into a single list through list comprehension.
We then computed the range by subtracting the smallest value from the largest and adding
2
"""