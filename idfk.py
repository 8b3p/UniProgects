from tkinter import*
from tkinter import font

root = Tk()
root.geometry("403x400+700+150")

text1 = Entry(root, width=50)
text2 = Entry(root, width=50)
text1.grid(row=1, column=0, padx=20,pady=5, ipady=15, columnspan=3)
text2.grid(row=0, column=0, padx= 20, pady=5, columnspan=3)

def number(num):
    text1.insert(END, num)

ClearFont = font.Font(size=20, weight='bold')
NumberFont = font.Font(size=20, weight='bold')

num1 = Button(root, text='1', command=lambda: number(1))
num1.grid(row=4, column=0, pady=5)
num1['font'] = NumberFont

num2 = Button(root, width=10, height=3, command=lambda: number(2))
num2.grid(row=4, column=1, pady=5)

num3 = Button(root, text='3', command=lambda: number(3))
num3.grid(row=4, column=2, pady=5)
num3['font'] = NumberFont

num4 = Button(root, width=10, height=3, command=lambda: number(4))
num4.grid(row=3, column=0, pady=5)

num5 = Button(root, width=10, height=3, command=lambda: number(5))
num5.grid(row=3, column=1, pady=5)

num6 = Button(root, width=10, height=3, command=lambda: number(6))
num6.grid(row=3, column=2, pady=5)

num7 = Button(root, width=10, height=3, command=lambda: number(7))
num7.grid(row=2, column=0, pady=5)

num8 = Button(root, width=10, height=3, command=lambda: number(8))
num8.grid(row=2, column=1, pady=5)

num9 = Button(root, width=10, height=3, command=lambda: number(9))
num9.grid(row=2, column=2, pady=5)

num0 = Button(root, width=10, height=3, command=lambda: number(0))
num0.grid(row=5, column=1, pady=5)

num0 = Button(root, width=10, height=3, command=lambda: number("."))
num0.grid(row=5, column=0, pady=5)

Clear = Button(root, text="clear", pady=1, command=lambda: text1.delete(0, END))
Clear.grid(row=5, column=2, pady=5)
Clear['font'] = ClearFont

root.mainloop()