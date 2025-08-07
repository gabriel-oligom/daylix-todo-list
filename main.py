while True:
    user_act = input("Type add, show, edit, complete or exit: ")
    user_act = user_act.strip()

    if user_act.lower().startswith("add"):
        new_todo = user_act[4:] # Pega tudo após os 4 primeiros caracteres, ou seja, remove "add " do início

        # Etapa 1: abre arquivo "todos.txt" em modo leitura ("r")
        # e transforma o conteúdo em uma lista, cada linha é um item.
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(new_todo + "\n")

        # Etapa 2: abre arquivo em modo escrita ("w"), apaga o conteúdo anterior
        # e escreve toda a lista atualizada no arquivo, item por item.
        with open("todos.txt", "w") as file:
                file.writelines(todos)

    elif user_act.lower().startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")  # remove quebra de linha
            print(f"{index + 1}: {todo}")
        print(f"The length of the list is: {len(todos)}")

    elif user_act.lower().startswith("edit"):
        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            edition = int(user_act[5:])
            edition -= 1

            your_todo = input("Write your todo: ") + "\n"
            todos[edition] = your_todo

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except IndexError:
            print("Your command is not valid.")
            continue

    elif user_act.lower().startswith("complete"):
        try:
            number = int(user_act[9:])

            with open("todos.txt", "r") as file:
                todos = file.readlines() # lê

            index = number - 1
            todo_to_remove = todos[index].strip("\n") # modifica
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos) # escreve

            message = f"You removed the item '{todo_to_remove}' from the list"
            print(message)
        except (IndexError, ValueError):
            print("That number is not part of the list.")
            continue

    elif user_act.lower().startswith("exit"):
        print("Goodbye!")
        break
    else:
        print("Oops! It seems to have a mistake here.")