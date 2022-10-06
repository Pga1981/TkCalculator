from curses.textpad import Textbox
from tkinter import *
from tkmacosx import Button

root = Tk()
root.configure(background='#4496f1')
root.title('TkCalculator')
root.geometry('386x188')

equation = StringVar()

def clear():
    equation.set('')

def press(num):
    equation.set(equation.get() + str(num))

def equalpress():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set('error')

expression_entry = Entry(root,textvariable=equation)
expression_entry.grid(row=0, columnspan=4,sticky='nswe')

btn7 = Button(root, text=' 7 ', fg='#000000', background='#efcb0c',command=lambda: press(7))
btn7.grid(row=1, column=0, sticky='nswe')

btn8 = Button(root, text=' 8 ', fg='#000000', background='#efcb0c',command=lambda: press(8))
btn8.grid(row=1, column=1, sticky='nswe')

btn9 = Button(root, text=' 9 ', fg='#000000', background='#efcb0c',command=lambda: press(9))
btn9.grid(row=1, column=2, sticky='nswe')

btn4 = Button(root, text=' 4 ', fg='#000000', background='#efcb0c',command=lambda: press(4))
btn4.grid(row=2, column=0, sticky='nswe')

btn5 = Button(root, text=' 5 ', fg='#000000', background='#efcb0c',command=lambda: press(5))
btn5.grid(row=2, column=1, sticky='nswe')

btn6 = Button(root, text=' 6 ', fg='#000000', background='#efcb0c',command=lambda: press(6))
btn6.grid(row=2, column=2, sticky='nswe')

btn1 = Button(root, text=' 1 ', fg='#000000', background='#efcb0c',command=lambda: press(1))
btn1.grid(row=3, column=0, sticky='nswe')

btn2 = Button(root, text=' 2 ', fg='#000000', background='#efcb0c',command=lambda: press(2))
btn2.grid(row=3, column=1, sticky='nswe')

btn3 = Button(root, text=' 3 ', fg='#000000', background='#efcb0c',command=lambda: press(3))
btn3.grid(row=3, column=2, sticky='nswe')

btn0 = Button(root, text=' 0 ', fg='#000000', background='#efcb0c',command=lambda: press(0))
btn0.grid(row=4, column=0, sticky='nswe',columnspan=2)

decimal = Button(root, text=' . ', fg='#000000', background='#eb860a',command=lambda: press('.'))
decimal.grid(row=4, column=2, sticky='nswe')

sum = Button(root, text=' + ', fg='#000000', background='#eb860a',command=lambda: press('+'))
sum.grid(row=1, column=3, sticky='nswe')

res = Button(root, text=' - ', fg='#000000', background='#eb860a',command=lambda: press('-'))
res.grid(row=2, column=3, sticky='nswe')

mult = Button(root, text=' * ', fg='#000000', background='#eb860a',command=lambda: press('*'))
mult.grid(row=3, column=3, sticky='nswe')

div = Button(root, text=' / ', fg='#000000', background='#eb860a',command=lambda: press('/'))
div.grid(row=4, column=3, sticky='nswe')

equal = Button(root, text=' = ', fg='#000000', background='#e31e63',command=equalpress)
equal.grid(row=5, column=3, sticky='nswe')

clearbtn = Button(root, text=' C ', fg='#000000', background='#e31e63',command=clear)
clearbtn.grid(row=5, column=0, sticky='nswe',columnspan=3)

text = Label(root,text='TkCalculator',fg='#000000',bg='#4496f1')
text.grid(row=6,column=0,sticky='nswe',columnspan=4)


root.mainloop()