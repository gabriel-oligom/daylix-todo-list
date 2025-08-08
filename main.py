def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    user_act = input("Type add, show, edit, complete or exit: ")
    user_act = user_act.strip()

    if user_act.lower().startswith("add"):
        new_todo = user_act[4:] # Pega tudo após os 4 primeiros caracteres, ou seja, remove "add " do início

        todos = get_todos(filepath="todos.txt")

        todos.append(new_todo + "\n")

        write_todos(filepath="todos.txt", todos_arg=todos)

    elif user_act.lower().startswith("show"):
        todos = get_todos("todos.txt")

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")  # remove quebra de linha
            print(f"{index + 1}: {todo}")
        print(f"The length of the list is: {len(todos)}")

    elif user_act.lower().startswith("edit"):
        try:
            todos = get_todos("todos.txt")

            edition = int(user_act[5:])
            edition -= 1

            your_todo = input("Write your todo: ") + "\n"
            todos[edition] = your_todo

            write_todos("todos.txt", todos)

        except IndexError:
            print("Your command is not valid.")
            continue

    elif user_act.lower().startswith("complete"):
        try:
            number = int(user_act[9:])

            todos = get_todos("todos.txt") # lê (uso de função)

            index = number - 1
            todo_to_remove = todos[index].strip("\n") # modifica
            todos.pop(index)

            write_todos("todos.txt", todos) # escreve (uso de função)

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