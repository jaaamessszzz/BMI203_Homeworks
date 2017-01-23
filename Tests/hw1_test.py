import numpy as np
from Homework1.Quicksort_Bubblesort import Sorting_Algorithms

def test_bubblesort():
    x = [1, 2, 4, 0, 6, 8, 10, 7, 5, 3, 9]
    sorted = Sorting_Algorithms.Bubblesort(x)
    assert sorted == [0,1,2,3,4,5,6,7,8,9,10]

    x.append("A")
    sorted = Sorting_Algorithms.Bubblesort(x)
    assert sorted == "List contains an non-int or -float element!"

    x = []
    sorted = Sorting_Algorithms.Bubblesort(x)
    assert sorted == "Unsorted list is empty!"

def test_quicksort():
    x = [1, 2, 4, 0, 6, 8, 10, 7, 5, 3, 9]
    sorted = Sorting_Algorithms.Quicksort(x)
    assert sorted == [0,1,2,3,4,5,6,7,8,9,10]

    x.append("A")
    sorted = Sorting_Algorithms.Bubblesort(x)
    assert sorted == "List contains an non-int or -float element!"

    x = []
    sorted = Sorting_Algorithms.Bubblesort(x)
    assert sorted == "Unsorted list is empty!"