#import module tkinter with the nickname tk
import tkinter as tk
#button actions
#allows the user to enter data
def enter():
    return None
#constants for color and fonts
BACKGROUNDCOLOR = "#FEF6C9"
FONTNAME="Courier"

#create a window and grid layout
window = tk.Tk()
window.minsize(800,600)
window.config(bg=BACKGROUNDCOLOR)
window.rowconfigure([0,1,2,3,4],minsize=100,weight=1)
window.columnconfigure([0,1,2,3,4],minsize=100,weight=1)
#it says hello :)
hellofrm = tk.Frame()
titleHello = tk.Label(text = "Hello", font =("courier", 45) ,padx= 30, pady= 50)
titleHello.grid(column=2 ,row=2)
#keeps the window open
window.mainloop()
