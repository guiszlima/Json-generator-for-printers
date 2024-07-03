from modules.common import choose_place
from modules.file_operations import save_json_data
from modules.model_operations import insert_model


def create_place(dic: dict, file: str):
    print()
    print("A opção escolhida foi: Criar Novo Prédio\n ")
    place = str(input('Qual será o nome de local? '))
    if place not in dic:
        dic[place] = {}
        save_json_data(file,dic)
        confirm_printer = str(input('Gostaría de adicionar uma impressora? [S/N]')).upper().strip()
        if confirm_printer[0] == "S":
            
            insert_model(dic)
        else:
            save_json_data(file, dic)
    else:
        print('Prédio já existe')



def change_place_name(dic):
    place_old =  choose_place(dic)
   
    new_name = str(input("Qual será o novo nome do prédio: \n"))
    if place_old not in dic:
        print("Este prédio não existe, Insira outro")
    elif new_name in dic:
        print("Este nome já existe")
    else:
        dic[new_name] = dic.pop(place_old)

def delete_place(dic):
    place = str(input("Qual prédio deseja deletar? "))
    confirm = str(input("""Para apagar o prédio escreva "confirmar" """))
    if confirm == "confirmar":
        print("Este prédio não existe, Insira outro") if place not in dic else dic.pop(place)

def change_printer_name(dic):
    place = str(input("Insira o prédio no qual a impressora se localiza: "))
    if place not in dic:
        print("Prédio não existe")
        return

    old_name = str(input("Qual impressora terá seu nome mudado? "))
    if old_name not in dic[place]:
        print("Essa impressora não existe")
        return

    new_name = str(input("Qual será o novo nome? "))
    if new_name in dic[place]:
        print("Este nome já existe")
        return

    dic[place][new_name] = dic[place].pop(old_name)
    dic[place][new_name]["Nome_Impressora"] = new_name
    print(f"Nome da impressora alterado de {old_name} para {new_name}")

def add_printer(dic, place, printer=False):
    if place not in dic:
        print("Prédio não existe")
        return False

    dicionario = {}
    if not printer:
        dicionario["Nome_Impressora"] = input("Digite o Nome da Impressora: ")
    else:
        dicionario["Nome_Impressora"] = printer
    if dicionario["Nome_Impressora"] in dic[place]:
        print('Impressora já existe nesse prédio')
        return False

    dicionario["Nome_Driver"] = input("Digite o Nome do Driver: ")
    dicionario["Endereco_IP"] = input("Digite o Endereço IP: ")
    dicionario["Caminho_Driver"] = input("Digite o Caminho do Driver: ")
    dicionario["Caminho_Driver_Servidor"] = input("Digite o Caminho do Driver no Servidor: ")

    dic[place][dicionario["Nome_Impressora"]] = dicionario
    return True

