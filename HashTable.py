from Airplane import *
from functions import *
from LinkedList import *
class HashTable:
    def __init__(self):
        self.maxSize = 3
        self.linked_list = LinkedList()
        self.arr = [self.linked_list for i in range(self.maxSize)]

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

    def add(self,array,val):
        print(len(array))
        index = -1
        for i in range(len(array)):
            if not checkIfFull(array[i]):
               index = i
               print(index)
               break
            else:
                continue
        return index


    def get(self,key):
        h = self.makeHash(key)
        return self.arr[h]

    def printArray(self):
        print(self.arr)

    def addNewAirplane(self, key, name, model):
        h = self.makeHash(key)
        pilot = ''
        value = [key, name, model, pilot]
        if key in self.arr[0]:
            print('El serial ya esta registrado.')
        else:
            Airplane(key, model, name, pilot)
            newArray = self.arr[h]
            index = self.add(newArray, value)
            """if index != -1:
                if self.arr[h][index][0] == None:
                    self.arr[h][index][0] = value
                else:
                    self.arr[h][index][1] = value"""
            print('Añadido satisfactoriamente.')
            print("\n")

