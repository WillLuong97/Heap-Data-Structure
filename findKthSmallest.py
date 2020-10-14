#Python3 program to implement heap to find the kth smallest element in any kind of search space


#Problem statement 
'''
378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

'''
#Using heapq, we will try to find the kth smallest element using min heap
import heapq
def kthSmallest(matrix, k):
    #base case: 
    if not matrix and not k:
        return None

    #create a list to store the first row of the matrix 
    result = matrix[0]
    #conver this reuslt into a min heap using the heapify command
    heapq.heapify(result)
    #traverse the rest of the row elemnts from the matrix into the created heap
    for row in matrix[1:]:
        for element in row:
            heapq.heappush(result, element)

    #get list of first k smallest element because 
    # nsmallest(k,list) method returns first k  
    # smallest element now print last element of  
    # that list
    listOfK = heapq.nsmallest(k, result)
    return listOfK[-1]


#Problem 2: Finding kth smallest in an unsorted array
'''
Given an array and a number k where k is smaller than size of array, 
we need to find the k’th smallest element in the given array. It is given that ll array elements are distinct.

Input: arr[] = {7, 10, 4, 3, 20, 15}
k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
k = 4
Output: 10
'''

#Time complexity: O(nlogn)
def kthSmallest_1D_Array(array, k):
    #sort the array (O(nlogn)) and return the element at k index
    sortedArray = sorted(array)
    return sortedArray[k-1]


def kthSmallest_1D_Array_MIN_HEAP(array, k):
    #Base case: 
    if not array or not k: 
        return None

    #convert the array into a min heap using the heapify structure
    heapq.heapify(array)
    
    listOfKthSmallest = heapq.nsmallest(k, array)

    return listOfKthSmallest[-1]

def main():
    print("FINDING KTH SMALLEST ELEMENT IN AN 2D ARRAY...")
    mat = [[10, 25, 20, 40],
               [15, 45, 35, 30],
               [24, 29, 37, 48],
               [32, 33, 39, 50]]
    k = 7


    matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
    K = 8

    arr1 = [7, 10, 4, 3, 20, 15]
    k1 = 3

    arr2 = [7, 10, 4, 3, 20, 15]
    k2 = 4

    print(kthSmallest(mat, 7))
    print(kthSmallest(matrix, K))
    # print(kthSmallest_1D_Array(arr1, k1))
    # print(kthSmallest_1D_Array(arr2, k2))

    print(kthSmallest_1D_Array_MIN_HEAP(arr1, k1))
    print(kthSmallest_1D_Array_MIN_HEAP(arr2, k2))

    print("END OF TESTING...")



main()