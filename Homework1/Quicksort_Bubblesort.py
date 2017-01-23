import numpy as np

class Sorting_Algorithms(object):
    def __init__(self):
        empty_list_ = []

    def Quicksort(self, unsorted_list):
        """
        1. Pick a list element as pivot
        2. Move all elements greater than pivot to right, less than pivot to left
        3. Do it again until pivot is only lement in subset

        Parameters
        ----------
        unsorted_list

        Returns
        -------

        """
        # Indicies of unsorted list
        start = 0
        end = len(unsorted_list) - 1 # Always use right-most element as pivot

        print("Starting index: {0}").format(start)
        print("Ending index: {0}").format(end)

        def sort(start, end):
            pivot = end
            swap_index = start

            # pivot_insertion_index = asdf

            for element in range(start, end - 1, 1):
                if unsorted_list[element] > unsorted_list[pivot]:
                    unsorted_list[swap_index], unsorted_list[element] = unsorted_list[element], unsorted_list[swap_index]
                    swap_index += 1

            print("Recursive pivot: {0}").format(end)
            print("Recursive swap index: {0}").format(swap_index)

            unsorted_list[swap_index], unsorted_list[end] = unsorted_list[end], unsorted_list[swap_index]

            sort(start, pivot - 1)
            sort(pivot + 1, end)

        sort(start, end)
        return unsorted_list


    def Bubblesort(self, unsorted_list):
        """
        This algorithm make n-1 passes though a list of length n and checks adjacent pairs with indexes i and i-1.
        If element i is less than element i-1, switch the two elements and continue.

        Returns
        -------
        test_list_ : sorted list in original list variable
        """
        list_length = len(unsorted_list)

        print(unsorted_list)
        print(list_length)

        # Make n passes through array
        for element_index in range( list_length ):
            # Iterate from first element through unsorted section
            for current_index in range( list_length - (element_index + 1) ): # +1 to account for 0 indexing
                if unsorted_list[current_index] > unsorted_list[current_index + 1]:
                    unsorted_list[current_index], unsorted_list[current_index + 1] = unsorted_list[current_index + 1], unsorted_list[current_index]

        print("Sorted List: {0}\n\n").format(unsorted_list)
        return unsorted_list

def main():
    print("\n\nRunning sort...\n\n")
    # test_list = [213, 2, 45, 432, 5346, 3457, 347, 746, 647, 6845, 87, 87, 6759, 867, 986, 658]
    test_list = [ x * 100 for x in np.random.random(20)]

    print("Unsorted List: {0}\n\n").format(test_list)

    sort_stuff = Sorting_Algorithms()
    # sort_stuff.Bubblesort(test_list)
    sort_stuff.Quicksort(test_list)

main()