
x = str(input("Ingrese la oración para poder continuar: ", ))

y = len(x.split()) 

"""la funcion len() es la que realmente hace de contador
así cuenta con la característica de split() explicada abajo
"""

"""acá uso la condición separador de espacion split() para que tome los
espacios en blanco y en base a éso haga lo siguiente
"""

print("En la siguiente frase hay: " + str(y) + " palabras.")
