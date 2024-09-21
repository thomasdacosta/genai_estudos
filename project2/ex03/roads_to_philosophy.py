import requests
import sys

from bs4 import BeautifulSoup

passos = []
argv = sys.argv[1:]
soma = 0

def pesquisa_pagina(texto):
    try:
        link = "https://en.wikipedia.org/wiki/" + texto
        requisicao = requests.get(link)
        site = BeautifulSoup(requisicao.text, "html.parser")

        i = 0
        for div in site.find_all("div", id="mw-content-text"):
            link = div.find_all("a")[i]
            valor = link.get("href")

            while "#" in valor or ":" in valor:
                link = div.find_all("a")[i]
                valor = link.get("href")
                i += 1

            if len(link) <= 0:
                print("It leads to a dead end!")
                break

            if "Philosophy" in valor:
                print(f"{len(passos)} roads from {argv[0]} to philosophy!")
                break

            if valor.startswith("/wiki"):
                valor = valor[6:]

            print(valor)
            passos.append(valor)

            pesquisa_pagina(valor)
    except Exception as e:
        print(f"Error: {e}. Unable to continue")


if len(argv) <= 0:
    print("#### ERRO #### --> NENHUMA PAGINA DA WIKIPEDIA FOI PASSADO COMO PARAMETRO")
    print()
    print("## Instruções de comando:")
    print(" " * 4 + "roads_to_philosophy.py \"pagina wikipedia\"")
else:
    print(pesquisa_pagina(argv[0]))
