from Airplane import *
import functions
from HashTable import HashTable
import pickle 

def main():

    hashTable = HashTable()

    # Creacion de lista de diccionarios 
    airplane_name = []
    airplane_model = [] 
    pilot = ""             

    if functions.file_existence('hashTable.txt'):
        with open('hashTable.txt', 'rb') as f:
            hashTable.setArray(pickle.load(f))      
    
    if functions.file_existence('airplaneModel.txt'):
        with open('airplaneModel.txt', 'rb') as f:
            airplane_model = pickle.load(f)

    if functions.file_existence('airplaneName.txt'):
        with open('airplaneName.txt', 'rb') as f:
            airplane_name = pickle.load(f)

    print("\n¡Bienvenido a la Aerolinea de Aviones de Occidente Aviocc!\n")
    
    loop = True
    while loop:
        
        num_funcion = functions.numeros()

        # Ingresar un nuevo avion
        if num_funcion==1:
            serial = functions.validacion_serial()
            while functions.check_if_exists(airplane_name, serial,  "serial"):
                print("\nEl serial previamente insertado ya existe en la base de datos, intentelo de nuevo")
                serial = functions.validacion_serial()

            modelo  = functions.model_name()
            while functions.check_if_exists(airplane_model, modelo,  "model"):
                print("\nEl modelo previamente insertado ya existe en la base de datos, intentelo de nuevo")
                modelo  = functions.model_name()

            name = functions.plane_name()
            while functions.check_if_exists(airplane_name, name,  "name"):
                print("\nEl nombre previamente insertado ya existe en la base de datos, intentelo de nuevo")
                name = functions.plane_name()

            avion = Airplane(serial,modelo,name,pilot)
            hash = hashTable.makeHash(serial)
            hashTable.add(hash,avion, airplane_model,airplane_name)
            # Borrar
            print(airplane_name)
            print(airplane_model)


        
        # Buscar un Avion
        elif num_funcion==2:
        # if hashTable.checkIfEmpty() == False:
            while True:
                try:
                    searchtype = int(input("""
Desea buscar por:

1. Nombre del Avion
2. Modelo del Avion 
3. Serial del Avion 
>>> """))
                    break 
                except ValueError:
                    print("\nERROR: Debe ingresar un número")
                    
            # Buscar Avion por Nombre
            if searchtype == 1:

                airplaneName = functions.plane_name()
                searchSerial = functions.binary_search_name_model(airplane_name, airplaneName, "name")
                # print(searchSerial)
                if searchSerial == "":
                    print('\nEl Avion no existe')
                else:
                    hash = hashTable.makeHash(searchSerial)
                    hashTable.getArray()[hash].find_airplane(searchSerial)
                
            # Buscar Avion por Modelo
            elif searchtype == 2:

                airplaneModel = functions.model_name()
                searchSerial = functions.binary_search_name_model(airplane_model, airplaneModel, "model")
                if searchSerial == "":
                    print('\nEl Avion no existe')
                else:
                    hash = hashTable.makeHash(searchSerial)
                    hashTable.getArray()[hash].find_airplane(searchSerial)
            
            # Buscar Avion por Serial
            elif searchtype ==3:
                airplaneSerial = functions.validacion_serial()
                hash = hashTable.makeHash(airplaneSerial)
                hashTable.getArray()[hash].find_airplane(airplaneSerial)
            else:
                print('\nOpcion invalida')
            

        # Asignar Piloto a un Avion
        elif num_funcion==3:
            while True:
                try:
                    searchtype = int(input("""
¿Cómo desea elegir el avion para asignarle el piloto? 
  1. Por Nombre del Avion
  2. Por Modelo del Avion 
  3. Por Serial del Avion
  >>> """))
                    break 
                except ValueError:
                    print("\nERROR: Debe ingresar un numero")

            # Asignar Piloto por Nombre del Avion
            if searchtype == 1:

                pilot = functions.pilot_name() 
                while hashTable.search_for_captain(pilot):
                    print("\nEl nombre del piloto previamente insertado ya tiene un avión asignado, ingrese otro nombre, por favor.")
                    pilot = functions.pilot_name()
                    
                airplaneName = functions.plane_name()
                searchSerial = functions.binary_search_name_model(airplane_name, airplaneName, "name")
                if searchSerial == "":
                    print('\nEl Avion no existe')
                else:
                    hash = hashTable.makeHash(searchSerial)
                    hashTable.getArray()[hash].assign_pilot(searchSerial, pilot)
                    hashTable.getArray()[hash].find_airplane(searchSerial)

            # Asignar Piloto por Modelo del avion
            elif searchtype == 2:

                pilot = functions.pilot_name() 
                while hashTable.search_for_captain(pilot):
                    print("\nEl nombre del piloto previamente insertado ya tiene un avión asignado, ingrese otro nombre, por favor.")
                    pilot = functions.pilot_name()

                airplaneModel = functions.model_name()
                searchSerial = functions.binary_search_name_model(airplane_model, airplaneModel, "model")
                if searchSerial == "":
                    print('\nEl Avion no existe')
                else:
                    hash = hashTable.makeHash(searchSerial)
                    hashTable.getArray()[hash].assign_pilot(searchSerial, pilot)
                    hashTable.getArray()[hash].find_airplane(searchSerial)

            # Asignar Piloto por Serial del Avion
            elif searchtype == 3: 

                pilot = functions.pilot_name() 
                while hashTable.search_for_captain(pilot):
                    print("\nEl nombre del piloto previamente insertado ya tiene un avión asignado, ingrese otro nombre, por favor.")
                    pilot = functions.pilot_name()

                airplaneSerial = functions.validacion_serial()
                hash = hashTable.makeHash(airplaneSerial)
                hashTable.getArray()[hash].assign_pilot(airplaneSerial, pilot)
                hashTable.getArray()[hash].find_airplane(airplaneSerial)

            else:
                print("\nOpción invalida")

        # Vaciar Piloto
        elif num_funcion==4:

            while True:
                try: 
                    searchtype = int(input("""
¿Cómo desea vacíar el avion? 
  1. Por Nombre del Avion
  2. Por Modelo del Avion 
  3. Por Serial del Avion
  >>> """))
                    break 
                except ValueError:
                    print("\nERROR: Dato ingresado no es numérico")

            # Vaciar Piloto del Avion por Nombre del Avion
            if searchtype == 1:

                airplaneName = functions.plane_name()
                searchSerial = functions.binary_search_name_model(airplane_name, airplaneName, "name")
                if searchSerial == "":
                    print('\nEl Avion no existe')
                else:
                    hash = hashTable.makeHash(searchSerial)
                    hashTable.getArray()[hash].delete_pilot(searchSerial)
                    hashTable.getArray()[hash].find_airplane(searchSerial)
            
            # Vaciar Piloto del Avion por Modelo del Avion
            elif searchtype == 2:

                airplaneModel = functions.model_name()
                searchSerial = functions.binary_search_name_model(airplane_model, airplaneModel, "model")
                if searchSerial == "":
                    print('El Avion no existe')
                else:     
                    hash = hashTable.makeHash(searchSerial)
                    hashTable.getArray()[hash].delete_pilot(searchSerial)
                    hashTable.getArray()[hash].find_airplane(searchSerial)
            
            # Vaciar Piloto del Avion por Serial del Avion
            elif searchtype == 3:

                airplaneSerial = functions.validacion_serial()
                if searchSerial == "":
                    print('El Avion no existe')
                else:
                    hash = hashTable.makeHash(airplaneSerial)
                    hashTable.getArray()[hash].delete_pilot(searchSerial)
                    hashTable.getArray()[hash].find_airplane(searchSerial)
            
            else:
                print("\nOpción invalida")

        # Eliminar Avion
        elif num_funcion==5:
            while True:
                try:
                    searchtype = int(input("""
¿Cómo desea eliminar el avion de la flota? 
1. Por Nombre del Avion
2. Por Modelo del Avion 
3. Por Serial del Avion
>>> """))
                    break 
                except ValueError:
                    print("\nERROR: Dato ingresado no es numérico")

            # Eliminar por nombre del avion
            if searchtype == 1:

                airplaneName = functions.plane_name()

                searchSerial = functions.binary_search_name_model(airplane_name, airplaneName, "name")
                if searchSerial == "":
                    print('El Avion no existe')
                else:
                    hash = hashTable.makeHash(searchSerial)
                    ser = hashTable.getArray()[hash].delete2(searchSerial, airplane_model, airplane_name)
                    airplane_name = [x for x in airplane_name if not(x["serial"] == ser)]
                    airplane_model = [x for x in airplane_model if not(x["serial"] == ser)]


                # hashTable.getArray()[hash].find_airplane(searchSerial)
            
            # Eliminar por Modelo del avion
            elif searchtype == 2:

                airplaneModel = functions.model_name()

                searchSerial = functions.binary_search_name_model(airplane_model, airplaneModel, "model")
                if searchSerial == "":
                    print('El Avion no existe')
                else:
                    hash = hashTable.makeHash(searchSerial)
                    ser = hashTable.getArray()[hash].delete2(searchSerial, airplane_model, airplane_name)
                    airplane_model = [x for x in airplane_model if not(x["serial"] == ser)]
                    airplane_name = [x for x in airplane_name if not(x["serial"] == ser)]


                # hashTable.getArray()[hash].find_airplane(searchSerial)
            
            # Eliminar por Serial del avion
            elif searchtype == 3: 

                airplaneSerial = functions.validacion_serial()
                hash = hashTable.makeHash(airplaneSerial)

                ser = hashTable.getArray()[hash].delete2(airplaneSerial, airplane_model, airplane_name)
                airplane_model = [x for x in airplane_model if not(x["serial"] == ser)]
                airplane_name = [x for x in airplane_name if not(x["serial"] == ser)]

            else:
                print("\nOpción inválida")

        elif num_funcion == 6:
            hashTable.showArray()

        exit = functions.salida()

        if exit==2:
            # Almacenar datos en el disco duro 
            with open('hashTable.txt', 'wb') as file:
                pickle.dump(hashTable.getArray(), file)
            with open('airplaneModel.txt', 'wb') as file:
                pickle.dump(airplane_model, file)
            with open('airplaneName.txt', 'wb') as file:
                pickle.dump(airplane_name, file)

            print("\n¡Hasta pronto!")
            loop = False

main()