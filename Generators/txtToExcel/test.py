import os


txtFileName = input("Name of txt File: ")
while txtFileName == "":
    txtFileName = input("Name of txt File: ")


txtFile = open("txtFiles/" + txtFileName + ".txt", "r")
txtString = txtFile.read()
print(len(txtString))