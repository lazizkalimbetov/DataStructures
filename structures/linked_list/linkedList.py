'''
Linked list objects test
'''

from linkedListFuncs import Node, LinkedList

One = Node('One')
Two = Node('Two')    
Three = Node('Three')

llist = LinkedList()
llist.head = One
# print(llist.head.data)

llist.head.next = Two
# print(llist.head.next.data)

llist.head.next.next = Three
# print(llist.head.next.next.data)

''' Testing functions '''
# # List of nodes
# llist.printlist()

# Add object to the start of list
llist.addstart('Zero')
# print(llist.head.data)

# Adding object after some node
# llist.addAfter(Two, 'Example')
# llist.printlist()

# Adding object in the end of list
llist.addend('Four')
# llist.printlist()

# Deleting object from list
llist.deleteNode('Four')
llist.printlist()


