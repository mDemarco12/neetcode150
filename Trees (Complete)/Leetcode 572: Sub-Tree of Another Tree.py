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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # recursion? Start with edge cases
        if not root: return False
        if not subRoot: return True

        # compare the trees
        if self.sameTree(root, subRoot):
            return True

        # what if they aren't the same subtree?
        # compare t to right/left subtree of s
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    # we will define a helper function
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If both are None, they're the same
        if not root and not subRoot:
            return True

        # If one is None and the other isn't, they're different
        if not root or not subRoot:
            return False

        # Compare current nodes and recursively check children
        if root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))

        return False

    def sol(self) -> None:
        # Create the test trees
        root = [1, 2, 3, 4, 5]
        subRoot = [2, 4, 5]

        # Convert arrays to TreeNode structures
        r1 = self.createTreeFromArray(root)
        sr = self.createTreeFromArray(subRoot)

        # Check if subRoot is a subtree of root
        result = self.isSubtree(r1, sr)

        # Print results with more context
        print(f"Root tree: {self.treeToString(r1)}")
        print(f"Subtree: {self.treeToString(sr)}")
        print(f"Is subtree present? {result}")


solution = Solution()

solution.sol()
