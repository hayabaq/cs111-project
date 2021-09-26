import tkinter as tk

def add():
    print('add')

def select_item():
    pass
def remove_item():
    pass
def update_item():
    pass
def clear_text():
    pass
LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (main, add):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(main)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        add_btn = tk.Button(self, text ="Add",command = lambda : controller.show_frame(add))
        add_btn.pack()
        remove_btn = tk.Button(self, text="Remove Part", width=10, command=remove_item)
        remove_btn.pack()
        update_btn = tk.Button(self, text="Update Part", width=10, command=update_item)
        update_btn.pack()
        clear_btn = tk.Button(self, text="Clear Input", width=10, command=clear_text)
        clear_btn.pack()
        scrollbar = tk.Scrollbar(self)
        todo_list = tk.Listbox(self, yscrollcommand = scrollbar.set )
        for line in range(100):
            todo_list.insert(tk.END, "This is line number " + str(line))
        scrollbar.pack()
        todo_list.pack()
        scrollbar.configure(command=todo_list.yview)
        todo_list.bind('<<ListboxSelect>>', select_item)

class add(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = tk.Button(self, text ="Dashboard",
                            command = lambda : controller.show_frame(main))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
      
app = tkinterApp()
app.title('Task Manager')
app.geometry('700x350')
app.mainloop()