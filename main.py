import sumar, restar, multiplicacion, dividir, suma_avanzada

# Presentación del menú
print('Calculadora Open Source')
print('Elige una operación a realizar')
print('1. Suma dos números')
print('2. Resta dos números')
print('3. Multiplica dos números')
print('4. Divide dos números')
print('5. Suma varios números')
op = int(input('Elige el número de opción:\t'))

if op == 1:
    print('Suma de dos números')
    a = float(input('Escribe el primer sumando: '))
    b = float(input('Escribe el segundo sumando: '))
    c = sumar.sumar(a, b)
    print(f"El resultado es {c}")
elif op == 2:
    print('Resta de dos números')
    a = float(input('Escribe el minuendo: '))
    b = float(input('Escribe el sustraendo: '))
    c = restar.restar(a, b)
    print(f"El resultado es {c}")
elif op == 3:
    print('Producto de dos números')
    a = float(input('Escribe el primer factor: '))
    b = float(input('Escribe el segundo factor: '))
    c = multiplicacion.multiplicar(a, b)
    print(f"El resultado es {c}")
elif op == 4:
    print('División de dos números')
    a = float(input('Escribe el dividendo: '))
    b = float(input('Escribe el divisor: '))
    c = dividir.dividir(a, b)
    print(f"El resultado es {c}")
elif op == 5:
    print('Suma de varios números')
    n = int(input('Escribe el número de sumandos que quieres sumar: '))
    c = suma_avanzada.suma_avanzada(n)
    print(f"El resultado es {c}")
else:
    print('Tu opción no es válida')