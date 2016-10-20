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
