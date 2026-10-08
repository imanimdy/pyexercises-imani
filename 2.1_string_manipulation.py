"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a sentence by user
# 2. Process: Program applies four different string transformations of a sentence
# 3. Out: four different transformations of sentence displayed
# 4. My four transformations, and when each is useful: 
# upper() - useful for all letter need to be capitalized
#lower() -  useful for when all leters need to be lowercase
#title() - useful for sentences/phrases that are for title where each first letter need to be capital
#replace() - useful when changing one character of text into another


# Your code below

sentence = input("enter a sentence:")
#The input is going to ask me to enter a sentence

result1 = sentence.upper()
print("uppercase:", result1)
#Test try first

result2 = sentence.lower()
result3 = sentence.title()
result4 = sentence.replace("","_")
#The rest of the text transformations

print("uppercase:", result1)
print("lowercase:", result2)
print("title case:", result3)
print("spaces replaced:", result4)
#Every transformation to be printed

#Everything came out as expected 