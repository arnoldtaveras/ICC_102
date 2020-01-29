n1 = -1
n2 = -1

while(n1 <= 0 or n2 <= 0):
    n1 = int(input("Digite un multiplicando: "))
    n2 = int(input("Digite un multiplicandor: "))

    if(n1 <= 0 or n2 <= 0):
        print("Error.solo numeros positivos")

acumulador = n1

while(n2 > 1):
    n1 = n1 + acumulador
    n2 = n2 - 1

print(n1)
    
