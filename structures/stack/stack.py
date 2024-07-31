
class Stack:
    '''
    Stack list
    '''
    def __init__(self):
        self.stack = []

    def __str__(self):
        return self.stack

    def isEmpty(self):
        ''' Checking if stack is empty '''
        return (len(self.stack)) == 0
    
    def push(self, data):
        ''' Adding a new element '''
        self.stack.append(data)
        return data
    
    def pop(self):
        ''' Popping the first element '''
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()
        
    def peek(self):
        ''' Peeking to the first element '''
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]
    