# Suma avanzada
def suma_avanzada(n):
    if n > 0:
        suma = 0
        for i in range(n):
            suma = suma + float(input('Escribe el sumando {i}'))
        return suma
    else:
        return None