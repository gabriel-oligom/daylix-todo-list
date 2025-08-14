import functions
import FreeSimpleGUI as sg

label = sg.Text("Type a To-Do:")
input_box = sg.InputText(tooltip="Enter to-do", key="to-do")
add_Button = sg.Button("Add")

window = sg.Window("Daylix To-Do App",
                    layout=[[label],[input_box,add_Button]],
                    font=("Helvetica", 18))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()