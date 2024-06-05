import functions
import FreeSimpleGUI as sg

label = sg.Text("Ingrese una tarea")
input_box = sg.InputText(tooltip="Escriba la tarea")
add_button = sg.Button("Agregar")

window = sg.Window('Mi aplicación de tareas por hacer', layout=[[label], [input_box, add_button]])
window.read()
window.close()
