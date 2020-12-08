import xlsxwriter as excelWriter
import datetime


def excelReportGeneration(allData):
    currentDataAndTime = datetime.datetime.now()
    # print(currentDataAndTime)
    dateAndTime = currentDataAndTime.strftime("%Y.%m.%d-%H.%M.%S")
    # print(formatedTimeAndDate)
    excelfileName = "report-" + str(dateAndTime) + ".xlsx"
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

# dataFromDatabase = [[1, "Ali", "Yunus", 45],[2,"Kamran","Latif",49],[3,"Jamil","Rizwan",41],[4,"Hussain","Aslam",39],[5,"Usman", "Hassan",31]]
dataFromDatabase = [[1, "Ali", 45],[2,"Kamran",49],[3,"Jamil",41],[4,"Hussain",39],[5,"Usman",31]]


import sqlite3
import numpy as np
conn = sqlite3.connect("employee.db")
cur = conn.cursor()
cur.execute("SELECT * FROM employee")
# cur.execute("INSERT INTO employee VALUES (NULL,?,?,?,?,?,?,?,?)", (None,np.arange(0,500,0.5)))
# conn.commit()
cur.execute("SELECT * FROM employee")
rows = cur.fetchall()


conn.close()
print(rows)
excelReportGeneration(rows)