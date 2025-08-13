# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y, %H:%M:%S")
print(f"It is {now}") 

while True:
    user_act = input("Type add, show, edit, complete or exit: ")
    user_act = user_act.strip()

    if user_act.lower().startswith("add"):
        new_todo = user_act[4:] # pega tudo após os 4 primeiros caracteres, ou seja, remove "add " do início

        todos = functions.get_todos() # chama get_todos com argumento padrão filepath="todos.txt"

        todos.append(new_todo + "\n")

        functions.write_todos(todos_arg=todos, filepath="todos.txt") # não é necessário escrever o filepath, pode deixar apenas o "todos"

    elif user_act.lower().startswith("show"):
        todos = functions.get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")  # remove quebra de linha
            print(f"{index + 1}: {todo}")
        print(f"The length of the list is: {len(todos)}")

    elif user_act.lower().startswith("edit"):
        try:
            todos = functions.get_todos()

            edition = int(user_act[5:])
            edition -= 1

            your_todo = input("Write your todo: ") + "\n"
            todos[edition] = your_todo

            functions.write_todos(todos) # default argument

        except IndexError:
            print("Your command is not valid.")
            continue

    elif user_act.lower().startswith("complete"):
        try:
            number = int(user_act[9:])

            todos = functions.get_todos() # lê (uso de função)

            index = number - 1
            todo_to_remove = todos[index].strip("\n") # modifica
            todos.pop(index)

            functions.write_todos(todos) # escreve (uso de função)

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