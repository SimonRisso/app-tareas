import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("Es", now)
while True:
    user_action = input("Escriba agregar, mostrar, editar, completada o salir: ")
    user_action = user_action.strip().lower()
    
    if user_action.startswith('agregar'):
        user_task = user_action[8:]
        print(user_task)
        
        tasks = functions.get_tasks()
    
        tasks.append(user_task + "\n")
        
        functions.write_tasks(tasks)
                
    elif user_action.startswith('mostrar'):
        tasks = functions.get_tasks()
        
        # new_tasks = []
        
        # for task in tasks:
        #     new_task = task.strip("\n")
        #     new_tasks.append(new_task)
        
        # new_tasks = [task.strip("\n") for task in tasks]
        
        for index, task in enumerate(tasks):
            task = task.strip("\n")
            chain = f"{index + 1}-{task}"
            print(chain)
            
    elif user_action.startswith('editar'):
        try:
            number = int(user_action[7:])
            number -= 1
            
            tasks = functions.get_tasks()
            
            new_task = input(f"Edite la tarea: ") 
            tasks[number] = new_task + "\n"
            
            functions.write_tasks(tasks)
        except ValueError:
            print("Indique el número de la tarea a editar seguido del comando 'editar'.")
            continue
            
    elif user_action.startswith('completada'):
        try:
            number = int(user_action[10:])
            
            tasks = functions.get_tasks()
            
            index = number - 1
            task_to_remove = tasks[index].strip("\n")
            tasks.pop(index)
            
            functions.write_tasks(tasks)
            
            message = f"La tarea '{task_to_remove}' fue removida"
            print(message)
        except IndexError:
            print("No hay un artículo con ese número.")
            continue
            
    elif user_action.startswith('salir'):
        break 
    
    else:
        print("Comando inválido")

print("El programa terminó!")

