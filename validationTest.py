# Jeromie Clark
# CS325 - Project 1
# Maximum Sum Subarray Experimental Analysis
from __future__ import print_function
import sys
from maxSumSubarray import maxSubArray
from maxSumSubarray import iteration
from maxSumSubarray import enumeration
#from maxSumSubarray import dynamic_programming


# Result object populated and returned by algorithm
class Result:
    data = []
    result = 0

    def __init__(self):
        self.data = []
        self.result = 0

    def writeData(self, outFile):
        outString = None
        outString = ','.join(str(d) for d in self.data)
        print("[{}]".format(outString), file=outFile)

    def writeResult(self, outFile):
        print(str(self.result), file=outFile)

# Just an example algorithm implementation
# Takes a List of inputData, returns an output string
def divideAndConquerStart(inputData):
    res = Result()
    info = maxSubArray(inputData, 0, len(inputData) - 1)
    res.result = info[0]
    res.data = inputData[info[1]:info[2]+1]
    return res

def iterationStart(inputData):
    res = Result()
    info = iteration(inputData)
    res.result = info[0]
    res.data = inputData[info[1]:info[2]+1]
    return res

def enumerationStart(inputData):
    res = Result()
    info = enumeration(inputData)
    res.result = info[0]
    res.data = inputData[info[1]:info[2]+1]
    return res

# doValidationTest
# For each line in inFile, passes a list of integers to inFile

# Parameters:
# function = name of the function to test, must accept a List as input
# iterations = number of iterations to run the test (more iterations = more accuracy)
# size = size of random input data to generate for function
# inFile (optional) = input file to use (size is ignored)
# outFile (optional) = file to output results to

def doValidationTest(function, inFile, outFile):

    outFile = open(outFile, 'a+')   #allows for appending

    print(function.func_name, ": ", file=outFile) #adds the function name to the output file (which is the helper function, not the original)

    with open(inFile, 'r') as inFile:
        for line in inFile:
            line = line.strip()
            line = line.strip('[]')
            ints = line.split(',')
            inputData = [int(i) for i in ints]

            # We have to print the input data
            inputString = None
            inputString = ','.join(str(d) for d in inputData)
            print("[{}]".format(inputString), file=outFile)

            # Run the algorithm
            res = function(inputData)

            # Write the processed Data
            res.writeData(outFile)

            # Write the result
            res.writeResult(outFile)

            # Print a newline
            print("\n", file=outFile)

# Example Call
# Executes exampleAlg 10 times, using 10 digits of input data
print("Peforming Validation Test")
doValidationTest(iterationStart, "./testData/MSS_TestProblems.txt", "./outfile.txt")
doValidationTest(enumerationStart, "./testData/MSS_TestProblems.txt", "./outfile.txt")
doValidationTest(divideAndConquerStart, "./testData/MSS_TestProblems.txt", "./outfile.txt")
#doValidationTest(dynamic_programming, "./testData/MSS_TestProblems.txt", "./outfile.txt")