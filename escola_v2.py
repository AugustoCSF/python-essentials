#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.2.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Listar alunos em cada atividade por sala

atividades = [("Inglês", aula_ingles), ("Música", aula_musica), ("Dança", aula_danca)]

for atividade, aula in atividades:
    turma_1 = set(sala1) & set(aula)
    turma_2 = set(sala2) & set(aula)

    print(f"Alunos de {atividade}")
    print("Sala 1", turma_1)
    print("Sala 2", turma_2)
    print("-" * 25)