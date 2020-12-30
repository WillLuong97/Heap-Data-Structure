#Problem 1705. Maximum Number of Eaten Apples

'''
There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.

You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.

Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.
Example 1:

Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
Output: 7
Explanation: You can eat 7 apples:
- On the first day, you eat an apple that grew on the first day.
- On the second day, you eat an apple that grew on the second day.
- On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
- On the fourth to the seventh days, you eat apples that grew on the fourth day.
Example 2:

Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
Output: 5
Explanation: You can eat 5 apples:
- On the first to the third day you eat apples that grew on the first day.
- Do nothing on the fouth and fifth days.
- On the sixth and seventh days you eat apples that grew on the sixth day.
 

Constraints:

apples.length == n
days.length == n
1 <= n <= 2 * 104
0 <= apples[i], days[i] <= 2 * 104
days[i] = 0 if and only if apples[i] = 0.
'''
#Function to solve the program using heap data structure. 
#Eat the apple that is going to rot first, we do this by storing the number of apple grown in each day and its rot day onto a heap and then we pop out the one with
#the smallest or completely run out of time rot day
import heapq
def eatenApples(apples, days):
    #base case: 
    if not len(apples) or not len(days):
        return None

    day = 0
    heap = []
    result = 0

    while heap or day < len(apples):
        #put all value of apple and its rot day onto the heap
        #if the apple is still within the list boundary and still have valid apple
        if day < len(apples) and apples[day] > 0: 
            heapq.heappush(heap, [days[day] + day, apples[day]])

        #Throwing out the rotten apples: (we have passed the rotten day or we dont have anymore apple to eat)
        while heap and (heap[0][0] <= day or heap[0][1] <= 0):
            heapq.heappop(heap)
        #otherwise: we keep eating the apple until they are rotten or run out
        if heap: 
            heap[0][1] -= 1
            result += 1

        day += 1
    return result
#Time complexity: O(n), since len(apples) == len(days) so the algorithm only needs to push onto the heap and pop from them
#Space complexity: O(n) we built a heap that can store n amount apple+rot day into the heap
#Main function to run the test cases: 
def main():
    print("TESTING MAXIMUM OF APPLE EATEN")
    apples = [1,2,3,5,2]
    days = [3,2,1,4,2]
    apples_1 = [3,0,0,0,0,2]
    days_1 = [3,0,0,0,0,2] 
    print(eatenApples(apples, days))
    print(eatenApples(apples_1, days_1))

    print("END OF TESTING...")

main()