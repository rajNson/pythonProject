import tkinter
from tkinter import *

# window = Tk()
# button.pack()
# label.pack()
# label = Label(window,text="WELLCOME")

# button.pack()
# label.pack()

import tkinter
parent_widget= tkinter.Tk()
entry_widget = tkinter.Entry(parent_widget)
entry_widget.insert(0,"type your text here")

button= Button(parent_widget,text="OK",width=30,height=30)
label=Label(parent_widget,text="WELLCOME")
scale_widget=tkinter.Scale( parent_widget, from_= 0,to = 100,orient=tkinter.VERTICAL)
scale_widget.set(25)
scale_widget.pack()
entry_widget.pack()
button.pack()
label.pack()
tkinter.mainloop()


