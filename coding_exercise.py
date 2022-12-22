user_action  = input('Enter the country you are from: ')
user_action = user_action.lower()

match user_action:
    case "USA":
        print("Hello")
    
    case "India":
        print("Namasta")
    
    case "Germany":
        print("Hallo")
    
    case _:
        print("I do not know that country")