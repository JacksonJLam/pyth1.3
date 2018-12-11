#chal1.py
#Jacksom Lambert 12-11-18
#Finds the value of x raised to the y power

import math

def main() :
    print("This script will find the the value of x raised to the y power")
    print(" ")
    x = eval(input("Enter the X value: "))
    print(" ")
    y = eval(input("Enter the Y value: "))
    ans = math.pow(x,y)
    print(" ")
    print("The answer is ", ans)
    input("Hit enter to exit")

main()
