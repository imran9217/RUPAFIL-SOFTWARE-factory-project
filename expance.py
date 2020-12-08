from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image
from tkinter.font import Font
from tkinter import messagebox









from sqlite3 import dbapi2 as sqlite
import datetime
name = []
rs = []
# now = date()
month = ['January','February','March','April','May','Jun','July','August','September','October','November','December']

c=sqlite.connect("stock.db")
cur=c.cursor()


def insert_expenses():
    global day,name,rs,date
    success = True
    try:
        for i in range(len(name)):
            print(date,name[i].get(),rs[i].get())
            sql ="CREATE TABLE IF NOT EXISTS  expenses(date text,name text, rs number );"
            cur.execute(sql)
            sql = "insert into expenses(date,name,rs) values(date('%s'),'%s',%.2f);"% (date,name[i].get(),float(rs[i].get()))
            cur.execute(sql)
            print(sql)
    except Exception as exp:
        c.rollback()
        success = False
        # insert_error(exp)
    if success:
        c.commit()
        # insert_info("Expenses Successfully Inserted")
        messagebox.showinfo('Successfull', 'Expenses Successfully Inserted')
        # total =rs[i]
        # ref(date)
total =35020
def Addexpances_gui():
    enter_exp_root = Toplevel()
    enter_exp_root.state("zoomed")
    enter_exp_root.configure(bg='orange')

    # FONT'S DESIGNS

    img_add =PhotoImage(file="ADD.png")
    img_add_lable=Label(enter_exp_root,image=img_add,bg='orange')
    img_add_lable.pack(side=TOP)

    font_design = Font(family='Times New Roman', size=22)
    buttons_font_design = Font(family='Times New Roman', size=16)
    last_button_font_design = Font(family='Times New Roman', size=20)

    # FARMES

    top_frame = Frame(enter_exp_root, height=100,bg='orange')

    center_frame = Frame(enter_exp_root,bg='orange')
    line_1_label_frame = Frame(center_frame,bg='orange')

    name_and_rs_label_frame = Frame(center_frame,bg='orange')
    name_1_label_frame = Frame(name_and_rs_label_frame,bg='orange')
    rs_1_label_frame = Frame(name_and_rs_label_frame,bg='orange')

    upper_entery_text_boxes_farme = Frame(center_frame,bg='orange')
    entery_text_box_1_farme = Frame(upper_entery_text_boxes_farme,bg='orange')
    entery_text_box_2_farme = Frame(upper_entery_text_boxes_farme,bg='orange')

    lower_entery_text_boxes_frame = Frame(center_frame,bg='orange')
    entery_text_box_3_farme = Frame(lower_entery_text_boxes_frame,bg='orange')
    entery_text_box_4_farme = Frame(lower_entery_text_boxes_frame,bg='orange')

    # space_frame_1 = Frame(center_frame, width=200, height=100,bg='orange')

    buttons_frame = Frame(center_frame,bg='orange')

    # space_frame_2 = Frame(center_frame, width=200, height=100,bg='orange')

    expenses_label_frame = Frame(center_frame,bg='orange')

    # space_frame_3 = Frame(center_frame, width=200, height=20,bg='orange')

    name_rs_delete_label_frame = Frame(center_frame,bg='orange')

    line_2_label_frame = Frame(center_frame,bg='orange')

    last_labels_frame = Frame(center_frame,bg='orange')

    # LABELS

    line_1_label = Label(line_1_label_frame, text="--------------------------------------------------------------",
                         font=font_design,bg='orange')
    name_1_label = Label(name_1_label_frame, text="Name", font=font_design,bg='orange')
    rs_1_label = Label(rs_1_label_frame, text="Rs.", font=font_design,bg='orange')
    design_label_1 = Label(expenses_label_frame, text="|-------------------------------------|", font=font_design,bg='orange')
    expenses_label = Label(expenses_label_frame, text="|      Expensis of this Date       |", font=font_design,bg='orange')
    design_label_2 = Label(expenses_label_frame, text="|-------------------------------------|", font=font_design,bg='orange')
    name_2_label = Label(name_rs_delete_label_frame, text="Name", font=font_design,bg='orange')
    rs_2_label = Label(name_rs_delete_label_frame, text="Rs.", font=font_design,bg='orange')
    delete_label = Label(name_rs_delete_label_frame, text="Delete", font=font_design,bg='orange')
    line_2_label = Label(line_2_label_frame, text="-------------------------------------------------------------",
                         font=font_design,bg='orange')
    total_label = Label(last_labels_frame, text="Total", font=font_design,bg='orange')
    equal_label = Label(last_labels_frame, text="=", font=font_design,bg='orange')
    zero_label = Label(last_labels_frame, text= total, font=font_design,bg='orange')

    # ENTERY TEXT BOXES
    # date = now.replace(day=i)



    name = Entry(entery_text_box_1_farme, width=20, font=font_design)
    rs = Entry(entery_text_box_2_farme, width=20, font=font_design)
    # entery_text_box_3 = Entry(entery_text_box_3_farme, width=20, font=font_design)
    # entery_text_box_4 = Entry(entery_text_box_4_farme, width=20, font=font_design)

    # BUTTONS

    add_box_button = Button(buttons_frame, text="-------", font=buttons_font_design)
    insert_button = Button(buttons_frame, text="Insert", font=buttons_font_design,command=insert_expenses)
    renturn_to_mainmenu_button = Button(buttons_frame, text="Return To Main Menu", font=buttons_font_design, command=enter_exp_root.destroy)

    # FARME'S PACKING

    top_frame.pack(side=TOP, fill=BOTH)

    center_frame.pack()

    line_1_label_frame.pack()

    name_and_rs_label_frame.pack()
    name_1_label_frame.pack(side=LEFT)
    rs_1_label_frame.pack(side=RIGHT)

    upper_entery_text_boxes_farme.pack()
    entery_text_box_1_farme.pack(side=LEFT)
    entery_text_box_2_farme.pack(side=RIGHT)

    lower_entery_text_boxes_frame.pack()
    # entery_text_box_3_farme.pack(side=LEFT)
    # entery_text_box_4_farme.pack(side=RIGHT)

    center_frame.pack()

    # space_frame_1.pack(fill=BOTH)

    buttons_frame.pack()

    # space_frame_2.pack(fill=BOTH)

    expenses_label_frame.pack()

    # space_frame_3.pack(fill=BOTH)

    name_rs_delete_label_frame.pack()

    line_2_label_frame.pack()

    last_labels_frame.pack()

    # LABEL'S PACKING

    line_1_label.pack()

    name_1_label.pack(padx=110)
    rs_1_label.pack(padx=110)

    design_label_1.pack()
    expenses_label.pack()
    design_label_2.pack()

    name_2_label.grid(padx=50, row=1, column=1)
    rs_2_label.grid(padx=50, row=1, column=2)
    delete_label.grid(padx=50, row=1, column=3)
    line_2_label.pack()

    total_label.grid(padx=50, row=1, column=1)
    equal_label.grid(padx=50, row=1, column=2)
    zero_label.grid(padx=50, row=1, column=3)

    # ENTERY TEXT BOXES'S PACKING

    name.pack()
    rs.pack()
    # entery_text_box_3.pack()
    # entery_text_box_4.pack()

    # BUTTON'S PACKING

    add_box_button.grid(padx=10, row=1, column=1)
    insert_button.grid(padx=10, row=1, column=2)
    renturn_to_mainmenu_button.grid(padx=10, row=1, column=3)

    enter_exp_root.mainloop()

