#Leetcode 451. Sort Characters By Frequency

#Problem statement: 

'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''
#problem solving using a dictionary
def frequencySort(s):
    #base case: 
    if not s:
        return None

    result = ""
    #dictionary to store the element in the string and its repeated values
    dictionary = {}
    for i in range(len(s)):
        #if the element already in the dictionary, increment its repeated value by 1
        if s[i] in dictionary:
            dictionary[s[i]] += 1
        #if not, add it in the dictionary and set it value to 1
        else: 
            dictionary[s[i]] = 1


    #sort the dictionary by its value, so that the biggest value would stay on the top
    sortedDict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    for key, value in sortedDict: 
        for _ in range(value): 
            result += key

    return result



#main function to run program
def main():
    print("TESTING SORTING BY CHARACTER FREQUENCY...")
    test_string_1 = "tree"
    test_string_2 = "cccaaa"
    test_string_3 = "Aabb"
    test_string_4 = "abc"
    print(frequencySort(test_string_1))
    print(frequencySort(test_string_2))
    print(frequencySort(test_string_3))
    print(frequencySort(test_string_4))
    print("END OF TESTING...")
main()