from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToArray(self, root):
        """
        Convert a binary tree to an array representation.
        The array representation follows LeetCode's format where null nodes are represented as None.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_has_value = False  # Flag to check if we should keep adding nulls

            for _ in range(level_size):
                node = queue.popleft()

                if node is None:
                    result.append(None)
                    queue.append(None)
                    queue.append(None)
                else:
                    result.append(node.val)
                    level_has_value = True
                    queue.append(node.left)
                    queue.append(node.right)

            # If this level had no actual nodes, remove all nulls from this level
            if not level_has_value:
                while result and result[-1] is None:
                    result.pop()
                break

        # Remove trailing nulls if any
        while result and result[-1] is None:
            result.pop()

        return result

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        if not preorder or not inorder:
            return None

        # create root and mid-node. Also create left and right roots
        root = TreeNode(preorder[0])  # the val of root is the 1st value of preorder: index 0
        mid = inorder.index(preorder[0])  # find the position of that value in the inorder arr
        root.left = self.buildTree(preorder[1: mid + 1], inorder[: mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

    def sol(self) -> None:
        pOrder1, iOrder1 = [1, 2, 3, 4], [2, 1, 3, 4]
        pOrder2, iOrder2 = [1], [1]

        tree1, tree2 = self.buildTree(pOrder1, iOrder1), self.buildTree(pOrder2, iOrder2)
        sol1 = self.treeToArray(tree1)
        sol2 = self.treeToArray(tree2)

        print(
            f"Build Tree from Preorder & Inorder Traversal: Solution #1\n{sol1}")  # output: [1, 2, 3, None, None, None, 4]
        print(f"Build Tree from Preorder & Inorder Traversal: Solution #2\n{sol2}")  # output: [1]


solution = Solution()
solution.sol()
