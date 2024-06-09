"""Este programa imprime a tabuada do 1 ao 10"""
__version__ = 0;0;1
__author__ = "Augusto Ferreira"

numeros = list(range(1, 11))

for numero in numeros:
    print(f"Tabuada do {numero}:")
    for n in numeros:
        print(f"{numero} x {n} = ", numero * n)