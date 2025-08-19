# Projeto Daylix: To-Do List📝
#### Gerenciador de Tarefas (Terminal + GUI + Web App)
Daylix é um gerenciador de tarefas simples que utiliza estrutura de dados e manipulação de arquivos `.txt` para armazenar informações.  
O projeto possui três modos de uso:

1. **Modo Terminal (CLI)**: gerencie tarefas pelo terminal.  
2. **Modo Gráfico (GUI)**: interface simples usando FreeSimpleGUI.  
3. **Web App (Streamlit)**: interface web interativa para gerenciar tarefas no navegador.

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

#### Web App (Streamlit)
- Adicionar tarefas via campo de texto
- Concluir tarefas clicando nas checkboxes
- Lista de tarefas atualizada dinamicamente

### 🗂️ Estrutura do Projeto
- `main.py`: código principal (loop de interação com o usuário)
- `functions.py`: funções para ler/escrever tarefas
- `todos.txt`: arquivo para salvar as tarefas
- `gui.py`: interface gráfica
- `web.py`: web app


### 🧱 Estrutura do Código
O código está organizado com funções para:
* `get_todos(filepath=FILEPATH)`: lê as tarefas do arquivo (default `"todos.txt"`) e retorna uma lista
* `write_todos(todos, filepath=FILEPATH)`: salva a lista de tarefas no arquivo (default `"todos.txt"`)

### Como usar (GUI)
1. Clone o repositório.
2. Instale a dependência FreeSimpleGUI, caso ainda não tenha.
3. Execute o arquivo gui.py no Python.

#### Como usar (Web App)
1. Abra `web.py` no Python.
2. Instale dependências:
```bash
pip install streamlit
streamlit run web.py
```