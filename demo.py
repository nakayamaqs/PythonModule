#!/usr/bin/env python
# encoding: utf-8
# Here's a simple script (feels like a program, though) Quick sort list of numbers/string etc.
# Sourcecode from MIT Open course ware

def quick_sort(list):
    """
    Quicksort using list comprehensions
    >>> quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
    [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9]
    >>> quick_sort(["bob","alice","barry","zoe","charlotte","fred","marvin"])
    ['alice', 'barry', 'bob', 'charlotte', 'fred', 'marvin', 'zoe']
    >>> quick_sort([5,6,9,1,5,8,3,4,5,10,4])
    [1, 3, 4, 4, 5, 5, 5, 6, 8, 9, 10]
    """
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = quick_sort([x for x in list[1:] if x < pivot])
        greater = quick_sort([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater

def run_quicksort():
    demolist = [5,6,9,1,5,8,3,4,5,10,4];
    print("Before sorting: "+ str(demolist));
    print("After sorting: "+ str(quick_sort(demolist)))

# run_quicksort()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
