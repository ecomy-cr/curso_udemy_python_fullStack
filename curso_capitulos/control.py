# if 2 < 5:
    # print('2 es menor que 5')

# # a == b
# # a < b
# # a > b
# # a != b
# # a <= b
# # a >= b

# if 2 == 2:
    # print('2 es igual a 2')

# if 2 == 3:
    # print('2 es igual a 3')

# if 2 > 5:
    # print('2 es mayor a 5')

# if 5 > 2:
    # print('5 es mayor a 2')

# if 2 != 2:
    # print('2 es distinto a 2')

# if 3 != 2:
    # print('3 es distinto a 2')

# if 3 >= 2:
    # print('3 es mayor o igual a 2')

# if 3 <= 3:
    # print('3 es menor o igual a 3')
"""
if 2 > 5:
    print('dos es menor a 5 en if')
elif 2 > 5:
    print('2 menor a 5 en elif')
elif 2 < 5:
    print('2 menor a 5 en segundo elif')
else:
    print('yo me imprimo solo si todo lo anterior evalua en falso')


if 2 > 5:
    print('dos es menor a 5 en if')
else:
    print('yo me imprimo solo si todo lo anterior evalua en falso 2')

if 2 < 5: print('if de una linea')

print('cuando devuelve true') if 5 > 2 else print('cuando devuelve false')

if 2 < 5 and 3 > 2:
    print('ambas devuelven true')

if 2 < 5 and 3 < 2:
    print('hay una falsa, esto no se mostrará')

if 1 < 0 or 1 > 0: # si una condición evalua en true se ejecuta la instrucción
    print('una de las dos condiciones devolvió true')

if 1 < 0 or 1 < 0: # si ambas condiciones son falsas entonces no se ejecuta
    print('si ambas condiciones evaluan en true no se ejecuta esto')


"""


#4 operaciones basicas Calculadora

# dato = input('Ingrese dato: ')

# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

# if lista.count(dato) > 0:
    # print('El dato existe:', dato)
# else:
    # print('El dato no existe :(', dato)
"""
primero = input('Ingrese primer número: ')

try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit() #exit en cmd es igual

segundo = input('Ingrese segundo número: ')

try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('ingrese operación: ')

if simbolo == '+':
    print('Suma:', primero + segundo)
elif simbolo == '-':
    print('Resta:', primero - segundo)
elif simbolo == '*':
    print('Multiplicación:', primero * segundo)
elif simbolo == '/':
    print('División:', primero / segundo)
else:
    print('El símbolo ingresado no es válido')

"""

