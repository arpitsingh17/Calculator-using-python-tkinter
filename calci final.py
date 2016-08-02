from tkinter import *


class Calci():
    def __init__(self):

        self.result = []
        self.resultprice = []
        self.x = 0

        window = Tk()
        window.title = "Calculator"

        self.v = IntVar()

        Radiobutton(window, text="List", variable=self.v, value=1).grid(row=0,column = 1)
        Radiobutton(window, text="Calci", variable=self.v, value=2).grid(row=0, column =3)

        label1 = Label(window, text="Enter Product name")
        label1.grid(row=1, sticky=W)
        label2 = Label(window, text="Enter Price")
        label2.grid(row=2)

        self.string = StringVar()
        self.entry = Entry(window, textvariable=self.string, font="Helvetica 17 bold")
        self.entry.grid(row=2,column=1, columnspan=5)

        output_heading = Label(window, text="Product" + "        " + "Price")
        output_heading.grid(row=0,column=8, sticky=N)

        self.txt = StringVar()
        self.output_screen = Label(window, textvariable=self.txt)
        self.output_screen.grid(row=2, column=8, columnspan=10, rowspan=6, sticky=N)

        self.string_name = StringVar()
        self.entry_name = Entry(window, textvariable=self.string_name, font="Helvetica 17 bold")
        self.entry_name.grid(row=1,column=1, columnspan=5)
        self.entry_name.focus()

        but_7 = Button(window, height=2, width=2, padx=10, pady=10, text="7",
                       command=lambda txt="7": self.addchar(txt))
        but_7.grid(row=3,column=0, padx=1, pady=1,sticky = E)

        but_8 = Button(window, height=2, width=2, padx=10, pady=10, text="8",
                       command=lambda: self.addchar('8'))
        but_8.grid(row=3,column=1, padx=1, pady=1)

        but_9 = Button(window, height=2, width=2, padx=10, pady=10, text="9",
                       command=lambda: self.addchar('9'))
        but_9.grid(row=3,column=2, padx=1, pady=1)

        but_div = Button(window, height=2, width=2, padx=10, pady=10, text="/",
                         command=lambda: self.addchar("/"))
        but_div.grid(row=3,column=3, padx=1, pady=1)

        but_clear = Button(window, height=2, width=2, padx=10, pady=10, text="clr",
                           command=lambda: self.cleartext())
        but_clear.grid(row=3,column=4, padx=1, pady=1)

        but_del = Button(window, height=2, width=2, padx=10, pady=10, text="<-",
                         command=lambda: self.delete())
        but_del.grid(row=3, column=5, padx=1, pady=1)

        but_4 = Button(window, height=2, width=2, padx=10, pady=10, text="4",
                       command=lambda: self.addchar("4"))
        but_4.grid(row=4,column=0, padx=1, pady=1,sticky = E)

        but_5 = Button(window, height=2, width=2, padx=10, pady=10, text="5",
                       command=lambda: self.addchar("5"))
        but_5.grid(row=4,column=1, padx=1, pady=1)

        but_6 = Button(window, height=2, width=2, padx=10, pady=10, text="6",
                       command=lambda: self.addchar("6"))
        but_6.grid(row=4,column=2, padx=1, pady=1)

        but_multiply = Button(window, height=2, width=2, padx=10, pady=10, text="*",
                              command=lambda: self.addchar("*"))
        but_multiply.grid(row=4,column=3, padx=1, pady=1)

        but_openbrace = Button(window, height=2, width=2, padx=10, pady=10, text="(",
                               command=lambda: self.addchar("("))
        but_openbrace.grid(row=4,column=4, padx=1, pady=1)

        but_closebrace = Button(window, height=2, width=2, padx=10, pady=10, text=")",
                                command=lambda: self.addchar(")"))
        but_closebrace.grid(row=4,column=5, padx=1, pady=1)

        but_1 = Button(window, height=2, width=2, padx=10, pady=10, text="1",
                       command=lambda: self.addchar("1"))
        but_1.grid(row=5,column=0, padx=1, pady=1,sticky = E)

        but_2 = Button(window, height=2, width=2, padx=10, pady=10, text="2",
                       command=lambda: self.addchar("6"))
        but_2.grid(row=5,column=1, padx=1, pady=1)

        but_3 = Button(window, height=2, width=2, padx=10, pady=10, text="3",
                       command=lambda: self.addchar("3"))
        but_3.grid(row=5,column=2, padx=1, pady=1)

        but_subtract = Button(window, height=2, width=2, padx=10, pady=10, text="-",
                              command=lambda: self.addchar("-"))
        but_subtract.grid(row=5,column=3, padx=1, pady=1)

        but_0 = Button(window, height=2, width=2, padx=10, pady=10, text="0",
                       command=lambda: self.addchar("0"))
        but_0.grid(row=6,column=0, padx=1, pady=1,sticky = E)

        but_dot = Button(window, height=2, width=2, padx=10, pady=10, text=".",
                         command=lambda: self.addchar("."))
        but_dot.grid(row=6,column=1, padx=1, pady=1)

        but_per = Button(window, height=2, width=2, padx=10, pady=10, text="%",
                         command=lambda: self.addchar("%"))
        but_per.grid(row=6,column=2, padx=1, pady=1)

        but_add = Button(window, height=2, width=2, padx=10, pady=10, text="+",
                         command=lambda: self.addchar("+"))
        but_add.grid(row=6,column=3, padx=1, pady=1)

        but_equals = Button(window, height=2, width=8, padx=10, pady=10, text="=",
                            command=lambda: self.equals())
        but_equals.grid(row=6,column=4, columnspan=2, padx=1, pady=1)

        but_list = Button(window, height=2, width=8, padx=10, pady=10, text="Add to List",
                          command=lambda: self.list())
        but_list.grid(row=5,column=4, columnspan=2, padx=1, pady=1)

        window.mainloop()

    def addchar(self, char):
        self.string.set(self.string.get() + (str(char)))

    def cleartext(self):
        self.string.set('')
        self.string_name.set('')

    def delete(self):
        if self.entry.focus_get():
            self.string.set(self.string.get()[0:-1])
        elif self.entry_name.focus_get():
            self.string_name.set(self.string_name.get()[0:-1])




    def list(self):

        if self.v.get() == 1:
            try:
                self.result.append(self.string_name.get() + "        " + self.string.get())
                self.resultprice.append(self.string.get())

                self.string.set('')
                self.string_name.set('')


            except:
                self.error = True
                result = "Error"

                # self.string.set(result)
            self.txt.set(self.result)
        elif self.v.get()==2:
            self.entry.focus()
            self.string_name = ''
            result = ''
            try:
                result = eval(self.string.get())
            except:
                self.error = True
                result = "Error"

            self.string.set(result)

    def equals(self):
        if self.v.get()==1:
            finaloutputprice = 0
            try:
                for num in self.resultprice:
                    finaloutputprice = float(num) + finaloutputprice


            except:
                self.error = True
                result = "Error"

            self.string_name.set("Total Price =")
            self.string.set(finaloutputprice)
        elif self.v.get()==2:
            self.entry.focus()
            self.string_name = ''
            result = ''
            try:
                result = eval(self.string.get())
            except:
                self.error = True
                result = "Error"

            self.string.set(result)


Calci()
