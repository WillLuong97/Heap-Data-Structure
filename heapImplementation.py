#This python file will implement and solve problem using the Heap data structure in computer science.

#Ugly Number 2: 

#Problem statement: 
'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

'''

#Algorithm to solve: 
'''
The idea is to build the array of ugly number until it reaches n and then return the value at that nth value
'''
def nthUglyNumber(n):
    #base case: 
    if not n: 
        return 0

    #create an ugly number array that will start out with 1
    uglyNumberArray = [1]
    #pointer that we would used to calculate the ugly number
    x = y = z = 0


    #build the ugly number array until n
    while len(uglyNumberArray) < n: 
        uglyNumber = min(uglyNumberArray[x]*2, uglyNumberArray[y] *3, uglyNumberArray[z]*5)

        uglyNumberArray.append(uglyNumber)

        #if the ugly number we are looking at is the prime factor of 2, then we we will increment x
        if uglyNumber == uglyNumberArray[x]*2:
            x += 1

        #if the ugly number we are looking at is the prime factor of 3, then increment y
        if uglyNumber == uglyNumberArray[y]*3:
            y += 1

        #if the ugly number we are looking at is the prime factor of 5, then increment z
        if uglyNumber == uglyNumberArray[z]*5:
            z += 1

    return uglyNumberArray[-1]



#Main function to run the program
def runUglyNumberII():
    print("TESTING UGULY NUMBER...")
    test_value = 12
    print(nthUglyNumber(test_value))
    print("END OF TESTING...")
runUglyNumberII()