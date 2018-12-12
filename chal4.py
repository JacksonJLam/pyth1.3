#chal4.py
#Jackson Lambert 12-12-18
#Answers the famous chessboard question
import math
def main() :
    print("This script solves the classic chessboard problem")
    print("The problem asks how much grains of wheat would be on a chessboard if each")
    print("Subsequent square had twice the amount of wheat as the last")
    print("There are 64 squares on a chessboard")
    for i in range(65) :
        x = 2 ** i
        ans = x - 1
    print(" ")
    print("The would be a total of", ans, " grains of wheat")
main()
