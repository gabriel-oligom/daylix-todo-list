# Projeto Daylix: To-Do List📝
#### Gerenciador de Tarefas (Modo Terminal + Interface Gráfica)
Daylix é um gerenciador de tarefas simples que utiliza estrutura de dados e manipulação de arquivos `.txt` para armazenar informações.  
Agora conta também com uma **versão inicial de interface gráfica** construída com FreeSimpleGUI, permitindo gerenciar tarefas com cliques.

### Funcionalidades
#### Modo Terminal
- ➕`add [tarefa]`
- 📄`show`
- 📝`edit [número]`
- ✅`complete [número]`
- ❌`exit`

#### Modo Gráfico (GUI)
- Adicionar tarefas via campo de texto
- Editar tarefas existentes
- Concluir tarefas e removê-las da lista

### 🗂️ Estrutura do Projeto
- `main.py`: código principal (loop de interação com o usuário)
- `functions.py`: funções para ler/escrever tarefas
- `todos.txt`: arquivo para salvar as tarefas
- `gui.py`: interface gráfica


### 🧱 Estrutura do Código
O código está organizado com funções para:
* `get_todos(filepath=FILEPATH)`: lê as tarefas do arquivo (default `"todos.txt"`) e retorna uma lista
* `write_todos(todos, filepath=FILEPATH)`: salva a lista de tarefas no arquivo (default `"todos.txt"`)

### Como usar (GUI)
1. Clone o repositório.
2. Instale a dependência FreeSimpleGUI, caso ainda não tenha.
3. Execute o arquivo gui.py no Python..

### 📌 Futuras melhorias
- Transformar o projeto em um web app
- Fazer o deploy da aplicação