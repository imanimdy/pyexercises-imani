"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: list of 8 monthly budgets 
# 2. Process: the program creates four reordered versions of the list, each one on a copy, then displays the original at the end to prove it did not change
# 3. Out: Out: the list in four orders (increasing, decreasing, reversed, and sorted by the last digit, then the original list
# 4. My four orders, and which ones modify the original: orted() and slicing return a new list. .sort() and .reverse() modify the list in place, so they must only be used on a copy.


# Your code below

# Your code below
budgets = [1200, 800, 1500, 950, 2000, 700, 1800, 1100]

# Order 1: increasing (new list)
print("Increasing:", sorted(budgets))

# Order 2: decreasing (new list)
print("Decreasing:", sorted(budgets, reverse=True))

# Order 3: reversed with slicing (new list)
print("Reversed (last month first):", budgets[::-1])

# Order 4: alphabetical order of the numbers as text (new list)
print("As text (alphabetical):", sorted(budgets, key=str))

# Demonstration of in place methods, used on a copy only
copy = budgets.copy()
copy.sort()
print("Copy after .sort() (in place):", copy)

# Proof that the original is intact
print("Original list:", budgets)

#The use of GPT was needed