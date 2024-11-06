class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                # pop stack twice, add vals, and append to stack
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # pop twice, subtract the one was that popped 2nd from 1st
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                # same as " + ", except " * "
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                # ditto to " - "
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                # we need to convert char to a number
                stack.append(int(c))
        return stack[0]


'''
What is Polish Notation (PN)? Well it is a arithmetic approach invented by... you guessed it... a polish guy (Jan Łukasiewicz)
Jokes asides, polish notation is math optimized for computer operations using a set of instructions and operators.
There are different approaches to PN, but we will focus on reverse PN. 
Numbers are declared and operations are assigned . (123*+) is (1*2+3). Dividing will reverse the assignment of operators

Treat operators + and - as default assignment (A + B), while operators * and / will be reversed ( B / A)
Use a stack to track most recent numeral and pop numeral/operator when encountered. 
Use if else statements to append and pop from the stacks. 
After all operations are complete, the solution is in index[0] of the stack. 

'''
solution = Solution()

tokens1 = ["2", "1", "+", "3", "*"]
tokens2 = ["1", "2", "+", "3", "*", "4", "-"]
'''
Tokens1 Explanation 
((2+1)*3) = 9
Tokens2 Explanation 
Explanation: ((1 + 2) * 3) - 4 = 5
'''

print(solution.evalRPN(tokens1))
print(solution.evalRPN(tokens2))
