# CS325_400_F2016
# Jeromie Clark
# Project 2
# Adapted from HW4 group code 

# minCoins
# Implements a dynamic programming algorithm that returns the minimum number
# of coins required to make an arbitrary amount of change

def minCoins(coinArray, amount):

 # Base Case
 if (amount == 0):
     return 0

 # The worst-case scenario is that we return all pennies
 # Build an array big enough to hold pennies for the whole amount
 candidateArr = [0] * (amount + 1)

 # Check the last possible position in the array
 # If it's non-zero, we're done
 # I think this is equivalent to amount == 0
 #if candidateArr[amount] != 0:
 #    return finalArr[amount]

 # build the amount out with pennies
 # then consolidate pennies to nickels to dimes to quarters until we can't
 # consolidate anymore
 for eachCent in range(amount+1):

    currentMinCoins = eachCent

    # Evaluate each of the available coins that's smaller or equal to the amount
    for currentCoin in [coin for coin in coinArray if coin <= eachCent]:

        if candidateArr[eachCent - currentCoin] + 1 < currentMinCoins:
            currentMinCoins = 1 + candidateArr[eachCent - currentCoin]

        candidateArr[eachCent] = currentMinCoins

 return candidateArr[amount]

# Main

def main():
 coinArray = [1, 5, 10, 25]
 # changeToCheck = [0, 1, 5, 7, 12, 15, 23, 44, 68, 75, 99, 3, 10, 15, 16]
 changeToCheck = [10]


 # Initialize an array to store our candidate values
 #candidateArr = [0] * (max(changeToCheck)+1)

 for change in changeToCheck:
#     print("Change needed: %s Min Coins: %s" % (change, minCoins(candidateArr, coinArray, change)))
     print("Change needed: %s Min Coins: %s" % (change, minCoins(coinArray, change)))


if __name__ == "__main__":
    main()
