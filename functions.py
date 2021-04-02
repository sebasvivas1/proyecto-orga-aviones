def binary_search_name_model(array, element, str):
    """[Verifica si el elemento introducido se encuentra en la lista dada]

    Args:
        product_list ([list]): [Lista]
        product ([str]): [Nombre del elemento a buscar]

    Returns:
        [None o impresión]
    """
    first = 0 
    last = len(array)-1
    index = -1 
    result = ""

    while (first <= last):
        mid = (first+last)//2 
        if (array[mid][str]) == element:
            result =  array[mid]["serial"]
            return result
        else:
            if element < array[mid][str]:
                last = mid -1
            else: 
                first = mid+1
                
    return result
    



def checkIfFull(array):
    arrayFull = False 
    if array[0]!= None and array[1]!= None:
        arrayFull = True
    return arrayFull

def file_existence(file_name):
    """[Verifica si el archivo existe o no]

    Returns:
        [bool]: [Dependiendo de la existencia del archivo]
    """
    try: 
        with open(file_name) as f:
            return True
    except FileNotFoundError as e:
        return False 
"""
def serial():
    while True:
        try:
            serial= input("Ingrese el Serial del Avión: ")
        except:
            pass
    return serial 
"""

def model_name():
    while True:
        try:
            model = input("Ingrese el Módelo del Avión (20 carácteres máximo): ")
            if 0<len(model)<21:
                break 
        except:
            pass
    return model 

def pilot_name():
    while True:
        try:
            pilotName = input("Ingrese el Nombre del Piloto (15 carácteres máximo): ")
            if 0<len(pilotName)<16:
                break 
        except:
            pass
    return pilotName 

def plane_name():
    while True:
        try:
            planeName = input("Ingrese el Nombre del Avión (15 carácteres máximo): ")
            if 0<len(planeName)<12:
                break 
        except:
                pass
    return planeName

def validacion_serial():
    loop = True
    while loop:
        serial = input("Por favor ingrese un serial: ")
        primera_letra = serial[0]
        numeros = serial[1:7]
        if len(serial)>8:
            print("Serial invalido (mayor de 8 caracteres) ")
        elif primera_letra.isupper()==False:
            print("Serial invalido (primera letra no es capital)")
        elif numeros.isdigit()==False:
            print("Serial invalido (no agrego numeros)")
        else:
            loop = False
    return serial

def sortNameList(arr):
    orderedList = sorted(arr, key = lambda k: k['name'])
    return orderedList


def sortModelList(arr):
    orderedList = sorted(arr, key = lambda k: k['model'])
    return orderedList
    # for x in orderedList:
    #     print((x['model']))
    
def insertToList(key1, val, key2, serial):
    dict = {}
    dict[key1] = val
    dict[key2] = serial
    return dict.copy()
    

def numeros():
    loop = True
    num_operacion = 0
    while loop:
        try:
            num_operacion = int(input('''
        Por favor ingrese los siguientes numeros si desea:

        1. Ingresar un nuevo avion
        2. Buscar un avion
        3. Asignarle un piloto a un avion
        4. Liberar un avion
        5. Eliminar un avion

        '''))
        except ValueError:
            print("\nIngrese un numero por favor")

        if num_operacion==1 or num_operacion==2 or num_operacion==3 or num_operacion==4 or num_operacion==5 or num_operacion ==7:
            loop = False
            return num_operacion
        else:
            print("\nPor favor ingrese un numero valido")

def salida():
    loop = True
    while True:
        try:
            chao= int(input("Ingrese 0 si desea salir o 1 si desea volver a empezar\n ==>"))
        except ValueError:
            print("\nPor favor ingrese un numero por favor")
        if chao==1 or chao==0:
            loop = False
            return chao
        else:
            print("\Por favor ingrese un numero valido")