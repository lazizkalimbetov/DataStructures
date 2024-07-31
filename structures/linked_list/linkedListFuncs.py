'''

Linked lists functions
author: Laziz Kalimbetov

'''

class Node:
    ''' Each element of the Node '''
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    ''' List creating '''
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def addstart(self, new_data):
        ''' Adding new object to list (0 index) '''

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def addAfter(self, prev_node, new_data):
        ''' Adding node after some node '''

        if prev_node == None:
            print("Node not found")
            return
        
        new_node = Node(new_data)       
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def addend(self, new_data):
        ''' Adding node in the end of list '''
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node    
            return 
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        ''' Deleting object from list '''

        temp = self.head
        if (temp and temp.data == key):
            self.head = temp.next
            temp = None
            return 
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return f"{key} not found"
        
        prev.next = temp.next
        temp = None

    
        
