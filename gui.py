import functions
import FreeSimpleGUI as sg

label = sg.Text("Type a To-Do:")
input_box = sg.InputText()
add_Button = sg.Button("Add")

window = sg.Window("Daylix To-Do App", layout=[[label], [input_box, add_Button]])
window.read()
window.close()