#Problem 1673. Find the Most Competitive Subsequence

'''
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

 

Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
Example 2:

Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= nums.length
'''
#We only need to construct one subsequent that is the most competitive. We do this by storing each element from the array into a stack and pop them out if the next element 
#from the array is lesser than the one we are currently at. In the end, when we are done processing, all remaining element in the stack would be the result element
#Time complexity: O(n), n is the number of all element in the nums array
#Space complexity: O(k), we just need to store the stack with the size of K
def mostCompetitive(nums, k):
	#base case
	if not nums or not k:
		return []
	#the stack that we use to keep track of which element to keep for the subsequent
	stack = []
	for index, num in enumerate(nums):
		#append element to the stack if we are decreasing the search size by k but still have element to loook for
		remainding = len(nums) - index
		
		#condition to pop from the stack:
		while stack and num < stack[-1] and (len(stack) + remainding) > k:
			stack.pop()
		
		#we only append more element if the subsequent has not been maxed out
		if len(stack) < k:
			stack.append(num)

	return stack 



#Main function to run the test cases:
def main():
	print("TESTING FIND THE MOST COMPETITIVE SUBSEQUENCE")
	nums_1 = [3,5,2,6]
	k_1 = 2
	nums_2 = [2,4,3,3,5,4,9,6]
	k_2 = 4
	
	print(mostCompetitive(nums_1, k_1))	
	print(mostCompetitive(nums_2, k_2))	

	print("END OF TESTING...")

main()
