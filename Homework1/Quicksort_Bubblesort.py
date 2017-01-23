import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import timeit

class Sorting_Algorithms(object):
    def __init__(self):
        empty_list = []

    def Quicksort(self, unsorted_list):
        """
        1. Pick a list element as pivot
        2. Move all elements greater than pivot to right, less than pivot to left
        3. Do it again until pivot is only element in subset

        Note:  all commented out print statements were for debugging

        Parameters
        ----------
        unsorted_list: unsorted input list with n elements

        Returns
        -------
        unsorted_list: input list sorted in place
        """
        # Checks
        if not all(isinstance(x,float or int) for x in unsorted_list):
            return ("List contains an non-int or -float element!")
        if len(unsorted_list) < 0:
            return ("Unsorted list is empty!")

        # print("Unsorted List: {0}\n\n").format(unsorted_list)

        # Start and end indicies of unsorted list
        start = 0
        end = len(unsorted_list) - 1

        # print("Starting index: {0}").format(start)
        # print("Ending index: {0}").format(end)

        def sort(start, end):
            if start < end:

                # print("\n**** STARTING NEXT ITERATION ****\n")
                # print "Subsection length: {0}".format(len(unsorted_list[start:end]))

                pivot = end
                swap_index = start

                # print("\n**** Before Sort ****")
                # print("Pivot {0}: {1}").format(end, unsorted_list[end])
                # print("Swap index: {0}").format(swap_index)

                for element in range(start, end, 1):
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
                # print "Subsection left indicies: {0} {1}".format(start, swap_index - 1)
                # print "Subsection right indicies: {0} {1}".format(swap_index + 1, end)

                sort(start, swap_index - 1)
                sort(swap_index + 1, end)

        # Recursive sort
        sort(start, end)

        # print("\n\nSorted list: {0}\n\n").format(unsorted_list)

        return unsorted_list


    def Bubblesort(self, unsorted_list):
        """
        This algorithm make n-1 passes though a list of length n and checks adjacent pairs with indexes i and i-1.
        If element i is less than element i-1, switch the two elements and continue.

        Parameters
        ----------
        unsorted_list: unsorted input list with n elements

        Returns
        -------
        unsorted_list: input list sorted in place
        """
        # Checks
        if not all(isinstance(x,float or int) for x in unsorted_list):
            return ("List contains an non-int or -float element!")
        if len(unsorted_list) < 0:
            return ("Unsorted list is empty!")

        # print("Unsorted List: {0}\n\n").format(unsorted_list)

        list_length = len(unsorted_list)

        # Make n passes through array
        for element_index in range( list_length ):
            # Iterate from first element through unsorted section
            for current_index in range( list_length - (element_index + 1) ): # +1 to account for 0 indexing
                if unsorted_list[current_index] > unsorted_list[current_index + 1]:
                    unsorted_list[current_index], unsorted_list[current_index + 1] = unsorted_list[current_index + 1], unsorted_list[current_index]

        # print("Sorted List: {0}\n\n").format(unsorted_list)

        return unsorted_list

def plot_timecourse():
    exponential_trials = [100 * increment for increment in range(1, 11)]

    def sort_decorator(function, iterations):
        sort_stuff = Sorting_Algorithms()
        test_list = [[x * 100 for x in np.random.random(iterations)] for y in range(100)]

        def wrapper():
            return function(sort_stuff, test_list)
        return wrapper

    n_trials = []
    time_quick = []
    time_bubble = []

    for trials in exponential_trials:
        wrapped_quick = sort_decorator(test_quick, trials)
        wrapped_bubble = sort_decorator(test_bubble, trials)

        print trials
        n_trials.append(trials)
        time_quick.append(timeit.timeit(wrapped_quick, number=1))
        time_bubble.append(timeit.timeit(wrapped_bubble, number=1))

    df = pd.DataFrame({
        "Trial_Number": n_trials,
        "Quicksort": time_quick,
        "Bubblesort": time_bubble
    })

    print(n_trials)
    print(time_quick)
    print(time_bubble)

    fig, ax = plt.subplots()
    sns.despine()
    sns.set_style("whitegrid")

    sns.regplot("Trial_Number", "Quicksort", df, fit_reg=False, label="Quicksort", color="red")
    sns.regplot("Trial_Number", "Bubblesort", df, fit_reg=False, label="Bubblesort", color="blue")

    t2 = np.arange(0.0, n_trials[-1], 1)

    popt, pcov = sp.optimize.curve_fit(n_squared, df.Trial_Number, df.Bubblesort)
    print popt
    print pcov
    plt.plot(t2, n_squared(t2, popt[0]), 'b--')

    popt, pcov = sp.optimize.curve_fit(n_log_n, df.Trial_Number, df.Quicksort)
    print popt
    print pcov
    plt.plot(t2, n_log_n(t2, popt[0]), 'r--')

    plt.xlim(0, n_trials[-1] + 0.1 * n_trials[-1])
    plt.ylim(0, 10)

    plt.ylabel("Run time (seconds)")
    fig.suptitle("Sort Algorithm Run Time as a Funciton of Input Size")

    plt.show()

def n_squared(input_N, const):
    return const * input_N**2

def n_log_n (input_N, const):
    return const * input_N * np.log(input_N)

def test_quick(sort_stuff, test_lists):
    for list in test_lists:
        sort_stuff.Quicksort(list)

def test_bubble(sort_stuff, test_lists):
    for list in test_lists:
        sort_stuff.Bubblesort(list)

def main():
    print("\n\nRunning sort...\n\n")

    test_list = [x * 100 for x in np.random.random(100)]

    sort_stuff = Sorting_Algorithms()
    sort_result = sort_stuff.Quicksort(test_list)
    print(sort_result)

    # plot_timecourse()

main()