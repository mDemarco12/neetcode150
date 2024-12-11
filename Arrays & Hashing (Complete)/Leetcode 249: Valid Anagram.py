'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
    Input: s = "racecar", t = "carrace"
Output: true

Example 2:
    Input: s = "jar", t = "jam"
Output: false

Constraints:
    s and t consist of lowercase English letters.
'''


def isAnagram(s: str, t: str) -> bool:
    '''Cheating: these are built-in functions. Useful in the realworld
                but your interviewer may want the algo
                     -> return sorted(s) == sorted(t)
                     -> return Counted(s) == counted(t) '''
    if len(s) != len(t):
        return False
    # create two hashmaps
    countS, countT = {}, {}
    # start index in s
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0) #get the current char in s, return o if it does not exist
        countT[t[i]] = 1 + countT.get(t[i], 0) #1 will increment the counter to the next char
    return countS == countT

print(isAnagram(s="racecar", t="carrace"))
