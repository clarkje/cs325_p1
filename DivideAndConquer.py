# Author: Andrew Kittrell
# CS325 Project 1
# Psuedocode gathered from pg 71-72 of CLRS's "Introduction to Algorithms" 3rd Edition

# Returns the maximum sub array that crosses the midpoint of the array
# array - The list of values that the subarray will be found in
# start - beginning index of the array
# mid - middle index of the array
# end - the last index in the array
def maxCrossingSubarray(array, start, mid, end):
    leftSum = -float('inf')
    sum = 0
    maxLeftIdx = mid
    for i in reversed(xrange(start, mid+1, 1)):
        sum = sum + array[i]
        if sum > leftSum:
            leftSum = sum
            maxLeftIdx = i

    rightSum = -float('inf')
    sum = 0
    maxRightIdx = mid+1
    for i in xrange(mid+1, end+1, 1):
        sum = sum + array[i]
        if sum > rightSum:
            rightSum = sum
            maxRightIdx = i

    return(leftSum+rightSum,maxLeftIdx ,maxRightIdx)

#Returns the maximum sub array of an array
# array - the list of values that we wish to find the maximum sub array in
# start - the first index of the array
# end - the last index of the array
def maxSubArray(array, start, end):
    if start == end:        #only one value in the array
        return [array[0], start, end]
    else:
        mid = (start + end)/2
        leftStats = maxSubArray(array, start, mid)
        rightStats = maxSubArray(array, mid+1, end)
        middleStats = maxCrossingSubarray(array, start, mid, end)

        if leftStats[0] >= rightStats[0] and leftStats[0] >= middleStats[0]:
            return leftStats
        elif rightStats[0] >= leftStats[0] and rightStats[0] >= middleStats[0]:
            return rightStats
        else:
            return middleStats
