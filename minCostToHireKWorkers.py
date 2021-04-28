#857. Minimum Cost to Hire K Workers
'''
There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.
Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
 

Note:

1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.

Observation: no matter the number of the workers, we only need to guarantee that one workers is paid with their expected minimum wage. This worker
will be the "BASED_EMPLOYEE" and for the rest of the worker, we just need to scale down that number. We want to pick out the worker with the highest 
salary out of the rest and pay that money and then scale down for the other workers. This way we guarantee the smallest amount of money paid. For each "BASE_EMPLOYEE" worker will be paid their expected minimum wage, we will also keep track of hiring k workers where each p
 
Approach: 

As in Approach 1, the space of worker selections (and their associated cost) is partitioned according to the worker that will get paid their minimum wage. Denote this worker's wage and quality by W, Q and ratio R := W/Q. The price for worker i will then be q[i]*R which is >= w[i] if and only if ratio[i] <= R. 
Thus, with a given worker's wage fixed to his min wage, only those workers with smaller ratio can be included in the group (otherwise the chosen worker would need to get paid above his min wage), and therefore, 
keeping track of the lowest quality workers with ratio <= R while increasing R will find the min cost selection.
'''
import heapq
def mincostToHireWorkers(quality, wage, k):
	#create an array to store the worker ratio from worker with lowest quality to highest
	#we want to focus on the ones with less money
	workerRatio = sorted(((w/q), q, w) for q, w in zip(quality, wage))
	#Initialize the varible: 
	result = float('inf')
	pool = [] #store the number of candidate for us to pull out
	sumQuality = 0
	#iterate through the ratios to find the workers with lowest wage
	for ratio, q, w in workerRatio:
		#add candidate into the pool
		heapq.heappush(pool, -q)
		#calculate the sum of quality:
		sumQuality += q
		
		if(len(pool) > k):
			sumQuality += heapq.heappop(pool)
	
		if(len(pool) == k):
			result = min(result, sumQuality * ratio)
	return float(result)

'''
Time complexity: O(nlogn), where N is the number of workers 
Space complextiy: O(n), n is the size of the heap that we have to allocate space for
'''


#Main function to run the test cases: 
def main():
	print("TESTING MINIMUM COST TO HIRE K WORKERS...")
	quality = [10,20,5]
	wage = [70,50,30]
	K = 2
	print(mincostToHireWorkers(quality, wage, K))


	quality = [3,1,10,10,1]
	wage = [4,8,2,2,7]
	K = 3
	print(mincostToHireWorkers(quality, wage, K))


	print("END OF TESTING...")

main()
