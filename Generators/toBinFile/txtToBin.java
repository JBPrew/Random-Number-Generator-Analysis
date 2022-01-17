
//imports necesarry packages
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class txtToBin {
  public static void main(String[] args) throws IOException {
    // asks for file path of desired text file
    Scanner s = new Scanner(System.in);
    System.out.print("File Name: "); // usually "C:\SciFair\txtToBinFile\smam.txt" "C:\SciFair\RNGExcel.txt"
    String inputFile = s.nextLine(); // takes in input
    System.out.print("Bin Output Name: ");
    String binOutput = s.nextLine(); // takes in input
    if (binOutput.equals("")) {
      binOutput = inputFile;
    }
    s.close();
    File file = new File("txtFiles/" + inputFile + ".txt"); // creates file in the java program
    byte[] fileData = new byte[(int) file.length()]; // new byte array with length of text file
    System.out.println(file.length()); // prints length of file for checking with initial input
    // imports data to byte array
    FileInputStream in = new FileInputStream(file);
    in.read(fileData);
    in.close(); // closes the scanner

    // converts fileData byte array to string
    String content = new String(fileData);

    // writes to bin file
    try {
      File binFile = new File("C:/SciFair/binFiles/" + binOutput + ".bin"); // creates the binfile in the program
      FileWriter myWriter = new FileWriter(binFile); // activates writing to the file
      myWriter.write(content); // writes the content to the .bin file
      myWriter.close(); // closes the writer
      System.out.println("Successfully wrote to the file."); // confirms the data was converted to a .bin file
    } catch (IOException e) { // catches an error and reports it
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}