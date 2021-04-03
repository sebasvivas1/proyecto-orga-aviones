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
    print(result)
    return result

def check_if_exists(array, element, str):
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
    result = False

    while (first <= last):
        mid = (first+last)//2 
        if (array[mid][str]) == element:
            result =  True 
            return result
        else:
            if element < array[mid][str]:
                last = mid -1
            else: 
                first = mid+1            
    return result
    
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

def model_name():
    while True:
        try:
            model = input("\nIngrese el Módelo del Avión (20 carácteres máximo): ").capitalize()
            if 0<len(model)<21:
                break 
        except:
            pass
    return model 

def pilot_name():
    while True:
        try:
            pilotName = input("\nIngrese el Nombre del Piloto (15 carácteres máximo): ").capitalize()
            if 0<len(pilotName)<16:
                break 
        except:
            pass
    return pilotName 

def plane_name():
    while True:
        try:
            planeName = input("\nIngrese el Nombre del Avión (12 carácteres máximo): ").capitalize()
            if 0<len(planeName)<13:
                break 
        except:
                pass
    return planeName

def validacion_serial():
    loop = True
    while loop:
        serial = input("\nIngrese el Serial del Avión: ")
        primera_letra = serial[0]
        numeros = serial[1:8]
        if len(serial) != 9:
            print("Serial inválido (Debe ingresar 9 carácteres) ")
        elif primera_letra.isupper()==False:
            print("Serial inválido (Primera letra no está en mayúscula)")
        elif numeros.isdigit()==False:
            print("Serial inválido (No agregó numeros)")
        else:
            loop = False
    return serial

def sortNameList(arr):
    orderedList = sorted(arr, key = lambda k: k['name'])
    return orderedList

def sortModelList(arr):
    orderedList = sorted(arr, key = lambda k: k['model'])
    return orderedList
    
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
Por favor, ingrese el número correspondiente a la operación que desea ejecutar:

  1. Ingresar un nuevo avion
  2. Buscar un avion
  3. Asignarle un piloto a un avion
  4. Liberar un avion
  5. Eliminar un avion
  6. Mostrar base de datos
  >>> '''))
        except ValueError:
            print("\nIngrese un número, por favor")

        if num_operacion==1 or num_operacion==2 or num_operacion==3 or num_operacion==4 or num_operacion==5 or num_operacion == 6 :
            loop = False
            return num_operacion
        else:
            print("\nPor favor ingrese un numero valido")

def salida():
    loop = True
    while True:
        try:
            chao= int(input("""
Ingrese: 
  1. Para volver a empezar
  2. Para salir
  >>> """))
        except ValueError:
            print("\nPor favor, ingrese un número")
        if chao==1 or chao==2:
            loop = False
            return chao
        else:
            print("\Por favor, ingrese un número válido")
