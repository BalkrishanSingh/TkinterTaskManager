from FuncClass import *
import tkinter as tk
from tkinter.font import Font
from tkinter.constants import DISABLED, END, INSERT, NORMAL

root = tk.Tk(className='TaskManager')
root.geometry('640x640')
root.resizable(False,False)
root.configure(bg='#C15E63')

task_list = TaskList()
main_font = Font(size=20)
titleFont = Font(size=35)

#Title Box
title_box = tk.Text(root,height=1,width=10,font=titleFont)
title_box.insert(INSERT,'Task Manager')
title_box.config(state=DISABLED)
title_box.place(x=195,y=50)

#Adding Tasks
content = tk.StringVar()
ask_task = tk.Entry(root,textvariable=content,bg='#439E56',width=30,font=Font(size=18))
ask_task.place(x=120,y=135)

add_task = tk.Button(
    root,text='Add Task',fg='#C15E63',font=main_font,
    command=Callback(get_task,task_list,content)
    )
add_task.place(x=470,y=134)

#Updating and Deleting Task
task_id = tk.StringVar()
index = tk.Entry(root,textvariable=task_id,width=5,bg='#439E56',font=Font(size=20))
index.place(x=110,y=180)
update = tk.Button(
    root,text='Update',font=main_font,fg='#C15E63',
    command=Callback(update,task_list,task_id,content)
    )
update.place(x=200,y=180)

completion = tk.Button(root,text='Status',font=main_font,fg='#C15E63',
    command=Callback(completed,task_list,task_id)
    )
completion.place(x=310,y=180)

delete = tk.Button(
    root,text='Delete',font=main_font,fg='#C15E63',
    command= Callback(delete,task_list,task_id)
)
delete.place(x=410,y=180)

#Showing Tasks
content_box = tk.Text(root,height=10,width=32,font=main_font)
content_box.config(state=DISABLED)
content_box.place(x=95,y=220)

Show_task = tk.Button(
    root,text='Show Task',fg='#C15E63',font=main_font,
    command=Callback(show_tasks,content_box,task_list)
    )
Show_task.place(x=245,y=460)

root.mainloop()