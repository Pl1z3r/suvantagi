@echo off

REM Verifica se a pasta venv existe
if exist venv (
    echo Ativando o ambiente virtual...
    call venv\Scripts\activate
) else (
    echo Criando ambiente virtual...
    python -m venv venv
    call venv\Scripts\activate
)

REM Instala as dependências
echo Instalando as dependências do requirements.txt...
pip install -r requirements.txt

REM Executa o main.py
echo Executando o main.py...
python main.py %*
