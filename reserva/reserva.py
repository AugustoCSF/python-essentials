import sys

code_price = {}
code_reservado = []

print("Estes são os quartos disponíveis:\n")

with open('reservados.txt', 'r') as file:
    for line in file:
        values = line.strip().split(',')
        code_reservado.append(int(values[0]))

with open('quartos.txt', 'r') as file:
    next(file)
    for line in file:
        values = line.strip().split(",")
        
        code = int(values[0])
        price = float(values[2])
        code_price[code] = price

        if code in code_reservado:
            continue
        print(line.replace(",", " | ").strip())

cliente = input("Digite seu nome completo: ")

room = int(input("Qual o número (código) do quarto que deseja reservar? "))
if room not in code_price.keys():
    print("Esse quarto não existe, escolha apenas um da lista")
    sys.exit(1)
elif room in code_reservado:
    print("Esse quarto já está reservado, escolha apenas um da lista")
    sys.exit(1)

days = int(input("Por quantos dias você quer reservar o quarto? (ao digitar enter você já estará confirmando esta reserva) "))
total = days * code_price[room]

with open("reservados.txt", "a") as reservados_file:
    reservados_file.write(f"{room},{cliente},{days},{total:.2f}\n")

print(f"A sua reserva foi concluida com sucesso! O valor a pagar será R${total:.2f}")