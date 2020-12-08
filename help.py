from tkinter import *
file = open("help.txt", "r",encoding='utf-8')
x=(file.read())
help_root=Toplevel()
def destroy():
    help_root.destroy()

def help_fun():

    help_root.state('zoomed')
    help_root.configure(bg="orange")
    im_help=PhotoImage(file="help_bar.png")
    img_help_lable =Label(help_root,image=im_help)
    img_help_lable.pack(side=TOP)





    txt=Label(help_root,bg='black',fg='green',text=x,height=30,width=500)
    txt.pack(expand=10,fill=BOTH)

    scrollbar = Scrollbar(txt)
    scrollbar.pack(side=RIGHT, fill=Y)










    im_help_end = PhotoImage(file="menu_end.png")
    img_help_lable_end = Label(help_root, image=im_help_end)
    img_help_lable_end.pack(side=BOTTOM)

    btn = Button(help_root, bg='red', text="BACK TO MAIN MENU", width=20, height=2 ,command=destroy)
    btn.pack(side=BOTTOM,fill=BOTH)

    help_root.mainloop()
help_fun()
