# CS325_400_F2016
# Jeromie Clark
# Project 2
# Adapted from HW4 group code

# changedp
# Implements a dynamic programming algorithm that returns the minimum number
# of coins required to make an arbitrary amount of change

from __future__ import print_function
import math
import sys

def changedp(coinArray, amount):

    # Base Case
    if (amount == 0):
        return 0

    # Create an array, which stores the minimum number of coins for
    # each possible value from 1 ... amount

    # Technically, the first element should be 0, but since we evaluate the base case
    # first, we'll never consider it anyway...
    minCoinArray = [float("inf")] * (amount + 1)
    usedCoinArray = [0] * len(coinArray)

    # Compute the minimum coins required for all values from 1 to amount
    for value in range(amount + 1):

        # Populate special cases to get things started
        if (value == 0):
            minCoinArray[0] = 0;
        elif (value == 1):
            minCoinArray[1] = 1;
        else:
            # Consider all coins smaller than value
            for coin in coinArray:
                # If the coin is less than or equal to the value of the element we're considering
                if (coin <= value):
                    # Check the already-computed minCoin value at this element,
                    # less the value of the coin we're considering
                    minCoins = minCoinArray[value - coin] + 1;
                    # If that result is not our sentinel value (float(inf)) and
                    # the number of coins is less than the number of smaller coins
                    # used to compute the value, then we'll take it
                    if (minCoins != float("inf") and minCoins < minCoinArray[value]):
                        minCoinArray[value] = minCoins

    # Once we've computed the minimum coins required, we can just get the
    # value from the last element
    return minCoinArray

# Main

def main():
    filename = sys.argv[1]
    inFile = filename + ".txt"
    outFile = filename + "change.txt"

    outFile = open(outFile,'w')
    print("Algorithm: Dynamic Programming", file=outFile)

    with open(inFile, 'r') as inFile:

        for line in inFile:
            if (line.count("[") > 0):

                line = line.strip()
                line = line.strip('[]')
                ints = line.split(',')
                coinArray = [int(i) for i in ints]

            else:
                change = int(line)
                minCoinArray = changedp(coinArray, change)
                print(minCoinArray, file=outFile)
                print(minCoinArray[change], file=outFile)


if __name__ == "__main__":
    main()
