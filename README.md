# Projeto Daylix: To-Do List📝
#### Gerenciador de Tarefas (Escopos Iniciais do Projeto)
Daylix é um gerenciador de tarefas simples que utiliza estrutura de dados e manipulação de arquivos `.txt` para o armazenamento de informações. 

### Funcionalidades
O projeto Daylix funciona como uma lista de tarefas que o usuário pode modificar, adicionando, editando ou removendo os itens da lista com os comandos:
- ➕`add [tarefa]`
- 📄`show`
- 📝`edit [número]`
- ✅`complete [número]`
- ❌`exit`

### 🗂️ Estrutura do Projeto
- `main.py`: código principal (loop de interação com o usuário)
- `functions.py`: funções para ler/escrever tarefas
- `todos.txt`: arquivo para salvar as tarefas
- `gui.py`: protótipo de interface gráfica


### 🧱 Estrutura do Código
O código está organizado com funções para:
* `get_todos(filepath=FILEPATH)`: lê as tarefas do arquivo (default `"todos.txt"`) e retorna uma lista
* `write_todos(todos, filepath=FILEPATH)`: salva a lista de tarefas no arquivo (default `"todos.txt"`)


### Como usar  
1. Clone o repositório  
2. Execute no terminal `python main.py` ou `py main.py` (requer Python instalado)  
3. Siga as instruções na tela  

### 📌 Futuras melhorias
- Validação de entrada de usuário
- Interface gráfica completa (`gui.py`)