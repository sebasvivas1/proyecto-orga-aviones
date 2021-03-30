from Airplane import *
from HashTable import *

hashTable = HashTable()

def main():

    hashTable.addNewAirplane("B1239808", "El Coloso", "Boeing 746")
    print(hashTable.makeHash("B1239808"))

    hashTable.addNewAirplane("B1239808", "El Coloso", "Boeing 746")
    print(hashTable.makeHash("B1239808"))

    hashTable.addNewAirplane("B1239288", "El Amigo", "Boeing 747")
    print(hashTable.makeHash("B1239288"))

    hashTable.addNewAirplane("A1982372", "El Junior", "Boeing 748")
    print(hashTable.makeHash("A1982372"))

    hashTable.addNewAirplane("A1982372", "El Junior", "Boeing 748")
    print(hashTable.makeHash("A1982372"))

    hashTable.addNewAirplane("A9893293", "El Odiosito", "Boeing 748")
    print(hashTable.makeHash("A9893293"))

    hashTable.addNewAirplane("A8572838", "El Fortachon", "Boeing 748")
    print(hashTable.makeHash("A8572838"))

    hashTable.addNewAirplane("A8572838", "El Fortachon", "Boeing 748")
    print(hashTable.makeHash("A8572838"))

    hashTable.addNewAirplane("C1872348", "El Crack", "Boeing 748")
    print(hashTable.makeHash("C1872348"))

    hashTable.addNewAirplane("Z9876543", "El Gafo", "Boeing 748")
    print(hashTable.makeHash("Z9876543"))

    hashTable.printArray()

main()