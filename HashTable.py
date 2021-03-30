from Airplane import *
class HashTable:
    def __init__(self):

        self.maxSize = 3
        self.aviones = [None for i in range(2)]
        self.arrayPrueba = [self.aviones for i in range(8)]
        self.arr = [self.arrayPrueba for i in range(self.maxSize)]

    def makeHash(self,key):
        hashVal = 0
        p = 53
        p_pow = 1

        for char in key:
            hashVal = (hashVal + (ord(char)) * p_pow) % self.maxSize
            p_pow = (p_pow * p) % self.maxSize
        return hashVal

    def add(self,key,val):
        h = self.makeHash(key)
        self.arr[h] = val

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
            self.add(key, value)
            print('Añadido satisfactoriamente.')

