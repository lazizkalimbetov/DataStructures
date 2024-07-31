from materials import nums, nums2, languages
from random import randrange

def summa(array):
    ''' Quick sort algorithm
        Calculating the sum of an array 
    '''
    if len(array) == 1:
        return array[0]
    else:
        return array.pop() + summa(array)
        
# print(summa(nums))

def quicksort(array):
    '''
        Sorting algorithm
    '''
    if len(array) < 2:
        return array
    else:
        pivot = array.pop(randrange(len(array)))
        # pivot = array.pop(0)
        small = [ i for i in array if i<= pivot ]
        big = [i for i in array if i > pivot]
        print(f"{small} + [{pivot}] + {big}")
        return quicksort(small) + [pivot] + quicksort(big)

# print(quicksort(nums))
# print(quicksort(nums2))

def wordsort(array):
    ''' Algorithm which sorts array by the length of object in array '''
    if len(array) < 2:
        return array
    else: 
        pivot = array.pop(randrange(len(array)))
        small = [i for i in array if len(i) <= len(pivot)]
        big = [i for i in array if len(i) > len(pivot)]
        print(f"{small} + [{pivot}] + {big}")
        return wordsort(small) + [pivot] + wordsort(big)
    
# print(wordsort(languages))
