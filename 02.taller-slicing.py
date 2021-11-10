import numpy as np

"""
Generar un arreglo tridimensional de tamaño 9x9x9 con los número enteros del 0 al 728.
"""

arreglo = np.arange(729).reshape(9,9,9)

"""
Imaginar que el arreglo se divide en 27 arreglos de 3x3x3; desarrollar una función que permita intercambiar la posición de dos de estos bloques, pasándole como argumento únicamente la identificación de los bloques a intercambiar (los bloques se deben identificar con números del 0 al 26)
"""

def intercambiar(array, posA, posB):
    if(posA<0 or posA>26 or posB<0 or posB>26):
        print("El valor ingresado no es válido")
        return
    temp = array[posA]
    array[posA] = array[posB]
    array[posB] = temp
    return array

"""
Test
"""

arreglo1 = np.arange(729).reshape(27,3,3,3)

print(arreglo1)
intercambiar(arreglo1, 2, 1)
print(arreglo1)