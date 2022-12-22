from functions import get_todos, write_todos
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
if __name__ == '__main__':
    

    print(f"Hello Today is: {now}")

    while True:
        user_action = input("Enter, Show, Edit, Complete, Exit: ")
        # Need to reasign the variable. The strip method only returns a new string and not reasign the variable.
        user_action = user_action.strip().lower()
        
        if user_action.startswith('add'):
            
            todo_item = user_action[4:] + '\n'            
            
            todo = get_todos()             
                
            todo.append(todo_item)             
                
            write_todos( todo)  
                                             
        elif user_action.startswith('show'):      
            
            todo = get_todos()                                    
            
            for index, items in enumerate(todo):
                items = items.strip('\n')
                row = f"{index + 1}-{items}"
                print(row)
        
        elif user_action.startswith('edit'):
            
            try:
                number = int(user_action[5:])               
                number = number - 1  
                    
                todo = get_todos() 
                                                                
                print(f"You have selected {todo[number]}")
                todo[number] = input('Enter new todo: ')
            
                write_todos( todo)
                
            except ValueError:
                print('Your command is not valid.')
                continue  
            # Continue will rerun the loop.
        
        elif user_action.startswith('complete'):
            try:            
    
                completed_item = int(user_action[9:])                    
                todo = get_todos()     
                todo.pop(completed_item-1)
                
                write_todos( todo)
                    
            except IndexError:
                print('No item with that number')
                continue
        
        elif 'exit' in user_action:
            break
        
        else:
            print('Invalid command.')                
    print("Goodbye")
                