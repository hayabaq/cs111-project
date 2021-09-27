import tkinter as tk
from tkcalendar import Calendar
#class something():

LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
    todo = [['xyz','20,sep'],['thing2','22,sep']]
    def add(self, task):
        todo.append()

    def select_item(self, event):
        print('select')

    def remove_item(self):
        print('remove')

    def update_item(self):
        print('update')

    def clear_text(self):
        print('clear')

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {} 
        for F in (main, add):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(main)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        add_btn = tk.Button(self, text ="Add",command = lambda : controller.show_frame(add))
        add_btn.pack()
        scrollbar = tk.Scrollbar(self)
        todo_list = tk.Listbox(self, yscrollcommand = scrollbar.set )
        for line in controller.todo:
            todo_list.insert(tk.END, str(line[0]+" "+line[1]))
        scrollbar.pack()
        todo_list.pack()
        scrollbar.configure(command=todo_list.yview)
        todo_list.bind('<<ListboxSelect>>', controller.select_item)

class add(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text ="Page 1", font = LARGEFONT)
        label.pack()
        label1 = tk.Label(self,text="Task: ")
        label1.pack()
        task = tk.Text(self,height=5, width=40)
        task.pack( )
        label2 = tk.Label(self,text="Due to: ")
        label2.pack()
        dueDate= tk.StringVar()
        due = tk.Entry(self, textvariable =dueDate)
        due.pack( )
        cal = Calendar(self, selectmode='day', year=2021, month=9, day=27)
        cal.pack(fill="both")
        button3 = tk.Button(self, text ="pick", command=lambda:dueDate.set(cal.selection_get()))
        button3.pack()
        button2 = tk.Button(self, text ="Submit",
                            command = controller.add)
        button2.pack()
        button1 = tk.Button(self, text ="Dashboard",
                            command = lambda : controller.show_frame(main))
        button1.pack()
        
      
app = tkinterApp()
app.title('Task Manager')
app.geometry('700x350')
app.mainloop()