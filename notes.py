#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotacao geral sobre carreira de tecnologia

$ notes.py 1 tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

arguments = sys.argv[1:]

path = os.curdir
filepath = os.path.join(path, "notes.txt")

if not arguments:
    print("Usage error")
    sys.exit(1)

cmds = ("new", "1")
if arguments[0] not in cmds:
    print("Invalid command")
    sys.exit(1)

if arguments[0] == "1":
    #leitura das notas
    for line in open(filepath, "r"):
        title, tag, text = line.split("\t") 
        if tag.lower() == arguments[1].lower():
            print(title)
            print(text)
            print("-" * 30)

if arguments[0] == "new":
    titulo = arguments[1]
    text = [
        f"{titulo}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]

    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

