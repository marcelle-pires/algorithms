# Find the least value of array and return its index

def find_least(array):
    least = array[0]
    index = 0

    for i in range(0, len(array)):
        if array[i] < least:
            index = i
            least = array[i]

    return index

# Selection sort algorithms
# Input: receive an array 
# Output: return a new array sorted from high to low

def selection_sort(array):
    newArray = []

    for i in range(0, len(array)):
        least = find_least(array)
        newArray.append(array.pop(least))

    return newArray
