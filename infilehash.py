#in file hasher

from tkinter import *

def fle_handle():
    hash_num = 0
    file = field_1.get()
    opnfile = open(file,'r')
    for line in opnfile:
        hash_num += len(line)
        print(line)
    hash_output(hash_num)

def hash_output(x):
    field_2.insert(0,x)

root = Tk()

label_1 = Label(root,text='Enter the file name here: ')
label_1.grid(row=0,column=0)
label_2 = Label(root,text='This is your hash number: ')
label_2.grid(row=1,column=0)

field_1 = Entry(root,width=35)
field_1.grid(row=0,column=1)
field_2 = Entry(root,width=35)
field_2.grid(row=1,column=1)

button_1 = Button(root,text='OK',command=fle_handle)
button_1.grid(row=1,column=3)






root.mainloop()
