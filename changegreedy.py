# Author: Caleigh Runge-Hottman 
#    (with main from Jeromie Clark and Andrew Kittrell)
# CS 325 - 400 Fall 2016
# Project 2

from __future__ import print_function
import math
import sys

def changegreedy(V, A):
    denoms = V[::-1]  # reversed list of denominations
    changeToMake = A  # remaining change to make
    C = [0] * len(V)  # coin change list
    m = 0             # total number of coins used

    for i in range (0, len(denoms)):
        while (changeToMake >= denoms[i]):
            changeToMake -= denoms[i]
            C[i] += 1
            m += 1

    # reverse the order of coins per requirements 
    C.reverse() 
    return (C, m)


# Main
# Code by Jeromie Clark
# Slightly edited by Andrew Kittrell and Caleigh Runge-Hottman

def main():
    filename = sys.argv[1]
    inFile = filename + ".txt"
    outFile = filename + "change.txt"

    outFile = open(outFile,'w')
    print("Algorithm: Greedy", file=outFile)

    with open(inFile, 'r') as inFile:

        for line in inFile:
            if (line.count("[") > 0):

                line = line.strip()
                line = line.strip('[]')
                ints = line.split(',')
                coinArray = [int(i) for i in ints]

            else:
                change = int(line)
                minCoinArray = changegreedy(coinArray, change)
                print(minCoinArray, file=outFile)
                totalCoins = 0
                for i in minCoinArray:
                    totalCoins += i
                print(totalCoins, file=outFile) 

if __name__ == "__main__":
    main()
