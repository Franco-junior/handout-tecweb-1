import json
def extract_route (requisicao):
    lista = requisicao.split()
    for palavra in lista:
        if palavra[0] == '/':
            retorno = palavra[1:]
            return retorno
        
def read_file(path):
    with open(path, 'rb') as arquivo:
        return arquivo.read()
    
def load_data(nome_arquivo):
    with open(f'data/{nome_arquivo}') as arquivo:
        return json.loads(arquivo.read())
    
def load_template(nome_arquivo):
    with open(f'templates/{nome_arquivo}') as arquivo:
        return arquivo.read()

