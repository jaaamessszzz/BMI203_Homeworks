import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import timeit

class Sorting_Algorithms(object):
    def __init__(self):
        self.quick_assignments = 0
        self.quick_conditionals = 0
        self.quicksort_assignments = []
        self.quicksort_conditionals = []

        self.bubble_assignments = 0
        self.bubble_conditionals = 0
        self.bubblesort_assignments = []
        self.bubblesort_conditionals = []

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

        self.quick_assignments = 0
        self.quick_conditionals = 0

        # Checks
        if not all([isinstance(x, (float, int)) for x in unsorted_list]):
            return ("List contains an non-int or -float element!")
        if len(unsorted_list) == 0:
            return ("Unsorted list is empty!")

        # print("Unsorted List: {0}\n\n").format(unsorted_list)

        # Start and end indicies of unsorted list
        start = 0
        end = len(unsorted_list) - 1

        self.quick_assignments += 2

        # print("Starting index: {0}").format(start)
        # print("Ending index: {0}").format(end)

        def sort(start, end):
            if start < end:

                self.quick_conditionals += 1

                # print("\n**** STARTING NEXT ITERATION ****\n")
                # print "Subsection length: {0}".format(len(unsorted_list[start:end]))

                pivot = end
                swap_index = start

                self.quick_assignments += 2

                # print("\n**** Before Sort ****")
                # print("Pivot {0}: {1}").format(end, unsorted_list[end])
                # print("Swap index: {0}").format(swap_index)

                for element in range(start, end, 1):

                    self.quick_assignments += 1

                    # print("Element {0}: {1}").format(element, unsorted_list[element])
                    if unsorted_list[element] < unsorted_list[pivot]:

                        self.quick_conditionals += 1

                        unsorted_list[swap_index], unsorted_list[element] = unsorted_list[element], unsorted_list[swap_index]

                        self.quick_assignments += 2

                        # print("Swapped {0} with {1}").format(unsorted_list[swap_index], unsorted_list[element])
                        swap_index = swap_index + 1

                        self.quick_assignments += 1

                # print("\n**** After Sort ****")
                # print("Pivot {0}: {1}").format(end, unsorted_list[end])
                # print("Swap index: {0}").format(swap_index)

                unsorted_list[swap_index], unsorted_list[end] = unsorted_list[end], unsorted_list[swap_index]

                self.quick_assignments += 2

                # print("Sorting progress: {0}").format(unsorted_list)
                # print "Subsection left indicies: {0} {1}".format(start, swap_index - 1)
                # print "Subsection right indicies: {0} {1}".format(swap_index + 1, end)

                sort(start, swap_index - 1)
                sort(swap_index + 1, end)

        # Recursive sort
        sort(start, end)

        # print("\n\nSorted list: {0}\n\n").format(unsorted_list)

        self.quicksort_assignments.append(self.quick_assignments)
        self.quicksort_conditionals.append(self.quick_conditionals)

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
        self.bubble_assignments = 0
        self.bubble_conditionals = 0

        # Checks
        if not all([isinstance(x, (float, int)) for x in unsorted_list]):
            return ("List contains an non-int or -float element!")
        if len(unsorted_list) == 0:
            return ("Unsorted list is empty!")

        # print("Unsorted List: {0}\n\n").format(unsorted_list)

        list_length = len(unsorted_list)

        self.bubble_assignments += 1

        # Make n passes through array
        for element_index in range( list_length ):
            # Iterate from first element through unsorted section
            for current_index in range( list_length - (element_index + 1) ): # +1 to account for 0 indexing
                if unsorted_list[current_index] > unsorted_list[current_index + 1]:
                    self.bubble_conditionals += 1

                    unsorted_list[current_index], unsorted_list[current_index + 1] = unsorted_list[current_index + 1], unsorted_list[current_index]

                    self.bubble_assignments += 2

        # print("Sorted List: {0}\n\n").format(unsorted_list)

        self.bubblesort_assignments.append(self.bubble_assignments)
        self.bubblesort_conditionals.append(self.bubble_conditionals)

        return unsorted_list

    def plot_timecourse(self):
        exponential_trials = [100 * increment for increment in range(1, 11)]

        def sort_decorator(function, iterations):
            test_list = [[x * 100 for x in np.random.random(iterations)] for y in range(100)]

            def wrapper():
                return function(test_list)
            return wrapper

        n_trials = []
        time_quick = []
        time_bubble = []

        avg_quick_assign = []
        avg_quick_condit = []
        avg_bubble_assign = []
        avg_bubble_condit = []


        for trials in exponential_trials:
            wrapped_quick = sort_decorator(self.test_quick, trials)
            wrapped_bubble = sort_decorator(self.test_bubble, trials)

            n_trials.append(trials)
            time_quick.append(timeit.timeit(wrapped_quick, number=1))
            time_bubble.append(timeit.timeit(wrapped_bubble, number=1))

            avg_bubble_assign.append(np.mean(self.bubblesort_assignments[trials - 100 : trials - 1]))
            avg_bubble_condit.append(np.mean(self.bubblesort_conditionals[trials - 100 : trials - 1]))

            avg_quick_assign.append(np.mean(self.quicksort_assignments[trials - 100 : trials - 1]))
            avg_quick_condit.append(np.mean(self.quicksort_conditionals[trials - 100 : trials - 1]))

        df = pd.DataFrame({
            "Trial_Number": n_trials,
            "Quicksort": time_quick,
            "Bubblesort": time_bubble
        })

        print(n_trials)
        print(time_quick)
        print(time_bubble)

        counts_df = pd.DataFrame({
            "Avg_bubble_assignmets" : avg_bubble_assign,
            "Avg_bubble_conditionals" : avg_bubble_condit,
            "Avg_quick_assignmets" : avg_quick_assign,
            "Avg_quick_conditionals" : avg_quick_condit
        })

        counts_df.to_csv("Algorithm_scaling_counts.csv")

        # Set up plotting
        sns.set_style("whitegrid", {'axes.grid' : False})
        fig, ax = plt.subplots()

        sns.regplot("Trial_Number", "Bubblesort", df, fit_reg=False, label="Bubblesort", color="blue")
        sns.regplot("Trial_Number", "Quicksort", df, fit_reg=False, label="Quicksort", color="red")

        # Set axes
        plt.xlim(0, n_trials[-1] + 0.1 * n_trials[-1])
        plt.ylim(0, 15)

        # Set Legend
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels, loc=2)
        plt.setp(plt.gca().get_legend().get_texts(), fontsize=12)

        # Set figure text
        plt.xlabel("Random Input List Size")
        plt.ylabel("Run time (seconds)")
        figure_title = fig.suptitle("Sort Algorithm Run Time as a Funciton of Input Size", fontsize=20)

        t2 = np.arange(0.0, n_trials[-1], 1)

        popt, pcov = sp.optimize.curve_fit(self.n_squared, df.Trial_Number, df.Bubblesort)
        print (popt)
        print (pcov)
        plt.plot(t2, self.n_squared(t2, popt[0]), 'b--')

        ax.text(40, 12, r"Bubblesort fit to $f(N) = constant * N^2$", fontsize=12)
        ax.text(40, 11.25, r"Bubblesort fitted constant = $%s$" % popt[0], fontsize=12)

        popt, pcov = sp.optimize.curve_fit(self.n_log_n, df.Trial_Number, df.Quicksort)
        print (popt)
        print (pcov)
        plt.plot(t2, self.n_log_n(t2, popt[0]), 'r--')

        ax.text(40, 10.5, r"Quicksort fit to $f(N) = constant * Nlog(N)$", fontsize=12)
        ax.text(40, 9.75, r"Quicksort fitted constant = $%s$" % popt[0], fontsize=12)

        fig.savefig("Algorithm_Scaling.pdf", dpi=300, bbox_inches="tight", bbox_extra_artists = [figure_title])

    def n_squared(self, input_N, const):
        return const * input_N**2

    def n_log_n (self, input_N, const):
        return const * input_N * np.log(input_N)

    def test_quick(self, test_lists):
        for list in test_lists:
            self.Quicksort(list)

    def test_bubble(self, test_lists):
        for list in test_lists:
            self.Bubblesort(list)

def main():
    print("\n\nRunning sort...\n\n")

    # test_list = [x * 100 for x in np.random.random(100)]

    sort_stuff = Sorting_Algorithms()
    # sort_result = sort_stuff.Quicksort(test_list)
    # print(sort_result)

    sort_stuff.plot_timecourse()

if __name__ == "__main__":
    main()