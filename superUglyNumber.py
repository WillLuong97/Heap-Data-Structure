# Python3 program to solve the Leetcode 313: super ugly number using a heap
#Problem statement: 
'''
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
'''
import heapq
#Heap approach
def nthSuperUglyNumber(n, primes):
    #base case: 
    if not primes: 
        return None
    if n == 1: 
        return 1
    
    #important variable to construct and store the super ugly number array
    result = []
    minHeap = [1]
    seen = set()
    #loop until there is no other element in the minheap
    while minHeap: 
        uglyNumberTest = heapq.heappop(minHeap)
         
        result.append(uglyNumberTest)
        if len(result) == n: 
            return result[-1]   #the last element in the result array would be the nth ugly number that we are looking for

        #loop through the prime list and multiply our uglyNumber with the prime number to make other ugly number in the array
        for node in primes:
            if uglyNumberTest * node not in seen:
                seen.add(uglyNumberTest*node)
                heapq.heappush(minHeap, uglyNumberTest * node)

    return result[-1]



#driver code: 
def main():
    print("TESTING SUPER UGLY NUMBER...")
    test_val_1 = 12
    test_prime_list = [2,7,13,19]
    print(nthSuperUglyNumber(test_val_1, test_prime_list))
    print("END OF TESTING...")
main()