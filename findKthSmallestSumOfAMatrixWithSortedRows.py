#Problem 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows

'''
You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.

 

Example 1:
Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  

Example 2:
Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17

Example 3:
Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
Example 4:

Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12
 

Constraints:

m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= k <= min(200, n ^ m)
1 <= mat[i][j] <= 5000
mat[i] is a non decreasing array.

'''
import heapq
#Divide and Conuquer method, we divide the martix into halves and add them into a serperate array to add each element together
def kthSmallest(mat, k):
	#Base case: 
	if not mat: 
		return 0 
	result = helper(mat, k)
	return result[k-1]

#helper method to partition the matrix
def helper(mat, k):
	#base case:
	if len(mat) == 1:
		return mat[0]

	#divide the matrix: 
	mid = len(mat) // 2
	#parts: 
	left = helper(mat[:mid], k)
	right = helper(mat[mid:], k)

	#adding the part's element together:
	return merge(left, right, k)


#function to add the element in the parts togehter: 
def merge(left, right, k):
	#the result array will store all smallest sum
	result = []
	if not left or not right or not k:
		return result
	#the heap will store the sum of each element in all row
	heap = []
	#adding each element from each rows together
	for i in left: 
		for j in right: 
			heapq.heappush(heap, i+j)

	while heap and k>0:
		result += [heapq.heappop(heap)]
		k-=1

	return result




#Main function to run the test cases: 
def main():
	print("TESTING FIND KTH SMALLEST SUM OF A MATRIX WITH SORTED ROWS...")
	mat_1 = [[1,3,11],[2,4,6]]
	k_1 = 5
	mat_2 = [[1,10,10],[1,4,5],[2,3,6]]
	k_2 = 7
	mat_3 =[[1,3,11],[2,4,6]]   
	k_3 = 9

	print(kthSmallest(mat_1, k_1))
	print(kthSmallest(mat_2, k_2))
	print(kthSmallest(mat_3, k_3))

	print("END OF TESTING...")
main()
