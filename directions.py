# Hey Guys, I hope you all are ready for some fun assignment and I assume you have not forgotten what we have practised :D
#
# So here is the question for you all:
#
#
# A mars rover traverses in a plane from its origin point(0,0).
# The rover can only walk in 4 absolute directions -
# North(Traverses up), South(Traverses down), East (Traverses right), West(Traverses left).
# The footprints of the rover is shown as following:
#
# North 5
# South 3
# West 3
# East 2
#
# The numbers after compass directions are walked steps.
# Write a program to compute the displacement from current position after a sequence of walked path's movement and original point.
# If the distance evaluated is in float, then just print the nearest integer.
#
#
# -Sample Test case-
# If the following are steps the rover walked given as input to the program:
# North 5
# South 3
# West 3
# East 2
# Then, the output of the evaluation should be:
# 2

# TODO: Create a program with above instructions

# print("Enter in following manner N x , S x , W x , E x  Where x is distance and N,S,W,E representws the direction\n")

from math import sqrt

direct_m = {'N': 0, 'S': 0, 'W': 0, 'E': 0}

n = int(input("Enter No of directions "))
for i in range(n):
    ch = input("Enter which direction you are going with distance : \t").upper().strip()

    if ch == "N" or ch == "NORTH":
        dist = direct_m['N'] + int(input("Enter distance traveled in NORTH direction : \t "))
        direct_m.update({'N': dist})
    elif ch == "S" or ch == "SOUTH":
        dist = direct_m['S'] + int(input("Enter distance traveled in SOUTH direction : \t "))
        direct_m.update({'S': dist})
    elif ch == "W" or ch == "WEST":
        dist = direct_m['W'] + int(input("Enter distance traveled in WEST direction : \t "))
        direct_m.update({'W': dist})
    elif ch == "E" or ch == "EAST":
        dist = direct_m['E'] + int(input("Enter distance traveled in EAST direction : \t "))
        direct_m.update({'E': dist})

print(direct_m)

x = direct_m['E'] - direct_m['W']
y = direct_m['N'] - direct_m['S']

print("X : " + str(x) + " \t Y : " + str(y))

dist_from_origin = int(sqrt((x * x) + (y * y)))
print("The distance from origin is  :  " + str(dist_from_origin))
