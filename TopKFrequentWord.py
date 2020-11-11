#Python3 program to solve leetcode problem 692. Top K Frequent Words

#problem statement
'''
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

'''

from collections import Counter
from collections import OrderedDict

import heapq
#Count the frequency of each word and then assign them into a list and sort from smallet to largest, this way we would be able to find the repeating elemnt
def topKFrequent(words, k):
    #base case: no word or k, return nothing
    if not words or not k: 
        return None

    #variable to store the final result
    result = []
    # create a dictionary to store the amout of frequency an element exisit in: 
    freqDict = list(Counter(words).items())

    #Sort the array and then reverse it so that all the element with higher frequency can be accessed first 
    sotredDict = OrderedDict(sorted(freqDict))

    #reverse the dictioanry
    reversedDict = sorted(sotredDict.items(), key=lambda x:x[1], reverse=True)
    
    for element, frequency in reversedDict:
        result.append(element)

    return result[0:k]
#time complexity: O(n), the algorithm will have to go through every element in the array to count its frequency, not to mention, there are sorting operation, which is built in, so its time complexity would 
#o(nlogn). 
#space complexity: O(n), we create a dictionary from all the unique element in the array


#Function to solve the problem using the Heap data structure to sovle the problem, hoping to solve it with a lesser time complexity

def topKFrequent_HEAP(words, k):
    #base case: 
    if not words or not k: 
        return None

    #create a dictionarny to count the element frequency
    freqDict = Counter(words).items()
    #create the element frequency array
    heap = [(-freq, element) for element, freq in freqDict]
    #turn it into a heap
    heapq.heapify(heap)
    #keep popping the array until it reaches k
    return [heapq.heappop(heap)[1] for _ in range(k)]

    
#time complexity: O(nlog(k))
#space complexity: O(n)
def main():
    print("TESTING TOP K FREQUENT WORDS...")
    arr1 = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    arr2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k_2 = 4
    print(topKFrequent(arr1, k))
    print(topKFrequent(arr2, k_2))
    print(topKFrequent_HEAP(arr1, k))
    print(topKFrequent_HEAP(arr2, k_2))
    print("END OF TESTING...")

main()