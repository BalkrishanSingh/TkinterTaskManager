import tkinter as tk
from types import NoneType
from typing import List, Text
from datetime import datetime
from tkinter.font import Font
from tkinter.constants import DISABLED, END, INSERT, NORMAL

def binary_search(list,target):
    if isinstance(target,str) or target == '':
        try:
            target = int(target)
        except :
            print('Invalid Input')
        
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first+last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None
def delete_task(TaskList,position):
    try:
        del TaskList[position]
        for task in TaskList[position:]:
            task.id -= 1
    except ValueError:
        print('Invalid Input')

class Task:
    def __init__(self,id:int,content:str) -> None:
        self.id = id
        self.content = content
        self.status:bool = False
        self.last_modified:datetime = datetime.now().__str__()

    def update_content(self,updated_content):
        self.content = updated_content
        self.last_modified = datetime.now().__str__()

    def update_status(self,updated_status:bool):
        self.status = updated_status
        self.last_modified = datetime.now().__str__()

    def __str__(self) -> str:
        return f"Task ID:{self.id}\nContent: {self.content}\nCompleted: {self.status}\nLast Modified: {self.last_modified}\n"
class TaskList:
    def __init__(self):
        self.list:list = []
        
    def add_task(self,content):
        id = (len(self.list)+1)
        task = Task(id,content)
        self.list.append(task)

    def get_task_id(self,id:int):
        id_list = [task.id for task in self.list]
        position = binary_search(id_list,id)
        if position is not None:
            return position

    def update_task(self,id:int,content):
        position = self.get_task_id(id)
        try:
            task = self.list[position]
        except:
            print('Invalid Input')
        else:
            if content != '':
                task.content = content
            task.last_modified = datetime.now().__str__()

    def delete_task(self,id):
        position = self.get_task_id(id)
        delete_task(self.list,position)

    def update_status(self,id):
        task_pos = self.get_task_id(id)
        if self.list[task_pos].status == False:
            self.list[task_pos].status = True
        else:
            self.list[task_pos].status = False
    def __len__(self):
        return len(self.list)

    def __str__(self) -> str:
        list =  [task.__str__() for task in self.list]
        str = '\n'.join(list)
        return str
    
class Callback:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    def __call__(self):
        self.func(*self.args, **self.kwargs)
        
def get_task(TaskList,StringVar):
    TaskList.add_task(StringVar.get())

def show_tasks(Text,TaskList):
    Text.config(state=NORMAL)
    Text.delete(1.0,END)
    Text.insert(INSERT,TaskList.__str__())
    Text.config(state=DISABLED)

def update(TaskList,TextVar,ContentVar):
    id = TextVar.get()
    content = ContentVar.get()
    TaskList.update_task(id,content)

def delete(TaskList,TextVar):
    id = TextVar.get()
    try:
        id = int(id)
        TaskList.delete_task(id)
    except:
        print('Invalid Input')
def completed(TaskList,TextVar):
    try:
        id = TextVar.get()
        TaskList.update_status(id)
    except:
        print('Invalid Input')
    
        