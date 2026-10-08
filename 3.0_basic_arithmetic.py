"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Numbers input by user and calculatd with the four operations
# 2. Process:Program calculates with the four operations
# 3. Out:Result from the four operations 
# 4. What happens when the second number is zero, and why: Program displays a message instead of dividing, because division by zero causes an error.


# Your code below
first = float(input("enter the first number:"))
second = float(input("enter the second number:"))

# Inputting of numbers by user

print ("the sum of these two numbers is:", first + second)
#Test try. Adding 7 and 2 
print (first - second)
print (first * second)

if second != 0:
    division = first / second
    print("The division of two numbers is:", division)
else:
    print("The number 2 that you have entered is zero")

print (first / second)
# Every arithmetic function worked 

print ("Result will most likely be 3 when second number is // by 2:", first // second)
# ChatGPT told me that // and / are two different division forms

#When second number is 0. There is a division error


