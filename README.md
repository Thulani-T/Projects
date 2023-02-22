line 9: Comment says the code creates a method. You should consider saying the code creates a string object
line 11: This code seems to hard code the print out for the fibonacci series. This means that even when the maxNumber value is changed, the output will remain the same
line 21: Maybe consider rephrasing the output message? I can't seem to make out what it means.
line 25: the .substring() method in the String class returns the string variable without the first character. Is this what you want to do?
line 26: Should the method called here not be reverse_string() instead? method reverseString does not seem to appear anywhere in this class
line 26: I am not sure that I understand the logic in the values passed in the method reverse_string(). What is this code supposed to do? 
line 28: I am not sure that I understand the definition of this method. Should the parameter maxNumber be of data type T? Is T even a data type?
line 30: If maxNumber is already defined as the parameter, you should remove "int" as this suggests a duplicate definition of this value
lines 36 to 43: It is a good idea using a for loop here...Well done! The logic here is also spot on!!
lines 38 to 40: It is absolutely not incorrect the way you have used your comments here. You could also use block commenting when your comments are longer than a single line.
		(e.g /*On each iteration, we are assigning second number
	               *to the first number and assigning the sum of last two
	     		*numbers to the second number */
line 11: I would invoke the method "function()" in the main method or remove the method altogether and have its contents in the main method.

*If you require any more clearity on this review. Please feel free to make contact with me.