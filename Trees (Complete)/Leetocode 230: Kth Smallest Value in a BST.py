from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # helper function to create the bst
    def create_bst(self, values: List[int]) -> Optional[TreeNode]:
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = [root]
        i = 1

        while queue and i < len(values):
            node = queue.pop(0)

            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root

    # help function to display the BST
    def treeToString(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "[]"

        result = []
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current:
                result.append(str(current.val))
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append("null")

        # Remove trailing nulls
        while result and result[-1] == "null":
            result.pop()

        return "[" + ", ".join(result) + "]"

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we will use iterative method for solving this solution
        # so we need a stack, a counter, and set curr to root
        n, curr = 0, root
        stack = []

        # when executing this loop, use "or" instead of "and" as "and" will not execute
        while curr or stack:
            # keep going left
            while curr:
                stack.append(curr)
                curr = curr.left

            # when this loop is None, we need to pop, increment n...
            # compare n to k, and traverse right
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right

    def sol(self) -> None:
        tree1, k1 = [2, 1, 3], 1
        tree2, k2 = [4, 3, 5, 2, None], 4

        t1 = self.create_bst(tree1)
        t2 = self.create_bst(tree2)

        s1 = self.kthSmallest(t1, k1)  # output: 1
        s2 = self.kthSmallest(t2, k2)  # output: 5

        print(f"The values of Tree 1: {self.treeToString(t1)}\nThe values of Tree 2: {self.treeToString(t2)}\n")

        print(f"The Kth value of tree 1 is {s1} and tree 2 is {s2} ")


'''
Michael here. This problem is simple. We need to traverse a binary search tree and return the kth smallest value.
So first off, the kth smallest value is the kth index in a sorted bst. 
So if we go through a BST in order, we will find our kth value if it is present. 
so we will iterate through the left side of the BST, adding the nodes we visit to a stack.
Once we reach a null value, we pop the previous value and go right. As we traverse/pop, we increment the value of n.
Once n is equal to k, we return the value k. 
Else we keep traversing, adding values to the stack, popping, and moving right till stack is empty.
The kth value does not exist if the stack is empty, so the answer will be None. 
'''

solution = Solution()

solution.sol()
