class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        firstNode = Node(value)
        self.top = firstNode
        self.height = 1

    def printList(self):
        node = self.top
        while node:
            print(node.value, end = " ")
            node = node.next
        print()
    
    def push(self,value):
        nodePush = Node(value)
        if self.height == 0:
            self.top = nodePush
        else:
            nodePush.next = self.top
            self.top = nodePush
        self.height += 1

    def pop(self):
        nodePop = self.top
        if self.height == 0:
            return None
        self.top = nodePop.next
        nodePop.next = None
        self.height -= 1
        return nodePop


    
my_stack = Stack(4)
my_stack.push(3)
my_stack.push(1)
print(my_stack.pop().value)
print(my_stack.pop().value)
print(my_stack.pop().value)
print(my_stack.pop())
print(my_stack.pop())



my_stack.printList()


