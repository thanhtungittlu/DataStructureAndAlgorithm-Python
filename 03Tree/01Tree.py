class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def __r_contains(self, currentNode, value):
        if currentNode == None:
            return False
        if currentNode.value == value:
            return True
        if value < currentNode.value:
            return self.__r_contains(currentNode.left, value)
        if value > currentNode.value:
            return self.__r_contains(currentNode.right, value)
    
    def _r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_insert(self,currentNode, value):
        if currentNode == None:
            return Node(value)
        if value < currentNode.value:
            currentNode.left =  self.__r_insert(currentNode.left, value)
        if value > currentNode.value:
            currentNode.right = self.__r_insert(currentNode.right, value)
        return currentNode
    def _r_insert(self,value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)


    
my_tree = BinarySearchTree()
my_tree._r_insert(47)
my_tree._r_insert(21)
my_tree._r_insert(76)
my_tree._r_insert(18)
my_tree._r_insert(27)
my_tree._r_insert(52)
my_tree._r_insert(82)

print('BST Contains 27:')
print(my_tree._r_contains(27))


print('\nBST Contains 17:')
print(my_tree._r_contains(17))
                


