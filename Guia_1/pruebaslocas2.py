def fib(num):
    if(num<0):
        print("La función de Fibonacci no aplica a numeros negativos")
    else:
        a=0
        b=1

        print(a)
        print(b)

        for i in range(num+1):
            c=a+b
            a=b
            b=c
            if(c<=num):
                print(c)
            else:
                break
num=int(input("Enter the number till you want to see in fibonacci series : "))
fib(num)
