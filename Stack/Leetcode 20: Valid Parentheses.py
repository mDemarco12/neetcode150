class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        # HashMap of parentheses values
        closeToOpen = {")": "(", "]": "[", "}": " {"}

        for c in s:
            # if this char is in close: every key is always a closing para
            if c in closeToOpen:
                # make sure stack != empty
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # if they don't match or empty
                else:
                    return False
            # if we don't get a closing para
            else:
                stack.append(c)
        return True if not stack else False


solution = Solution()

stack1 = "[]"
stack2 = "([{}])"

print(solution.isValid(stack1))
print(solution.isValid(stack2))
