from objectives import Objective


class ToDoList:
    def __init__(self):
        self.objective_list = []

    def add_objective(self):
        while True:
            name = input("What do you want to name this Todo? > ")
            
