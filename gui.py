import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("LightBlue3")
clock = sg.Text("", key="clock")
label = sg.Text("Type a To-Do:")
input_box = sg.InputText(tooltip="Enter to-do", key="to-do")
add_Button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="items",
                       enable_events=True, size=[40, 10])
edit_Button = sg.Button("Edit")
complete_Button = sg.Button("Complete")
exit_Button = sg.Button("Exit")
window = sg.Window("Daylix To-Do App",
                    layout=[[clock], 
                            [label],
                            [input_box,add_Button],
                            [list_box, edit_Button, complete_Button], 
                            [exit_Button]],
                            font=("Helvetica", 18))

while True:
    event, values = window.read(timeout=100) 
    window["clock"].update(value=time.strftime("%b %d, %Y, %H:%M:%S"))
   # print(1, event)
   # print(2, values)
   # print(3, values["items"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window["items"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["items"][0]
                new_todo = values["to-do"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["items"].update(values=todos)
            except IndexError:
                sg.popup("Please, select an item first.", font=("Helvetica", 15))
        case "Complete":
            try:
                todo_to_complete = values["items"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["items"].update(values=todos)
                window["to-do"].update(value="")
            except IndexError:
                sg.popup("Please, select an item first", font=("Helvetica", 15))
        case "Exit":
            break
        case "items":
            window["to-do"].update(value=values["items"][0])
        case sg.WIN_CLOSED:
            break

window.close()