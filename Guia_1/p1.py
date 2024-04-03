# Ejercicio 1 (Agregale un titulo bien fachero)
print("La suma y el producto de dos números.")

x = int(input("Ingrese el primer numero: ")) 
# Te correji detalles de ortografia, no se pone "=", se usa ":" y se deja un espacio al final
y = int(input("El segundo: "))
'''
Los input son metodos para interactuar con el usuario, una forma de ingresar un dato y poder trabajar con ello.
'''

''' Se usan estas comillas cuando el comentario se alarga mucho, el # se usa solamente para oraciones cortas
acá lo que estendí es que el input le dice mostrate ésto que está entre parentesís, 
entonces lo muestra y una vez que se lo das (al valor numérico en nuestro caso), 
usa el valor numérico que es lo que especifiqué cuando puse el int del principio de la línea
'''

print("El resultado de la suma es: ", x + y)
print("El resultado de el producto es: ", x * y)
