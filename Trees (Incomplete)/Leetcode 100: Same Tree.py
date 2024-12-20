from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we will use recursion
        # base cases
        if not p and not q:
            return True

        # if both are not empty, but one has a different value...
        if not p or not q or p.val != q.val:
            return False

        # we will begin recursively traversing the tree
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))

    def sol(self) -> None:
        # Create TreeNode objects from arrays
        p1_tree = self.createTreeFromArray([1, 2, 3])
        q1_tree = self.createTreeFromArray([1, 2, 3])
        p2_tree = self.createTreeFromArray([4, 7])
        q2_tree = self.createTreeFromArray([4, None, 7])

        # Compare the trees and print results
        print("Test case 1:", self.isSameTree(p1_tree, q1_tree))
        print("Test case 2:", self.isSameTree(p2_tree, q2_tree))


# Create an instance and run the solution
solution = Solution()
solution.sol()
