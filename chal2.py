#chal2.py
#Jackson Lambert 12-11-18
#Tells how long it takes to serve x amount of customers

def main():
    print("This script will find how long it takes to serve x amount of customers")
    print("It takes 4 minutes to serve each customers")
    print(" ")
    x = eval(input("Enter the number of customers in the line: "))
    time = 4 * x
    print(" ")
    print("It takes " ,time, "minutes to serve", x, "customers")
    print(" ")
    input("Hit enter to exit" )
main()
