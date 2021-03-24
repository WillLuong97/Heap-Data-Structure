#Problem 1792. Maximum Average Pass Ratio
'''
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.
Example 1:
Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

Example 2:
Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
Constraints:

1 <= classes.length <= 105
classes[i].length == 2
1 <= passi <= totali <= 105
1 <= extraStudents <= 105


#Approach: 
1. Brute force + Heap data structure: from the list of extra students, we will add the one of them to each claseses and calculat the difference betweem the original raitos 
with the new ratios after being updated with the new extra students. 
2. Any classes with the higher difference will be stored into the heap data struture, where we can pop them out and check with the new updaed ratios

Time complexity: O(n) 

'''
import heapq
def maxAverageRatio(classes, extraStudents):
	result = 0
	#the heap to store the differences between the current passing ratios and updated passing ratios
	difference = [0] * len(classes)
	for i in range(len(classes)):
		passCount = classes[i][0]
		totalCount = classes[i][1]
		#init the heap with some preliminary differences, just add 1 student into each class
		currentRatio = passCount / totalCount
		updatedRatio = (passCount + 1) / (totalCount + 1)
		diff = updatedRatio - currentRatio
		difference[i] = (-diff, passCount, totalCount)
	heapq.heapify(difference)
	
	#start adding the extra students into the array
	while(extraStudents > 0):
		#pop the highest element from the heap, this would give us the difference with the highest value
		_, passCount, totalCount = heapq.heappop(difference)
		#assign a student to a class
		passCount += 1
		totalCount += 1
		currentRatio = passCount / totalCount
		updatedRatio = (passCount + 1) / (totalCount + 1)
		diff = updatedRatio - currentRatio
		heapq.heappush(difference, (-diff, passCount, totalCount))
		extraStudents -= 1
	for _, passCount, totalCount in difference: 
		result += passCount / totalCount
	return result/len(classes)
		 


#Main function to run the test case: 
def main():
	print("TESTING MAXIMUM AVERAGE PASS RATIO...")
	#test cases:
	classes =[[1,2],[3,5],[2,2]]
	extraStudents = 2
	print(maxAverageRatio(classes, extraStudents))
	
	classes =[[2,4],[3,9],[4,5],[2,10]]
	extraStudents = 4
	print(maxAverageRatio(classes, extraStudents))
	
	print("END OF TESTING...")

main()
