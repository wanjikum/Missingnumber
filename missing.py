"""Missing Number Lab"""
def find_missing(array1, array2):
    """A function that returns the extra number in the array"""
    if len(array1) == len(array2):
        return 0
    else:
        result = set(array1) ^ set(array2)
        result = list(result)
        return result[0]
