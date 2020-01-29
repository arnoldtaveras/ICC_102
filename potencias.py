numeropositivo = -1
potencia = -1

while (numeropositivo <= 0 or potencia <= 0):
    numeropositivo = int(input("Digite una base: "))
    potencia = int(input("Digite una potencia: "))

    if(numeropositivo <= 0 or potencia <= 0):
        print ("Error. solo numeros positivos")

acumulador = numeropositivo

while (potencia > 1):
    potencia = potencia - 1
    numeropositivo = numeropositivo * acumulador

print(numeropositivo)
        
