package main

import ( //imports necessary packages
	"fmt"
	"log"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func main() {
	s1 := rand.NewSource(time.Now().UnixNano()) //creates the seed to be inputted to the rand package
	r1 := rand.New(s1)                          //seeds the rand package using s1
	fmt.Print("File Name: ")                    //asks for user input of file name
	var desiredFile string                      //declares desiredFile as a string. Allows for direct scanning using fmt and reduces packages (no bufio package)
	fmt.Scanln(&desiredFile)                    //scans the user input and stores it in desiredFile string
	if desiredFile == "" {                      //assigns a random integer as a name if no name is given
		desiredFileInt := r1.Intn(1000)
		desiredFile = strconv.Itoa(desiredFileInt)
	}

	fmt.Print("Number of Data Points: ") //asks for user input of number of trials
	var trials int                       //declares trials as a integer. Allows for direct scanning using fmt and reduces packages (no bufio package)
	fmt.Scan(&trials)                    //scans the user input and stores it in trials int
	if trials == 0 {                     //assigns 625000 as the trial number if 0 is given as the input
		trials = 2500 * 2500
	}

	fmt.Println(desiredFile) //prints and confirms user input
	fmt.Println(trials)      //prints and confirms user input

	file, err := os.Create("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/GOSeeded" + desiredFile + ".txt") //creates the file
	if err != nil {                                                                    //prints the error if their is an error in creating the file
		log.Fatal("Cannot create file", err)
	}
	defer file.Close() //does not close the file until the main function is finished

	for i := 1; i <= trials; i++ { //for loops runs for the inputted number of trials and adds a random integer [0,2) to the file meaning 0s and 1s are added
		if i%100000 == 0 {
			fmt.Println(i)
		}
		fmt.Fprintf(file, strconv.Itoa(r1.Intn(2)))
	}
	fmt.Println("Successfully wrote to file") //confirms file was wrriten to succesfully
}
