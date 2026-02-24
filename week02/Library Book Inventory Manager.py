import os
import json
import pandas as pd

class LibraryInventoryManager: # This class manages the inventory of books in a library, allowing users to issue and return books.
    def __init__(self, fileName= 'inventory'):
        self.fileName= f"{fileName}.json"
        
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        if os.path.isfile(self.fileName) and os.access(self.fileName, os.R_OK):
            pass
        else:
            print ("Either file is missing or is not readable, creating file...")
            with open(self.fileName, 'w') as db_file:
                json.dump([], db_file)
        
        while True:
            self.book_search=input('Input the Book name: ').strip().lower()
            self.issue_or_return= input('Do you want to (Issue/Return): ').strip().lower()
            
            if self.issue_or_return== 'issue':
                self.issue()
                break
            elif self.issue_or_return== 'return':
                self.return_book()
                break
            else:
                print('Invalid input. Please enter "Issue" or "Return".')
                continue
        
        
    
    
    def issue(self):
        ''' This function allows a user to issue a book from the library inventory. It checks if the book is available, and if so, it collects user information and updates the inventory accordingly.'''
        
        with open(self.fileName, 'r') as f:
            data= json.load(f)
        
        
        for counter, book in enumerate(data):
            if book['title'] == self.book_search and book['count'] > 0:
                print('Book is available.')
                user_name= input('Input your name: ').strip().lower()
                phone_number= input('Input your phone number: ').strip()
                
                while True:
                    try:
                        number_of_days= int(input('Input number of days you want to issue the book: ').strip())
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid integer for the number of days.")
                
                data[counter]['count'] -= 1
                print(f"{user_name} has issued {book['title']}.")
                
                issue_key = f"{user_name}_{self.book_search}"
                
                book['issue'][issue_key] = {
                    'user': user_name,
                    'phone': phone_number,
                    'issue_date': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'days': number_of_days
                }
                
                break
            
            else:
                print('Book is not available.')

        
        with open(self.fileName, 'w') as f:
            json.dump(data, f, indent=4)
    
    
    def return_book(self):
        '''This function allows a user to return a book to the library inventory. It checks if the book was issued to the user, and if so, it updates the inventory accordingly.'''
        
        with open(self.fileName, 'r') as f:
            data= json.load(f)
            
            user_name= input('Input your name: ').strip().lower()
            
            for counter, book in enumerate(data):
                if book['title'] == self.book_search and f'{user_name}_{self.book_search}' in book['issue']: # Check if the book title matches and if the user has issued that book
                    data[counter]['count'] += 1
                    print(f"{user_name} has returned {book['title']}.")
                    del book['issue'][f'{user_name}_{self.book_search}']
                    break
                    
            with open(self.fileName, 'w') as f:
                json.dump(data, f, indent=4)



class Book: # This class manages the inventory of books in a library
    def __init__(self, fileName= 'inventory'):
        
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        self.fileName= f"{fileName}.json"
        
        if os.path.isfile(self.fileName) and os.access(self.fileName, os.R_OK):
            pass
        else:
            print ("Either file is missing or is not readable, creating file...")
            with open(self.fileName, 'w') as db_file:
                json.dump([], db_file)
        
        while True:
            action= input("Enter 'add' to add a book, 'remove' to remove a book, or 'view' to view the inventory: ").strip().lower()
            
            if action == 'add':
                self.add()
                break
            elif action == 'remove':
                self.remove()
                break
            elif action == 'view':
                self.view()
                break
            
        while True:
            ask_user= input("Do you want to do another operation? (y/n): ").strip().lower()
            if ask_user == 'y':
                Book()
            elif ask_user == 'n':
                print("Goodbye!")
                break
            break
        
    
    def add(self):
        '''This function adds a book to the inventory'''
        
        with open(self.fileName, 'r') as file:
            data = json.load(file)
        
        while True:
            title= input("Enter the book title: ").strip()
            author= input("Enter the book author: ").strip()
            
            try:
                inventory_number= int(input("Enter the book inventory number: ").strip())
            
            except ValueError:
                print("Invalid input. Please enter a valid integer for the inventory number.")
                continue
            
            if title and author and inventory_number:
                break
            else:
                print("All fields are required. Please try again.")
                continue
        
        data.append({
            'title': title,
            'author': author,
            'count': inventory_number,
            'issue': {}
        })
        
        with open(self.fileName, 'w') as file:
            json.dump(data, file, indent=4)
    
    
    
    def remove(self):
        '''This function removes a book from the inventory'''
        
        with open(self.fileName, 'r') as file:
            data = json.load(file)
        
        title_to_remove = input("Enter the title of the book to remove: ").strip()
        
        data = [book for book in data if book['title'] != title_to_remove]
        
        with open(self.fileName, 'w') as file:
            json.dump(data, file, indent=4)
    
    
    
    def view(self):
        '''This function displays the inventory of books'''
        
        with open(self.fileName, 'r') as file:
            data = json.load(file)
        
        if not data:
            print("The inventory is empty.")
        else:
            # Create a DataFrame from the data
            df= pd.DataFrame(data)
            df.drop(columns=['issue'], inplace=True)
            print(df)
            
            # Create a DataFrame to calculate the total number of inventory books and issued books
            dp= pd.DataFrame(data)
            print(f"number of books in inventory: {df['count'].sum()}")
            print("number of issued books: ", dp['issue'].apply(len).sum())
            print(f"total number of books: {df['count'].sum() + dp['issue'].apply(len).sum()}")



password= '0123456789' # I can put it in .env file but I didn't make it for testing

while True:
    ask= input("select your role(User/Manager): ").strip().lower()

    if ask== 'user':
        LibraryInventoryManager()
        break
    
    elif ask== 'manager':
        ask_password= input('Input your password: ').strip()
        
        if ask_password== password:
            print("Welcome!")
            Book()
            break
        
        else:
            print('Sorry! Invalid password')
            break
    else:
        print('Invalid input. Please enter "User" or "Manager".')
        continue
