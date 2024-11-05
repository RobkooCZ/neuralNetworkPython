from math import sqrt # import the square root function from the math module
from sortingAlgorithms import bubbleSort # import the bubble sort function from the algorithm file

def checkForNumbers(numbers: list, checkNumberCount: bool) -> bool: # simple function to check if a list contains numbers
    if not numbers and checkNumberCount:
        print("The list must contain at least one number.")
        return False
    for number in numbers:
        if not isinstance(number, (int, float)):
            print("The list must contain only numbers.")
            return False
    
    return True
    
def countNumbers(numbers: list) -> int: # simple function to count how many numbers there are in a list
    numberCount: int = 0

    if not checkForNumbers(numbers, True):  # Ensure the input is valid
        return False
    
    for number in numbers:
        numberCount += 1

    return numberCount

def mean(numbers: list) -> float: # Function for calculate the mean value of a list of numbers
    addedNumbers: float = 0
    numberCount: int = countNumbers(numbers)
    
    if not checkForNumbers(numbers, True):  # Ensure the input is valid
        return False
    
    for number in numbers:
        addedNumbers += number

    return addedNumbers / numberCount

def median(numbers: list) -> float: # function to find the median of a list of numbers
    numbersCount: int = countNumbers(numbers)
    numbers: list = bubbleSort(numbers)

    if not checkForNumbers(numbers, True):  # Ensure the input is valid
        return False
    
    if numbersCount % 2 == 0:
        median1 = numbers[numbersCount // 2]
        median2 = numbers[numbersCount // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = numbers[numbersCount // 2]
    return median
    
def mode(numbers: list) -> float: # function to find the mode of a list of numbers
    if not checkForNumbers(numbers, True):  # Ensure the input is valid
        return False
    
    frequency = {}  # Dictionary to store each number and its frequency
        
    # Count the occurrences of each number
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    # Find the number with the highest frequency
    mostAppearedNumber: int = None
    maxCount: int = 0
    for number, count in frequency.items():
        if count > maxCount:
            maxCount = count
            mostAppearedNumber = number

    return mostAppearedNumber

def standardDeviation(numbers: list) -> float: # function to find the standard deviation of a list of numbers
    numberCount: int = countNumbers(numbers)
    meanValue: float = mean(numbers)
    sigma: float = 0

    if not checkForNumbers(numbers, True):  # Ensure the input is valid
        return False
    
    for number in numbers:
        sigma += (number - meanValue) ** 2

    sigma /= numberCount

    return sqrt(sigma)

def variation(numbers: list) -> float: # function to find the variation of a list of numbers
    numberCount: int = countNumbers(numbers)
    meanValue: float = mean(numbers)
    variation: float = 0

    if not checkForNumbers(numbers, True):  # Ensure the input is valid
        return False
    
    for number in numbers:
        variation += (number - meanValue) ** 2

    variation /= numberCount

    return variation

def percentile(numbers: list, percent: int) -> float: # function to find the percentile of a list of numbers
    numberCount: int = countNumbers(numbers)

    if not checkForNumbers(numbers, True):  # Ensure the input is valid
        return False
    
    numbers = bubbleSort(numbers)  # Sort the list
    rank = (percent / 100) * (numberCount)  # Calculate the rank of the percentile

    # Adjust the rank for 0-based index
    index = int(rank)

    if index == rank:  # If rank is an integer, return that value
        return numbers[index - 1]  # Subtract 1 for 0-based index
    else:  # If rank is not an integer, return the value at floor(rank)
        return numbers[index]  # This gives the next highest value