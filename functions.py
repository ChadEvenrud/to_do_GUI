def get_todos(filepath='files/todos.txt'):
    """ Reads a text file and returns list of todo items"""
    with open(filepath, 'r') as file:
            todo_local = file.readlines() 
    return todo_local

def write_todos(todos_arg, filepath='files/todos.txt'):
    """ Write a todo items list and stores in a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)        
        print('List updated')