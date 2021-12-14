import tkinter as tk
app = tk.Tk()
equation = ""
result=""

def clear():
    global equation, result
    equation=""
    result=""
    text.set(0)
def sign():
    global equation, result
    try:
        tmp =text.get()
        if tmp != 0:
            result = int(tmp)* -1
            equation=equation.replace(tmp,str(result))
            text.set(result)
    except:
        text.set("Error")
        result=""
        equation=""
def store(num):
    global equation, result
    try:
        if not num.isnumeric() and equation=="" and result=="":
            equation="0"+num
        elif not num.isnumeric() and equation=="" and result!="":
            equation=result+num
        elif len(equation.split())==3 and not num.isnumeric():
            calculate()
            equation=result+num
        elif num.isnumeric():
            equation+=num
            if len(equation.split())==1:
                text.set(equation.split()[0])
            elif len(equation.split())==3:
                text.set(equation.split()[2])
        else:
            equation+=num
        print(equation)
    except:
        text.set("Error")
        equation=""
        result="" 
def calculate():
    global equation , result
    try:
        if equation=="" and result=="":
            text.set(str(0))  
        else:    
            result= str(eval(equation))
            text.set(result)
            equation=""
    except:
        text.set("Error")
        equation=""
        result=""

#Entry window 
text = tk.StringVar()
screen = tk.Entry(app, textvariable =text , state='readonly').grid(row=0, column=0, columnspan=4 ,sticky="nesw")
#Buttons matrix 
clearbtn = tk.Button(app, text='AC',highlightbackground='grey', command=clear).grid(row=1, column=0,sticky="nesw")
signbtn = tk.Button(app, text='+/-',highlightbackground='grey', command=sign).grid(row=1, column=1,sticky="nesw")
remainderbtn = tk.Button(app, text='%',highlightbackground='grey', command=lambda:store(' % ')).grid(row=1, column=2,sticky="nesw")
dividebtn = tk.Button(app, text='÷',highlightbackground='grey', command=lambda:store(' / ')).grid(row=1, column=3,sticky="nesw")
btn7 = tk.Button(app, text='7',highlightbackground='grey', command=lambda:store('7')).grid(row=2, column=0,sticky='nesw')
btn8 = tk.Button(app, text='8',highlightbackground='grey', command=lambda:store('8')).grid(row=2, column=1,sticky='nesw')
btn9 = tk.Button(app, text='9',highlightbackground='grey', command=lambda:store('9')).grid(row=2, column=2,sticky='nesw')
multiplybtn = tk.Button(app, text='x',highlightbackground='grey', command=lambda:store(' * ')).grid(row=2, column=3,sticky='nesw')
btn4 = tk.Button(app, text='4',highlightbackground='grey', command=lambda:store('4')).grid(row=3, column=0,sticky='nesw')
btn5 = tk.Button(app, text='5',highlightbackground='grey', command=lambda:store('5')).grid(row=3, column=1,sticky='nesw')
btn6 = tk.Button(app, text='6',highlightbackground='grey', command=lambda:store('6')).grid(row=3, column=2,sticky='nesw')
minusbtn = tk.Button(app, text='-',highlightbackground='grey', command=lambda:store(' - ')).grid(row=3, column=3,sticky='nesw')
btn1 = tk.Button(app, text='1',highlightbackground='grey', command=lambda:store('1')).grid(row=4, column=0,sticky='nesw')
btn2 = tk.Button(app, text='2',highlightbackground='grey', command=lambda:store('2')).grid(row=4, column=1,sticky='nesw')
btn3 = tk.Button(app, text='3',highlightbackground='grey', command=lambda:store('3')).grid(row=4, column=2,sticky='nesw')
plusbtn = tk.Button(app, text='+',highlightbackground='grey', command=lambda:store(' + ')).grid(row=4, column=3,sticky='nesw')
btn0 = tk.Button(app, text='0',highlightbackground='grey', command=lambda:store('0')).grid(row=5, columnspan=2, column=0,sticky='nesw')
dotbtn = tk.Button(app, text='.',highlightbackground='grey', command=lambda:store('.')).grid(row=5, column=2,sticky='nesw')
equalbtn = tk.Button(app, text='=',highlightbackground='grey', command=calculate).grid(row=5, column=3,sticky='nesw')
#Application title
app.title('Calculator')
#Initial window's size
app.geometry('350x400')
#Make the button responsive when the window's size change
for i in range(6):
    app.grid_rowconfigure(i,  weight =1)
for i in range(4):
    app.grid_columnconfigure(i,  weight =1)
app.mainloop()