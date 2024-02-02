'''
Description:
Create a simple to-do list application where users can add tasks, mark them as completed, and remove them. 
This project will involve basic concepts like user input, data storage, and simple logic.
'''
# to-do list application

def menu():
    print("""
 ---------------------
|        Menu         |
 ---------------------
|1| Add Task          |
|2| Display Tasks     |
|3| Remove Task       |
|4| Save and Exit     |
------------------------""")

class features:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
         
    def display_task(self):      
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
                  
    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            remove_task = self.tasks.pop(task_index-1)
            print(f"{remove_task} : task is remove")
        else:
            print("Invalid task index.")
         
    def save_task(self,filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("No saved to-do list found.")

    
         
todo_list = features()
todo_list.load_from_file('todo_list.txt')
while True:
    menu()

    opperation = input("Enter the number to do the task:")
    if opperation == '1':
        task = input("Enter the task: ")
        todo_list.add_task(task)

    elif opperation == '2':
        todo_list.display_task()

    elif opperation == '3':
        index = int(input("Enter the index of the task"))
        todo_list.remove_task(index)

    elif opperation == '4':
        todo_list.save_task('todo_list.txt')
        print("To-Do List saved. Exiting...")
        break
    else:
        print("Please select from 1 to 4")   

