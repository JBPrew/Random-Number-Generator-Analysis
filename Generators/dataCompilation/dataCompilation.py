import xlsxwriter #imports packages used in the file
import xlrd
import os

workbook = xlsxwriter.Workbook("C:/Users/Jack's PC/Desktop/GHP/Project/StatResults/FinalResults.xlsx") #creates the excel file workbook
worksheet = workbook.add_worksheet() #adds a worksheet to the excel file
print("Excel Sheet Created") #confirms that the worksheet was created
# Start from the first cells. Rows and columns are zero indexed.
row = 0
col = 0

languages = ['C#', "C++", "Go", "Java","JavaScript", "Julia", "Python", "R", "Ruby"]
testNames = ['ApproximateEntropy', 'BlockFrequency', 'CumulativeSums', 'FFT', 'Frequency', 'LinearComplexity', 'LongestRun', 'NonOverlappingTemplate', 'OverlappingTemplate', 'RandomExcursions', 'RandomExcursionsVariant', 'Rank', 'Runs', 'Serial', 'Universal']

worksheet.write(row, col, "Languages")
col +=1
for test in testNames:
    worksheet.write(row, col, test)
    col+=1
row +=2
col = 0
for lang in languages:
    worksheet.write(row, col, lang)
    for test in testNames:
        fileLoc = "C:/Users/Jack's PC/Desktop/GHP/Project/StatResults/" + lang + "/" + test + "/results.txt"
        with open(fileLoc, "r") as file:
            stats = file.readlines()
            
        col +=1
        
        # #write all
        # for line in stats:
        #     worksheet.write(row, col, line)
        #     print('lol')
        #     col += 1
    
        #write average
        sum = 0
        for line in stats:
            sum += float(line)
        worksheet.write(row, col, sum / (len(stats)))
        
        
    row += 1
    col = 0

workbook.close()