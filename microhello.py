"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha variável LANG devidamente configurada ex:

        export LANG = pt_BR

Execução:
        pynthon3 hello.py
        ou 
        ./microhello.py
"""
__version__ = "0.0.1"
__author__ = "Graciele Santos"
__license__ = "Unlicense"

import os 

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World"

if current_language == "pt_BR":
	msg = "Olá, Mundo!"
elif current_language == "it_IT":
	msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
	msg = "Bonjour, Monde!"

print(msg)
