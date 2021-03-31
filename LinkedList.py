class Node:
    def __init__(self):
        self.data = [None for i in range(2)]
        self.next = None
        self.previous = None
        self.isFull = False
    
    def setData(self, airplane):
        if self.data[0] == None:
            self.data[0] = airplane
        elif self.data[1] == None:
            self.data[1] = airplane
    
    def checkIfFull(self):
        if self.data[0]!= None and self.data[1] != None:
            self.isFull = True 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self. size = 0
    
    def traverse(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add(self, data):
        if self.size < 8:
            "nodeHasSpace(data)
            newNode = Node()
            newNode.setData(data)
            if self.head is None:
                self.head = newNode
                self.tail = self.head
            else:
                newNode.previous = self.tail
                self.tail.next = newNode
                self.tail = newNode
            self.size = self.size + 1
        else:
            print("La lista está llena")

    def delete(self, target):
        if self.head is None:
            raise Exception("No hay elementos en esta lista")
        
        if self.head.data[0] == target or self.head.data[1] == target:
            self.head = self.head.next
            return 

        previousNode = self.head
        for node in self:
            if node.data[0] == target or node.data[1] == target:
                previousNode.next = node.next 
                return 
            previousNode = node

        raise Exception("El nodo con el dato busqueda no fue encontrado") 
