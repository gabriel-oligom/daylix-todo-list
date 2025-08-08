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
- `main.py`: código principal
- `todos.txt`: arquivo para salvar as tarefas

### 🧱 Estrutura do Código
O código está organizado com funções para:
* `get_todos(filepath)`: lê as tarefas do arquivo e retorna uma lista (`todos`)
* `write_todos(filepath, todos)`: recebe a lista de tarefas (`todos`) e salva no arquivo

### Como usar  
1. Clone o repositório  
2. Execute no terminal `python main.py` ou `py main.py` (requer Python instalado)  
3. Siga as instruções na tela  

#### 📌 Observações Importantes
- O projeto é uma versão inicial e vai receber melhorias, como:
  - Validação de entrada
  - Interface gráfica no futuro