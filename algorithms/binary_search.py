from materials import clients

def binary_search(list, item):
    '''
    Searching algorithm

    list/dictionary must be sorted.

    BIG O = log2(len(list))

    args: list/dict, item
    '''
    low = 0 
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            high = mid + 1
    return f"{item} not found"


result = binary_search(clients, 'Jordan')
print(result)
