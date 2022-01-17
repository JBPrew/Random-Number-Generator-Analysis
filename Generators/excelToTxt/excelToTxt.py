
# Reading an excel file using Python
import xlrd
 
# Give the location of the file
loc = ("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/RNG Generator/Excel/RNGExcelFinal.xlsx")
print('start')
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print("Excel found")
 
txtFileClear =  open("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/ExcelFinal.txt", "w") #opens the file as writable in order to clear the file if it already exists
txtFileClear.write("") #clears the file by writing nothing into it and overriding previous contents of the file 
txtFileClear.close() #closes the file so it can be opened again as appendable

txtFile = open("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/ExcelFinal.txt", "a") #opens the file as appendable so more data can be added

# For row 0 and column 0
for i in range (0, 4001):
    for j in range(2500):
        txtFile.write(str(sheet.cell_value(i, j))) #writes the random integer into the file