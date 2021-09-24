from tkinter import *
app = Tk()

#Add new item
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



def main():
    # Buttons
    def add_item():
        add_btn.destroy()
        remove_btn.destroy()
        update_btn.destroy()
        clear_btn.destroy()
        scrollbar.destroy()
        todo_list.destroy()
        task_label = Label(app,text='Task')
        task_label.pack()
        task_text= Text(app)
        task_text.pack()
        def back():
            main()
        back_btn = Button(app, text="Add Part",bg='blue', width=10, command=back)
        back_btn.pack()
    add_btn = Button(app, text="Add Part",bg='blue', width=10, command=add_item)
    add_btn.pack()
    remove_btn = Button(app, text="Remove Part", width=10, command=remove_item)
    remove_btn.pack()
    update_btn = Button(app, text="Update Part", width=10, command=update_item)
    update_btn.pack()
    clear_btn = Button(app, text="Clear Input", width=10, command=clear_text)
    clear_btn.pack()
    scrollbar = Scrollbar(app)
    todo_list = Listbox(app, yscrollcommand = scrollbar.set )
    for line in range(100):
        todo_list.insert(END, "This is line number " + str(line))
    scrollbar.pack()
    todo_list.pack()
    scrollbar.configure(command=todo_list.yview)
    todo_list.bind('<<ListboxSelect>>', select_item)
    

app.title('Todo List')
app.geometry('360x700')
main()
app.mainloop()