from random import randint # import the randint function from the random module

def bubbleSort(numbers: list) -> list: # simple bubble sort algorithm to sort a **SMALL** list (because of the time complexity)
    from mathFunctions import checkForNumbers, countNumbers # import only the functions I need from my math functions file
    length: int = countNumbers(numbers)

    if not checkForNumbers(numbers):  # Ensure the input is valid
        return False
    
    for i in range(length):
        for j in range(0, length - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def isListSorted(numbers: list) -> bool: # function to check if a list is sorted
    from mathFunctions import checkForNumbers, countNumbers # import only the functions I need from my math functions file
    length: int = countNumbers(numbers)

    if not checkForNumbers(numbers):  # Ensure the input is valid
        return False
    
    for i in range(length - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

def quickSort(numbers: list) -> list: # quick sort algorithm to sort a list of numbers
    from mathFunctions import checkForNumbers # import only the function I need from my math functions file

    # Check if the list contains at least one number
    if not checkForNumbers(numbers, False):  # Ensure the input is valid
        return []  # Return an empty list if the input is invalid

    if len(numbers) <= 1:  # Base case: if the list has 0 or 1 element, it's already sorted
        return numbers

    # Choose a random pivot
    randomListIndex = randint(0, len(numbers) - 1)
    pivot = numbers[randomListIndex]

    # Partitioning
    less = [number for number in numbers if number < pivot]
    equal = [number for number in numbers if number == pivot]
    greater = [number for number in numbers if number > pivot]

    # Recursively apply quickSort and concatenate results
    return quickSort(less) + equal + quickSort(greater)