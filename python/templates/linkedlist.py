class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        return

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        
        last = self.head
        while last.next != None:
            last = last.next
        
        last.next = newNode
        return
    
    def deleteAtBeginning(self):
        second = self.head.next
        self.head = second
        return

    def deleteAtEnd(self):
        prev = None
        last = self.head
        while last.next != None:
            prev = last
            last = last.next

        prev.next = None
        return

    def __repr__(self):
        temp = self.head
        while temp.next != None:
            print(temp.data, end = ' -> ')
            temp = temp.next
        print(temp.data, end = '\n')
        return