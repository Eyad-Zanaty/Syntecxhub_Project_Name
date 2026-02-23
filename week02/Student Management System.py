import os
import json
import pandas as pd


class MangementSystem: # this class is responsible for adding, updating, deleting and listing students in the system
    def __init__(self, fileName=None):
        self.fileName= fileName
        os.chdir(os.path.dirname(os.path.abspath(__file__)))


    def add(self):
        '''This function adds a student to the system'''
        
        myFile= open(self.fileName, "r")
        json_myFile= json.load(myFile)
        
        while True:
            try:
                student_id= int(input("The student ID: ").strip())
                
                for student in json_myFile:
                    if student['id'] == student_id:
                        print("ID already exists, Please try again.")
                        raise ValueError("ID already exists")
                
                student_name= input("The student Name: ").strip().lower()
                student_grade= input("The student Grade: ").strip().lower()
                break
            
            except:
                print("Invalid input")
                continue
    
        json_myFile.append({
            "id": student_id,
            "name": student_name,
            "grade": student_grade
        })
        with open(self.fileName, "w") as f:
            json.dump(json_myFile, f, indent=4)
    
    
    
    def update(self):
        '''This function updates the name or grade of a student by their ID'''
        
        myFile= open(self.fileName, "r")
        json_myFile= json.load(myFile)
        while True:
            try:
                search_id= input("Input student ID: ")
                search_id= int(search_id)
                for i, student in enumerate(json_myFile):
                        data= input("What do you want to update? (name/grade): ").strip().lower()
                        
                        if data == 'name':
                            new_name= input("Input new name: ").strip().lower()
                            json_myFile[i]['name']= new_name
                            with open(self.fileName, "w") as f:
                                json.dump(json_myFile, f, indent=4)
                        
                        elif data == 'grade':
                            new_grade= input("Input new grade: ").strip().lower()
                            json_myFile[i]['grade']= new_grade
                            with open(self.fileName, "w") as f:
                                json.dump(json_myFile, f, indent=4)
                break
            except:
                print("Invalid input, Please try again.")
                continue
    
    
    def delete(self):
        '''This functon deletes a student from the json file by their ID'''
        
        while True:
            try:
                deleted_id= int(input("Input the id of student you want to delete: ").strip())
                
                with open(self.fileName, 'r') as f:
                    data= json.load(f)
                
                for counter, values in enumerate(data):
                    
                    if values['id'] == deleted_id:
                        del data[counter]

                        with open(self.fileName, 'w') as f:
                            json.dump(data, f, indent=4)
                        print("Student deleted successfully.")
                
                break
            except:
                print("Invalid input, Please try again.")
                continue
    
    
    
    def list(self):
        '''This function lists all students in the system'''
        
        with open(self.fileName, 'r') as f:
            data= json.load(f)
        
        # using pandas to print the data in a table format
        df= pd.DataFrame(data)
        print(df)



class Student: # this class is responsible for taking the user input and calling the appropriate function in the MangementSystem class
    def __init__(self, fileName=None):
        
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        self.fileName= f"{fileName}.json"
        
        if os.path.isfile(self.fileName) and os.access(self.fileName, os.R_OK):
            # checks if file exists
            print ("File exists and is readable")
        else:
            print ("Either file is missing or is not readable, creating file...")
            with open(self.fileName, 'w') as db_file:
                json.dump([], db_file)
        
        while True:
            self.user_input= input('''Please select:
1- Add
2- Update
3- Delete
4- List                          
''').strip().lower()
            if self.user_input in ['add', 'update', 'delete', 'list']:
                break
            else:
                print("Invalid input, Please try again.")
                continue
        
        self.dealing_with_input(self.user_input)
    
    
    def dealing_with_input(self, user_input):

        while True:
            if user_input == 'add':
                MangementSystem(self.fileName).add()
            elif user_input == 'update':
                MangementSystem(self.fileName).update()
            elif user_input == 'delete':
                MangementSystem(self.fileName).delete()
            elif user_input == 'list':
                MangementSystem(self.fileName).list()
            
            
            while True:
                ask_user= input("Do you want to do another operation? (y/n): ").strip().lower()
                if ask_user == 'y':
                    Student('students_grade')
                elif ask_user == 'n':
                    print("Goodbye!")
                    break
                break
            break



Student('students_grade')