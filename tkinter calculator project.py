
from tkinter import *
from tkinter import Tk, StringVar

win = Tk()               # this is to create a basic window
win.geometry("312x324")  # this is for the size of the window
win.resizable(0, 0)      # this is to prevent from resizing the window
win.tittle("calculator")  # this is for window tittle


    ########  starting with the functions   ###############
    # 'btn_click' function:
    # this function continously update the input field whenever you enter a number

def btn_click(item, input_text=None):

    global expression
    expression = expression + str(item)
    input_text.set(expression)


    # 'bt_clear' function : this is used to clear the input field

def bt_clear(input_text=None):
    global expression
    expression = ""
    input_text.set("")

    # 'bt_equal':this method calculates the expression present in input field

    def bt_equal():
        pass
        global expression
        result = str(eval(expression))
    #  'eval': this function is used to evaluate the string expression directly result = str(eval(expression))
        input_text.set(result)
        expression = ""

    expression = ""

    #  'stringvar()' : it is used to get the instance of input field

    input_text = StringVar()

    # let us create a frame for input field

    input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)

    input_frame.pack(side=TOP)

    # let us create a input field inside the 'Frame'

    input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee" , bd=0, justify=RIGHT)
    input_field.grid(row=0, column=0)
    input_field.pack(ipady=10)
    # 'ipady' is internal padding increase the height of input field

    # let us create another 'Frame' for the button below the input 'Frame'
btns_Frame = Frame(win, width=312, height=272.5, bg="grey")
    
    # first row
    
clear = Button(btns_Frame, text= "C", fg= "black", width= 32, height= 3, bd= 0, bg= "#eee", cursor="hand2", command=lambda: bt_clear()).grid(row= 0, column= 0, columnspan= 3,padx= 1,pady= 1)
divide = Button(btns_Frame, text= "/", fg= "black", width= 10, height= 3, bd= 0, bg= "#eee", cursor="hand2", command=lambda: btn_click("/")).grid(row= 0, column= 3, padx= 1,pady= 1)

    # second row
    
seven = Button(btns_Frame, text = "7", fg = "black", width= 10, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: btn_click(7)).grid(row = 1 , column = 0, padx = 1, pady = 1)  
eight = Button(btns_Frame, text = "8", fg = "black", width= 10, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: btn_click(8)).grid(row = 1 , column = 1, padx = 1, pady = 1)  
ninw = Button(btns_Frame, text = "9", fg = "black", width= 10, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: btn_click(9)).grid(row = 1 , column = 2, padx = 1, pady = 1)  
multiply = Button(btns_Frame, text = "", fg = "black", width= 10, height=3, bd = 0, bg= "#eee", cursor= "hand2", command = lambda: btn_click("*")).grid(row = 1 , column = 3, padx = 1, pady = 1) 

    # third row
four = Button(btns_Frame, text = "4", fg = "black", width= 10, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: btn_click(4)).grid(row = 2 , column = 0, padx = 1, pady = 1)  
five = Button(btns_Frame, text = "5", fg = "black", width= 10, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: btn_click(5)).grid(row = 2 , column = 1, padx = 1, pady = 1)  
six = Button(btns_Frame, text = "6", fg = "black", width= 10, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: btn_click(6)).grid(row = 2 , column = 2, padx = 1, pady = 1)  
minus = Button(btns_Frame, text = "-", fg = "black", width= 10, height=3, bd = 0, bg= "#eee", cursor= "hand2", command = lambda: btn_click("-")).grid(row = 2 , column = 3, padx = 1, pady = 1)  

    # forth row
    
one = Button(btns_Frame, text = "7", fg = "black", width= 10, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: btn_click(1)).grid(row = 3 , column = 0, padx = 1, pady = 1)  
two = Button(btns_Frame, text = "7", fg = "black", width= 10, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: btn_click(2)).grid(row = 3 , column = 1, padx = 1, pady = 1)  
three = Button(btns_Frame, text = "7", fg = "black", width= 10, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: btn_click(3)).grid(row = 3 , column = 2, padx = 1, pady = 1)  
plus = Button(btns_Frame, text = "7", fg = "black", width= 10, height=3, bd = 0, bg= "#eee", cursor= "hand2", command = lambda: btn_click("+")).grid(row = 3 , column = 3, padx = 1, pady = 1)  

    #forth row

zero = Button(btns_Frame, text = "0", fg = "black", width= 21, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: btn_click(0)).grid(row = 4 , column = 0, columnspan = 2,padx = 1, pady = 1)
point = Button(btns_Frame, text = ".", fg = "black", width= 10, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: btn_click(".")).grid(row = 4 , column = 2, padx = 1, pady = 1)


def bt_equal():
    pass


equals = Button(btns_Frame, text = "=", fg = "black", width= 10, height=3, bd = 0, bg= "#fff", cursor= "hand2", command = lambda: bt_equal()).grid(row = 4 , column = 3, padx = 1, pady = 1) 

win.mainloop()
    





