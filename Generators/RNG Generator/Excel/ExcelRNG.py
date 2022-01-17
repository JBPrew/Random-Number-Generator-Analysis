import xlsxwriter #imports packages used in the file
import pandas as pd
import xlrd
import os
from random import randint

workName = input("Excel Worksheet Name: ") #Asks for user input as a string for the excel worksheet file name
if (workName == ""): #sets the default name if no name is given as a random integer
    workName = str(randint(0, 1000))

trials = int(input("Number of Data Points: ")) #Asks for user input for the number of trials and converts it into an integer
if (trials == 0): #sets the default number of trials if 0 is given as a 6250000
    trials = 6250000


# Create a workbook and add a worksheet.

workbook = xlsxwriter.Workbook("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/RNG Generator/Excel/RNGExcel" + workName +'.xlsx') #creates the excel file workbook
worksheet = workbook.add_worksheet() #adds a worksheet to the excel file
print("Excel Sheet Created") #confirms that the worksheet was created

# Start from the first cells. Rows and columns are zero indexed.
row = 0
col = 0


# Iterate over the data and write it out row by row.
for i in range(trials):
    worksheet.write_formula(row, col, '=RANDBETWEEN(0,1)') #writes the formula in the row and column in the for loop
    col+=1 #increases the column by 1 for the next for loop
    if (col >= 2500): #resets the column index to 0 and moves to the next row after reaching the 2500 column
        row += 1
        col = 0
print("Excel Sheet Filled") #confirms the worksheet has been filled
workbook.close() #closes the worbook and allows us to view it

#Attempts at getting excel to text file. Formatting was always wonky
# xlsx = pd.read_excel('C:/SciFair/RNG Generator/Excel/' + workName +'.xlsx', sheet_name = 'Sheet1')
# xlsxString = xlsx.to_string(header = False, index =False, sparsify = False, index_names = False, show_dimensions = False)
# txtFile = open('C:/SciFair/RNG Generator/Excel/' + workName +'.txt', "w")
# txtFile.write(xlsxString)
# txtFile.close()

# #Converts Excel to CSV
# read_file = pd.read_excel('C:/SciFair/RNG Generator/Excel/' + workName +'.xlsx', sheet_name = 'Sheet1')
# read_file.to_csv('C:/SciFair/RNG Generator/Excel/' + workName +'.csv', index = None, header=False)
# print("Converted to CSV")
# #Converts the CSV to TXT
# csv_file = 'C:/SciFair/RNG Generator/Excel/' + workName +'.csv'
# txt_file = 'C:/SciFair/RNG Generator/Excel/' + workName +'.txt'
# with open(txt_file, "w") as my_output_file:
#     with open(csv_file, "r") as my_input_file:
#         [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
#     my_output_file.close()
# print("Converted to txt")

# copyfile('C:/SciFair//RNG Generator/Excel/' + workName + '.xlsx', 'C:/SciFair//RNG Generator/Excel/' + workName + 'Sheet' + '.xlsx')
# os.rename('C:/SciFair//RNG Generator/Excel/' + workName +'.xlsx','C:/SciFair//RNG Generator/Excel/' + workName +'.txt')


print("Excel Sheet filled and openable") #confirms the workbook has closed and is now openable
