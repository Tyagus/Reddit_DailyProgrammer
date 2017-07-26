# /r/dailyprogrammer -> Challange #293
# Description:
# To disarm the bomb you have to cut some wires.
# These wires are either white, black, purple, red, green or orange.
# The rules for disarming are simple:
# * If you cut a white cable you can't cut white or black cable.
# * If you cut a red cable you have to cut a green one
# * If you cut a black cable it is not allowed to cut a white, green or orange one
# * If you cut a orange cable you should cut a red or black one
# * If you cut a green one you have to cut a orange or white one
# * If you cut a purple cable you can't cut a purple, green, orange or white cable

# # Code: Tiago Ribeiro

# import time for performance
import time
from constraint import *

start_time = time.time()

# For this problem I will use a CSP to solve it
# Has variables we have the wires which can be 1 (cut) or 0 (uncut)
# And the constraints are the rules given
# Edit: This solution is invalid, it serves to see how to solve a CSP in Python
# in this situation it would assume the order of cutting the cables is indiferent and we
# care only about the cables that need to be cut / left.

problem = Problem()
defusing = True
# Variables
problem.addVariable("w", [0, 1])
problem.addVariable("b", [0, 1])
problem.addVariable("r", [0, 1])
problem.addVariable("o", [0, 1])
problem.addVariable("p", [0, 1])
problem.addVariable("g", [0, 1])

# Constraints
problem.addConstraint(lambda w, b: w != b, ("w","b"))
problem.addConstraint(lambda r, g: r == g, ("r","g"))
problem.addConstraint(lambda b, w, g, o: b != w or b != g or b != o, ("b","w","g","o"))
problem.addConstraint(lambda o, r, b: o == r or o == b, ("o", "r", "b"))
problem.addConstraint(lambda g, o, w : g == o or g == w, ("g", "o", "w"))
problem.addConstraint(lambda p, g, o, w: p != g or p != o or p != w, ("p", "g", "o", "w"))
solution = problem.getSolution()

# I noticed we need only to look at the rules done immediately before,
# as such I will do a game to defuse, where the player chooses each cable in order with a counter (4 cables)
i = 4
rule = []
while(i > 0):
    print("CABLES LEFT: " + str(i))
    print("Choose cable: \n| W / R / B / O / G / P |")
    choice = input("Choice: ")
    choice = str(choice).lower()
    if choice in rule:
        print("BOOOOM!!! - You failed.")
        break
    if(choice=="w"):
        rule = ["w","b"]
    elif (choice == "r"):
        rule = ["w", "r", "b", "p", "o"]
    elif(choice=="b"):
        rule = ["w","g","o"]
    elif(choice=="o"):
        rule = ["w","o","p","g"]
    elif(choice=="g"):
        rule = ["r","b","g","p"]
    elif(choice=="p"):
        rule = ["p","g","o","w"]
    else:
        print("INVALID CHOICE")
        i = i + 1
    i = i - 1
if i<=0:
    print("Success!! - You defused the bomb.")