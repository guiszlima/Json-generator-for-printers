import os
import importlib

# Caminho para o diretório atual
module_dir = os.path.dirname(__file__)

# Itera sobre todos os arquivos no diretório atual
for file in os.listdir(module_dir):
    if file.endswith('.py') and file != '__init__.py':
        module_name = file[:-3]  # Remove a extensão .py
        module_path = f"{module_dir}/{file}"  # Caminho completo para o módulo
        
        # Importa o módulo dinamicamente
        importlib.import_module(f"modules.{module_name}", package=__name__)