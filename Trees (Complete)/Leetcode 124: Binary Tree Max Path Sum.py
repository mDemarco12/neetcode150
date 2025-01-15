from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # make res a global variable, and a list
        res = [root.val]

        def dfs(root):
            # basecase..
            if not root: return 0

            # calc the max of each side
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # update left and right max
            leftMax, rightMax = max(leftMax, 0), max(rightMax, 0)

            # calc max path WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # calc max WITHOUT split
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

    def sol(self) -> None:
        input1 = [1, 2, 3]
        input2 = [-15, 10, 20, None, None, 15, 5, -5]

        # create the bst with input
        tree1, tree2 = self.create_bst(input1), self.create_bst(input2)

        # find the max path given the tree
        sol1, sol2 = self.maxPathSum(tree1), self.maxPathSum(tree2) # output of sol1: 6; sol2: 40

        print(f"Max Path Sum in a Binary Tree:\nTree 1, {input1}, has a max sum of {sol1}")
        print(f"Tree 2, {input2}, has a max sum of {sol2}\n")


solution = Solution()

solution.sol()
