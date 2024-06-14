# esse programa printa HELLO WORLD!

"""Hello world multi_línguas

Este programa imprime HELLO WORLD de acordo com a língua do ambiente.

Como usar:
    Tenha a variavel LANG devidamente configurada.

    use:
        python hello.py
"""

__version__ = 0;0;1
__author__ = "Augusto Ferreira"
__license__ = "Unlicense"

import os

current_lang = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, world!",
    "it_IT": "Ciao, mondo!",
    "pt_BR": "Olá, mundo!",
    "fr_FR": "Bonjour, monde!",
}


print(msg[current_lang])