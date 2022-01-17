print "File Name: " #prompts user to input the file name
desiredFile = gets.chomp #takes user input as a string and stores it  in a variable, desiredFile
desiredFile = rand(1..1000).to_s if desiredFile == "" #sets the default name if no name is given as a random integer

print "Number of Data Points: " #prompts user to input the number of trials
trials = gets.chomp.to_i #takes user input for the number of data points and converts it into an integer and stores it in a variable, trials
trials = 2500*2500 if trials == 0 #sets the default number of trials if 0 is given as a 6250000

File.write("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/Ruby" + desiredFile + ".txt", "") #opens the file and writes to the file in order to clear the file if it already exists
file = File.open("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/Ruby" + desiredFile + ".txt", mode: "a") #opens the file as appendable so more data can be added
for i in 0...trials do #for loops runs for the inputted number of trials and adds a random integer [0,1] to the file meaning 0s and 1s are added
    file.write(rand(0..1)) #writes the random integer into the file
    puts i if i % 100000 == 0 #prints status updates as the file is being written showing progress
end

puts "Successfully wrote to file" #confirms succesful writing to the file