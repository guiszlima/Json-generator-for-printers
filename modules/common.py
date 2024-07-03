
def print_color(text, color_code):
        print(f"\033[{color_code}m{text}\033[0m")
def print_models(json_data):
    c= 0
    for modelo, detalhes in json_data.items():
        c += 1
        print_color(f"{c} Modelo: {modelo}", '2;32')  # Verde claro
        for chave, valor in detalhes.items():
            print_color(f"  {chave.replace('_', ' ')}: {valor}", '1;33')  # Amarelo brilhante
        print("\n")
def print_models_details(detalhes):
    c= 0
    for chave, valor in detalhes.items():
        c += 1
        print(f"{c} {chave}: {valor}")


def print_impressoras(dicionario):
    
 
    print()
    print_color("=== Impressoras Registradas ===", '1;32')  # Green bold
    for predio, impressoras in dicionario.items():
        print_color(f"Prédio: {predio}", '1;34')  # Blue bold
        for impressora, atributos in impressoras.items():
            print_color(f"    Impressora: {impressora}", '1;36')  # Cyan bold
            for chave, valor in atributos.items():
                print_color(f"        {chave}: {valor}", '1;37')  # White bold
        print()

def ask_model(dicionario):
   
   
   
    # Adiciona as novas chaves e valores ao dicionário
   
    dicionario["Nome_Driver"] = input("Digite o Nome do Driver: ").strip()
    dicionario["Caminho_Driver"] = input("Digite o Caminho do Driver na maquina: ").strip()
    dicionario["Caminho_Driver_Servidor"] = input("Digite o Caminho do Driver no Servidor: ").strip()
   
    return dicionario
 


def choose_place(dic):
    edificios_array = []
    c = 0
    for predio, key in dic.items():
        edificios_array.append(predio)
        print(c, predio)
        c += 1


    escolhaPredio = int(input('Qual lugar se encontra? Escolha um número:\n'))
    if escolhaPredio >= len(edificios_array):
        print("Prédio inválido")
        return

    return edificios_array[escolhaPredio]



def choose_model(dic):
    models_array = []

    for modelo, key in dic.items():
        models_array.append(modelo)

    escolhaNumero = int(input('Qual modelo deseja? Escolha um número:\n'))

    if escolhaNumero <= 0 or escolhaNumero > len(models_array):
        print("Número inválido. Escolha um número dentro do intervalo disponível.")
        return None
    print(models_array)
    print(models_array[escolhaNumero-1])
    return models_array[escolhaNumero - 1]

def choose_model_prop(model):
    model_attr_array = []
    
    # Itera sobre as chaves e valores do dicionário `model`
    for chave, valor in model.items():
        model_attr_array.append(chave)  # Adiciona o valor à lista `model_attr_array`
    
    print(model_attr_array)
    escolhaNumero = int(input('Qual modelo deseja? Escolha um número:\n'))

    if escolhaNumero <= 0 or escolhaNumero > len(model_attr_array):
        print("Número inválido. Escolha um número dentro do intervalo disponível.")
        return None
    
    return model_attr_array[escolhaNumero - 1]
