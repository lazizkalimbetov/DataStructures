from collections import deque
from materials import graph

def breadth_first_search(start_node, target='elon musk'):
    ''' Breadth-first search algorithm with Graph data structure '''
    search_queue = deque()
    search_queue += graph[start_node]
    searched = set()
    count = 0

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == target:
                print(f"{person} is found! {count}")
                return True
            else:
                count += 1
                search_queue += graph[person]
                searched.add(person)
    return False

print(breadth_first_search('you', 'elon musk'))


