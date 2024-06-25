"""
emite alertas de acordo com temperatura e umidade informadas pelo usuário
"""
try:
    temp = int(input("Qual a temperatura atual em graus celsius? ").strip())
except ValueError:
    print("Insira uma temperatura válida (EX: 35)")
    exit()
try:
    umidade = int(input("Qual a umidade do ar atual? ").strip())
except ValueError:
    print("Insira uma umidade válida (EX: 50)")
    exit()

if temp > 45:
    print("ALERTA! Perigo de calor extremo!")
elif (temp * 2) >= umidade:
    print("ALERTA! Perigo de calor úmido!")
elif temp >= 30 and temp < 45:
    print("Calor")
elif temp >= 13 and temp < 30:
    print("Está uma temperatura agradável")
elif temp > 0 and temp < 13:
    print("Está frio")
elif temp < 0:
    print("ALERTA! Frio extremo!")

