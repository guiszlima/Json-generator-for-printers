from  modules.common_printers import *
from modules.file_operations import save_json_data
from modules.common import print_impressoras
from modules.model_operations import *

def edit_printers(dic: dict):
    try:
        file = "impressoras.json"
        print()
        texto = 'Qual das Opções deseja Selecionar?\n'

        texto += '[1]Criar Novo Lugar\n'
        texto += '[2]Editar Nome de Prédio\n'
        texto += '[3]Deletar Prédio\n'
        texto += '[4]Editar Nome de Impressora\n'
        texto += '[5]Criar Modelo\n'
        texto += '[6]Inserir Modelo\n'
        texto += '[7]Editar Modelo Modelo\n'

        option = int(input(texto))
        if 1 > option or option > 7:
            print("Essa Opção não existe")
            return
        # Criar Lugar
        if option == 1:
            print_impressoras(dic)
            print("A opção escolhida foi: Criar Lugar\n ")
            create_place(dic,file)
            save_json_data(file,dic)
        # Editar nome prédio
        elif option == 2:
            print_impressoras(dic)
            print()
            print("A opção escolhida foi: Editar Nome de Prédio\n")
           
            change_place_name(dic)
            save_json_data(file, dic)
          # deletar lugar   
        elif option == 3:
            print_impressoras(dic)
            print()
            print("A opção escolhida foi: Deletar Prédio\n ")
            delete_place(dic)
            save_json_data(file, dic)
        # mudar nome impressora 
        elif option == 4:
            print_impressoras(dic)
            print()
            print("A opção escolhida foi: Editar Nome de Impressora\n ")
            change_printer_name(dic)
            save_json_data(file, dic)
        # criar model
        elif option == 5:
            print("A opção escolhida foi: Criar Modelo\n ")
            create_model()
        # inserir model
        elif option == 6:
            print("A opção escolhida foi: Inserir Modelo\n ")
            insert_model(dic)
        # editar model
        elif option == 7:
            print("A opção escolhida foi: Editar Modelo\n ")
            edit_models()


    except ValueError:
        print("Valor Invalido por favor coloque um número")
   # except Exception as e:
     #   print(f"Aconteceu um erro! por favor contate o Desenvolvedor responsavel\nErro: {e}")