from Airplane import *
from LinkedList import *
class HashTable:
    def __init__(self):

        #self.avionesIsFull = False
        self.maxSize = 3
        self.linked_list_0 = LinkedList()
        self.linked_list_1 = LinkedList()
        self.linked_list_2 = LinkedList()
        self.arr = [self.linked_list_0, self.linked_list_1, self.linked_list_2]
        # self.arr = [self.linked_list_0, self.linked_list_1, self.linked_list_2]

    def getArray(self):
        return self.arr

    def setArray(self, arr):
        self.arr = arr

    def makeHash(self,key):
        hashVal = 0
        p = 53
        p_pow = 1

        for char in key:
            hashVal = (hashVal + (ord(char)) * p_pow) % self.maxSize
            p_pow = (p_pow * p) % self.maxSize
        return hashVal

    def add(self,key,avion,listaModelo,listaNombre):
        self.arr[key].add(avion,listaModelo,listaNombre)
    
    def showArray(self):
        for i in range(3):
            print()
            print(f" Estamos en la posicion: {i}")
            self.arr[i].display()

    def get(self,key):
        h = self.makeHash(key)
        return self.arr[h]

    def search_for_captain(self, captain):
        for i in range(self.maxSize):
            if self.arr[i].find_pilot(captain):
                return True
        return False 




