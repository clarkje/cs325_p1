# Author: Andrew Kittrell
# Code adapted from Penn State Lecture:
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=6&cad=rja&uact=8
# &ved=0ahUKEwi-sPSftOzPA
# hVN3WMKHWWACkMQFgg-MAU&url=https%3A%2F%2Fwww.cis.upenn.edu%2F~matuszek%2Fcit594-2014%
# 2FLectures%2F30-dynamic-programming.ppt
# &usg=AFQjCNHuEQkc1UQjy_Y8lyy3KQ20l8FnAw&sig2=nhr5PkP8P4lxKq96jkZFFA

from __future__ import print_function
import sys

def totalcoins(arr1, arr2):
    total = 0
    for i in range(len(arr1)):
        total = total + arr1[i] + arr2[i]
    return total


def combineArrays(arr1, arr2):
    tempArr = [0] * len(arr1)
    for i in range(len(arr1)):
        tempArr[i] = arr1[i] + arr2[i]
    return tempArr


def changeslow(denom, changeAmount):
    solution = [0] * len(denom)
    for i in range(len(denom)):
        if changeAmount == denom[i]:
            solution[i] = 1
            return solution

    leastNumCoins = float("inf")
    for x in range(1, changeAmount):
        sol1 = changeslow(denom, x)
        sol2 = changeslow(denom, changeAmount-x)
        count = totalcoins(sol1, sol2)
        if count < leastNumCoins:
            leastNumCoins = count
            solution = combineArrays(sol1, sol2)

    return solution

# Main
# Code by Jeromie Lee
# Slightly edited by Andrew Kittrell

def main():
    filename = sys.argv[1]
    inFile = filename + ".txt"
    outFile = filename + "change.txt"

    outFile = open(outFile,'w')
    print("Algorithm: Divide and Conquer", file=outFile)

    with open(inFile, 'r') as inFile:

        for line in inFile:
            if (line.count("[") > 0):

                line = line.strip()
                line = line.strip('[]')
                ints = line.split(',')
                coinArray = [int(i) for i in ints]

            else:
                change = int(line)
                minCoinArray = changeslow(coinArray, change)
                print(minCoinArray, file=outFile)
                totalCoins = 0
                for i in minCoinArray:
                    totalCoins += i
                print(totalCoins, file=outFile)


if __name__ == "__main__":
    main()
