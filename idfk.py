from tkinter import* 

root = Tk()
root.geometry("500x400+700+150")

first = Entry(root, width=60)
second = Entry(root, width=60)
first.grid(row=1, column=0, padx=20, columnspan=3)
second.grid(row=0, column=0, padx= 20, pady=10, columnspan=3)

root.mainloop()