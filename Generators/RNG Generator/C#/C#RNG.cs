using System;

namespace CSharpRNG
{
  class Program
  {
    public static void Main(string[] args)
		{
      System.Random random = new System.Random(); 
      string desiredFile;
      Console.Write("File Name: "); // Type a number and press enter
      desiredFile = Console.ReadLine(); // Get user input from the keyboard
      if (desiredFile == "") {
          desiredFile = random.Next(0,1001).ToString();
          Console.WriteLine(desiredFile);
      }

      string trialsStr;
      Console.Write("Number of Data Points: "); // Type a number and press enter
      trialsStr = Console.ReadLine(); // Get user input from the keyboard
      int trials = Convert.ToInt32(trialsStr);
      if (trialsStr == "") {
          trials = 2500 * 2500;
      }

      Console.WriteLine("You entered '{0}'", desiredFile);
      Console.WriteLine("You entered '{0}'", trials);

      string fileLocation = "txtFiles/" + "C#" + desiredFile + ".txt";
      using (System.IO.StreamWriter file =
      new System.IO.StreamWriter("txtFiles/" + "C#" + desiredFile + ".txt"))
      {
        file.Write("");
      }

      using (System.IO.StreamWriter file =
      new System.IO.StreamWriter("txtFiles/" + "C#" + desiredFile + ".txt", true))
      {
        for (int i = 0; i < trials; i++)
        {
          file.Write(random.Next(0,2));
          if (i % 100000 == 0) {
            Console.WriteLine(i);
          }
        }
      }
      


    // ofstream file;
    // file.open(fileLocation, std::ios_base::app);
    // for (size_t i = 0; i < trials; i++)
    // {
    //     file << std::to_string(rand() % 2);
    //     if (i % 100000 == 0) {
    //         cout << "\n" + i;
    //     }
    // }
    // file.close();

		// }
    }
  }
}