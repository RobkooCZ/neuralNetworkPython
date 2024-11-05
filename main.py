from mathFunctions import * # import all functions from my file
from sortingAlgorithms import * # import all functions from my file

if __name__ == "__main__": # temporary test code to test if the quick sort algorithm works
    unsortedNumbers = [8, 3, 1, 7, 0, 10, 14]
    print(f"Unsorted numbers: {unsortedNumbers}")
    sortedNumbers = quickSort(unsortedNumbers)
    print(f"Sorted numbers: {sortedNumbers}")  # Output should be: [0, 1, 3, 7, 8, 10, 14]