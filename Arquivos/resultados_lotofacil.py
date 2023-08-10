import requests
from bs4 import BeautifulSoup


def obter_HTML(url):
    # como obter o User-Agent no chrome, pisquisa: my user agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/94.0.4606.61 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


# Obtém o número do último concurso da lotofácil
page = obter_HTML('https://www.estadao.com.br/loterias/lotofacil/')
concurso_atual = int(page.find('div', class_='header-informs-loteria').text.split(' ')[3])

# Responsável por minerar (extrair) os dados do site.
resultados_sorteados = []
quinze_em_quinze = []
for i in range(1, (concurso_atual + 1)):
    print(f'Concurso: {i}')
    page2 = obter_HTML(f'https://www.mazusoft.com.br/lotofacil/resultado.php?concurso={str(i)}/')
    numeros_sorteados = page2.find('div', 'result-ct-lf')
    for num in numeros_sorteados:
        numero = num.text.split()
        if len(numero) != 0:
            quinze_em_quinze.append(numero[0])
            if len(quinze_em_quinze) == 15:
                resultados_sorteados.append(quinze_em_quinze)
                quinze_em_quinze = []
