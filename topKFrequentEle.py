#Python3 program to solve the leetcode challenge of Top K Frequent Element using a Heap datastructure

#Problem statement: 
'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

'''
from collections import Counter
import heapq

def topKFrequent(nums, k):
    #base case: 
    if not nums or not k: 
        return None

    if k == len(nums):
        return nums
    #set up a hashmap using Counter to count how many times an element is repeated in the array
    #Structure: keys (the value itself): value (how many times the value is repeated)
    wordCounter = Counter(nums)

    #create a heap structure from the dictionary with the size of k
    #then we will populate the output array with the number that has the largest amount of time repeated
    #the amout of time repeated will then decrease until k is reached
    
    return heapq.nlargest(k, wordCounter.keys(), key=wordCounter.get)

    

#main function to test and run the program
def main():
    print("TEST FINDING MOST FREQUENT ELEMENT...")
    test_string = [1,1,1,2,2,3]
    test_k = 2

    test_nums = [1]
    test_val = 1

    print(topKFrequent(test_string, test_k))
    print(topKFrequent(test_nums, test_val))

    print("END OF TESTING...")

main()