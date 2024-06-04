FILEPATH = 'todos.txt'

def get_tasks(filepath=FILEPATH):
    """ Lee un archivo txt y devuelve una lista de las tareas por hacer """
    with open(filepath, 'r') as file:
        tasks_local = file.readlines()
    return tasks_local

def write_tasks(tasks_arg, filepath=FILEPATH):
    """ Escribe la lista de tareas para hacer en el archivo de texto """
    with open(filepath, 'w') as file:
        file.writelines(tasks_arg)    
        
print(__name__)

if __name__ == "__main__":
    print("Hola")
    print(get_tasks())
    
