import os # making current directory dynamic


def file_handling(fileName, method= 'r', value= '', tag= '', *args):
    '''This function handles file operations for the To-Do List Manager based on the provided method and parameters'''
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    myFile= open(fileName, method)
    
    lines= myFile.readlines()
    
    if method == 'a+':
        
        myFile.write(f'{tag}: {value}\n')
    
    
    elif method == 'r+' and 'delete' in value.split('-'):
        
        myFile.seek(0)
        for line in lines:
            if line.split(':')[1].strip() != value.split('-')[0]:
                myFile.write(line)
        myFile.truncate()
    
    elif method == 'r+' and 'done' in value.split('-'):
        
        myFile.seek(0)
        for line in lines:
            if line.split(':')[1].strip() != value.split('-')[0]:
                myFile.write(line)
            else:
                myFile.write(f'{line.split(":")[0]}: {line.split(":")[1].strip()} - done\n')
        myFile.truncate()
    
    elif method == 'r':
        
        for line in lines:
            if line != ' ' and tag in line.split(':')[0].strip().lower() :
                print(line.split(':')[1].strip())
    
    myFile.close()



def display_menu():
    '''This function displays the menu and handles user input for the To-Do List Manager'''
    
    while True: # This loop will continue until the user decides to exit the program
        
        while True: # This loop will continue until the user provides valid input for the action and tag
            try:
                action= input('''Tasks:
- Add
- View
- Delete
- Mark
''')
                tag= input('''Choose your task tag:
- Personal
- Work
''')
                action= action.strip().lower()
                tag= tag.strip().lower()
                break
            
            except ValueError:
                continue
        
        answers= ['add', 'view', 'delete', 'mark']
        tags= ['personal', 'work']
        
        if action in answers and tag in tags: # This condition checks if the user input for action and tag is valid
            if action == 'add':
                
                while True:
                    try:
                        value= input('Add your task: ')
                        value.strip().lower()
                        break
                    except ValueError:
                        continue
                    
                myFile= file_handling('myFile.txt', 'a+', f'{value}', f'{tag}')
            
            if action == 'view':
                
                myFile= file_handling('myFile.txt', 'r', '', tag= f'{tag}')
            
            if action == 'delete':
                
                value= input('Delete your task: ')
                value.strip().lower()
                myFile= file_handling('myFile.txt', 'r+', f'{value}-delete', f'{tag}')
            
            if action == 'mark':
                value= input('Mark your done task: ')
                value.strip().lower()
                myFile= file_handling('myFile.txt', 'r+', f'{value}-done', f'{tag}')
        
        else:
            print('Invalid input. Please try again.')
            continue
        
        while True: # This loop will continue until the user provides valid input for replaying the program
            replay= input('Do you want to continue? (yes/no): ')
            if replay.strip().lower() == 'yes':
                break
            
            elif replay.strip().lower() == 'no':
                print('Goodbye!')
                return 0
                
            
            else:
                print('Invalid input. Please try again.')
                continue


display_menu()