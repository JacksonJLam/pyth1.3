#chal5.py
#Jackson Lambert 12-12-18
#automatically decides what coins are due when change is given

def main() :
    print("This script will determine what coins are due when change is inputted")
    change = eval(input("Enter an amount 0-99: "))
    quarter = change // 25
    change = change % 25
    dime = change // 10
    change = change % 10
    nickel = change // 5
    change = change % 5
    penny = change // 1
    change = change % 1
    print("The Change you will receive is")
    print(quarter, "quarters")
    print(dime, "dimes")
    print(nickel, "nickels")
    print(penny, "pennies")
main()
        

        
