# Fibonacci series:
# the sum of two elements defines the next
# Serie de Fibonacci: la suma de dos elementos define el siguiente
a = 0
b = 1
while a < 100:
    print("el valor es",a)
    temp = a  # Guardar el valor de 'a' en una variable temporal
    a = b     # Asignar a 'a' el valor de 'b'
    b = temp + b  # Asignar a 'b' la suma de 'temp' (el antiguo valor de 'a') y 'b'

'''
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
'''

