class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self,key):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 23 ) % len(self.data_map)
        return myHash
    
    def printTable(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def setItem(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    
    def getItem(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:   
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1] 
        else:
            return None

    def keys(self):
        listKey = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    listKey.append(self.data_map[i][j][0])
        return listKey
myHashTable = HashTable()
myHashTable.setItem("Tung",24)
myHashTable.setItem("Thuong",123)
myHashTable.setItem("Thuy",49)
myHashTable.printTable()

print(myHashTable.getItem("Tung"))
print(myHashTable.keys())



    