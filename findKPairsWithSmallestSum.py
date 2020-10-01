#Python3 program to implement leetcode #373. Find K Pairs with Smallest Sums

#Problem statement
'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

Follow-up question:
1: What if K pairs of smallest mulitplications ?
2: Whaf if there are 3 arrays of nums ?
3: What if there are K arrays of nums ?


'''

import heapq
#brute force approach: Time complexity would be O(n*m), taking too much time achieve the task.
def kSmallestPairs(nums1, nums2, k):
    #base case: 
    if not nums1 or not nums2: 
        return []
    res = []


    #loop through the two nums to collect all possible element between them
    for i in nums1: 
        for j in nums2: 
            res.append([i,j])

    return sorted(res, key=lambda x:x[0]+x[1]) [:k]

    

#optimize approach: Min heap: Time complexity: O(k logk)
def kSmallestPairs_OPTIMIZED(nums1, nums2, k):
    #base case: 
    if not nums1 or not nums2 or not k:
        return []

    result = []
    heap = []        
    m = len(nums1)
    n = len(nums2)
    #Since the two array are sorted, the sum of the first two element in each array, would be smallest
    #so its sum would also be smallest.
    heapq.heappush(heap, [nums1[0] + nums2[0], 0, 0])
    while heap and len(result) < k: 
        #get the smallest elemetn out of the heap
        sumn, ind1, ind2 = heapq.heappop(heap)
        result.append([nums1[ind1], nums2[ind2]])
        #iterate to the next value in each of the array
        if ind2 + 1 < n: 
            heapq.heappush(heap, [nums1[ind1] + nums2[ind2 + 1], ind1, ind2 + 1])

        if ind2 == 0: 
            if ind1 + 1 < m: 
                heapq.heappush(heap, [nums1[ind1 + 1] + nums2[ind2], ind1 + 1, ind2])

    return result

#driver code:
def main(): 
    print("TESTING FIND K PAIRS WITH SMALLEST SUM...")
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3

    nums3 = [1,1,2]
    nums4 = [1,2,3]
    k1 = 2

    nums5 = [1,2]
    nums6 = [3]
    k2 = 3

    # print(kSmallestPairs(nums1, nums2, k))
    # print(kSmallestPairs(nums3, nums4, k1))
    # print(kSmallestPairs(nums5, nums6, k2))
    print(kSmallestPairs_OPTIMIZED(nums1, nums2, k))
    print(kSmallestPairs_OPTIMIZED(nums3, nums4, k1))
    print(kSmallestPairs_OPTIMIZED(nums5, nums6, k2))


    print("END OF TESTING...")
main()