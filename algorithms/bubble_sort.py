from materials import generate_nums_array

array = generate_nums_array(10, 0, 10)
print(array)
def bubble_sort(array: list) -> list:
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)

print(bubble_sort(array))