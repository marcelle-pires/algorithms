# Binary search algorithms
# Input: a list of values and one value to be searched
# Output: Return the index of searched value or 
# None if the number is not listed 

def binary_search(list, value: int):
    
    start = 0
    end = len(list) - 1

    while (start <= end):
        middle = (start+end) // 2
        tryValue = list[middle]

        if tryValue == value:
            return middle
        elif tryValue > value:
            end = middle - 1
        else:
            start = middle + 1
    
    return None