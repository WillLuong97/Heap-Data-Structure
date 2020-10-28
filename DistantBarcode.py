#Leetcode 1054. Distant Barcodes

#Problem statement: 
'''
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]
 

Note:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
'''
from collections import Counter
import heapq
#Function to solve the problem: 
def rearrangeBarcodes(barcodes):
    #base case: 
    if not barcodes:
        return []

    #result string that would store the element in the array
    result = []
    #create a counter of the barcodes
    counter = Counter(barcodes)
    heap = []
    prev = None

    #loop through the barcodes and negate the element in the coutenr
    for ele, counter  in counter.most_common():
        heapq.heappush(heap, (-counter, ele))

    #pop the least frequent number out of the heap
    while heap:
        count, num = heapq.heappop(heap)
        result.append(num)
        count += 1  #decrement the value of the count as one of the element has been placed in the heap
        #after each iteration, we will push it back into the heap if it still has frequency
        if prev:
            heapq.heappush(heap, prev)
        prev = (count, num) if count < 0 else None
    return result

#Time complexity: O(n), the algorithm wll have to go through every element in the array to count its frequency and begin the swapping.
#Space complexity: O(n), the result array will be created to store n amount of element from the original barcode string
#main function to run the program 
def main():
    print("TESTING DISTANT BARCODE...")
    test_input_0 = [1,1,1,2,2,2]
    test_input_1 = [1,1,1,1,2,2,3,3]

    print(rearrangeBarcodes(test_input_0))
    print(rearrangeBarcodes(test_input_1))
    print("END OF TESTING...")
main()