public class recursion
{
    public static void main(String[] args) 
    {
        String myStr = "desrever si gnirts eht";
        System.out.println(reverse_string(myStr));
        
        fibonacci(10);
    }
    //This method takes the string to be reversed as a parameter
    public static String reverse_string(String myStr)
    {
        //defines and initialises the string variable to hold the reversed string.
        String reversed = ""; 
        //checks if the string parameter is empty
        if(myStr.isEmpty())
        {
            System.out.println("String is empty.");
            return myStr;
        }
        else
        {
            /*loops through the entire string from the making 
             *the last character the first up till the first becomes 
             *the last in the reversed string
             */
            for(int i=myStr.length()-1; i>=0; i--)
            {
                reversed = reversed + myStr.charAt(i);
            }
            return reversed;
        }
    }
    /*This method takes in the maximum number as an integer. 
     *Note, this method returns no values but a printout instead.
    */
    public static void fibonacci(int maxNumber)
    {
        int previousNumber = 0;
        int nextNumber = 1;
        
        System.out.print("Fibonacci Series of "+maxNumber+" numbers: ");
        
    	for (int i = 0; i < maxNumber; i++)
    	{
    	    System.out.print(previousNumber+" ");
    	    /* Each time we run the loop, we are assigning the second number
    	     * to the first number and assigning the sum of last two
    	     * numbers to the second number
	     */
    	    int sum = previousNumber + nextNumber;
    	    previousNumber = nextNumber;
    	    nextNumber = sum;
    	 }
    }
}