import numpy as np
import timeit

class Sorting_Algorithms(object):
    def __init__(self):
        empty_list_ = []

    def Quicksort(self, unsorted_list):
        """
        1. Pick a list element as pivot
        2. Move all elements greater than pivot to right, less than pivot to left
        3. Do it again until pivot is only element in subset

        Note:  all commented out print statements were for debugging

        Parameters
        ----------
        unsorted_list: input list with n elements

        Returns
        -------
        unsorted_list: input list sorted in place
        """
        # Start and end indicies of unsorted list
        start = 0
        end = len(unsorted_list) - 1

        # print("Starting index: {0}").format(start)
        # print("Ending index: {0}").format(end)

        def sort(start, end):
            if start <= end:
                pivot = end
                swap_index = start

                # print("\n**** Before Sort ****")
                # print("Pivot {0}: {1}").format(end, unsorted_list[end])
                # print("Swap index: {0}").format(swap_index)

                for element in range(start, end):
                    # print("Element {0}: {1}").format(element, unsorted_list[element])
                    if unsorted_list[element] < unsorted_list[pivot]:
                        unsorted_list[swap_index], unsorted_list[element] = unsorted_list[element], unsorted_list[swap_index]
                        # print("Swapped {0} with {1}").format(unsorted_list[swap_index], unsorted_list[element])
                        swap_index = swap_index + 1

                # print("\n**** After Sort ****")
                # print("Pivot {0}: {1}").format(end, unsorted_list[end])
                # print("Swap index: {0}").format(swap_index)

                unsorted_list[swap_index], unsorted_list[end] = unsorted_list[end], unsorted_list[swap_index]

                # print("Sorting progress: {0}").format(unsorted_list)

                sort(start, swap_index - 1)
                sort(swap_index + 1, end)

        # Recursive sort
        sort(start, end)

        print("\n\nSorted list: {0}\n\n").format(unsorted_list)

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

    test_list = [ x * 100 for x in np.random.random(100)]
    print("Unsorted List: {0}\n\n").format(test_list)

    sort_stuff = Sorting_Algorithms()

    sort_stuff.Bubblesort(test_list)
    sort_stuff.Quicksort(test_list)

main()