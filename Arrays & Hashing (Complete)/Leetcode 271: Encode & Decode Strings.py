'''
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.
Please implement encode and decode
    Example 1:
    Input: ["neet","code","love","you"]
        Output:["neet","code","love","you"]
    Example 2:
    Input: ["we","say",":","yes"]
        Output: ["we","say",":","yes"]
'''

from typing import List


class Solution:
    # Read the string and set res = the length of the string (4) plus the delimiter plus the string itself
    # return the result
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0  # "i" will act a pointer to the position of the input string

        while i < len(s):  # While "i" is less than the length of s
            j = i  # Set j to i, j will act as our 2nd pointer
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res


# Test the Solution class
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test case
    original_strings = ["neet", "code", "love", "you"]

    print("Original strings:", original_strings)

    # Encode
    encoded = solution.encode(original_strings)
    print("Encoded string:", encoded)

    # Decode
    decoded = solution.decode(encoded)
    print("Decoded strings:", decoded)

    # Check if the decoded result matches the original
    print("Encoding/decoding successful:", original_strings == decoded)
    '''
    If we want to encode a string, we need a demiliter. We could use a char like "#" or "?" between strings...
    ... but what if the char shows up in the string? We could also use a single int as a delimiter, but the same errors occurs.
    So we combine both an int to signify the length of a string and a delimiter to let the algo know when to start decoding...
    ... regardless if the string is "Hello" vs "H#llo" vs "#12##"
    '''
