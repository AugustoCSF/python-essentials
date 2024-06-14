#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.2.0"

# Dados
salas = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

# Listar alunos em cada atividade por sala
for atividade, alunos in atividades.items():
    turma_por_sala = {
        "sala1": set(salas["sala1"]) & set(alunos),
        "sala2": set(salas["sala2"]) & set(alunos)
    }

    print(f"Alunos de {atividade}")
    for sala, turma in turma_por_sala.items():
        print(f"{sala.capitalize()}: {sorted(turma)}")
    print("-" * 25)