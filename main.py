from tkinter import *

win = Tk()
win.geometry("270x150")
# win.resizable(0, 0)
win.title("Calculator")

equation = StringVar()
expression = ""
# program
def button_click(item):
    global expression
    expression = expression + str(item)
    equation.set(expression)


def button_clear():
    global expression
    expression = ""
    equation.set("")


def button_equation():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("invalid!")
        expression = ""


def main():
    #
    input_field = Entry(win, textvariable=equation)
    input_field.grid(columnspan=4, ipadx=70)
    button1 = Button(win, text=' 1 ', fg='black', bg='red',
                     command=lambda: button_click(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(win, text=' 2 ', fg='black', bg='red',
                     command=lambda: button_click(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(win, text=' 3 ', fg='black', bg='red',
                     command=lambda: button_click(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(win, text=' 4 ', fg='black', bg='red',
                     command=lambda: button_click(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(win, text=' 5 ', fg='black', bg='red',
                     command=lambda: button_click(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(win, text=' 6 ', fg='black', bg='red',
                     command=lambda: button_click(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(win, text=' 7 ', fg='black', bg='red',
                     command=lambda: button_click(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(win, text=' 8 ', fg='black', bg='red',
                     command=lambda: button_click(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(win, text=' 9 ', fg='black', bg='red',
                     command=lambda: button_click(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(win, text=' 0 ', fg='black', bg='red',
                     command=lambda: button_click(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(win, text=' + ', fg='black', bg='red',
                  command=lambda: button_click("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(win, text=' - ', fg='black', bg='red',
                   command=lambda: button_click("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(win, text=' * ', fg='black', bg='red',
                      command=lambda: button_click("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(win, text=' / ', fg='black', bg='red',
                    command=lambda: button_click("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(win, text=' = ', fg='black', bg='red',
                   command=button_equation, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(win, text='Clear', fg='black', bg='red',
                   command=button_clear, height=1, width=7)
    clear.grid(row=5, column='1')

    Decimal = Button(win, text='.', fg='black', bg='red',
                     command=lambda: button_click('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    win.mainloop()

main()

# finished