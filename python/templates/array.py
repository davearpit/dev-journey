class Array:
    def __init__(self, size):
        self.array = []
        self.size = size

    def insert(self, value, position = -1):
        if len(self.array) + 1 == self.size or (position > 0 and position <= self.size):
            return 'array is full'

        if position == -1:
            self.array.append(value) 
        else:
            self.array[position - 1] = value

        return

    def delete(self, position = -1):
        if len(self.array) == 0 or (position > 0 and position <= self.size):
            return 'position beyond bounds'
        
        if position == -1:
            self.array.remove(self.array[-1])
        else:
            self.array.pop(position - 1)

        return
    
    def search(self, value):
        for pos, el in enumerate(self.array):
            if el == value:
                return pos
            
        return None
    
    def sort(self):
        length = len(self.array)
        for pos_1 in range(0, length):
            sorted = length - pos_1
            for pos_2 in range(0, sorted):
                if pos_2 + 1 == sorted:
                    continue
                if self.array[pos_2] > self.array[pos_2 + 1]:
                    temp = self.array[pos_2]
                    self.array[pos_2] = self.array[pos_2 + 1]
                    self.array[pos_2 + 1] = temp
        
        return self.array
    
    def __repr__(self):
        return repr(self.array)