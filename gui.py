import functions
import FreeSimpleGUI as sg

label = sg.Text("Ingrese una tarea")
input_box = sg.InputText(tooltip="Escriba la tarea", key="tarea")
add_button = sg.Button("Agregar")
list_box = sg.Listbox(values=functions.get_tasks(), key="tareas",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Editar")

window = sg.Window('Mi aplicación de tareas por hacer',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["tareas"])
    match event:
        case "Agregar":
            tasks = functions.get_tasks()
            new_task = values['tarea'] + "\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window["tareas"].update(values=tasks)
            
        case "Editar":
            task_to_edit = values["tareas"][0]
            new_task = values["tarea"]
            
            tasks = functions.get_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            functions.write_tasks(tasks)
            window["tareas"].update(values=tasks)
            
        case "tareas":
            window["tarea"].update(value=values["tareas"][0])
            
        case sg.WIN_CLOSED:
            break
            
window.close()
