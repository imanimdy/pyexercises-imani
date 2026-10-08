"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: List of numbers from exercise 4.0
# 2. Process: Select the third item in the list and use a for loop to go through each number.
# 3. Out: Display the third item and print each number with the message "My favorite number is".
# 4. What I compute for each item, and why it is worth showing:
#My list is about numbers from 1 to 10.
# I used the code to find the third item, which is 1, and display each number individually.
# This is interesting because it shows how Python can access specific items and go through a list.


# Your code below

#List taken from 4.0
list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]

print("The third item in the list", list_of_numbers[3])

for number in list_of_numbers:
    print("My favorite number is", + number)

print("Total:", sum(list_of_numbers))