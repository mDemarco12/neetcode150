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

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # create a function that will run our nested code
        def dfs(root):
            if not root: return [True, 0]

            # determine if left and right subtrees are balanced
            left, right = dfs(root.left), dfs(root.right)

            # is the left, right, and root balanced...
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # return boolean val and equal heights if true
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

    def sol(self) -> None:
        tree1 = self.createTreeFromArray([1, 2, 3, None, None, 4])
        tree2 = self.createTreeFromArray([1, 2, 3, None, None, 4, None, 5])

        t1 = self.isBalanced(tree1)
        t2 = self.isBalanced(tree2)

        print(f"Tree1 is {t1} and Tree2 is {t2}")


sol = Solution()
sol.sol()
