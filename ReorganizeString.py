#Leetcode 767. Reorganize String


'''
Problem statement: 
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
'''
def reorganizeString(S):
    #base case: 
    if not S:
        return None
    N = len(S)
    A

    




#main function to test the program
def main():
    print("TESTING REORGANIZE STRING...")
    s_01 = "aab"
    s_02 = "aaab"

    print(reorganizeString(s_01))
    print(reorganizeString(s_02))
    
    print("END OF TESTING...")

main()