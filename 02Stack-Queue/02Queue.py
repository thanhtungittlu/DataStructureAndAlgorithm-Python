class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        firstNode = Node(value)
        self.first = firstNode
        self.last = firstNode
        self.length = 1

    def printList(self):
        node = self.first
        while node:
            print(node.value, end= " ")
            node = node.next
        print()

    def enqueue(self,value):
        node = Node(value)
        if self.length == 0:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        node = self.first   
        if self.length == 1:
            self.first = self.last = None
        else:    
            self.first = node.next
            node.next = None
        self.length -= 1

        return node


myQueue = Queue(3)
myQueue.enqueue(2)
myQueue.enqueue(1)
myQueue.printList()

print(myQueue.dequeue().value)
print(myQueue.dequeue().value)
print(myQueue.dequeue().value)
myQueue.printList()

print(myQueue.dequeue())

myQueue.printList()