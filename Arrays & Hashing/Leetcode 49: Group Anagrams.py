'''
Given an array of strings strs, group all anagrams together into sub-lists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
    Example 1:
        Input: strs = ["act","pots","tops","cat","stop","hat"]
        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    Example 2:
        Input: strs = ["x"]
        Output: [["x"]]
'''
from collections import defaultdict


def groupAnagrams(strs):
    res = defaultdict(list)  # create an empty dictionary list

    for s in strs:  # read through strs
        count = [0] * 26  # init values a..z

        for c in s:  # cor character in string
            count[ord(c) - ord("a")] += 1  # Increment count of current char and convert a = 0, b = 1 ... z = 25
        res[tuple(count)].append(s)  # Group anagrams with same count
    return res.values()  # return all values from our dict


# The key insight here is that anagrams will have the same character count.
# By using this count as a key, we group all anagrams together.
print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
print(groupAnagrams(["x"]))
