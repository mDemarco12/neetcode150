from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # creates the tree
    def createTreeFromArray(self, arr: List[int], index: int = 0) -> Optional[TreeNode]:
        # Check if index is valid and value is not None
        if index >= len(arr) or arr[index] is None:
            return None

        # Create node with current value
        node = TreeNode(arr[index])

        # Recursively create left and right subtrees
        node.left = self.createTreeFromArray(arr, 2 * index + 1)
        node.right = self.createTreeFromArray(arr, 2 * index + 2)

        return node

    # converts tree to string for output
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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # our global variable to keep track of diameter
        # result = 0: Error. The root starts at 1, not 0...
        result = 1

        # Created a nested f(x) for DFS, returns Height
        def dfs(curr):
            if not curr: return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal result

            result = max(result, left + right)
            # calculate the height
            return 1 + max(left, right)

        dfs(root)
        return result

    def sol(self) -> None:
        # process: Create tree, calc diameter, and output results
        tree1 = self.createTreeFromArray([1, None, 2, 3, 4, 5])  # should be 3
        tree2 = self.createTreeFromArray([1, 2, 3, 4, 5, 6, 7])  # should be 2

        t1 = self.diameterOfBinaryTree(tree1)
        t2 = self.diameterOfBinaryTree(tree2)

        print(f"The diameter of the two Binary Tree's are = {t1} and {t2}")


solution = Solution()

solution.sol()
