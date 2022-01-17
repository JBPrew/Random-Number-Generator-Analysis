#include <iostream>
#include <string>
#include <fstream>
#include <time.h>
using namespace std;

int main()
{
    srand(time(NULL));
    string desiredFile;
    cout << "File Name: "; // Type a number and press enter
    getline (cin, desiredFile); // Get user input from the keyboard
    if (desiredFile == "") {
        desiredFile = std::to_string(rand() % 1001);
    }

    string trialsStr;
    cout << "Number of Data Points: "; // Type a number and press enter
    getline (cin, trialsStr); // Get user input from the keyboard
    int trials = stoi(trialsStr);


    cout << "Your File Name is: " << desiredFile; // Display the input value
    cout << "\nYour Number of Data Points: " << trials; // Display the input value
    
    string fileLocation = "C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/C++Seeded" + desiredFile + ".txt";

    //clears the file if there is an existing one
    ofstream fileCheck;
    fileCheck.open(fileLocation);
    fileCheck << "";

    ofstream file;
    file.open(fileLocation);
    for (size_t i = 0; i < trials; i++)
    {
        file << std::to_string(rand() % 2);
        if (i % 100000 == 0) {
            cout << i;
            cout << "\n";
        }
    }
    file.close();
    return 0;
}
