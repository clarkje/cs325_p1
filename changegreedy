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

def main():
#    A = 15
#    V = [1,2,4,8]
#    A = 29
    A = 31
    V = [1, 3, 7, 12]
    result = changegreedy(V, A)

    print result[0]
    print 'min number of coins: ', result[1]    

if __name__ == "__main__":
    main()
