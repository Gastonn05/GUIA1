def ordenar_lista_numeros():
    # Pedir al usuario que ingrese una lista de números separados por espacios
    entrada = input("Ingresa una lista de números separados por espacios: ")
    
    # Dividir la entrada en una lista de strings
    numeros = entrada.split()

    
    # Ordenar la lista de números de menor a mayor
    numeros_ordenados = sorted(numeros)
    
    # Devolver la lista ordenada de números
    return numeros_ordenados

# Ejemplo de uso:
lista_ordenada = ordenar_lista_numeros()
print("Lista ordenada de menor a mayor:", lista_ordenada)
