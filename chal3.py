#chal3.py
#Jackson Lambert 12-11-18
#Tells the cost of x bikes and y helmets
def main():
    print("This script will find how much a bike shop will make when x amount of bikes are sold")
    print(" ")
    x = eval(input("Enter the amount of bikes sold in a month: "))
    bike = x * 250
    for i in range(0,x + 1,5) :
        helm = i/5 * 50
    total = bike + helm
    bike = str(bike)
    helm = str(helm)
    print(" ")
    print("The shop will profit", total)
    print("$" + bike, "comes from bikes and $" + helm, "comes from helmets")
    print(" ")
    input("Hit enter to exit" )
main()
