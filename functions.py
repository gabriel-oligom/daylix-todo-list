FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Lê um arquivo de texto e retorna uma lista de itens to-do. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH): # default parameters come AFTER the required parameters in the function
    """ Escreve a lista de itens to-do em um arquivo de texto. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

