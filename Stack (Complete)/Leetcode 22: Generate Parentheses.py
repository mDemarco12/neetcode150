class Solution:
    '''
    You are given an integer n. Return all well-formed parentheses strings that...
    you can generate with n pairs of parentheses.
    Example 1:
        Input: n = 1
        Output: ["()"]

    '''

    def generateParenthesis(self, n: int):
        # we only add open parentheses if open < n
        # we only add a closing parentheses if closed < open
        # the function is valid IIF open == closed == n;

        stack = []
        res = []

        # recursive function
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                # append an open p, recursively append backtrack
                # update our stack, so pop the char
                stack.append("(")
                # update our counters
                backtrack(openN + 1, closedN)
                # clear value from stack
                stack.pop()

            if closedN < openN:
                stack.append(")")
                # update our counters
                backtrack(openN, closedN + 1)
                # clear value from stack
                stack.pop()

        # call the function with default values
        backtrack(0, 0)
        return res


solution = Solution()

n1 = 1
n2 = 3

print(solution.generateParenthesis(n1))  # solution: ['()']
print(solution.generateParenthesis(n2))  # solution: ['((()))', '(()())', '(())()', '()(())', '()()()']
