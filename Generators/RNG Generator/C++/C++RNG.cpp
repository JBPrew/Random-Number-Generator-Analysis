#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
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
    if (trialsStr == "") {
        trials = 2500 * 2500;
    }

    cout << "Your File Name is: " << desiredFile; // Display the input value
    cout << "\nYour Number of Data Points: " << trials; // Display the input value
    
    string fileLocation = "txtFiles/C++" + desiredFile + ".txt";

    //clears the file if there is an existing one
    ofstream fileCheck;
    fileCheck.open(fileLocation);
    fileCheck << "";

    ofstream file;
    file.open(fileLocation, std::ios_base::app);
    for (size_t i = 0; i < trials; i++)
    {
        file << std::to_string(rand() % 2);
        if (i % 100000 == 0) {
            cout << "\n" + i;
        }
    }
    file.close();
    return 0;
}
