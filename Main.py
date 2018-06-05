import tkinter
import Flanger as Fl
from tkinter import Label
from tkinter import Entry
from tkinter import Scale
from tkinter import Button
from tkinter import messagebox
from tkinter import Frame
from tkinter import Tk

def flangerCreate():
    filename = entry_1.get()
    rate = scale_1.get()
    depth = scale_2.get()
    new_filename = entry_2.get()
    if(entry_1.get()==''):
        messagebox.showinfo('Error', 'Empty filename!')
    elif(entry_2.get()==''):
        messagebox.showinfo('Error', 'Empty filename!')
    else:
        Fl.flang(filename+'.wav', rate, depth, new_filename)
        messagebox.showinfo('Flanger', 'Flanged successfully!')
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    scale_1.set(1)
    scale_2.set(0)

class Flanger(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        self.winfo_toplevel().title("Digital Flanger Effect")
        label_1 = Label(self, text='DSP Project', relief='raised', justify='center', pady=4, width=50)
        label_2 = Label(self, text='Filename:', relief='groove', justify='left', pady=4, anchor='w', width=50)
        entry_1 = Entry(self, width=59)
        scale_1 = Scale(self, length = 360, from_=1, to=20, resolution=1, relief='sunken', label='Rate:', tickinterval=1, orient='horizontal', highlightcolor='green')
        scale_2 = Scale(self, length = 360, from_=0, to=1, resolution=0.01, relief='sunken', label='Depth:', orient='horizontal', highlightcolor='green')
        label_3 = Label(self, text='New filename:', relief='groove', justify='left', pady=4, anchor='w', width=50)
        entry_2 = Entry(self, width=59)
        button_1 = Button(self, text='Flange', justify='center', pady=4, width=50, relief='raised', command=flangerCreate)
        label_1.pack()
        label_2.pack()
        entry_1.pack()
        scale_1.pack()
        scale_2.pack()
        label_3.pack()
        entry_2.pack()
        button_1.pack()

root = Tk()
flanger = Flanger(root)
root.geometry('370x290')
root.mainloop()
