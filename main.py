from Airplane import *
import functions
from LinkedList import *
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

airplane_name = [
]

airplane_model = [
]


from HashTable import HashTable

hashTable = HashTable()
LinkedList = LinkedList()

def main():
    pilot = ""
    searchSerial = ""
    name = ""
    model = ""
    hash = 0
    searchSerial = ""

    print(hashTable.getArray())

    loop = True
    while loop:
        print("\nBienvenido a la aerolinea de Aviones de Occidente Aviocc!\n")
        num_funcion = functions.numeros()

        # Ingresar un nuevo avion
        if num_funcion==1:
            modelo  = functions.model_name()
            name = functions.plane_name()
            serial = functions.validacion_serial()
            avion = Airplane(serial,modelo,name,pilot)
            hash = hashTable.makeHash(serial)
            hashTable.add(hash,avion, airplane_model,airplane_name)
            print(hashTable.getArray()[hash].head.data[0].name)
            print(airplane_name)
            print(airplane_model)
        
        # Buscar un Avion
        elif num_funcion==2:
            searchtype = int(input('Desea buscar por Nombre del Avion (1), por Modelo del Avion (2) o por Serial del Avion (3)? \n ==>'))

            # Buscar Avion por Nombre
            if searchtype == 1:
                functions.sortNameList(airplane_name)
                airplaneName = input('Introduzca el Nombre del Avion. \n ==> ')
                searchSerial = functions.binary_search_name_model(airplane_name, airplaneName, "name")
                print(searchSerial)
                hash = hashTable.makeHash(searchSerial)
                hashTable.getArray()[hash].find_airplane(searchSerial)
                
            # Buscar Avion por Modelo
            elif searchtype == 2:
                functions.sortModelList(airplane_model)
                airplaneModel = input('Introduzca el Modelo del Avion \n ==> ')
                searchSerial = functions.binary_search_name_model(airplane_model, airplaneModel, "model")
                hash = hashTable.makeHash(searchSerial)
                hashTable.getArray()[hash].find_airplane(searchSerial)
            
            # Buscar Avion por Serial
            elif searchtype ==3:
                pass
            else:
                print('Opcion invalida.')

        # Asignar Piloto a un Avion
        elif num_funcion==3:
            searchtype = int(input("Como desea elegir el avion? Por Nombre del Avion (1), por Modelo del Avion (2), por Serial del Avion (3)\n ==> "))

            # Asignar Piloto por Nombre del Avion
            if searchtype == 1:
                functions.sortNameList(airplane_name)
                pilot = functions.pilot_name()
                # Check if pilot is already in a plane.
                #  .....
                airplaneName = input('Introduzca el Nombre del Avion. \n ==> ')
                searchSerial = functions.binary_search_name_model(airplane_name, airplaneName, "name")
                hash = hashTable.makeHash(searchSerial)
                hashTable.getArray()[hash].assign_pilot(searchSerial, pilot)
                hashTable.getArray()[hash].find_airplane(searchSerial)

            # Asignar Piloto por Modelo del avion
            elif searchtype == 2:
                functions.sortModelList(airplane_model)
                pilot = functions.pilot_name()
                # Check if pilot is already in a plane.
                #  .....
                airplaneModel = input('Introduzca el Modelo del Avion. \n ==> ')
                searchSerial = functions.binary_search_name_model(airplane_model, airplaneModel, "model")
                hash = hashTable.makeHash(searchSerial)
                hashTable.getArray()[hash].assign_pilot(searchSerial, pilot)
                hashTable.getArray()[hash].find_airplane(searchSerial)


            # Asignar Piloto por Serial del Avion
            elif searchtype == 3: 
                # Asigancion de piloto buscando el avion por el serial.
                pass
            else:
                print("Invalid Option.")

        # Vaciar Piloto
        elif num_funcion==4:

            searchtype = int(input("Como desea vaciar el avion? Por Nombre del Avion (1), por Modelo del Avion (2)\n ==> "))

            # Vaciar Piloto del Avion por Nombre del Avion
            if searchtype == 1:
                functions.sortNameList(airplane_name)
                # Check if pilot is already in a plane.
                #  .....
                airplaneName = input('Introduzca el Nombre del Avion. \n ==> ')
                searchSerial = functions.binary_search_name_model(airplane_name, airplaneName, "name")
                hash = hashTable.makeHash(searchSerial)
                hashTable.getArray()[hash].delete_pilot(searchSerial)
                hashTable.getArray()[hash].find_airplane(searchSerial)
            
            # Vaciar Piloto del Avion por Modelo del Avion
            elif searchtype == 2:
                functions.sortModelList(airplane_model)
                # Check if pilot is already in a plane.
                #  .....
                airplaneModel = input('Introduzca el Modelo del Avion. \n ==> ')
                searchSerial = functions.binary_search_name_model(airplane_model, airplaneModel, "model")
                hash = hashTable.makeHash(searchSerial)
                hashTable.getArray()[hash].delete_pilot(searchSerial)
                hashTable.getArray()[hash].find_airplane(searchSerial)
            
            else:
                print("Invalid Option")

        # Eliminar Avion
        elif num_funcion==5:

            searchtype = int(input("Como desea eliminar el avion? Por Nombre del Avion (1), por Modelo del Avion (2)\n ==> "))

            # Eliminar por nombre del avion
            if searchtype == 1:
                functions.sortNameList(airplane_name)

                airplaneName = input('Introduzca el Nombre del Avion. \n ==> ')
                searchSerial = functions.binary_search_name_model(airplane_name, airplaneName, "name")
                hash = hashTable.makeHash(searchSerial)
                hashTable.getArray()[hash].delete2(searchSerial, airplane_model, airplane_name)
                # hashTable.getArray()[hash].find_airplane(searchSerial)
            
            elif searchtype == 2:
                functions.sortModelList(airplane_model)

                airplaneModel = input('Introduzca el Modelo del Avion. \n ==> ')
                searchSerial = functions.binary_search_name_model(airplane_model, airplaneModel, "model")
                hash = hashTable.makeHash(searchSerial)
                hashTable.getArray()[hash].delete2(searchSerial, airplane_model, airplane_name)
                # hashTable.getArray()[hash].find_airplane(searchSerial)
            
            else:
                print("Invalid Option")
        elif num_funcion == 7:
            hashTable.getArray()[hash].display()

        exit = functions.salida()
        if exit==0:
            print("\nHasta pronto!")
            loop = False

main()