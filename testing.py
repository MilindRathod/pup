from tkinter import *
main=Tk()
scroll-Scrollbar (main)
scroll.pack(f1ll=Y,side-RIGHT)
#listbox
lb=Listbox(main,yscrollcommand-scroll.set)
for 1 in range(30):

    Ib.insert (END, "Number "+str(1))
lb.pack()

scroll.config(command lb.yview)
main.mainloop()
# root = Tk()
# root.geometry("400x300")

# v1 = DoubleVar()

# def show1():
#     sel = "Horizontal Scale Value - " + str(v1.get())
#     l1.config(Text = sel,font = ("Courier" , 14))

# s1 = Scale(root , variable=v1,from_=1,to=100,orient=HORIZONTAL)
# l3 = Label(root,text="Horizontal Scaler")
# b1 = Button(root,text="Display Horizontal",command=show1,bg="yellow")

# l1 = Label(root)
# s1.pack(anchor=CENTER)
# l3.pack()
# b1.pack(anchor=CENTER)
# l1.pack()

# root.mainloop()


