import requests
from time import sleep


# Lista de controle para armazenar os últimos dois resultados de double
lista_controle_double = []
while True:
    try:
        # Faz uma requisição para a API para obter os dados mais recentes de double
        dados = requests.get('https://historicoblaze.com.br/api/v1/double/history?isSequence=1').json()['data'][0]
        cor = int(dados['color'])  # 1 -> Vermelho, 2 -> Preto, 0 -> Branco
        numero = int(dados['roll'])
        data = dados['date']

        # Adiciona os dados à lista de controle
        lista_controle_double.append([cor, numero, data])

        # Verifica se a lista de controle tem exatamente dois resultados de double
        if len(lista_controle_double) == 2:
            if lista_controle_double[0] == lista_controle_double[1]:
                del lista_controle_double[0]  # Remove o primeiro resultado duplicado
            else:
                # Obtém os dados do segundo resultado de double da lista
                dados_double = lista_controle_double[1]
                cor_double = dados_double[0]
                numero_double = dados_double[1]
                del lista_controle_double[0]  # Remove o primeiro resultado da lista

                # Imprime o resultado do double de acordo com a cor
                if cor_double == 1:
                    print(f'Vermelho, {numero_double}')
                elif cor_double == 2:
                    print(f'Preto, {numero_double}')
                else:
                    print(f'Branco, {numero_double}')
    except TypeError:
        pass

    sleep(1)
