from random import randint #imports necessary packages

desiredFile = input("File Name: ") #Asks for user input as a string for the desired file name and stores it in a variable, desiredFile
if (desiredFile == ""): #sets the default name if no name is given as a random integer
    desiredFile = str(randint(0, 1000))

trials = int(input("Number of Data Points: ")) #Asks for user input for the number of data points and converts it into an integer and stores it in a variable, trials
if (trials == 0): #sets the default number of trials if 0 is given as a 6250000
    trials = 2500*2500


txtFileClear =  open("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/Python" + desiredFile + ".txt", "w") #opens the file as writable in order to clear the file if it already exists
txtFileClear.write("") #clears the file by writing nothing into it and overriding previous contents of the file 
txtFileClear.close() #closes the file so it can be opened again as appendable

txtFile = open("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/Python" + desiredFile + ".txt", "a") #opens the file as appendable so more data can be added
for i in range(trials): #for loops runs for the inputted number of trials and adds a random integer [0,1] to the file meaning 0s and 1s are added
    txtFile.write(str(randint(0, 1))) #writes the random integer into the file
    if i % 100000 == 0: #prints status updates as the file is being written showing progress
        print(i)
txtFile.close() #closes the file

print("Successfully wrote to file") #confirms succesful writing to the file
