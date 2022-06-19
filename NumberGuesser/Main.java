package NumberGuesser;
import java.util.Scanner;

import java.lang.Math;


public class Main {
    public static boolean gotAnswer = false;
    public static int tries = 0;
    public static void main(String[] args) 
    {
        
        Scanner input = new Scanner(System.in);
        System.out.println("Would you like to play number guesser? type yes or no");
        //Str ans = input.next();
        if(input.next().equals("yes"))
        {
            System.out.println("Great! Let's do this!");
            int Number = (int)(Math.random() * 100);
            //int number = Number;
            System.out.println(Number);
            while(gotAnswer == false)
            {
                System.out.println("Guess a number");
                tries++;
                System.out.println(guess(input.nextInt(), Number));
                
            }
        }
        input.close();
    }
    
    public static String guess(int guessNum , int num)
    {
        if(guessNum == num)
        {   
            gotAnswer = true;
            return ("You got it!"+ " It took you " + tries + " tries to get the number");
        }

        else if(guessNum < num)
        {
            return ("The number is greater than that");
        }

        else
        {
            return ("The number is less than that");
        }
    }
    
}


