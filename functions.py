def binary_search_name(array, element):
    """[Verifica si el elemento introducido se encuentra en la lista dada]

    Args:
        product_list ([list]): [Lista]
        product ([str]): [Nombre del elemento a buscae]

    Returns:
        [None o impresión]
    """
    first = 0 
    last = len(product_list)-1
    index = -1 
    while (first <= last) and (index == -1):
        mid = (first+last)//2 
        if (product_list[mid]).name == product:
            return (product_list[mid])
        else: 
            if product < (product_list[mid]).name:
                last = mid-1
            else: 
                first = mid+1
    return print('¡Resultado no encontrado!') 


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

def model():
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




