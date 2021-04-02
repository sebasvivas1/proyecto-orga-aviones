class Node:
    def __init__(self):
        self.data = [None for i in range(2)]
        self.next = None
        self.previous = None
        self.isFull = False
        self.isEmpty = True 
    
    def updateData(self, airplane):
        if self.data[0] == None:
            self.data[0] = airplane
        elif self.data[1] == None:
            self.data[1] = airplane
        
    def deleteData(self,target):
        if self.data[0].serial == target:
            self.data[0] = None
        elif self.data[1].serial == target:
            self.data[1] = None
        
    def checkIfFull(self):
        if self.data[0]!= None and self.data[1] != None:
            self.isFull = True 
            return self.isFull
        
    def checkIfEmpty(self):
        if self.data[0]!=None or self.data!=None:
            self.isEmpty = False 
            return self.isEmpty