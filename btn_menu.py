from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image


def calculator():
    import CALCULATOR

def help():
    import help


def data_base():
    import new_employee

def contact_us():
    import about_us

def addandence():

    import attandence
    pass

def graph():
    import graph


def expance():
    import expance

def note_pad():
    import SAVE_FILE_FILE_HANDLING





def menu_fun():
    menu_btn_root = Toplevel()
    menu_btn_root.state('zoomed')
    menu_btn_root.title("RUPAFILL MENU")
    menu_btn_root.configure(bg='#131c21')
    font_design = Font(family='Times New Roman', size=22)
    buttons_font_design = Font(family='Times New Roman', size=16)

    # FRAMES

    top_frame = Frame(menu_btn_root, bg='#131c21', height=150)
    left_frame = Frame(menu_btn_root, bg='#131c21', width=150)
    right_frame = Frame(menu_btn_root, bg='#131c21', width=150)
    center_frame = Frame(menu_btn_root, bg='#131c21', width=100)
    bottom_frame = Frame(menu_btn_root, bg='#131c21', height=150)

    # IMAGES

    image_1 = ImageTk.PhotoImage(Image.open("menu.png"))
    image_2 = ImageTk.PhotoImage(Image.open("L1.jpeg"))
    image_3 = ImageTk.PhotoImage(Image.open("L2.jpeg"))
    image_4 = ImageTk.PhotoImage(Image.open("note.png"))
    image_5 = ImageTk.PhotoImage(Image.open("L4.jpeg"))
    image_6 = ImageTk.PhotoImage(Image.open("L5.jpeg"))
    image_7 = ImageTk.PhotoImage(Image.open("L6.jpeg"))
    image_8 = ImageTk.PhotoImage(Image.open("data.png"))
    image_9 = ImageTk.PhotoImage(Image.open("expna.png"))
    image_10 = ImageTk.PhotoImage(Image.open("menu_end.png"))


    image_1_button = Button(top_frame, image=image_1 )
    image_2_button = Button(center_frame, image=image_2,command=calculator)
    image_3_button = Button(center_frame, image=image_3,command=addandence)
    image_4_button = Button(center_frame, image=image_4,command=note_pad)
    image_5_button = Button(center_frame, image=image_5,command=help)
    image_6_button = Button(center_frame, image=image_6,command=graph)
    image_7_button = Button(center_frame, image=image_7,command=contact_us)
    image_8_button = Button(center_frame, image=image_8,command=data_base)
    image_9_button = Button(center_frame, image=image_9,command=expance)
    image_10_button = Button(bottom_frame, image=image_10)

    # FRAME'S PACKING

    top_frame.pack(side=TOP, fill=BOTH)
    bottom_frame.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
    left_frame.pack(side=LEFT, fill=BOTH)
    right_frame.pack(side=RIGHT, fill=BOTH)
    center_frame.pack(fill=BOTH)

    # BUTTON'S PACKING

    image_1_button.pack()
    image_2_button.grid(padx=10, pady=10, row=1, column=1)
    image_3_button.grid(padx=10, pady=10, row=1, column=2)
    image_4_button.grid(padx=10, pady=10, row=1, column=3)
    image_5_button.grid(padx=10, pady=10, row=1, column=4)
    image_6_button.grid(padx=10, pady=10, row=2, column=1)
    image_7_button.grid(padx=10, pady=10, row=2, column=2)
    image_8_button.grid(padx=10, pady=10, row=2, column=3)
    image_9_button.grid(padx=10, pady=10, row=2, column=4)
    image_10_button.pack(side=BOTTOM)

    menu_btn_root.mainloop()

menu_fun()