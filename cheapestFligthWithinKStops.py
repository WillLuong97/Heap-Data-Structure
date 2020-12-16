#Problem 787. Cheapest Flights Within K Stops

'''
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 

Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
'''
from collections import  defaultdict
import heapq
def findCheapestPrice(n, flights, src, dst, K):
    #base case: 
    if not n or not flights:
        return None
    graph = defaultdict(list)
    queue = []
    #create a dictionary that store the node/neighbor relationship of the current graph
    for u,v,cost in flights:
        graph[u].append((v, cost))
    
    #create a pripority queue: 
    heapq.heapify(queue)
    heapq.heappush(queue, (0, src, K+1))
    #begin the BFS: 
    while queue:
        cost, curr_node, allowed_edge = heapq.heappop(queue)
        #if the current node is the destination, then return the cost to get here
        if curr_node == dst:
            return cost

        #if not, explore other neighbors
        for neighbor, c in graph[curr_node]:
            if allowed_edge > 0: #we still have edges to travel through
                heapq.heappush(queue, (cost + c, neighbor, allowed_edge-1))

    return -1

#time complexity: O(V+E) => O(N), where n is the length of the array
#space complexity: O(n), extra space to store the queue and its element 
        
    
#main function to run the test cases
def main():
    print("TESTING CHEAPEST FLIGHT WITHIN K STOPS...")
    #test cases 1:
    n = 3
    edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    #test cases 2: 
    n_01 = 3
    edges_01 = [[0,1,100],[1,2,100],[0,2,500]]
    src_01 = 0
    dst_01 = 2
    k_01 = 0
    print(findCheapestPrice(n, edges, src, dst, k))
    print(findCheapestPrice(n_01, edges_01, src_01, dst_01, k_01))
    print("END OF TESTING...")
main()