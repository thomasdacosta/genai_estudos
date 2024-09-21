import requests
from sys import argv

argv = argv[1:]
soma = 0

def pesquisa_wikipedia(subject):
    extract = ""
    try:
        url = 'https://pt.wikipedia.org/w/api.php'
        params = {
                'action': 'query',
                'format': 'json',
                'titles': subject,
                'prop': 'extracts',
                'exintro': True,
                'explaintext': True,
            }

        response = requests.get(url, params=params)
        data = response.json()

        query = data["query"]["pages"]

        key, value = list(query.items())[0]

        if "extract" in value:
            extract = value["extract"]
            salvar_arquivo(subject, extract)
        else:
             extract = ""

    except Exception as e:
        print(f"#### ERRO #### --> NÃO FOI POSSIVEL CONECTAR NA API DA WIKIPEDIA {e}")

    if extract == "":
        return "#### ERRO #### --> SEM RETORNO DA PESQUISA"
    else:
        return extract

def salvar_arquivo(arquivo, conteudo):
    arquivo = arquivo.replace(" ", "_").lower()
    with open(arquivo + ".wiki", "w") as arquivo:
        arquivo.write(conteudo)

if len(argv) <= 0:
    print("#### ERRO #### --> NENHUM TERMO DE PESQUISA FOI PASSADO COMO PARAMETRO")
    print()
    print("## Instruções de comando:")
    print(" " * 4 + "request_wikipedia.py \"termo a ser buscado\"")
else:
    print(pesquisa_wikipedia(argv[0]))
