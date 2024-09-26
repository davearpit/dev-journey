class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, value):
        if len(self.queue) + 1 >= self.size:
            return 'Queue is full'
        
        for pos, el in enumerate(self.queue):
            temp = el
            if pos == 0:
                self.queue[pos] = value
            else:
                self.queue[pos] = temp

        return self.queue
        
    def dequeue(self):
        if len(self.queue) == 0:
            return 'Queue is empty'
        
        return_value = None
        for pos, el in enumerate(self.queue):
            if pos == 0:
                return_value = el
            else:
                self.queue[pos - 1] = el

            return return_value
        
    def peek(self):
        if len(self.queue) == 0:
            return 'Queue is empty'
        
        return self.queue[0]
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False
    
    def isFull(self):
        if len(self.queue) == self.size:
            return True
        return False
            