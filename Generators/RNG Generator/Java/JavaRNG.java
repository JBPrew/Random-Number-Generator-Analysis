import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;
import java.io.IOException;

public class JavaRNG {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("File Name: ");
        String desiredFile = s.nextLine(); // takes in input
        if (desiredFile.equals("")) {
            desiredFile = Integer.toString((int) (Math.random() * 1001));
        }
        System.out.print("Number of Data Points: ");
        int trials = s.nextInt(); // takes in input
        if (trials == 0) {
            trials = 2500 * 2500;
        }
        s.close();
        
        File file = new File("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/Java" + desiredFile + ".txt");
        
        if (file.exists()){
            try {
                FileWriter myWriter = new FileWriter(file, false);
                myWriter.write("");
                myWriter.close();
                System.out.println("Successfully cleared the file.");
            } catch (IOException e) {
                System.out.println("An error occurred.");
                e.printStackTrace();
            }
        }

        try (FileWriter myWriter = new FileWriter(file, true)) {
            for (int i = 0; i < trials; i++) {
                myWriter.write(Integer.toString((int) (Math.random() * 2))); // writes the content to the .bin file
                if (i % 100000 == 0) {
                    System.out.println(i);
                }
            }
            myWriter.close(); // closes the writer
        } catch (IOException e) { // catches an error and reports it
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        System.out.println("Successfully wrote to the file."); // confirms the data was converted to a .bin file

    }
}