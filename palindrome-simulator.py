# palindrome numbers are numbers that are the same number when their digits are reversed

# (e.g 636 is 636 reversed, making it a palindrome)


# to make a project determining if a number is a palindrome, take an input from the user
#use a for loop to traverse the digits, and see if the new number equals the original number

# palindrome numbers are numbers that are the same number when their digits are reversed

# (e.g 636 is 636 reversed, making it a palindrome)


# to make a project determining if a number is a palindrome, take an input from the user
#use a for loop to traverse the digits, and see if the new number equals the original number


print("This is a Palindrome Simulator. We will check to see if a number you give us is a palindrome.")
number_test = int(input("Enter your number: "))

new_number = number_test
reversed = 0
while new_number > 0:
        digit = new_number % 10
        reversed = reversed * 10 + digit
        new_number//=10

#for(x) in range (len(number_test)):
    #This will print the number entered in reverse,
    #starting from the last number and going back to the first
    #print number_test()


if (number_test == reversed):
        print("Your number is a palindrome!")
else:
        print("Unfortunately, your number is not a palindrome.")
        print("Remember for a number to be a palindrome, we need to be able to print the same digits forwards and backwards.")