# Ejercicio 4
print("Verifica si tu numero es primo o no")
x = int(input("Escriba aquí su número: "))

def primo(x): #define si el numero es primo o no
    for i in range(2, x): #divide el numero por todos los numeros desde el 2, hasta todos numeros en adelante del 2 excepto el mismo numero elegido y los numeros por delante 
        if(x%i) == 0: #indica que si es igual a 0 no puede retornar como true, porq 0 no es primo :)
            return False #indica False cuando no es primo
    return True #indica True cuando es primo

print(primo(x))
