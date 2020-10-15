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
import collections
#Count the frequency of each word and then assign them into a list and sort from smallet to largest, this way we would be able to find the repeating elemnt
def topKFrequent(words, k):
    p = 



def main():
    print("TESTING TOP K FREQUENT WORDS...")
    arr1 = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(topKFrequent(arr1, k))
    print("END OF TESTING...")

main()