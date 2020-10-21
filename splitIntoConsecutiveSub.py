#Problem 659. Split Array into Consecutive Subsequences


#Problem statement:

'''
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
Example 3:

Input: [1,2,3,4,4,5]
Output: False
 

Constraints:

1 <= nums.length <= 10000
'''
from collections import defaultdict
import heapq
def isPossible_HEAP(nums):
    #base case: 
    if not nums: 
        return False
    #dictionary to store the length and the group element
    groups = defaultdict(list)

    #loop through the array to find element
    for num in nums:
        #if there are no element currently stored in the dictionary that can be its consecutively before it
        # the create a new group and add it into it 
        if num - 1 not in groups:
            heapq.heappush(groups[num], (1, [num]))
    
        else:
            #extract the group that has an element that is consecutively before it to add the current element into it 
            _, group = heapq.heappop(groups[num - 1])
            group.append(num)
            heapq.heappush(groups[num], (len(group), group))
            if not groups[num - 1]:
                del groups[num - 1]
    #return true if all groups in the heap has the size of 3 and false if there is only one
    return all(heap[0][0] >= 3 for heap in groups.values())
# Time Complexity= O(nlgk), where k denotes the number of groups that end up with the same number
# Space Complexity = O(n)

#main function to run the program
def main():
    print("TESTING SPLIT ARRAY INTO SUBSEQUENCES...")
    input_01 = [1,2,3,3,4,5]
    input_02 = [1,2,3,3,4,4,5,5]
    input_03 = [1,2,3,4,4,5]

    print(isPossible_HEAP(input_01))
    print(isPossible_HEAP(input_02))
    print(isPossible_HEAP(input_03))

    print("END OF TESTING...")
main()