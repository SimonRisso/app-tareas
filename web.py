import streamlit as st
import functions

tasks = functions.get_tasks()

def add_task():
    task = st.session_state["new_task"] + "\n"
    print(task)
    tasks.append(task)
    functions.write_tasks(tasks)

st.title("My todo App")
st.subheader("Esta es mi aplicación de cosas por hacer")
st.write("Está diseñada para aumentar tu productividad")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        print(checkbox)
        tasks.pop(index)
        functions.write_tasks(tasks)
        del st.session_state[task]
        st.rerun()
    
st.text_input(label="", placeholder="Agregue una tarea...", on_change=add_task, key="new_task")
