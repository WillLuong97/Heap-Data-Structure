#problem 1005.  Maximize Sum Of Array After K Negations

#Problem statement: 
'''
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.
Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].

Note:

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100
'''
#Function to solve the problem with Greedy approach: 
#At each iteration of K, we will try to negate the smallest current element in the array and the element can be repeated 
def largestSumAfterKNegations(A, K):
    #base case: 
    if not A or not K:
        return None
    currentMin = 0
    while K:
        #take out the smallest number and negate it
        currentMin_Index = A.index(min(A))
        #then update it back in the array
        for i in range(len(A)):
            if i == currentMin_Index:
                A[i] *= -1
        #One negation time has been updated in the array
        K-=1

    return sum(A)
#Time complexity: O(n), where n is the total number of all element in the array
#Space complexity: O(1)
def main():
    print("TESTING MAXIMMIZE SUM OF ARRAY AFTER K NEGATIONS...")
    A_1 = [4,2,3]
    K_1 = 1
    A_2 = [3,-1,0,2]
    K_2 = 3
    A_3 = [2,-3,-1,5,-4]
    K_3 = 2
    print(largestSumAfterKNegations(A_1, K_1))
    print(largestSumAfterKNegations(A_2, K_2))
    print(largestSumAfterKNegations(A_3, K_3))
    print("END OF TESTING...")

main()