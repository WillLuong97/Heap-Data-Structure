#Problem 1753. Maximum Score From Removing Stones

'''
You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.
Example 1:

Input: a = 2, b = 4, c = 6
Output: 6
Explanation: The starting state is (2, 4, 6). One optimal set of moves is:
- Take from 1st and 3rd piles, state is now (1, 4, 5)
- Take from 1st and 3rd piles, state is now (0, 4, 4)
- Take from 2nd and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 6 points.
Example 2:

Input: a = 4, b = 4, c = 6
Output: 7
Explanation: The starting state is (4, 4, 6). One optimal set of moves is:
- Take from 1st and 2nd piles, state is now (3, 3, 6)
- Take from 1st and 3rd piles, state is now (2, 3, 5)
- Take from 1st and 3rd piles, state is now (1, 3, 4)
- Take from 1st and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 7 points.
Example 3:

Input: a = 1, b = 8, c = 8
Output: 8
Explanation: One optimal set of moves is to take from the 2nd and 3rd piles for 8 turns until they are empty.
After that, there are fewer than two non-empty piles, so the game ends.
 Constraints:

1 <= a, b, c <= 105
'''
import heapq
#Approach: at each pick, we will take out the stone in the two largest pile and leave the pile with the smallest number of stones behind and only takes out 
#stones from the smallest pile when one of the other two piles have been maxed out. 
def maximumScore(a, b, c):
	score = 0
	heap = [-a, -b, -c]
	heapq.heapify(heap)
	#keep taking out the 
	while heap[1]:
		#take out the two biggest heap, since heapop only return the smallest element from the heap, the biggesst value in pos would be the smallest in negative.
		s1 = heapq.heappop(heap)
		s2 = heapq.heappop(heap)
		score += 1
		heapq.heappush(heap, s1+1)
		heapq.heappush(heap, s2+1)
	
	return score

	
	


#Main function to run the test cases: 
def main():
	print("TESTING MAXIMUM SCORE FROM REMOVING STONES...")
	#test cases: 
	a = 2
	b = 4
	c = 6
	print(maximumScore(a,b,c))
	a = 4
	b = 4
	c = 6
	print(maximumScore(a,b,c))
	a = 1
	b = 8
	c = 8
	print(maximumScore(a,b,c))

	print("END OF TESTING...")	

main()




