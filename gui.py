import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass
    
sg.theme("DarkBrown6")

clock = sg.Text("", key="clock")
label = sg.Text("Ingrese una tarea")
input_box = sg.InputText(tooltip="Escriba la tarea", key="tarea")
add_button = sg.Button("Agregar", size=10)
list_box = sg.Listbox(values=functions.get_tasks(), key="tareas",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Editar")
complete_button = sg.Button("Completada")
exit_button = sg.Button("Salir")

window = sg.Window('Mi aplicación de tareas por hacer',
                   layout=[[clock],
                           [label], 
                           [input_box, add_button], 
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Agregar":
            tasks = functions.get_tasks()
            new_task = values['tarea'] + "\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window["tareas"].update(values=tasks)
            
        case "Editar":
            try:
                task_to_edit = values["tareas"][0]
                new_task = values["tarea"]
                
                tasks = functions.get_tasks()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task
                functions.write_tasks(tasks)
                window["tareas"].update(values=tasks)
            except IndexError:
                sg.popup("Por favor, primero seleccione una tarea", font=("Helvetica", 20))
        case "Completada":
            try:
                task_completed = values["tareas"][0]
                
                tasks = functions.get_tasks()
                tasks.remove(task_completed)
                functions.write_tasks(tasks)
                window["tareas"].update(values=tasks)
                window["tarea"].update(value="")
            except IndexError:
                sg.popup("Por favor, primero seleccione una tarea", font=("Helvetica", 20))
        case "Salir":
            break
        case "tareas":
            window["tarea"].update(value=values["tareas"][0])
        case sg.WIN_CLOSED:
            break
            
window.close()
