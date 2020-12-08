from tkinter import *
from tkinter import Entry
from sqlite3 import dbapi2 as sqlite
from tkinter.font import Font # THIS CLASS IS IMPORT FOR SETTING OF FONT SIZE AND FONT FAMILY
from tkinter import messagebox
login=sqlite.connect("LIRM TECH.db")
l=login.cursor()
from LOG_IN_DSIN import Login

class forgot_class(Login):
    def forgot_password(self):
        fg_root = Toplevel()
        fg_root.state("zoomed")
        fg_root.configure(bg='orange')

        def get_pass():

            u = un.get()
            # q = question_var.get()
            a = ans.get()
            password = ""
            if u == "" or a == "":
                messagebox.showwarning("Warning", "Please Fill All The Details")
            else:
                try:
                    sql = "select * from user where username='%s'  and answer='%s'" % (u, a)
                    l.execute(sql)
                except:
                    print("")
                count = 0
                for i in l:
                    password = i[1]
                if password != "":
                    messagebox.showinfo("Information", "Your Password is" + password)
                else:
                    messagebox.showerror("Error", "Wrong information")

        heading_font_design = Font(family='Times New Roman', weight='bold',
                                   size=24)  # FONT STYLE FOR HEADING LIKE ENTER DETAILS... & LINES
        text_font_design = Font(family='Times New Roman', size=18)  # FONT STYLE FOR SIMPLE TEXT
        boxes_font_design = Font(family="Times New Roman", size=16)  # FONT STYLE FOR TEXT BOXES
        question_button_font_design = Font(family='Times New Roman', size=10)
        simple_button_font_design = Font(family='Times New Roman', size=18)
        last_label_font_design = Font(family='Times New Roman', size=12, slant="italic", underline=1)

        # FRAMES

        left_frame = Frame(fg_root, bg='orange')
        right_frame = Frame(fg_root, bg='orange')

        center_frame = Frame(fg_root, bg='orange')
        logo_frame = Frame(center_frame, bg='orange')

        username_frame = Frame(center_frame, bg='orange')
        text_username_frame = Frame(username_frame, bg='orange')
        username_entery_box_frame = Frame(username_frame, bg='orange')

        password_frame = Frame(center_frame, bg='orange')
        text_password_frame = Frame(password_frame, bg='orange')
        password_entery_box_frame = Frame(password_frame, bg='orange')

        question_frame = Frame(center_frame, bg='orange')
        question_text_frame = Frame(question_frame, bg='orange')
        question_button_frame = Frame(question_frame, bg='orange')

        answer_frame = Frame(center_frame, bg='orange')
        answer_text_frame = Frame(answer_frame, bg='orange')
        answer_text_box_frame = Frame(answer_frame, bg='orange')

        two_buttons_frame = Frame(center_frame, bg='orange')
        create_account_frame = Frame(two_buttons_frame, bg='orange')
        close_frame = Frame(two_buttons_frame, bg='orange')

        line_frame = Frame(center_frame, bg='orange')

        label_and_button_frame = Frame(center_frame, bg='orange')
        label_frame = Frame(label_and_button_frame, bg='orange')
        button_frame = Frame(label_and_button_frame, bg='orange')

        bottom_line_frame = Frame(center_frame, bg='orange')

        # LABELS

        photo = PhotoImage(file="RUPAFIL.png")
        rupafil_logo_label = Label(logo_frame, image=photo, bg='orange')

        create_account_label = Label(logo_frame, text="Enter Details to forgot password", font=heading_font_design,
                                     bg='orange')
        line_label_1 = Label(logo_frame, text="---------------------------------------------------------------",
                             font=heading_font_design, bg='orange')

        username_label = Label(text_username_frame, text="Username", font=text_font_design, bg='orange')
        # password_label = Label(text_password_frame, text="Password", font=text_font_design)

        question_label = Label(question_text_frame, text="Choose a answer of this question", font=text_font_design,
                               bg='orange')

        answer_label = Label(answer_text_frame, text="Answer", font=text_font_design, bg='orange')

        line_label_2 = Label(line_frame, text="---------------------------------------------------------------",
                             font=heading_font_design, bg='orange')

        # have_a_account_label = Label(label_frame, text="If you already have a account then", font=last_label_font_design)

        line_label_3 = Label(bottom_line_frame, text="---------------------------------------------------------------",
                             font=heading_font_design, bg='orange')

        # BUTTONS

        question_button = Button(question_button_frame, text="WHAT IS YOUR RANK IN RUPAFIL ?  ",
                                 font=question_button_font_design)
        create_account_button = Button(create_account_frame, text="Create a Account", font=simple_button_font_design)
        close_button = Button(close_frame, text="Close", font=simple_button_font_design, bg='red')
        login_button = Button(button_frame, text="SHOW PASSWORD", font=simple_button_font_design, bg='lightblue',
                              command=get_pass)

        # ENTERY TEXT BOXES

        un = Entry(username_entery_box_frame, width=20, font=boxes_font_design)
        # password_text_box = Entry(password_entery_box_frame, width=20, font=boxes_font_design)
        ans = Entry(answer_text_box_frame, width=20, font=boxes_font_design)

        # FRAMES PACKING

        left_frame.pack(side=LEFT)

        center_frame.pack()

        logo_frame.pack(side=TOP)

        username_frame.pack()
        text_username_frame.pack(side=LEFT)
        username_entery_box_frame.pack(side=RIGHT)

        password_frame.pack()
        text_password_frame.pack(side=LEFT)
        password_entery_box_frame.pack(side=RIGHT)

        question_frame.pack()
        question_text_frame.pack(side=LEFT)
        question_button_frame.pack(side=RIGHT)

        answer_frame.pack()
        answer_text_frame.pack(side=LEFT)
        answer_text_box_frame.pack(side=RIGHT)

        two_buttons_frame.pack()
        create_account_frame.pack(side=LEFT)
        close_frame.pack(side=RIGHT)

        line_frame.pack()

        label_and_button_frame.pack()
        label_frame.pack(side=LEFT)
        button_frame.pack(side=RIGHT)

        bottom_line_frame.pack()

        right_frame.pack(side=RIGHT)

        # LABELS PACKING

        rupafil_logo_label.pack()
        create_account_label.pack()

        line_label_1.pack()
        username_label.pack(side=LEFT, padx=130)
        # password_label.pack(side=LEFT, padx=130)
        question_label.pack(side=LEFT, padx=10)
        answer_label.pack(side=LEFT, padx=140)
        line_label_2.pack()

        # have_a_account_label.pack(side=LEFT, padx=80)

        line_label_3.pack()

        # TEXT BOXES PACKING

        un.pack(side=RIGHT, padx=130)
        # password_text_box.pack(side=RIGHT, padx=130)
        ans.pack(side=RIGHT, padx=140)

        # BUTTONS PACKING

        question_button.pack(side=RIGHT, padx=20)
        create_account_button.pack(side=LEFT, padx=80, pady=30)
        close_button.pack(side=RIGHT, padx=160, pady=30)
        login_button.pack(side=RIGHT, padx=130)
        fg_root.mainloop()

m1_1=forgot_class()
m1_1.forgot_password()