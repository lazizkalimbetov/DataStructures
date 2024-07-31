from materials import languages

def linear_search(list, item):
    '''
        BIG O = len(list)

        args: list, item
    '''
    for n in range(len(list)):
        if list[n] == item:
            return n
        return f"{item} not found"
    
result = linear_search(languages, 'mandarin')
print(result)

