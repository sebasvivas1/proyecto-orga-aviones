class Node:
    def __init__(self):
        self.data = [None for i in range(2)]
        self.next = None
        self.previous = None
        self.isFull = False
        self.isEmpty = True 
    
    def setData(self, airplane):
        if self.data[0] == None:
            self.data[0] = airplane
        elif self.data[1] == None:
            self.data[1] = airplane
    
    def checkIfFull(self):
        if self.data[0]!= None and self.data[1] != None:
            self.isFull = True 
        return self.isFull
    
    def checkIfEmpty(self):
        if self.data[0]!=None or self.data!=None:
            self.isEmpty = False 
        return self.isEmpty
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.size = 0
    
    def traverse(self):
        node = self.head
        while node:
            itemValue = node.data
            node = node.next
            yield itemValue
    
    def check_if_has_space(self, newAirplane):
        current = self.head
        while current is not None:
            if not current.isFull:
                current.setData(newAirplane)
            current = current.next
    
    def find_airplane(self, value):
        current = self.head
        while current is not None:
            if current.data[0].serial == value:
                current.data[0].getAirplaneInfo()
            elif current.data[1].serial == value:
                current.data[1].getAirplaneInfo()
            current = current.next

            """
            P: ¿Cuando la usaré?
            R: Cuando me solicitan buscar un avión.
            
            P: ¿Cuál es mi parametro?
            R: La serial del avión 

            P: ¿cómo llamar esta función?
            R: arr[h].find_airplane(serial)
            """

    def add(self, data):
        if self.size < 8:
            self.check_if_has_space(data)
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
        
        if self.head.data[0].serial == target or self.head.data[1].serial == target:
            if self.head.checkIfEmpty():
                self.head = self.head.next
            else:
                if self.head.data[0].serial == target:
                    self.head.data[0] = None
                elif self.head.data[1].serial == target:
                    self.head.data[1] = None

        previousNode = self.head
        for node in self:
            if node.data[0] == target or node.data[1] == target:
                previousNode.next = node.next 
                return 
            previousNode = node

        raise Exception("El nodo con el dato busqueda no fue encontrado") 
