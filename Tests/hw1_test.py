import numpy as np
from Homework1.Quicksort_Bubblesort import Sorting_Algorithms

def test_bubblesort():
    unsorted_list = [1, 2, 4, 0, 6, 8, 10, 7, 5, 3, 9]
    sort_stuff = Sorting_Algorithms()

    my_sorted_list = sort_stuff.Bubblesort(unsorted_list=unsorted_list)
    print(my_sorted_list)
    print(type(my_sorted_list))
    assert my_sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    unsorted_list.append("A")
    my_sorted_list = sort_stuff.Bubblesort(unsorted_list=unsorted_list)
    assert my_sorted_list == "List contains an non-int or -float element!"

    unsorted_list = []
    my_sorted_list = sort_stuff.Bubblesort(unsorted_list=unsorted_list)
    assert my_sorted_list == "Unsorted list is empty!"

def test_quicksort():
    unsorted_list = [1, 2, 4, 0, 6, 8, 10, 7, 5, 3, 9]
    sort_stuff = Sorting_Algorithms()

    my_sorted_list = sort_stuff.Quicksort(unsorted_list=unsorted_list)
    print(my_sorted_list)
    print(type(my_sorted_list))
    assert my_sorted_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    unsorted_list.append("A")
    my_sorted_list = sort_stuff.Quicksort(unsorted_list=unsorted_list)
    assert my_sorted_list == "List contains an non-int or -float element!"

    unsorted_list = []
    my_sorted_list = sort_stuff.Quicksort(unsorted_list=unsorted_list)
    assert my_sorted_list == "Unsorted list is empty!"

test_bubblesort()
test_quicksort()