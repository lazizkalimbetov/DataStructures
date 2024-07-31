from materials import people

def count(n):
    print(n)
    if n<=1:
        return
    else:
        count(n-1)

# count(10)

def fact(n):
    print(n, end=' ')
    if n == 1:
        return 1
    else:
        return n * (fact(n-1))

# print(fact(8000))

def look_for_person(name):
    ''' Not recursion '''
    for item in people:
        if isinstance(item, list):
            for value in item:
                if value == name:
                    return f"{value} is found"
        else:
            print(f"{item} is not a list")
    return "404"    
print(look_for_person('Tetcher')) # Output: 404
print(look_for_person('Remark')) #Output: Remark is found

