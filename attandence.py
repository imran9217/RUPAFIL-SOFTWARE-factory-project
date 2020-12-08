from tkinter import *
from PIL import ImageTk,Image
from tkinter.font import Font
class attandence:

    car=0

def  attandence_personel():
    import attandence_back_end
    atn_personal_root = Toplevel()
    # atn_personal_root.state('zoomed')
    atn_personal_root.title("Personal Attendence")

    font_design = Font(family='Times New Roman', size=22)
    buttons_font_design = Font(family='Times New Roman', size=16)

    # FRAMES

    top_frame = Frame(atn_personal_root, bg='Orange', height=250)
    center_frame = Frame(atn_personal_root, bg='Orange')
    space_frame_1 = Frame(center_frame, bg='Orange', width=100, height=100)
    name_label_and_text_box_frame = Frame(center_frame)
    space_frame_2 = Frame(center_frame, bg='Orange', width=20, height=20)
    check_boxes_frame = Frame(center_frame)

    # IMAGE

    image_1 = ImageTk.PhotoImage(Image.open("per.png"))

    # LABELS

    image_label = Label(top_frame, image=image_1)
    name_label = Label(name_label_and_text_box_frame, text="Name", width=10, height=1, font=font_design)

    # TEXT BOX

    name_text_box = Entry(name_label_and_text_box_frame, font=font_design)

    # CHECK BOXES

    c_1 = Checkbutton(check_boxes_frame, text="Present", font=font_design, height=1, width=5)
    c_2 = Checkbutton(check_boxes_frame, text="Absent", font=font_design, height=1, width=5)
    c_3 = Checkbutton(check_boxes_frame, text="Leave", font=font_design, height=1, width=5)

    # FRAME'S PACKING

    top_frame.pack(fill=BOTH)
    center_frame.pack(fill=BOTH, expand=TRUE)
    space_frame_1.pack(fill=BOTH)
    name_label_and_text_box_frame.pack()
    space_frame_2.pack(fill=BOTH)
    check_boxes_frame.pack()

    # LABEL'S PACKING

    image_label.pack()
    name_label.pack(padx=20, pady=20)

    # TEXT BOXES'S PACKING

    name_text_box.pack(padx=20, pady=20)

    # CHECK BOXES PACKING

    c_1.grid(row=1, column=1)
    c_2.grid(row=2, column=1)
    c_3.grid(row=3, column=1)

    atn_personal_root.mainloop()


