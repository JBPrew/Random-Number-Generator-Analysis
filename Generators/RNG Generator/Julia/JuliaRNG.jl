# prompt to input
print("File Name: ") 
  
# Calling rdeadline() function
desiredFile = readline()

print("Number of Data Points: ")
trials = readline()
trials = parse(Int64, trials) 

open(string("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/Julia", desiredFile, ".txt"), "w") do file
    for i in 1:trials
        write(file, string(rand(0:1)))
    end
end