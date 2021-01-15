import tkinter as tk
import tkinter.font as font
from functools import partial
from math import *

row1 = [1, 2, 3, '+', 4, 5, 6, "-", 7, 8, 9, "/", "AC", 0, "DEL", 'x', '(', ')', ".", "^"]
row2 = ['sin', 'cos', 'tan', '+', 'asin', 'acos', 'atan', '-', 'exp', 'log', '∏', "/", "AC", 'i', "DEL", 'x', '(', ')']
expression = ''
no_of_equ = 2


class calc(tk.Tk):
    '''simple calculator interface starting page'''

    def __init__(self):
        super().__init__()
        self.title(" AJ's ---> CALCULATOR ")
        self.geometry("500x1500")
        myFont = tk.font.Font(size=15, weight='bold', font="Times")
        self.menu = tk.Frame(self, width=10)
        self.menu.place(x=0)
        self.two = tk.Frame(self)
        self.two.place(x=300)
        self.menu['bg'] = "#7a47d9"
        self.Btn1 = tk.Button(self.menu, width=15, text="SIMPLE CALC", command=partial(self.first))
        self.Btn1.grid(row=1, column=1, padx=25)
        self.Btn1['font'] = myFont
        self.Btn2 = tk.Button(self.menu, width=15, text="GRAPH", command=partial(self.secound))
        self.Btn2.grid(row=2, column=1, padx=25)
        self.Btn2['font'] = myFont
        self.Btn4 = tk.Button(self.menu, width=15, text="INTEGRATION", command=partial(self.forth))
        self.Btn4.grid(row=4, column=1, padx=25)
        self.Btn4['font'] = myFont
        self.Btn5 = tk.Button(self.menu, width=15, text="INTEG-LIMIT", command=partial(self.fith))
        self.Btn5.grid(row=5, column=1, padx=25)
        self.Btn5['font'] = myFont
        self.Btn6 = tk.Button(self.menu, width=15, text="DIFFERENTIATION", command=partial(self.sixth))
        self.Btn6.grid(row=6, column=1, padx=25)
        self.Btn6['font'] = myFont

    ''' first tool box it has simple arthematic operation'''

    def first(self):
        global expression
        expression = ''
        self.two.destroy()
        self.two = tk.Frame(self)
        self.two.place(x=280)
        self.two['bg'] = "orange"
        self.title("simple caculator")
        myFont = tk.font.Font(size=15, weight='bold')
        myFont1 = tk.font.Font(size=15)
        self.geometry("540x500")
        self.entry = tk.Frame(self.two)
        self.entry.pack()
        self.entry['bg'] = "orange"
        self.E1 = tk.Label(self.entry, bd=2, height=2, bg='light blue', fg="#ffffff", text="", justify=tk.LEFT,width=19)
        self.E1.pack(padx=2, pady=2)
        self.E1['font'] = myFont1
        self.fbtns = tk.Frame(self.two)
        self.fbtns.pack(side=tk.TOP)
        self.fbtns['bg'] = "orange"
        self.equal = tk.Frame(self.two)
        self.equal.pack()
        self.equal['bg'] = "orange"
        self.E = tk.Button(self.equal, text="=", width=13, height=2, command=partial(self.equalpress))
        self.E.grid(padx=2, pady=3, row=0, column=0)
        self.E['font'] = myFont
        self.c = tk.Button(self.equal, text="more", width=4, height=2, command=partial(self.toggle))
        self.c.grid(padx=2, pady=3, row=0, column=1)
        self.c['font'] = myFont
        self.btns = [self.create_btn(r) for r in row1]
        i, j = 0, -1
        for btn in self.btns:
            j += 1
            btn['font'] = myFont
            btn.grid(row=i, column=j, padx=2, pady=2)
            if j == 3:
                j = -1
                i += 1

    def toggle(self):
        myFont = tk.font.Font(size=15, weight='bold')
        if self.c['text'] == 'more':
            self.btns = [self.create_btn(r) for r in row2]
            self.c.configure(text='less')
        else:
            self.btns = [self.create_btn(r) for r in row1]
            self.c.configure(text='more')
        i, j = 0, -1
        for btn in self.btns:
            j += 1
            btn['font'] = myFont
            btn.grid(row=i, column=j, padx=2, pady=2)
            if j == 3:
                j = -1
                i += 1

    def press(self, num):
        global expression
        if len(expression) == 18:
            return
        if len(expression) == 1 and str(num) == '0' and expression[0] == '0':
            return
        if len(expression) == 1 and expression[0] == '0' and str(num) not in '+-/x^().':
            expression = str(num)
            self.E1['text'] = expression
            return
        if len(expression) != 0 and expression[-1] in '+-/x^' and num in '+-/x^':
            expression = expression[0:-1]
        expression += str(num)
        self.E1['text'] = expression

    def equalpress(self):
        try:
            global expression
            expression = expression.replace("exp", "ep")
            expression = expression.replace("x", "*")
            expression = expression.replace("^", "**")
            expression = expression.replace("sin", "sn")
            expression = expression.replace("i", "j")
            expression = expression.replace("∏", "pi")
            expression = expression.replace("sn", "sin")
            expression = expression.replace("ep", "exp")
            total = str(round(eval(expression), 18))
            total = total.replace('j', 'i')
            self.E1["text"] = str(total)
            expression = str(total)
        except:
            self.E1['text'] = " Error "
            expression = ""

    def clear(self):
        global expression
        expression = ""
        self.E1['text'] = ""

    def delete(self):
        global expression
        expression = expression[0:-1]
        self.E1["text"] = expression

    def create_btn(self, char):
        if char == "DEL":
            return tk.Button(self.fbtns, fg='green', text=char, width=4, height=3, command=partial(self.delete))
        elif char == "AC":
            return tk.Button(self.fbtns, fg='red', text=char, width=4, height=3, command=partial(self.clear))
        elif str(char) in '+-/x^().':
            return tk.Button(self.fbtns, fg='#0033cc', text=char, width=4, height=3,
                             command=partial(self.press, str(char)))
        return tk.Button(self.fbtns, fg='black', text=char, width=4, height=3, command=partial(self.press, str(char)))

    def secound(self):
        global no_of_equ
        no_of_equ = 2
        self.title("GRAPH")
        myFont = tk.font.Font(size=15, weight='bold')
        self.geometry("700x500")
        self.two.destroy()
        self.two = tk.Frame(self)
        self.two.place(x=300)
        self.graph = tk.Frame(self.two)
        self.graph.pack()
        self.equ = []
        self.l2 = tk.Label(self.graph, text="x-MIN RANGE:")
        self.l2["font"] = myFont
        self.l2.grid(row=0, column=0)
        self.e2 = tk.Entry(self.graph)
        self.e2.grid(row=0, column=1, pady=10)
        self.l3 = tk.Label(self.graph, text="x-MAX RANGE:")
        self.l3["font"] = myFont
        self.l3.grid(row=1, column=0)
        self.e3 = tk.Entry(self.graph)
        self.e3.grid(row=1, column=1, pady=10)
        self.equation()
        self.find = tk.Frame(self.two)
        self.find.pack()
        self.find1 = tk.Button(self.find, fg="green", text="Get Graph", command=self.draw)
        self.find1.grid(column=0, row=0, pady=10, padx=10)
        self.find1['font'] = myFont
        self.add = tk.Button(self.find, fg="green", text="Add Graph", command=self.equation)
        self.add.grid(column=1, row=0, pady=10, padx=10)
        self.add['font'] = myFont

    def equation(self):
        global no_of_equ
        if no_of_equ == 7:
            return
        myFont = tk.font.Font(size=15, weight='bold')
        self.l1 = tk.Label(self.graph, text="EQUATION : " + str(no_of_equ - 1) + " y=")
        self.l1["font"] = myFont
        self.l1.grid(row=no_of_equ, column=0)
        self.e1 = tk.Entry(self.graph)
        self.e1.grid(row=no_of_equ, column=1)
        self.equ += [self.e1]
        no_of_equ += 1

    def draw(self):
        import matplotlib.pyplot as plt
        import numpy as np
        a = int(self.e2.get())
        b = int(self.e3.get())
        x = np.linspace(a, b, 500)
        y = str(self.e1.get())
        c = ['red', 'blue', 'green', 'orange', 'black']
        y = y.replace("^", "**")
        global no_of_equ
        for i in range(no_of_equ - 2):
            y = str(self.equ[i].get())
            y = y.replace("^", "**")
            y = y.replace("sin", "np.sin")
            y = y.replace("cos", "np.cos")
            for j in range(len(y) - 1):
                if y[j].isdigit() and y[j + 1] == 'x':
                    y = y[0:j + 1] + '*' + y[j + 1:]
            plt.plot(x, eval(y), c[i], label="y =" + str(self.equ[i].get()))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('_______Your Graph_________')
        plt.legend()
        plt.grid()
        plt.show()

    def forth(self):
        self.title("")
        myFont = tk.font.Font(size=15, weight='bold')
        self.geometry("650x200")
        self.two.destroy()
        self.two = tk.Frame(self)
        self.two.place(x=300)
        self.inte = tk.Frame(self.two)
        self.inte.pack()

        self.l2 = tk.Label(self.inte, text="equation:" + " y=")
        self.l2["font"] = myFont
        self.l2.grid(row=1, column=0)
        self.e2 = tk.Entry(self.inte)
        self.e2.grid(row=1, column=1)

        self.l3 = tk.Label(self.inte, text="Answer :" + " y= ")
        self.l3["font"] = myFont
        self.l3.grid(row=2, column=0)
        self.l4 = tk.Label(self.inte, text="")
        self.l4["font"] = myFont
        self.l4.grid(row=2, column=1)

        self.f = tk.Button(self.inte, fg="green", text="integrate", command=self.int_result)
        self.f.grid(column=0, row=3, pady=10, padx=10)
        self.f['font'] = myFont
        # pass

    def int_result(self):
        import sympy
        import numpy as np
        x = sympy.Symbol('x')
        result = ''
        y = str(self.e2.get())
        y = y.replace("^", "**")
        y = y.replace('X', 'x')
        for j in range(len(y) - 1):
            if y[j].isdigit() and y[j + 1] == 'x':
                y = y[0:j + 1] + '*' + y[j + 1:]

        result = str(sympy.integrate(y, x))
        self.l4['text'] = result
        print(result)

    def fith(self):
        self.title('INTEGRATION')
        myFont = tk.font.Font(size=15, weight='bold')
        self.geometry("650x220")
        self.two.destroy()
        self.two = tk.Frame(self)
        self.two.place(x=300)
        self.derv = tk.Frame(self.two)
        self.derv.pack()

        self.l2 = tk.Label(self.derv, text="EQUATION :")
        self.l2["font"] = myFont
        self.l2.grid(row=0, column=0)
        self.e2 = tk.Entry(self.derv)  # equation
        self.e2.grid(row=0, column=1, pady=10)

        self.l3 = tk.Label(self.derv, text="LOWER LIMIT : ")
        self.l3["font"] = myFont
        self.l3.grid(row=1, column=0)
        self.e3 = tk.Entry(self.derv)  # lower limit
        self.e3.grid(row=1, column=1, pady=10)

        self.l4 = tk.Label(self.derv, text="UPPER LIMIT : ")
        self.l4["font"] = myFont
        self.l4.grid(row=2, column=0)
        self.e4 = tk.Entry(self.derv)  # upper limit
        self.e4.grid(row=2, column=1, pady=10)

        self.l = tk.Label(self.derv, text="Answer :" + " y= ")
        self.l["font"] = myFont
        self.l.grid(row=3, column=0)
        self.ll = tk.Label(self.derv, text="")
        self.ll["font"] = myFont
        self.ll.grid(row=3, column=1)

        self.find1 = tk.Button(self.derv, fg="green", text="integrate", command=self.integ)  # definite integeral
        self.find1.grid(row=5, column=0)
        self.find1['font'] = myFont

    def integ(self):
        import scipy.integrate as integrate  # not working
        import sympy

        x = sympy.Symbol('x')

        y = str(self.e2.get())
        a = float(self.e3.get())
        b = float(self.e4.get())

        y = y.replace("^", "**")
        y = y.replace('X', 'x')
        for j in range(len(y) - 1):
            if y[j].isdigit() and y[j + 1] == 'x':
                y = y[0:j + 1] + '*' + y[j + 1:];

        def f(x):
            return eval(y)

        result = integrate.quad(f, a, b)
        result = round(result[0], 10)
        self.ll['text'] = result

    def sixth(self):

        self.title('DIFFERENTIATION')
        myFont = tk.font.Font(size=15, weight='bold')
        self.geometry("650x170")
        self.two.destroy()
        self.two = tk.Frame(self)
        self.two.place(x=300)
        self.derv = tk.Frame(self.two)
        self.derv.pack()

        self.l2 = tk.Label(self.derv, text="EQUATION  y:")
        self.l2["font"] = myFont
        self.l2.grid(row=0, column=0)
        self.e2 = tk.Entry(self.derv)
        self.e2.grid(row=0, column=1)

        self.l3 = tk.Label(self.derv, text="ORDER    : ")
        self.l3["font"] = myFont
        self.l3.grid(row=1, column=0)
        self.e3 = tk.Entry(self.derv)
        self.e3.grid(row=1, column=1)

        self.l3 = tk.Label(self.derv, text="ANSWER :" + " y= ")
        self.l3["font"] = myFont
        self.l3.grid(row=2, column=0)
        self.l4 = tk.Label(self.derv, text="")
        self.l4["font"] = myFont
        self.l4.grid(row=2, column=1)

        self.find1 = tk.Button(self.derv, fg="green", text="Differentiate", command=self.diff)
        self.find1.grid(column=0, row=3)
        self.find1['font'] = myFont

    def diff(self):
        import sympy
        import matplotlib.pyplot as plt
        import numpy as np
        x = sympy.Symbol('x')
        result = ''
        y = str(self.e2.get())

        order = int(self.e3.get())

        y = y.replace("^", "**")
        y = y.replace('X', 'x')
        for j in range(len(y) - 1):
            if y[j].isdigit() and y[j + 1] == 'x':
                y = y[0:j + 1] + '*' + y[j + 1:];
        temp = y
        for i in range(order):
            result = str(sympy.diff(temp, x))
            temp = result
        result = str(result)

        print(result)

        self.l4['text'] = result


if __name__ == "__main__":
    app = calc()
    app.mainloop()



