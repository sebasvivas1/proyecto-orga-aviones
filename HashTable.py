from Airplane import *
from functions import *
from LinkedList import *
class HashTable:
    def __init__(self):

        self.avionesIsFull = False
        self.maxSize = 3
        self.linked_list = LinkedList()
        self.arr = [self.linked_list for i in range(self.maxSize)]

    def setAvionesIsFull(self):
        if aviones[0]!= None and aviones!= None:
            self.avionesIsFull = True

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
        print(hashVal)
        return hashVal

    def add(self,key,avion,listaModelo,listaNombre):
        self.arr[key].add(avion,listaModelo,listaNombre)


    def get(self,key):
        h = self.makeHash(key)
        return self.arr[h]

    def printArray(self):
        print(self.arr)


    def delete(self,key):
        h = self.makeHash(key)
        for group in range(len(self.arr[h])):
            if self.arr[h][group] == key:
                print(self.arr[h][group])
                self.arr[h] = None
                break
            else:
                print('no es igual')




