class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def printList(self):
        node = self.head
        while node:
            print(node.value, end = " ")
            node = node.next

        print("")

    def append(self, value):
        nodeAppend = Node(value)
        if self.length == 0:
            self.head = self.tail = nodeAppend
        else:
            self.tail.next = nodeAppend
            nodeAppend.prev = self.tail
            self.tail = nodeAppend

        self.length += 1
        return True

    def prepend(self, value):
        nodeAppend = Node(value)
        if self.length == 0:
            self.head = self.tail = nodeAppend
        else:
            nodeAppend.next = self.head
            self.head.prev = nodeAppend
            self.head = nodeAppend   

        self.length += 1 

        return True


    def pop(self):
        if self.length == 0:
            return None
        nodePop = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = nodePop.prev
            self.tail.next = None
            nodePop.prev = None
        self.length -= 1
        return nodePop
        

    def popFirst(self):
        if self.length == 0:
            return None
        nodePop = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = nodePop.next
            nodePop.next = None
            self.head.prev = None

        self.length -= 1
        return nodePop

    def get(self, index):
        if index < 0 or index >= self.length:
            print("Index out of range")
            return None
        if index < self.length/2:
            result = self.head
            for _ in range(index):
                result = result.next
        else:
            result = self.tail
            for _ in range(self.length - index - 1):
                result = result.prev
        
        return result

    def setValue(self, index, value):
        nodeReplace = self.get(index)
        if nodeReplace:
            nodeReplace.value = value
            return True
        return False

    def insert(self,index,value):
        if (index < 0) or (index >= self.length):
            print("index out of range linked list")
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        nodeInsert = Node(value)
        after = self.get(index)
        before = after.prev
        nodeInsert.prev = before
        nodeInsert.next = after

        before.next = nodeInsert
        after.prev = nodeInsert
        
        self.length += 1

        return True

    def removeByIndex(self, index):
        if (index < 0) or (index >= self.length):
            print("index out of range linked list")
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()

        nodeRemove = self.get(index)
        before = nodeRemove.prev
        after = nodeRemove.next

        before.next = after
        after.prev = before

        nodeRemove.next = nodeRemove.prev = None

        self.length -= 1

        return nodeRemove


myList = DoubleLinkedList()
myList.append(2)
myList.append(10)
myList.append(17)
myList.append(34)
myList.append(40)
myList.append(20)
myList.append(30)
myList.append(50)
myList.append(70)


print("-----------------")
myList.printList()
print("Head: ", myList.head.value)
print("Tail: ", myList.tail.value)
print("Length: ", myList.length)
print("-----------------")
print(myList.removeByIndex(1).value)
print(myList.removeByIndex(1).value)


myList.printList()
print("Head: ", myList.head.value)
print("Tail: ", myList.tail.value)
print("Length: ", myList.length)


