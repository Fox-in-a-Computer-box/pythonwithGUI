from tkinter import *
from tkinter.filedialog import askopenfilename


class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.button_1 = Button(
                        frame, text="Open File",fg='green',
                        command=self.file_open
                        )
        self.button_1.pack(side=TOP)

        self.label_1 = Label(
                       frame,text='The amount of characters in this file: '
                       )
        self.label_1.pack(side=LEFT)

        self.field_1 = Entry(
                  frame,width=15
                  )
        self.field_1.pack(side=LEFT)

        self.button_2 = Button(
                  frame, text='QUIT',command=self.quit_button
                      )
        self.button_2.pack(side=TOP)

    def file_open(self):
        char_count = 0
        fname = askopenfilename()
        file_handle = open(fname,'r')
        for line in file_handle:
            char_count += len(line)
        self.field_1.insert(0,char_count)

    def quit_button(self):
        root.destroy()

root = Tk()
root.title('Character counter')
root.geometry('400x300')

app = App(root)

root.mainloop()
root.destroy()
