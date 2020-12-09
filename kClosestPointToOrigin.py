#Leetcode 973. K Closest Points to Origin

'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
'''
import heapq
import math
def kClosest(points, K):
    #base case:
    if not points: 
        return None

    #declare some important variable 
    result = []
    heap = []
    #loop through the list of points and calcualte the euclidean distance
    for i in points:
        #i: (x,y)
        #extract the x and y coordinate from i
        x = i[0]
        y = i[1]
        distance = math.sqrt((x-0)**2 + (y-0)**2)
    
        heapq.heappush(heap, (distance, i))
    

    while K:
        #extract the smallest element out of the heap
        small = heapq.heappop(heap)
        result.append(small[1])
        K-=1

    return result




#Main function to run the program: 
def main():
    print("TESTING K CLOSEST POINT TO ORIGIN...")
    points_01 = [[1,3],[-2,2]]
    K_01 = 1
    points_02 = [[3,3],[5,-1],[-2,4]]
    K_02 = 2
    print(kClosest(points_01, K_01))
    print(kClosest(points_02, K_02))
    print("END OF TESTING...")
main()