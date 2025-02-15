from materials import numbers

def selection_sort(list):
    
    ''' Sorting algorithm '''

    for i in range(len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j

        list[i], list[min_index] = list[min_index], list[i]

    return list
print(selection_sort(numbers))

