class Todo: 
    def __init__(self,tid,title,description):
        self.tid = tid 
        self.title = title 
        self.description = description
        self.is_completed = False 
    def display(self):
        text = f"ID: {self.tid}\nTitle: {self.title}\nDescription: {self.description}\nIs Completed: {self.is_completed}"
        print(text)
    def display_partial(self):
        text = f"ID: {self.tid}\nTitle: {self.title}"
        print(text)
    def get_id(self):
        return self.tid
    def set_status(self,status):
        self.is_completed = status 
        
tid = 1 
title = "Python class"
description = "Classes & Objects"
todo1 = Todo(tid,title,description)
# print(todo1.tid)
# print(todo1.title)
# print(todo1.description)
# print(todo1.is_completed)
# todo1.display()
# todo1.display_partial()
# print(todo1.get_id())
todo1.set_status(True)
todo1.set_status(False)
todo1.display()
