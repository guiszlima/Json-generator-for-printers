import json
from time import sleep

def save_json_data(file_name, dic):
    try:
        dic = json.dumps(dic, indent=4)
        with open(file_name, 'w') as file:
            file.write(dic)
    except:
        print('Não foi possivel registrar a impressora, contate o desenvolvedor responsável')

def json_exists(file_path):
    try:
        with open(file_path, 'r') as file:
            data_dict = json.load(file)
            return data_dict if data_dict else {}
    except FileNotFoundError:
        print("Arquivo não existe \nCriando novo arquivo. . .")
        sleep(2)
        with open(file_path, 'w') as file:
            print('Arquivo Criado')
        return {}
    except json.JSONDecodeError:
        print("O conteúdo do arquivo está vazio ou inválido \nCriando novo arquivo. . .")
        sleep(2)
        with open(file_path, 'w') as file:
            print('Arquivo Criado')
        return {}
