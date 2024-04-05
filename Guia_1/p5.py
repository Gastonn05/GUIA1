
x = int(input("Indique los numeros que quiere ver en la secuencia -1 : ")) 

""" Basicamente ahí arriba te estoy diciendo
LACONCHA DE TU MADRE, DAME UN NUMERO :)
"""

print("Aquí comienza la sucección de Fibonacci: ")

#COMIENZA ACÁ CULIAU, QUE MÁS QUERÉS QUE TE EXPLIQUE


def fib(n):
    if n==1:
        return 0
    """
    Lesto, acá te puedo explicar: acá defino la funcion de fib y
    le digo que en primer lugar si me ponés 1 en los numeritos
    te devuelvo 0 con el if, onda, te dice: si n es igual a 1,
    pone a 0
    """
    if n==2:
        return 1
    """
    NO PIENSO VOLVER A EXPLICAR LO DE ARRIBA
    ES LITERALMENTE LO MISMO SOLO QUE UN NUMERO MAS
    EN LOS DOS, NOROMPASLASBOLAS
    """


    return fib(n-1)+fib(n-2)

"""
Corte, si no se cumlpe ninguna de las dos condiciones
agarras, y le clavas la funcion de fib, Perón, Mi general,
le mandas la fórmula mágica para que se realice el fibo
"""

for i in range(1,x):
    print(fib(i))

"""
Bueno mi loco, acá te digo que entre el 1 que te asigné
en la segundo if hasta el número que te hice elegir arriba
me imprimas la secuencia, y ya taría hecho
"""
"""
VAYA YENDO
NOPUEDESER QUE ESTA PORONGA ME DEMORÓ COMO 4HS
CABE ACLARAR QUE HUBO MOMENTOS DE PROCRASTINACION
PERO IGUAL, UNA BANDEJA
GRACIAS GRINGO CON CARA DE TROLO DE YOUTUBE POR LA EXPLICACION EN INGLISH
Pd: se llama Wrath of Math, nombre bien de puto
"""