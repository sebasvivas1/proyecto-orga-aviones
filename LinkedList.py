from Node import *

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
        current = self.head
        while current is not None:
            if not current.isFull:
                current.updateData(newAirplane)
                current = current.next
        
    def find_airplane(self, value):
        current = self.head
        while current is not None:
            if current.data[0] is not None:
                if current.data[0].serial == value:
                    print("Entro aqui")
                    return current.data[0].getAirplaneInfo()
            elif current.data[1] is not None:
                if current.data[1].serial == value:
                    print("Entro aqui tambien")
                    return current.data[1].getAirplaneInfo()
            
            current = current.next
        return print('Not found')

    def assign_pilot(self, value, pilot):
        current = self.head
        while current is not None:
            if current.data[0] is not None:
                if current.data[0].serial == value:
                    current.data[0].pilot = pilot
            if current.data[1] is not None:
                if current.data[1].serial == value:
                    current.data[1].pilot = pilot
            current = current.next

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
        if self.size < 8:
            self.check_if_has_space(data)
            newNode = Node()
            newNode.updateData(data)
            if self.head is None:
                self.head = newNode
                self.tail = self.head
                print('se anadio a la lista enlazada')
            else:
                newNode.previous = self.tail
                self.tail.next = newNode
                self.tail = newNode
                self.size = self.size + 1
                print('ahora se anadio a la lista enlazada')
            dictModelo["model"] = data.model
            dictModelo["serial"] = data.serial
            dictModelCopy = dictModelo.copy()
            
            dictNombre["name"] = data.name
            dictNombre["serial"] = data.serial
            dictNombreCopy = dictNombre.copy()
            
            listaModelo.append(dictModelCopy)
            listaNombre.append(dictNombreCopy)
            return listaModelo, listaNombre
        else:
            print("La lista está llena")


    def delete2(self, serial, airplane_model, airplane_name):
        current = self.head
        if self.head is None:
            print("La lista esta vacia.")
            return

        if self.head.next is None:
            if current.data[0] is not None:
                if current.data[0].serial == serial:
                    self.head.data[0] = None
                    return
                    # result1 = [x for x in airplane_model if not(x["serial"] == serial)]
                    # result2 = [x for x in airplane_name if not(x["serial"] == serial)]
                    # print(f"El avion de serial {serial} fue eliminado exitosamente")
                    # return result1, result2
                    
            elif current.data[1] is not None:
                if current.data[1].serial == serial:
                    self.head.data[1] = None
                    return
                    # result1 = [x for x in airplane_model if not(x["serial"] == serial)]
                    # result2 = [x for x in airplane_name if not(x["serial"] == serial)]
                    # print(f"El avion de serial {serial} fue eliminado exitosamente")
                    # return result1, result2
                    
            else:
                self.head = None
                self.size = self.size -1
                print("Avion no encontrado")
            return
        

        

                









































    # def delete(self, target):
    #     current = self.head
        
    #     if self.head is None:
    #         print("Head is None")
    #         raise Exception("No hay elementos en la lista")

    #     if current.data[0] is not None:
    
    #         if self.head.data[0].serial == target:
    #             if self.head.checkIfEmpty():
    #                 self.size = self.size - 1 
    #                 self.head = self.head.next
    #             else:
    #                 self.head.data[0] = None
                
    #             n = self.head
    #             while n.next is not None:
    #                 if n.data[0].serial == target:
    #                     break
    #                 n = n.next

    #         elif self.head.data[1] == target:
    #             if self.head.checkIfEmpty():
    #                 self.size = self.size - 1 
    #                 self.head = self.head.next
    #             else:
    #                 self.head.data[1] = None
                
    #             n = self.head
    #             while n.next is not None:
    #                 if n.data[1].serial == target:
    #                     break
    #                 n = n.next

    #     if current.data[1] is not None:

    #         if n.next is not None:
    #             if n.checkIfEmpty():
    #                 n.previous.next = n.previous
    #                 n.next.previous = n.previous
    #                 self.size = self.size - 1
    #             else:
    #                 n.deleteData(target)
    #         else:
    #             if n.data[1].serial == target:
    #                 if n.checkIfEmpty():
    #                     n.previous.next = None
    #                     self.size = self.size - 1
    #                 else:
    #                     n.deleteData(target)
    #             elif n.data[1].serial == target:
    #                 n.previous.next = None
    #                 self.size = self.size -1
    #         else:
    #             return print('Avion no encontrado')
    
    def display(self):
        current = self.head
        if(self.head == None):
            print('List is empty!')
            return
        print("Nodes of list:")
        while(current != None):
            print(current.data)
            current = current.next