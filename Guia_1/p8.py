print("Dupllicador de Caracteres")

def duplicar_elementos(lista):
    nueva_lista = []  # Acá aprendí que para guardar elementos se los guarda así dentro de la función
    
    for elemento in lista:
        nueva_lista.append(elemento)  
        """Acá aprendí q el culiadazo del append() agrega lo que 
        está en los paréntesis, y acá usamos el append dos veces
        para que nos duplique el elemento
        """
        nueva_lista.append(elemento)  
    
    return nueva_lista  # Devuelve la nueva lista con elementos duplicados

# Ejemplo de uso:
mi_lista = input("Indique la lista aquí para ser repetido cada elemento de ella: ", )
lista_duplicada = duplicar_elementos(mi_lista)
print("Lista original:", mi_lista)
print("Lista con elementos duplicados:", lista_duplicada)
