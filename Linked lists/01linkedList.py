class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def makeEmpty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def printList(self):
        node = self.head
        while node is not None:
            print(node.value, end=" ")  
            node = node.next
        print()

    def append(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
        else:
            self.tail.next = newNode

        self.tail = newNode
        self.length += 1

        return True

    def prepend(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        
        while (temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp

    def popFirst(self):
        if self.length == 0:
            return None
        nodePop = self.head
        self.head = self.head.next
        nodePop.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        
        return nodePop

    def get(self, index):
        if (index < 0) or (index >= self.length):
            print("index out of range linked list")
            return None
        resulNode = self.head 
        
        for _ in range(index):
            resulNode = resulNode.next
       
        return resulNode

    def setValueByIndex(self, index, value):
        nodeNew = self.get(index)
        if nodeNew:
            nodeNew.value = value
            return True
        return False


    def insert(self, index, value):
        
        if (index < 0) or (index >= self.length):
            print("index out of range linked list")
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        
        nodeInsert = Node(value)
        oldNodeBefore = self.get(index-1)
        nodeInsert.next = oldNodeBefore.next
        oldNodeBefore.next = nodeInsert
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

        nodeBefore = self.get(index - 1)
        nodeRemove = nodeBefore.next

        nodeBefore.next = nodeRemove.next
        nodeRemove.next = None

        self.length -= 1

        return nodeRemove


    def reverse(self):
        node = self.head
        self.head = self.tail      
        self.tail = node

        before = None
        for _ in range(self.length):
            after = node.next
            node.next = before
            before = node
            node = after
        

        
        

myLinkedList = LinkedList()
myLinkedList.append(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)



print("-----")
myLinkedList.printList()
print("Head: ", myLinkedList.head.value)
print("Tail: ", myLinkedList.tail.value)
print("Leng: ", myLinkedList.length)
print("-----")
myLinkedList.removeByIndex(4)
myLinkedList.printList()
print("-----")
print("Head: ", myLinkedList.head.value)
print("Tail: ", myLinkedList.tail.value)
print("Leng: ", myLinkedList.length)






                                                                                                                    