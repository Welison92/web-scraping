import requests
from bs4 import BeautifulSoup


def obter_HTML(url):
    # como obter o User-Agent no chrome, pisquisa: my user agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/94.0.4606.61 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


lista_controle_crash = []
while True:
    # Obtém o HTML e extrai os dados do Crash
    dados = obter_HTML('https://kitblaze.com/crash/?visitante=home').find('div', class_='content-crash').text.split('\n')

    # Remove os dados vazios da lista
    while '' in dados:
        dados.remove('')

    # Processa os dados do Crash
    dados_crash = []
    for indice in range(len(dados)):
        try:
            dado1, dado2 = dados[indice], dados[indice + 1]
            if ':' in dado1:
                dados_crash.append((float(dado2.split('X')[0]), dado1))
            else:
                dados_crash.append((float(dado1.split('X')[0]), dado2))
        except IndexError:
            pass

    # Adiciona os dados do Crash à lista de controle
    lista_controle_crash.append(dados_crash)

    # Mantém apenas os últimos 2 conjuntos de dados do Crash
    if len(lista_controle_crash) > 2:
        del lista_controle_crash[: 2]

    # Verifica se houve uma mudança significativa no Crash
    if len(lista_controle_crash) > 1:
        if lista_controle_crash[len(lista_controle_crash) - 1] == lista_controle_crash[len(lista_controle_crash) - 2]:
            del lista_controle_crash[0]
        else:
            # Imprimi o primeiro conjunto de dados do Crash se houve uma mudança significativa
            print(dados_crash[0])
