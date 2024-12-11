class Solution:
    '''
    Given a string s, find the length of the longest substring without duplicate characters.
    A substring is a contiguous sequence of characters within a string.
    Example 1:
    Input: s = "zxyzxyz"
        Output: 3
        Explanation: The string "xyz" is the longest without duplicate characters.
    '''

    def lengthOfLongestSubstring(self, s):
        # set for characters
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # While there is duplicate in charSet
            while s[r] in charSet:
                # Remove the left-most char from set
                charSet.remove(s[r])
                # update the left most pointer
                l += 1
                # then add the right-most char to set
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

    '''
    Explanation: We need to compare each substring for duplicates. We use the sliding window algo to keep track of 
    a left and right char. While there is s string[r] in the charSet, we need to remove it (this is the duplicate).
    By removing the char, we also need to update the left pointer. Else. we add r to the set as it is not a duplicate.
    We return the result as the max res versus the value of right minus left plus 1. 
    '''


solution = Solution()

s1 = "abcabcbb"  # output: 3
s2 = "pwwkew"  # output: 4

print(solution.lengthOfLongestSubstring(s1))
print(solution.lengthOfLongestSubstring(s2))
