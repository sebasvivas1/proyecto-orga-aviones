from Node import *
import functions 

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
        filled = False 
        current = self.head
        while current is not None:
            if not current.checkIfFull():
                current.updateData(newAirplane)
                filled = True 
            current = current.next
        return filled
                
        
    def find_airplane(self, value):
        current = self.head
        while current is not None:
            if current.data[0] is not None:
                if current.data[0].serial == value:
                    return current.data[0].getAirplaneInfo()
            elif current.data[1] is not None:
                if current.data[1].serial == value:
                    return current.data[1].getAirplaneInfo()
            current = current.next
        return print('\nEl avión no fue localizado en la base de datos')

    def find_pilot(self, captain):
        current = self.head
        while current is not None:
            if current.data[0] is not None:
                if current.data[0].pilot == captain:
                    return True
            elif current.data[1] is not None:
                if current.data[1].pilot == captain:
                    return True
            current = current.next
        return False

    def assign_pilot(self, value, pilot):
        registrado = False 
        current = self.head
        while current is not None:
            if current.data[0] is not None:
                if current.data[0].serial == value:
                    if current.data[0].pilot == "":
                        current.data[0].pilot = pilot
                        registrado = True
                    else:
                        print('\nEste avión ya tiene un piloto asignado, deberá liberarlo primero para asignarle un nuevo piloto')
            elif current.data[1] is not None:
                if current.data[1].serial == value:
                    if current.data[1].pilot == "":
                        current.data[1].pilot = pilot
                        registrado = True
                    else:
                        print('\nEste avión ya tiene un piloto asignado, deberá liberarlo primero para asignarle un nuevo piloto')
            current = current.next
        if registrado:
            print("Operación exitosa")

    def delete_pilot(self, value):
        current = self.head
        while current is not None:
            if current.data[0].serial == value:
                current.data[0].pilot = ""
            elif current.data[1].serial == value:
                current.data[1].pilot = ""
            current = current.next

    def add(self, data, listaModelo, listaNombre):
        dictModelo = {}
        dictNombre = {}
        contador = 0

        if self.size == 7:
            current = self.head
            while current is not None:
                if current.checkIfFull():
                    contador += 1
                current = current.next 

        if contador == 7:
            print("\nLa lista está llena")
            return listaModelo, listaNombre

        else:

            if self.check_if_has_space(data):
 
                dictModelo["model"] = data.model
                dictModelo["serial"] = data.serial
                dictModelCopy = dictModelo.copy()

                dictNombre["name"] = data.name
                dictNombre["serial"] = data.serial
                dictNombreCopy = dictNombre.copy()
                listaModelo.append(dictModelCopy)
                listaNombre.append(dictNombreCopy)
                
                listaModelo.sort(key=lambda item: item.get("model"))
                listaNombre.sort(key=lambda item: item.get("name")) 

                return listaModelo, listaNombre

            else:  
                newNode = Node()
                newNode.updateData(data)
                if self.head is None:
                    self.head = newNode
                    self.tail = self.head
                    self.size = self.size + 1
                else:
                    newNode.previous = self.tail
                    self.tail.next = newNode
                    self.tail = newNode
                    self.size = self.size + 1

                dictModelo["model"] = data.model
                dictModelo["serial"] = data.serial
                dictModelCopy = dictModelo.copy()

                dictNombre["name"] = data.name
                dictNombre["serial"] = data.serial
                dictNombreCopy = dictNombre.copy()
                listaModelo.append(dictModelCopy)
                listaNombre.append(dictNombreCopy)

                listaModelo.sort(key=lambda item: item.get("model"))
                listaNombre.sort(key=lambda item: item.get("name")) 

                return listaModelo, listaNombre

    def delete2(self, serial, airplane_model, airplane_name):
        current = self.head

        # Verificar si la lista es vacía
        if self.head is None:
            print("\nLa lista esta vacia.")

        # Borrar información de la cabeza o la misma cabeza
        elif self.head.next is None:
            if self.head.data[0] is not None:
                if self.head.data[0].serial == serial:
                    self.head.data[0] = None
                    print("\nAvion Eliminado")
                    if self.head.checkIfEmpty():
                        self.head = None
                        self.size = self.size -1
                        print("\nUn grupo secundario fue vaciado")
                    return serial
                    
            elif self.head.data[1] is not None:
                if self.head.data[1].serial == serial:
                    self.head.data[1] = None
                    print("\nAvion Eliminado")
                    if self.head.checkIfEmpty():
                        self.head = None
                        self.size = self.size -1
                        print("\nUn grupo secundario fue vaciado")
                    return serial              
        
        if self.head.data[0] is not None:
            if self.head.data[0].serial == serial:
                self.head.data[0] = None
                print("\nAvion Eliminado")
                if self.head.checkIfEmpty():
                    self.head = self.head.next
                    self.head.previous = None
                    self.size += -1
                    print("\nUn grupo secundario fue vaciado")
                return serial

        elif self.head.data[1] is not None:
            if self.head.data[1].serial == serial:
                self.head.data[1] = None
                print("\nAvion Eliminado")
                if self.head.checkIfEmpty():
                    self.head = self.head.next
                    self.head.previous = None
                    self.size += -1
                    print("\nUn grupo secundario fue vaciado")
                return serial 
        
        while current.next is not None:
            if current.data[0] is not None:
                if current.data[0] == serial:
                    break
            elif current.data[1] is not None:
                if current.data[1] == serial:
                    break
            current = current.next

        if current.next is not None:
            if current.data[0] is not None:
                if current.data[0].serial == serial:
                    current.data[0] = None
                    print("\nAvion Eliminado")
                    if current.checkIfEmpty():
                        current.previous.next = current.next
                        current.next.previous = current.previous
                        self.size += -1
                        print("\nUn grupo secundario fue vaciado")
                    return serial 
        
            elif current.data[1] is not None:
                if current.data[1].serial == serial:
                    current.data[1] = None
                    print("\nAvion Eliminado")
                    if current.checkIfEmpty():
                        current.previous.next = current.next
                        current.next.previous = current.previous
                        self.size += -1
                        print("\nUn grupo secundario fue vaciado")
                    return serial 
        else:
            if current.data[0] is not None:
                if current.data[0].serial == serial:
                    current.data[0] = None
                    print("\nAvion Eliminado")
                    if current.checkIfEmpty():
                        current.previous.next = None
                        self.size += -1
                        print("\nUn grupo secundario fue vaciado")
                    return serial 
        
            elif current.data[1] is not None:
                if current.data[1].serial == serial:
                    current.data[1] = None
                    print("\nAvion Eliminado")
                    if current.checkIfEmpty():
                        current.previous.next = None
                        self.size += -1
                        print("\nUn grupo secundario fue vaciado")
                    return serial 
            else:
                print("\nEl avión no fue localizado en la Base de Datos")

    def display(self):
        current = self.head
        if(self.head == None):
            print('\nNo hay aviones registrados')
            return
        while(current != None):
            if current.data[0] is not None:
                current.data[0].getAirplaneInfo()
            if current.data[1] is not None:
                current.data[1].getAirplaneInfo()
            current = current.next