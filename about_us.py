from tkinter import *

def about_fun():
    abo_root =Toplevel()
    abo_root.state('zoomed')

    im=PhotoImage(file="team_1.PNG")
    Label(abo_root,image=im).pack(fill=BOTH)
    abo_root.mainloop()

about_fun()