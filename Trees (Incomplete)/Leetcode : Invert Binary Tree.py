from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def createTreeFromArray(self, arr: List[int], index: int = 0) -> Optional[TreeNode]:
        if index >= len(arr):
            return None

        node = TreeNode(arr[index])
        node.left = self.createTreeFromArray(arr, 2 * index + 1)
        node.right = self.createTreeFromArray(arr, 2 * index + 2)
        return node

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

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case: There is no root
        if not root:
            return None

        # swap the children
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursion
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def sol(self) -> None:
        tree1, tree2 = [1, 2, 3, 4, 5, 6, 7], [3, 2, 1]

        # Create TreeNode structures
        root1 = self.createTreeFromArray(tree1)
        root2 = self.createTreeFromArray(tree2)

        # Invert and print trees
        inverted1 = self.invertTree(root1)
        inverted2 = self.invertTree(root2)

        print(self.treeToString(inverted1))
        print(self.treeToString(inverted2))


solution = Solution()

solution.sol()