def attandence():
    atn_root = Toplevel()
    atn_root.state("zoomed")

    font_design = Font(family='Times New Roman', size=22)
    buttons_font_design = Font(family='Times New Roman', size=16)

    # FRAMES

    top_frame = Frame(atn_root, bg='Orange', height=250)
    center_frame = Frame(atn_root, bg='Orange')
    space_frame_1 = Frame(center_frame, bg='Orange', width=200, height=100)
    line_1_frame = Frame(center_frame, bg='Orange')
    upper_label_and_buttons_frame = Frame(center_frame, bg='Orange')
    line_2_frame = Frame(center_frame, bg='Orange')
    buttons_frame = Frame(center_frame, bg='Orange')
    space_frame_2 = Frame(center_frame, bg='Orange', width=200, height=100)
    last_button_frame = Frame(center_frame)

    # IMAGE

    my_image = ImageTk.PhotoImage(Image.open("001.png"))

    # LABELS

    image_label = Label(top_frame, image=my_image)
    line_1_label = Label(line_1_frame,
                         text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                         bg='Orange', font=font_design)
    month_label = Label(upper_label_and_buttons_frame, text="December", height=1, width=10, bg='Orange',
                        font=font_design)
    line_2_label = Label(line_2_frame,
                         text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                         bg='Orange', font=font_design)

    # BUTTONS

    previous_button = Button(upper_label_and_buttons_frame, text="Previous", height=1, width=10,
                             font=buttons_font_design)
    next_button = Button(upper_label_and_buttons_frame, text="Next", height=1, width=10, font=buttons_font_design)
    update_button = Button(last_button_frame, text="Update", height=1, width=10, font=buttons_font_design)
    button_one = Button(buttons_frame, text="1", width=4, font=buttons_font_design,command=attandence_personel)
    button_two = Button(buttons_frame, text="2", width=4, font=buttons_font_design,command=attandence_personel)
    button_three = Button(buttons_frame, text="3", width=4, font=buttons_font_design,command=attandence_personel)
    button_four = Button(buttons_frame, text="4", width=4, font=buttons_font_design,command=attandence_personel)
    button_five = Button(buttons_frame, text="5", width=4, font=buttons_font_design,command=attandence_personel)
    button_six = Button(buttons_frame, text="6", width=4, font=buttons_font_design,command=attandence_personel)
    button_seven = Button(buttons_frame, text="7", width=4, font=buttons_font_design,command=attandence_personel)
    button_eight = Button(buttons_frame, text="8", width=4, font=buttons_font_design,command=attandence_personel)
    button_nine = Button(buttons_frame, text="9", width=4, font=buttons_font_design,command=attandence_personel)
    button_ten = Button(buttons_frame, text="10", width=4, font=buttons_font_design,command=attandence_personel)
    button_eleven = Button(buttons_frame, text="11", width=4, font=buttons_font_design,command=attandence_personel)
    button_twelve = Button(buttons_frame, text="12", width=4, font=buttons_font_design,command=attandence_personel)
    button_thirteen = Button(buttons_frame, text="13", width=4, font=buttons_font_design,command=attandence_personel)
    button_fourteen = Button(buttons_frame, text="14", width=4, font=buttons_font_design,command=attandence_personel)
    button_fifteen = Button(buttons_frame, text="15", width=4, font=buttons_font_design,command=attandence_personel)
    button_sixteen = Button(buttons_frame, text="16", width=4, font=buttons_font_design,command=attandence_personel)
    button_seventeen = Button(buttons_frame, text="17", width=4, font=buttons_font_design,command=attandence_personel)
    button_eighteen = Button(buttons_frame, text="18", width=4, font=buttons_font_design,command=attandence_personel)
    button_ninteen = Button(buttons_frame, text="19", width=4, font=buttons_font_design,command=attandence_personel)
    button_twenty = Button(buttons_frame, text="20", width=4, font=buttons_font_design,command=attandence_personel)
    button_twent_one = Button(buttons_frame, text="21", width=4, font=buttons_font_design,command=attandence_personel)
    button_twenty_two = Button(buttons_frame, text="22", width=4, font=buttons_font_design,command=attandence_personel)
    button_twenty_three = Button(buttons_frame, text="23", width=4, font=buttons_font_design,command=attandence_personel)
    button_twenty_four = Button(buttons_frame, text="24", width=4, font=buttons_font_design,command=attandence_personel)
    button_twenty_five = Button(buttons_frame, text="25", width=4, font=buttons_font_design,command=attandence_personel)
    button_twenty_six = Button(buttons_frame, text="26", width=4, font=buttons_font_design,command=attandence_personel)
    button_twenty_seven = Button(buttons_frame, text="27", width=4, font=buttons_font_design,command=attandence_personel)
    button_twenty_eight = Button(buttons_frame, text="28", width=4, font=buttons_font_design,command=attandence_personel)
    button_twenty_nine = Button(buttons_frame, text="29", width=4, font=buttons_font_design,command=attandence_personel)
    button_thirty = Button(buttons_frame, text="30", width=4, font=buttons_font_design,command=attandence_personel)
    button_thirty_one = Button(buttons_frame, text="31", width=4, font=buttons_font_design,command=attandence_personel)

    # FRAME'S PACKING

    top_frame.pack(fill=BOTH)
    center_frame.pack(fill=BOTH, expand=TRUE)
    line_1_frame.pack(fill=BOTH)
    upper_label_and_buttons_frame.pack()
    line_2_frame.pack(fill=BOTH)
    buttons_frame.pack()
    space_frame_2.pack()
    last_button_frame.pack()

    # LABELS PACKING

    image_label.pack()
    line_1_label.pack()
    month_label.grid(row=1, column=2)
    line_2_label.pack()

    # BUTTON'S PACKING

    previous_button.grid(padx=200, row=1, column=1)
    next_button.grid(padx=200, row=1, column=3)

    button_one.grid(row=1, column=1)
    button_two.grid(row=1, column=2)
    button_three.grid(row=1, column=3)
    button_four.grid(row=1, column=4)
    button_five.grid(row=1, column=5)
    button_six.grid(row=1, column=6)
    button_seven.grid(row=1, column=7)
    button_eight.grid(row=1, column=8)
    button_nine.grid(row=1, column=9)
    button_ten.grid(row=1, column=10)
    button_eleven.grid(row=1, column=11)
    button_twelve.grid(row=1, column=12)
    button_thirteen.grid(row=1, column=13)
    button_fourteen.grid(row=1, column=14)
    button_fifteen.grid(row=1, column=15)
    button_sixteen.grid(row=1, column=16)
    button_seventeen.grid(row=1, column=17)
    button_eighteen.grid(row=1, column=18)
    button_ninteen.grid(row=1, column=19)
    button_twenty.grid(row=1, column=20)
    button_twent_one.grid(row=2, column=1)
    button_twenty_two.grid(row=2, column=2)
    button_twenty_three.grid(row=2, column=3)
    button_twenty_four.grid(row=2, column=4)
    button_twenty_five.grid(row=2, column=5)
    button_twenty_six.grid(row=2, column=6)
    button_twenty_seven.grid(row=2, column=7)
    button_twenty_eight.grid(row=2, column=8)
    button_twenty_nine.grid(row=2, column=9)
    button_thirty.grid(row=2, column=10)
    button_thirty_one.grid(row=2, column=11)

    update_button.pack()

    atn_root.mainloop()


attandence()