import tkinter as tk
app = tk.Tk()
equation = ""

def clear():
    global equation
    equation=""
    text.set(0)
def sign():
    #print(text.get())
    if text.get() != 0:
        tmp = int(text.get())* -1
        text.set(tmp)
        #print("hurray")
def store(num):
    global equation 
    if num.isnumeric():
        text.set(num)
    equation= equation+str(num)
    print(equation)
def calculate():
    global equation 
    result= str(eval(equation))
    equation=result
    text.set(result)
text = tk.StringVar()
screen = tk.Entry(app, textvariable =text).grid(row=0, column=0, columnspan=4 )
clearbtn = tk.Button(app, text='AC', command=clear).grid(row=1, column=0)
signbtn = tk.Button(app, text='+/-', command=sign).grid(row=1, column=1)
remainderbtn = tk.Button(app, text='%', command=lambda:store('%')).grid(row=1, column=2)
dividebtn = tk.Button(app, text='÷', command=lambda:store('/')).grid(row=1, column=3)
btn7 = tk.Button(app, text='7', command=lambda:store('7')).grid(row=2, column=0)
btn8 = tk.Button(app, text='8', command=lambda:store('8')).grid(row=2, column=1)
btn9 = tk.Button(app, text='9', command=lambda:store('9')).grid(row=2, column=2)
multiplybtn = tk.Button(app, text='x', command=lambda:store('*')).grid(row=2, column=3)
btn4 = tk.Button(app, text='4', command=lambda:store('4')).grid(row=3, column=0)
btn5 = tk.Button(app, text='5', command=lambda:store('5')).grid(row=3, column=1)
btn6 = tk.Button(app, text='6', command=lambda:store('6')).grid(row=3, column=2)
minusbtn = tk.Button(app, text='-', command=lambda:store('-')).grid(row=3, column=3)
btn1 = tk.Button(app, text='1', command=lambda:store('1')).grid(row=4, column=0)
btn2 = tk.Button(app, text='2', command=lambda:store('2')).grid(row=4, column=1)
btn3 = tk.Button(app, text='3', command=lambda:store('3')).grid(row=4, column=2)
plusbtn = tk.Button(app, text='+', command=lambda:store('+')).grid(row=4, column=3)
btn0 = tk.Button(app, text='0', command=lambda:store('0')).grid(row=5, columnspan=2, column=1)
dotbtn = tk.Button(app, text='.', command=lambda:store('.')).grid(row=5, column=2)
equalbtn = tk.Button(app, text='=', command=calculate).grid(row=5, column=3)

app.title('Calculator')
#app.geometry('350x400')
app.mainloop()