from tkinter import* 

root = Tk()
root.geometry("403x400+700+150")

first = Entry(root, width=60)
second = Entry(root, width=60)
first.grid(row=1, column=0, padx=20,pady=5, ipady=15, columnspan=3)
second.grid(row=0, column=0, padx= 20, pady=5, columnspan=3)



root.mainloop()