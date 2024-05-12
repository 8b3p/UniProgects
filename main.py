from tkinter import*
from tkinter import font
from PIL import Image, ImageTk

root = Tk()
root.title("this is my calculator")
root.iconbitmap(default='images//calcicon.ico')
root.geometry("390x430+700+150")
root.config(bg='#444444')

global result
result = 0
global sign
sign = '+'
global lastNum
lastNum = 0
global ramPerhaps
ramPerhaps = 0
global percentage
percentage = 0

input = Entry(root, width=58, bg='#44444f', fg='#ffffff', borderwidth=3)
history = Entry(root, width=58, bg='#44444a', fg='#ffffff')
input.place(x=18, y=35)
history.grid(row=0, column=0, padx= 20, pady=5, columnspan=3)

img = Image.open("images/deleteicon.jpg")
img = img.resize((57,57), Image.ANTIALIAS)
Img = ImageTk.PhotoImage(img)


def number(num):
    input.insert(END, num)

def operation(Sign, perc):
    global sign, result, lastNum, ramPerhaps
    lastNum = input.get()
    if lastNum == '':
        lastNum = ramPerhaps
    percentage = perc
    if percentage == '%':
        if  sign == '+':
            result = result + float(lastNum)/100.0
        elif sign == '-':
            result = result - float(lastNum)/100.0
        elif sign == 'x':
            result = result * float(lastNum)/100.0
        elif sign == '÷':
            result = result / (float(lastNum)/100.0)
    else :
        if  sign == '+':
            result = result + float(lastNum)
        elif sign == '-':
            result = result - float(lastNum)
        elif sign == 'x':
            result = result * float(lastNum)
        elif sign == '÷':
            result = result / float(lastNum)    
    sign = Sign
    history.insert(END, str(lastNum) + str(sign))
    input.delete(0, END)
    if lastNum != '':
        ramPerhaps = lastNum


def equalNum():
    global result, sign, lastNum, percentage
    lastNum = input.get()
    input.delete(0, END)
    if percentage == '%':
        if  sign == '+':
            result = result + float(lastNum)/100.0
        elif sign == '-':
            result = result - float(lastNum)/100.0
        elif sign == 'x':
            result = result * float(lastNum)/100.0
        elif sign == '÷':
            result = result / (float(lastNum)/100.0)
    else :
        if  sign == '+':
            result = result + float(lastNum)
        elif sign == '-':
            result = result - float(lastNum)
        elif sign == 'x':
            result = result * float(lastNum)
        elif sign == '÷':
            result = result / float(lastNum)    
    sign = '+'
    history.insert(END, str(lastNum) + '=' + str(result))
    input.insert(0, result)
    result = 0

def clearBut():
    global result, sign
    input.delete(0, END)
    history.delete(0, END)
    result = 0 
    sign = '+'

def deleteNum():
    txt = input.get()[:-1]
    input.delete(0 , END)
    input.insert(0, txt)



ClearFont = font.Font(size=18, weight='bold')
NumberFont = font.Font(size=20, weight='bold')
subFont = font.Font(size=24, weight='bold')

num1 = Button(root, text='1', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: number(1))
num2 = Button(root, text='2', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: number(2))
num3 = Button(root, text='3', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: number(3))
num4 = Button(root, text='4', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: number(4))
num5 = Button(root, text='5', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: number(5))
num6 = Button(root, text='6', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: number(6))
num7 = Button(root, text='7', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: number(7))
num8 = Button(root, text='8', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: number(8))
num9 = Button(root, text='9', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: number(9))
num0 = Button(root, text='0', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: number(0))
dotBut = Button(root, text='.', bg='#444450', fg='#ffffff', padx=23, pady=5, command=lambda: number(".", "n"))
Clear = Button(root, text="clear", bg='#444450', fg='#ffffff', pady=7, padx=2, command=clearBut)
addBut = Button(root, text='+', bg='#444450', fg='#ffffff', padx=20, pady=39, command=lambda: operation('+', "n"))
subBut = Button(root, text='-', bg='#444450', fg='#ffffff', padx=21, pady=0, command=lambda: operation('-', "n"))
equalBut = Button(root, text='=', bg='#444450', fg='#ffffff', padx=20, pady=5, command=equalNum)
deleteBut = Button(root, image=Img, bg='#444450', fg='#ffffff', width=74, pady=5, command=deleteNum)
multiBut = Button(root, text='x', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: operation('x', "n"))
devBut = Button(root, text='÷', bg='#444450', fg='#ffffff', padx=20, pady=5, command=lambda: operation('÷', "n"))
percentBut = Button(root, text='%', bg='#444450', fg='#ffffff', padx=15, pady=5, command=lambda: operation('%', "%"))


num7.place(x=20, y=140)
num8.place(x=110, y=140)
num9.place(x=200, y=140)

num4.place(x=20, y=210)
num5.place(x=110, y=210)
num6.place(x=200, y=210)

num1.place(x=20, y=280)
num2.place(x=110, y=280)
num3.place(x=200, y=280)

dotBut.place(x=20, y=350)
num0.place(x=110, y=350)
equalBut.place(x=200, y=350)

Clear.place(x=290, y=140)
subBut.place(x=290, y=210)
addBut.place(x=290, y=280)

deleteBut.place(x=290, y=70)
multiBut.place(x=200, y=70)
devBut.place(x=110, y=70)
percentBut.place(x=20, y=70)


num1['font'] = NumberFont
num2['font'] = NumberFont
num3['font'] = NumberFont
num4['font'] = NumberFont
num5['font'] = NumberFont
num6['font'] = NumberFont
num7['font'] = NumberFont
num8['font'] = NumberFont
num9['font'] = NumberFont
num0['font'] = NumberFont
dotBut['font'] = NumberFont
Clear['font'] = ClearFont
addBut['font'] = NumberFont
subBut['font'] = subFont
equalBut['font'] = NumberFont
multiBut['font'] = NumberFont
devBut['font'] = NumberFont
percentBut['font'] = NumberFont


root.mainloop()
