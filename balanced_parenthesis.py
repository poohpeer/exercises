# -*- coding: utf-8 -*-

def is_balanced(string):
    counter = 0

    for char in string:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1

        if counter < 0:
            return False

    return counter == 0

user_input = raw_input("Please enter string with parenthesis: ")

if "(" not in user_input:
    print "No parenthesis in string."
    exit(1)

if is_balanced(user_input):
    print "The parenthesis are balanced."
    exit(1)
print "The parenthesis are not balanced."
exit (0)