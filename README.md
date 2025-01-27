## Instalar o ambiente do python
python -m venv <nome_ambiente>

## Ativar o ambiente do python no windows
.\bytes\Scripts\activate

## Instalar dependências do python em requirements
pip install -r requirements.txt

## Enviar dependencias pro arquivo requirements
pip freeze > requirements.txt

## Criar executável
pip install pyinstaller
pyinstaller --onefile --noconsole --add-data "sync.png;." --add-data "carregar_todos.png;." --add-data "fechar.png;." --add-data "sem_rede.png;." --add-data "switch_network_on.png;." main.py
