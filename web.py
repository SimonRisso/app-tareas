import streamlit as st
import functions

tasks = functions.get_tasks()

st.title("My todo App")
st.subheader("Esta es mi aplicación de cosas por hacer")
st.write("Está diseñada para aumentar tu productividad")

for task in tasks:
    st.checkbox(task)
    
st.text_input(label="", placeholder="Agregue una tarea...")