import math

#*******************************************************************************
# AUTHOR:  Caleigh Runge-Hottman
#          (with pseudocode provided from Professor Glencora Borradaile, OSU)
# DATE:  10 October 2016
# DESCRIPTION:
#  Given an aray of small integers, this program computes the maximum total sum
#  of a consecutive sequence of numbers (i.e., a subarray) using 4 different
#  algorithms:  enumeration, iteration, divide & conquer, dynamic programming
#  e.g. MaxSubarray([31, -41, 59, 26, -53, 58, 97, -93, -23, 84]) = 187
#       (where the subarray is [59, 26, -53, 58, 97]).
#*******************************************************************************

#*******************************************************************************
# Maximum Sum Subarray -- Enumerative Algorithm
# ANALYSIS: O(n^3). (O(n^2) pairs * O(n) compute each sum)
# (Depends cubically on the size of the input)
#*******************************************************************************
def enumeration(A):
    maxSum = subarraySum = 0
    startIndex = subarrayStart = 0
    endIndex = subarrayEnd = 0
    n = len(A)

    # each iteration determines the beginning subarray index
    for i in range (0, n):
        startIndex = i
        # each iteration resets sum & determines the ending subarray index
        for j in range (i, n):
            subarraySum = 0
            endIndex = j
            # each iteration adjusts the sum
            for k in range(i, j+1):
                subarraySum += A[k]
            #keep the max sum found so far (& its corresponding array)
            if subarraySum > maxSum:
                maxSum = subarraySum
                subarrayStart = startIndex
                subarrayEnd = endIndex

    #return max sum found (& its corresponding array)
    return [maxSum, subarrayStart, subarrayEnd]


#********************************************************************************
# Maximum Sum Subarray -- Iterative Algorithm
# ANALYSIS: O(n^2). (O(n) i-iterations * O(n) j-iterations * O(1) update sum)
# (Depends quadratically on the size othe input)
#********************************************************************************
def iteration(A):
    maxSum = subarraySum = 0
    subarrayStart = startIndex = 0
    subarrayEnd = endIndex =  0
    n = len(A)

    # each iteration determines the beginning subarray index & resets sum
    for i in range (0, n):
        startIndex = i
        subarraySum = 0
        # each iteration determines the ending subarray index
        for j in range (i, n):
            endIndex = j
            subarraySum += A[j]
            # keep max sum found so far
            if subarraySum > maxSum:
                maxSum = subarraySum
                subarrayStart = startIndex
                subarrayEnd = endIndex
    # return max sum found so far & its corresponding array.
    return [maxSum, subarrayStart, subarrayEnd]

#*******************************************************************************
# Maximum Sum Subarray -- Divide and Conquer
# ANALYSIS: O(n log n). (O(n) per level * O(log n) depth)
#*******************************************************************************
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


#*******************************************************************************
# Maximum Sum Subarray -- Dynamic programming (a.k.a., recursion-inversion )
# Running time: O(n)
#*******************************************************************************
def dynamicMaxSumSubarray(a):
    n = len(a)
    maxSum = float("-inf")
    endingHereSum = float("-inf")

    for j in range(0,n):
        # since the high of any subarray ending @ index j must be j,
        # every iteration automatically sets ending-here-high to j.
        endingHereHigh = j

        # Check whether the maxsubarray ending at index j only contains a[j].
        # As we enter an iteration of the loop, ending_here_sum has the sum
        #  of the values in a max subarray ending at j-1.
        # If ending_here_sum + a[j] > a[j], we extend the max subarray ending
        #  at index j-1 to include index j. The test in the if statement
        #  just subtracts out a[j] from both sides.
        if (endingHereSum > 0):
            endingHereSum = endingHereSum + a[j]

        # Otherwise, if maxsubarray ending at index j contains more than just a[j],
        #  we start a new subarray at index j, so both its low and high ends have
        #  the value j (note: ending_here_high = j, above.) and its sum is a[j].
        else:
            endingHereLow = j
            endingHereSum = a[j]

        # Once we know the max subarray ending at index j, we test to see whether
        # it has a greater sum than the max subarray found so far, ending at any
        # position less than or equal to j.
        # If the sum is greater, we update low, high and max_sum appropriately.
        if (endingHereSum > maxSum):
            maxSum = endingHereSum    # sum of vals found in max subarray so far
            subarrayStart = endingHereLow        # low of the max subarray found so far
            subarrayEnd = endingHereHigh      # high of the max subarray found so far

    return (maxSum, subarrayStart, subarrayEnd)


#*******************************************************************************
# 				MAIN
#*******************************************************************************
def main():
    arr = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
  #  arr = [30, 25, 88, 44, 12, -142, -44, 9, 9, 0, -152, 434, 342, 52, 32, 4, 92, -152 ]

    iterResult = iteration(arr)
    enumResult = enumeration(arr)
    iterList = []
    enumList = []


    print '********** Iteration Results **********'
    print 'max sum: ', iterResult[0]

    print 'corresponding array: ',
    for i in range (iterResult[1], iterResult[2] + 1):
        if (i == iterResult[1]):
            print '[', arr[i], ',' ,
        elif (i == iterResult[2]):
            print arr[i], ']\n'
        else:
            print arr[i], ',' ,

    print '********** Enumeration Results **********'
    print 'max sum: ', enumResult[0]

    print 'corresponding array: ',
    for i in range (enumResult[1], enumResult[2] + 1):
        if (i == enumResult[1]):
            print '[', arr[i], ', ',
        elif (i == enumResult[2]):
            print arr[i], ']\n'
        else:
            print arr[i], ', ',

if __name__ == "__main__":
    main()
