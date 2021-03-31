
"""def main():
    
    print("\n¡Bienvenido a la Base de Datos de Aviocc Airlines!")

    while True: 

        while True:
            try:
                user_choice = int(input("\n¿Qué operación desea efectuar?  \n1. Insertar Avión \n2. Buscar Avión \n3. Asignar Piloto a un Avión \n4. Liberar Avión \n5. Eliminar Avión de la Flota \n6. Salir \n>>>  "))
                if user_choice not in range(7):
                    raise ValueError
                break
            except ValueError:
                print("\nERROR: Dato ingresado no forma parte de las opciones dadas")

        if user_choice==1:
            pass

        elif user_choice==2:

            while True: 

                while True:
                    try:
                        search_choice = int(input("\n¿Cómo desea realizar la búsqueda? \n1. Por Serial \n2. Por Modelo \n3. Por Nombre \n>>>  "))
                        if search_choice not in range(4):
                            raise ValueError
                        break
                    except ValueError:
                        print("\nERROR: Dato ingresado no forma parte de las opciones dadas")

                if search_choice==1:
                    print("Serial")
                    break

                elif search_choice==2:
                    print("Modelo")
                    break

                elif search_choice==3:
                    print("Nombre")
                    break

        elif user_choice==3:
            pass

        elif user_choice==4:
            pass

        elif user_choice==5:
            pass

        elif user_choice==6:
            print("\n¡Hasta luego!")
            break 

if __name__ == "__main__":
    main()
    """

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