def expan():

    ex_root=Toplevel()
    ex_root.state("zoomed")
    ex_root.configure(bg="orange")

    global im
    im = PhotoImage(file="ex.png")

    im_lable=Label(ex_root,image=im)
    im_lable.pack(side=TOP)

    # FONT'S DESIGNS

    font_design = Font(family='Times New Roman', weight='bold', size=22)
    buttons_font_design = Font(family='Times New Roman', size=16)
    last_button_font_design = Font(family='Times New Roman', size=20)

    # FRAMES

    left_frame = Frame(ex_root, width=150,bg="orange")
    right_frame = Frame(ex_root, width=150,bg="orange")
    top_frame = Frame(ex_root, height=150,bg="orange")
    bottom_frame = Frame(ex_root, height=100,bg="orange")

    center_frame = Frame(ex_root,bg="orange")
    month_and_label_frame = Frame(center_frame,bg="orange")
    line_label_frame = Frame(center_frame,bg="orange")

    buttons_frame = Frame(center_frame,bg="orange")

    last_button_frame = Frame(center_frame,bg="orange")

    # LABELS

    month_label = Label(month_and_label_frame, text="Current Month December", font=font_design,bg="orange")
    today_date_label = Label(month_and_label_frame, text=datetime.datetime.now(), font=font_design,bg="orange")
    line_label = Label(line_label_frame, text="-----------------------------------------------------", font=font_design,bg="orange")

    # BUTTONS

    button_one = Button(buttons_frame, text="1", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_two = Button(buttons_frame, text="2", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_three = Button(buttons_frame, text="3", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_four = Button(buttons_frame, text="4", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_five = Button(buttons_frame, text="5", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_six = Button(buttons_frame, text="6", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_seven = Button(buttons_frame, text="7", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_eight = Button(buttons_frame, text="8", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_nine = Button(buttons_frame, text="9", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_ten = Button(buttons_frame, text="10", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_eleven = Button(buttons_frame, text="11", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_twelve = Button(buttons_frame, text="12", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_thirteen = Button(buttons_frame, text="13", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_fourteen = Button(buttons_frame, text="14", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_fifteen = Button(buttons_frame, text="15", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_sixteen = Button(buttons_frame, text="16", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_seventeen = Button(buttons_frame, text="17", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_eighteen = Button(buttons_frame, text="18", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_ninteen = Button(buttons_frame, text="19", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_twenty = Button(buttons_frame, text="20", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_twent_one = Button(buttons_frame, text="21", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_twenty_two = Button(buttons_frame, text="22", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_twenty_three = Button(buttons_frame, text="23", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_twenty_four = Button(buttons_frame, text="24", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_twenty_five = Button(buttons_frame, text="25", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_twenty_six = Button(buttons_frame, text="26", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_twenty_seven = Button(buttons_frame, text="27", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_twenty_eight = Button(buttons_frame, text="28", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_twenty_nine = Button(buttons_frame, text="29", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_thirty = Button(buttons_frame, text="30", width=7, font=buttons_font_design,command=Addexpances_gui)
    button_thirty_one = Button(buttons_frame, text="31", width=7, font=buttons_font_design,command=Addexpances_gui)

    return_mainmenu_button = Button(last_button_frame, text="Return to Main Menu", width=20, height=2,
                                    font=last_button_font_design,bg= 'gray', command=ex_root.destroy)

    # FARME'S PACKING

    left_frame.pack(side=LEFT, fill=BOTH)
    right_frame.pack(side=RIGHT, fill=BOTH)
    top_frame.pack(side=TOP, fill=BOTH)
    bottom_frame.pack(side=BOTTOM, fill=BOTH)
    center_frame.pack()
    month_and_label_frame.pack()
    line_label_frame.pack()

    buttons_frame.pack()

    last_button_frame.pack()

    # LABLE'S PACKING

    month_label.pack()
    today_date_label.pack()
    line_label.pack()

    # BUTTON'S PACKING

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
    button_eleven.grid(row=2, column=1)
    button_twelve.grid(row=2, column=2)
    button_thirteen.grid(row=2, column=3)
    button_fourteen.grid(row=2, column=4)
    button_fifteen.grid(row=2, column=5)
    button_sixteen.grid(row=2, column=6)
    button_seventeen.grid(row=2, column=7)
    button_eighteen.grid(row=2, column=8)
    button_ninteen.grid(row=2, column=9)
    button_twenty.grid(row=2, column=10)
    button_twent_one.grid(row=3, column=1)
    button_twenty_two.grid(row=3, column=2)
    button_twenty_three.grid(row=3, column=3)
    button_twenty_four.grid(row=3, column=4)
    button_twenty_five.grid(row=3, column=5)
    button_twenty_six.grid(row=3, column=6)
    button_twenty_seven.grid(row=3, column=7)
    button_twenty_eight.grid(row=3, column=8)
    button_twenty_nine.grid(row=3, column=9)
    button_thirty.grid(row=3, column=10)
    button_thirty_one.grid(row=4, column=1)

    return_mainmenu_button.pack()

    ex_root.mainloop()



def stock_month_panel():

    stock_root_month=Toplevel()
    stock_root_month.configure(bg="orange")
    stock_root_month.state("zoomed")

    font_design = Font(family='Times New Roman', size=22)

    # FRAMES

    top_frame = Frame(stock_root_month, bg='Orange', height=250)
    bottom_frame = Frame(stock_root_month, bg='Orange', height=450)
    center_frame = Frame(stock_root_month, bg='Orange')
    space_frame_1 = Frame(center_frame, bg='Orange', width=200, height=100)
    month_label_frame = Frame(center_frame)
    date_label_frame = Frame(center_frame)
    space_frame_2 = Frame(center_frame, bg='Orange', width=200, height=30)
    buttons_frame = Frame(center_frame)
    space_frame_3 = Frame(center_frame, bg='Orange', width=200, height=100)
    last_button_frame = Frame(center_frame, bg='Orange', )

    # IMAGE

    my_image = ImageTk.PhotoImage(Image.open("tag.jpeg"))

    # LABELS

    image_label = Label(top_frame, image=my_image)
    month_label = Label(month_label_frame, text="Current Month : December", bg='Orange', font=font_design)
    date_label = Label(date_label_frame, text="Today's Date : 2020-12-06", bg='Orange', font=font_design)

    # BUTTONS

    button_one = Button(buttons_frame, text="January", width=10, font=font_design, command =expan)
    button_two = Button(buttons_frame, text="Feburary", width=10, font=font_design, command =expan)
    button_three = Button(buttons_frame, text="March", width=10, font=font_design, command =expan)
    button_four = Button(buttons_frame, text="April", width=10, font=font_design, command =expan)
    button_five = Button(buttons_frame, text="May", width=10, font=font_design, command =expan)
    button_six = Button(buttons_frame, text="June", width=10, font=font_design, command =expan)
    button_seven = Button(buttons_frame, text="July", width=10, font=font_design, command =expan)
    button_eight = Button(buttons_frame, text="August", width=10, font=font_design, command =expan)
    button_nine = Button(buttons_frame, text="September", width=10, font=font_design, command =expan)
    button_ten = Button(buttons_frame, text="October", width=10, font=font_design, command =expan)
    button_eleven = Button(buttons_frame, text="November", width=10, font=font_design, command =expan)
    button_tweleve = Button(buttons_frame, text="December", width=10, font=font_design, command =expan)

    last_button = Button(last_button_frame, text="Return To Main Menu", width=20, font=font_design, command=stock_root_month.destroy)

    # FRAME'S PACKING

    top_frame.pack(fill=BOTH)
    center_frame.pack(fill=BOTH)
    space_frame_1.pack(fill=BOTH)
    month_label_frame.pack(fill=BOTH)
    date_label_frame.pack(fill=BOTH)
    space_frame_2.pack(fill=BOTH)
    buttons_frame.pack()
    space_frame_3.pack(fill=BOTH)
    last_button_frame.pack()
    bottom_frame.pack(fill=BOTH)

    # LABEL'S PACKING

    month_label.pack(fill=BOTH)
    date_label.pack(fill=BOTH)
    image_label.pack()

    # BUTTON'S PACKING

    button_one.grid(row=1, column=1)
    button_two.grid(row=1, column=2)
    button_three.grid(row=1, column=3)
    button_four.grid(row=1, column=4)
    button_five.grid(row=1, column=5)
    button_six.grid(row=1, column=6)
    button_seven.grid(row=2, column=1)
    button_eight.grid(row=2, column=2)
    button_nine.grid(row=2, column=3)
    button_ten.grid(row=2, column=4)
    button_eleven.grid(row=2, column=5)
    button_tweleve.grid(row=2, column=6)

    last_button.pack()
    # if name == "" or rs == "":
    #     messagebox.showwarning('Warning', 'Please Fill all the details')
    stock_root_month.mainloop()


stock_month_panel()


import xlsxwriter as excelWriter
import datetime


def excelReportGeneration(allData):
    currentDataAndTime = datetime.datetime.now()
    # print(currentDataAndTime)
    dateAndTime = currentDataAndTime.strftime("%Y.%m.%d-%H.%M.%S")
    # print(formatedTimeAndDate)
    excelfileName = "report-stock" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()
    row = 0
    column = 0
    # print(len(allData[0]))
    # myWorksheet.write(row, column, "Id")
    # myWorksheet.write(row, column+1, "Name")
    # myWorksheet.write(row, column+2, "Marks")
    for eachRow in allData:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0
    myWorkbook.close()




import sqlite3

conn = sqlite3.connect("stock.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS  expenses(date text,name text, rs number );")

cur.execute("SELECT * FROM expenses")
rows = cur.fetchall()


conn.close()
print(rows)
excelReportGeneration(rows)
# stock_month_panel()

