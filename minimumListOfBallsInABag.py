#Problem 1760. Minimum Limit of Balls in a Bag

'''
You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.
`:wq:Example 1:

Input: nums = [9], maxOperations = 2
Output: 3
Explanation: 
- Div:ide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.
Example 2:

Input: nums = [2,4,8,2], maxOperations = 4
Output: 2
Explanation:
- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
The bag with the most number of balls has 2 balls, so your penalty is 2 an you should return 2.
Example 3:

Input: nums = [7,17], maxOperations = 2
Output: 7
 

Constraints:

1 <= nums.length <= 105
1 <= maxOperations, nums[i] <= 109


Appraoch: 
Given a threshold t (max number of balls per final bag), we need at least ceil(n / t) of bags to split n balls. The required operations is then ceil(n / t) - 1. For example a bag of n = 10 balls and threshold t = 4, we need to split them into (4, 4, 2) 3 bags, which requires 2 split operations.
Binary search on the threshold which takes O(logM) time, where M is the maximum number of balls in each bags. Checking if a certain threshold is feasible take O(N) for N bags. Together, the time complexity is O(N log M).
'''
#Binary Search approach: 
from math import ceil
def minimumSize(nums, maxOperations):
	#helper method to check if we could divide the ball in each  bag into the threshold number, while
	#sastifying the number of operations allows
	def checkThreshold(threshold):
		#keep track of how many operations it would take to divde into the threshold
		count = 0
		if threshold <= 0:
			return False
		#loop through each bags and check for the number of operations that it would take eacb bags to divide the balls into
		for bag in nums:
			if bag > threshold:
				#check how long it would take to divide into the theshold
				count += int(ceil(bag / threshold)) - 1
				if count > maxOperations:
					return False
		return True

	#appy binary search to find the threshold
	nums = sorted(nums, reverse=True)
	right = nums[0] #biggest threshold in the current search space 
	left = 0	#smallest threshold in the current search space
	while right - left > 1:
		mid = (right + left) // 2
		if checkThreshold(mid):
			right = mid
		else: 
			left = mid
	
	return right


#Main function to run the test cases: 
def main():
	print("TESTING MINIMUM LIMITS OF BALLS IN BAGS...")
	nums = [9]
	maxOperations = 2
	print(minimumSize(nums, maxOperations))
	nums = [2, 4, 8 ,2]
	maxOperations = 4
	print(minimumSize(nums, maxOperations))

	nums = [7, 17]
	maxOperations = 2
	print(minimumSize(nums, maxOperations))

	print("END OF TESTING...")

main()
