from time import sleep

import sys

from modules.edit_printer_main import edit_printers

from modules.file_operations import json_exists, save_json_data


file_name = 'impressoras.json'
json_data  = json_exists(file_name)
 
if not json_data:
    print("Json vazio, começando processo de criação de um json. . .")
    impressoras = dict()
    predio = str(input("Qual o nome do local? ")).strip()
   
    impressoras[predio] = {}
    print("Prédio criado")
    save_json_data(file_name,impressoras)
    edit = str(input("Gostaria de Editar o Json? [S/N] ")).strip().upper()
    if edit[0] == "S":
        while True:
            edit_printers(impressoras)
            leave = str(input("Deseja Continuar no programa? [S/N]")).strip().upper()
            if leave[0] == "N":
                print('Programa Finalizado')
                sys.exit()
    else:
        print("Programa Finalizado")
        sleep(0.6)
        sys.exit()
else:
    while True:
        edit_printers(json_data)
        leave = str(input("Deseja Continuar no programa? [S/N]")).strip().upper()
        if leave[0] == "N":
            print('Programa Finalizado')
            sys.exit()
    while True:
        edit_printers(json_data)
        leave = str(input("Deseja Continuar no programa? [S/N]")).strip().upper()
        if leave[0] == "N":
            print('Programa Finalizado')
            sys.exit()