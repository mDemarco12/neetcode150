class Solution:
    s1 = "Was it a car or a cat I saw?"
    s2 = "tab a cat"

    def isPalindrome(s):
        '''
        This solution uses built-in functions and consumers more mem than two pointer solutio.
        '''

        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

    print(isPalindrome(s1))
    print(isPalindrome(s2))
