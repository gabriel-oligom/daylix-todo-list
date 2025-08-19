import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    if new_todo.strip() != "":
        todos.append(new_todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


st.title("Daylix - Todo App")
st.subheader("This is my Task Manager App!!")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new todo...", 
              on_change=add_todo, key="new_todo") 