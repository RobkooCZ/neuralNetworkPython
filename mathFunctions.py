def checkForNumbers(numbers): # simple function to check if a list contains numbers
    if not numbers:
        print("The list must contain at least one number.")
        return False
    for number in numbers:
        if not isinstance(number, (int, float)):
            print("The list must contain only numbers.")
            return False
    
def countNumbers(numbers): # simple function to count how many numbers there are in a list
    numbersCheck: bool = checkForNumbers(numbers)
    numberCount: int = 0

    if not numbersCheck:
        return False
    
    for number in numbers:
        numberCount += 1

    return numberCount

def bubbleSort(numbers): # simple bubble sort algorithm to sort a **SMALL** list (because of the time complexity)
    numbersCheck: bool = checkForNumbers(numbers)
    length: int = countNumbers(numbers)

    if not numbersCheck:
        return False
    
    for i in range(length):
        for j in range(0, length - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def mean(numbers): # Function for calculate the mean value of a list of numbers
    answer: float = 0
    numberCount: int = countNumbers(numbers)
    numbersCheck: bool = checkForNumbers(numbers)
    
    if not numbersCheck:
        return False
    
    return answer / numberCount

def median(numbers): # function to find the median of a list of numbers
    numbersCheck: bool = checkForNumbers(numbers)
    numbersCount: int = countNumbers(numbers)
    numbers: list = bubbleSort(numbers)

    if not numbersCheck:
        return False
    
    if numbersCount % 2 == 0:
        median1 = numbers[numbersCount // 2]
        median2 = numbers[numbersCount // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = numbers[numbersCount // 2]
    return median
    
def mode(numbers): # function to find the mode of a list of numbers
    numbersCheck: bool = checkForNumbers(numbers)  # Check if all elements are numbers

    if not numbersCheck:
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