class Solution():

    def permutation(self, s1, s2):
        # edge case: s1 shouldn't exceed s2
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            # add 1 to matches if s1 matches char in s2
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # start of sliding window portion
        l = 0
        for r in range(len(s1), len(s2)):
            # edge case
            if matches == 26: return True

            # sliding window for
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # sliding window for r
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26


'''
Thought-process: We need need to compare the strings in s1 to s2 to see if there is a permutation. 
It is costly to compare each value, so we can use hashmaps and the sliding window algo to compare the len of s2 to the len of s1.
We need to convert each set to ascii to assess its char. Then we increment matches by 1 if s1 and s2 are the same ( 'ab' -> 'axb' = a, 1; b,1; x,1)
Associate l and r to ascii value, then set the s2Count index based on l or r.
At the end, we need to increment l by 1 to count each char and then (Not return true) return matches == to 26 (You will get True if the matches = 26, otherwise false. 
'''

solution = Solution()

print(solution.permutation("ab", "lexcabee"))  # result: True
print(solution.permutation("abc", 'baxyzabc'))  # result: True
print(solution.permutation("cav", "wwwweqqqaqser"))
