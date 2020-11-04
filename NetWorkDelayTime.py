#Problem 743. Network Delay Time
'''
Problem statement: 
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:



Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
'''
from collections import defaultdict
import heapq
#Approach: Heap implemenation
def networkDelayTime(times, N, K):
    #base case: 
    if not times or not N or not K:   #no set of nodes, so we cannot return anything 
        return -1

    #creating a graph from the list of nodes: 
    graph = defaultdict(list)
    for u, v, w in times: 
        graph[u].append((v,w))

    #heap to store all the current node to check if a network needed to be broacasted
    nodeQ = [(0, K)]    #this heap would store the distance needed to reach the node and the node itself
    #dictionary to store the distance of each node that has been broadcasted
    dist = {}
    while nodeQ: 
        distance, node = heapq.heappop(nodeQ)
        #if the node already broadcasted the signal, then we do not need to check it
        if node in dist: continue
        dist[node] = distance
        #loop through the neighbors of the current node and broadcast the signal
        for neigh, d in graph[node]: 
            if neigh not in dist:
                heapq.heappush(nodeQ, (d+distance, neigh))

    return max(dist.values()) if len(dist) == N else -1



        


    


#Main function to test the program
def main():
    print("TESTING NETWORK DELAY TIME...")
    test_times = [[2,1,1],[2,3,1],[3,4,1]]
    test_N = 4
    test_K = 2
    print(networkDelayTime(test_times, test_N, test_K))
    print("END OF TESTING....")
main()