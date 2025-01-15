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

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # create nested helper function
        def valid(node, left, right):
            # edge case 1: Empty BST
            if not node: return True  # an empty BST is valid...
            # edge case 2: if left and right are not "aligned"
            if not (node.val < right and node.val > left):
                return False

            # recursive call...
            # the left subtree is valid if left is between node.val and right
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))

    def sol(self) -> None:
        tree1 = [2, 1, 3]
        tree2 = [4, 3, 7, 4, 8]

        t1, t2 = self.create_bst(tree1), self.create_bst(tree2)
        d1, d2 = self.treeToString(t1), self.treeToString(t2)
        a1, a2 = self.isValidBST(t1), self.isValidBST(t2)

        print(f"Values for Tree 1 and Tree 2: \nTree 1: {d1}\nTree 2: {d2}")
        print(f"Tree 1 validates as {a1} as a BST, while Tree 2 is {a2}")


solution = Solution()

solution.sol()
