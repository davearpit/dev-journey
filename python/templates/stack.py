class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, el):
        if len(self.stack) >= self.size:
            return 'Stack is full'
        
        self.stack.append(el)
        return self.stack
    
    def pop(self):
        if len(self.stack) == 0:
            return 'Stack is empty'
        
        el = self.stack.remove(-1)
        return el
    
    def peek(self):
        if len(self.stack) == 0:
            return 'Stack is empty'
        
        return self.stack[-1]
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def isFull(self):
        if len(self.stack) == self.size:
            return True
        return False