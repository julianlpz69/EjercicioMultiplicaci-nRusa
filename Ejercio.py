# Reto 2: Multiplicación Rusa
# El método de multiplicación rusa consiste en multiplicar sucesivamente por 2 el multiplicando y
# dividir por 2 el multiplicador hasta que el multiplicador tome el valor 1.
# Luego, se suman todos los multiplicandos correspondientes a los multiplicadores impares.
# Dicha suma es el producto de los dos números. La siguiente tabla muestra el cálculo realizado para
# multiplicar 37 por 12, cuyo resultado final es 12 + 48 + 384 = 444.

import math

try:

    Multiplicador = int(input("\nIngrese Multiplicador: \t"))
    Multiplicando = int(input("\nIngrese Multiplicando: \t"))
    resultado = 0

    while Multiplicador > 0.6:
        if Multiplicador % 2 != 0:
            resultado += Multiplicando
            
        Multiplicador = (math.floor(Multiplicador/2))
        Multiplicando = (math.floor(Multiplicando*2))
             
    print(f"\n Resultado: {resultado}")
    
except:
    print("\nIngresa un numero Valido")