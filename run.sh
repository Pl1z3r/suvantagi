#!/bin/bash

# Verifica se o ambiente virtual existe
if [ -d "venv" ]; then
    echo "Ativando o ambiente virtual..."
    source venv/bin/activate
else
    echo "Criando ambiente virtual..."
    python3 -m venv venv
    source venv/bin/activate
fi

# Instala as dependências
echo "Instalando as dependências do requirements.txt..."
pip install -r requirements.txt

# Executa o main.py
echo "Executando o main.py..."
python src/main.py "@$"
