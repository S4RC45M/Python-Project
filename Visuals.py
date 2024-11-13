#import module tkinter with the nickname tk
import tkinter as tk

#constants for color and fonts
BACKGROUNDCOLOR = "#FEF6C9"
FONTNAME=""

#create a window and grid layout
window = tk.Tk()
window.minsize(800,600)
window.config(bg=BACKGROUNDCOLOR)
window.rowconfigure([0,1,2,3,4],minsize=100,weight=1)
window.columnconfigure([0,1,2,3,4],minsize=100,weight=1)

window.mainloop()