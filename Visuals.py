import tkinter as tk

window = tk.Tk()

window.minsize(700,600)
window.rowconfigure([0,1,2,3,4],minsize=100,weight=1)
window.columnconfigure([0,1,2,3,4],minsize=100,weight=1)

window.mainloop()