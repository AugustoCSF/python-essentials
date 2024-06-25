"""
Pede que o usuário informe palavras e duplica as vogais dessas palavras
"""

duplicadas = []

while True:
    palavra = input("Digite uma palavra ou pressione enter para sair: ").strip()
    if not palavra:
        break
    result = ""
    for letter in palavra:
        #TODO: considerar acentos
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            result += letter * 2
        else:
            result += letter
    
    duplicadas.append(result)

print(*duplicadas, sep="\n")