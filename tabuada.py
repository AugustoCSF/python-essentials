"""Este programa imprime a tabuada do 1 ao 10"""
__version__ = 0;1;1
__author__ = "Augusto Ferreira"

numeros = list(range(1, 11))
largura = 20

for numero in numeros:
    title = f"Tabuada do {numero}".center(largura, "-")
    print()
    print(title)
    print()
    for n in numeros:
        print(f"{numero} x {n} = {numero * n}".center(largura))
    print()
    print("_" * largura)