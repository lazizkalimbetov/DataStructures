from random import randint

# materials for binary search algorithm
clients = {1: 'Michael',
           2: 'Jordan',
           3: 'Jennifer',
           4: 'Lopez',
           5: 'Hoshimjon'}

# materials  for linear search algorithm
languages = ['english', 'spanish', 'german', 'russian']

# materials for selection sort algorithm
numbers = [89, 67, 84, 2, 3 ]

# materials for recursion algorithm
actors = ['Charlie', 'Chaplin', 'Merylin', 'Monro']
singers = ['Taylor', 'Swift', 'Kendrick', 'Lamar']
scientists = ['Albert', 'Einstein', 'Louie', 'Paster']
authors = ['Erich', 'Remark', 'Fridrich', 'Nitsche', 'Fyodor', 'Dostoyevsky']

people = [actors, singers, scientists, authors]

# materials for quick sort algorithm
nums = [1,2,3,4,5,6,7,8,9,10]
nums2 = [45, 67, 34, 65, 24, 43, 15, 78, 1, 87]

languages = ['c', 'python', 'js', 'kotlin', 'java', 'ruby', 'flutter']


#  materials for bubble sot algorithm
def generate_nums_array(count,min, max, sorted=False):
    array = list()
    if min > max:
          return "min must be smaller than max"
    else:
        for _ in range(count):
            array.append(randint(min, max))
    if sorted == True:
         array.sort()
    return array
        

# materials for Breadth-first search algorithm
graph = {
        'you': ['ali', 'vali', 'tohir'], 'ali': ['aziza', 'olim'], 'vali': ['botir', 'ziyoda'],
         'tohir': ['elon musk', 'mohir'], 'olim': [], 'aziza': [], 'botir': [], 'ziyoda': ['aziza'],
         'elon musk': [], 'mohir': []
        }


# materials for greedy algorithms

binolar = {
    'B01': {10, 16, 17},
    'B02': {1, 4, 11, 30},
    'B03': {17, 18, 27, 30},
    'B04': {1, 7, 17, 19, 30},
    'B05': {7, 11, 15, 17, 20},
    'B06': {6, 7, 11},
    'B07': {23, 30},
    'B08': {10, 14, 18, 25, 29},
    'B09': {10, 16, 17, 19},
    'B10': {10, 13, 19},
    'B11': {1, 3, 6, 13, 16},
    'B12': {8, 12},
    'B13': {5, 10, 15},
    'B14': {5, 8, 17, 23, 24},
    'B15': {2, 9, 21, 22, 26, 28}
}

