from modules.common import  print_models,print_models_details,print_impressoras,ask_model,choose_model,choose_model_prop,choose_place

from modules.file_operations import json_exists, save_json_data



models_file = 'models.json'





def create_model():
    json_data = json_exists(models_file)
   
    if json_data:
        print_models(json_data)
   
    else:
        print("Json está vazio!")
   
    while True:
        nome_model = input("Digite o Nome do Model: ").strip()
   
        if nome_model in json_data:
            print("Este Modelo já existe")
            return
   
        dicionario = {}  
        dicionario = ask_model(dicionario)
        
       
        json_data[nome_model] = dicionario
        save_json_data(models_file,json_data)
        stop = str(input("Gostaria de fazer mais um model [S/N]: ")).strip().upper()

        if stop[0] == "N":
            save_json_data(models_file,json_data)
            break
       
def insert_model(dic):
   
    models = json_exists(models_file)
    
    if not models:
        print('Modelo não existe')
        ask = str(input("Deseja criar um modelo? [S/N]: ")).upper().strip()
        if ask[0] == 'S':
            create_model()
        else:
            return
    else:
        print_models(models)
        model = choose_model(models)

        if model not in models:
            print('Esse modelo não existe, crie um modelo')
            return
        
        print_impressoras(dic)
        place = choose_place(dic)

        if place not in dic:
            print("Este prédio não existe")
            return

        printerToAdd = str(input("Qual o nome da impressora? (Caso a impressora não exista será criado uma nova) \n")).strip()

        if printerToAdd in dic[place]:
            dic[place]["Nome_Driver"] = models[model]["Nome_Driver"]
            dic[place]["Caminho_Driver"] = models[model]["Caminho_Driver"]
            dic[place]["Caminho_Driver_Servidor"] = models[model]["Caminho_Driver_Servidor"]
            return
        else:
            printerIP = str(input('Qual o endereço Ip da Impressora? ')).strip()
            new_printer = {
                "Nome_Impressora": printerToAdd,
                "Nome_Driver": models[model]["Nome_Driver"],
                "Endereco_IP": printerIP,
                "Caminho_Driver": models[model]["Caminho_Driver"],
                "Caminho_Driver_Servidor": models[model]["Caminho_Driver_Servidor"]
            }
            dic[place][printerToAdd] = new_printer
            print("foi criado uma nova impressora e inserido o model")
        
def edit_models():
   json_data = json_exists(models_file)
   print_models(json_data)
   model = choose_model(json_data)
   
   if model not in json_data:
    print("Esse modelo não existe")
    return
   print('Modelo a ser editado:  \n')
   print_models_details(json_data[model])
   attr = choose_model_prop(json_data[model])
   print('Atributo a ser editado: ', json_data[model][attr],'\n')
   new_val = str(input("Qual será o novo valor? ")).strip()
   json_data[model][attr] = new_val
   save_json_data(models_file,json_data)
