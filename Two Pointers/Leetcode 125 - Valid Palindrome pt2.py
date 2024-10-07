class Solution:

    def isPalindrome(self, s):
        # Two pointer solution
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):  # While we are the left pointer
                l += 1  # increment by 1
            while r > l and not self.alphaNum(s[r]):  # while wr are the right pointer
                r -= 1  # decrement by 1
            if s[l].lower() != s[r].lower():  # if left is not equal to right, not palindrome
                return False
            # increment left and right after each iteration
            l += 1
            r -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


solution = Solution()

# Test Cases
s1 = "Was it a car or a cat I saw?"
s2 = "tab a cat"

print(solution.isPalindrome(s1))
print(solution.isPalindrome(s2))
