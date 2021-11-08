import random

print('Adivina el número escondido entre el 0 y el 99')

numeroAleatorio = random.randint(0, 99)
intentos = 10

while(intentos > 0):
    print('Intentos restantes:',intentos)
    valor = int(input('Ingrese valor: '))

    if valor == numeroAleatorio:
        puntaje = intentos*10
        print('Has ganado... tu puntaje es', puntaje, 'de 100')
        break
    elif(valor > numeroAleatorio):
        print('El número secreto es menor\n')
    else:
        print('El número secreto es mayor\n')
    
    intentos -= 1
else:
    print('No has conseguido adivinar, el número era', numeroAleatorio)
    print('Tu puntaje es de 0')
    
