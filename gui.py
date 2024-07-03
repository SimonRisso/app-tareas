import functions
import FreeSimpleGUI as sg

label = sg.Text("Ingrese una tarea")
input_box = sg.InputText(tooltip="Escriba la tarea", key="tarea")
add_button = sg.Button("Agregar")

window = sg.Window('Mi aplicación de tareas por hacer',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Agregar":
            tasks = functions.get_tasks()
            new_task = values['tarea'] + "\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
        case sg.WIN_CLOSED:
            break
        
window.close()
