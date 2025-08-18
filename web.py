import streamlit as st
import functions

todos = functions.get_todos()

def add_todos():
    user_new_todo = st.session_state["new_todo"]
    todos.append(user_new_todo)
    functions.write_todos(todos)


st.title("Daylix - Todo App")
st.subheader("This is my Task Manager App!!")

st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...", 
              on_change=add_todos, key="new_todo") 
