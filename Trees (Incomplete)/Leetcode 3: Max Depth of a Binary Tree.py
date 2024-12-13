from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createTreeFromArray(self, arr: List[int], index: int = 0) -> Optional[TreeNode]:
        if index >= len(arr) or arr[index] is None:
            return None

        node = TreeNode(arr[index])
        node.left = self.createTreeFromArray(arr, 2 * index + 1)
        node.right = self.createTreeFromArray(arr, 2 * index + 2)
        return node

    def treeToString(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "[]"

        result = []
        queue = deque([root])

        while queue:
            current = queue.popleft()
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

    def maxDepthRecursion(self, root: Optional[TreeNode]) -> int:
        # base case:
        if not root:
            return 0

        left = self.maxDepthRecursion(root.left)
        right = self.maxDepthRecursion(root.right)

        return 1 + max(left, right)

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:
            # traverse entire level, add the next level, then increment the level
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [[root, 1]]
        res = 0

        while stack:
            # pop node and depth from stack
            node, depth = stack.pop()

            # if node is not null...we have at least 1 value
            if node:
                res = max(res, depth)
                # add nodes to the stack
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])

        return res

    def sol(self) -> None:
        root1 = self.createTreeFromArray([1, 2, 3, None, None, 4])
        root2 = self.createTreeFromArray([])

        print("Max Depth of Binary Tree Using Different Methods:\n")

        # Recursion results
        r1 = self.maxDepthRecursion(root1)
        r2 = self.maxDepthRecursion(root2)
        print(f"Recursion method: Tree 1 depth = {r1}, Tree 2 depth = {r2}")

        # BFS results
        r3 = self.maxDepthBFS(root1)
        r4 = self.maxDepthBFS(root2)
        print(f"BFS method: Tree 1 depth = {r3}, Tree 2 depth = {r4}")

        # Iterative results
        r5 = self.maxDepthIterative(root1)
        r6 = self.maxDepthIterative(root2)
        print(f"Iterative method: Tree 1 depth = {r5}, Tree 2 depth = {r6}")


# Run the solution
solution = Solution()
solution.sol()
