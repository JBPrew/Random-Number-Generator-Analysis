import xlsxwriter
import pandas as pd
import xlrd
from xlsxwriter.utility import xl_rowcol_to_cell

txtFileName = input("Name of txt File: ")
while txtFileName == "":
    txtFileName = input("Name of txt File: ")

workName = input("Excel Worksheet Name: ")
if (workName == ""):
    workName = txtFileName
# Create a workbook and add a worksheet.

txtFile = open("txtFiles/" + txtFileName + ".txt", "r")
# txtFileLength = len(txtFile.readlines())
txtString = txtFile.read()


workbook = xlsxwriter.Workbook('C:/SciFair/txtToExcel/' + workName + '.xlsx')
worksheet = workbook.add_worksheet()
print("Excel Sheet Created")


# Start from the first cell. Rows and columns are zero indexed.
row = 5
col = 0

start = xl_rowcol_to_cell(row, col)

# Iterate over the data and write it out row by row.
for i in range(len(txtString)):
    worksheet.write(row, col, int(txtString[i]))
    col += 1
    if (col >= 2500):
        row += 1
        col = 0
print("Excel Sheet Filled")
col = 2500
end = xl_rowcol_to_cell(row, col)
worksheet.write_formula(0, 0, "=AVERAGE(" + start + ":" + end + ")")
worksheet.write_formula(1, 0, "=MEDIAN(" + start + ":" + end + ")")
worksheet.write_formula(2, 0, "=MODE(" + start + ":" + end + ")")
workbook.close()
