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

    def goodNodes(self, root: TreeNode) -> int:
        # we need a new function
        def dfs(node, maxVal):
            if not node: return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            # we need to count the ## of good nodes in each subtree
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)

    def sol(self) -> None:
        root1 = [2, 1, 1, 3, None, 1, 5]  # output is 3
        root2 = [1, 2, -1, 3, 4]  # output is 4

        r1 = self.create_bst(root1)
        r2 = self.create_bst(root2)

        s1 = self.goodNodes(r1)
        s2 = self.goodNodes(r2)

        print(f"The Good Nodes in Binary Tree 1 are {s1}\n" +
              f"The Good Nodes in Binary Tree 2 are {s2}")


solution = Solution()

solution.sol()
