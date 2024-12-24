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

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # start at the root:
        cur = root

        # while cur is not null...
        while cur:
            # case 1: p and q are both > root
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

    def sol(self) -> None:
        root1 = [5, 3, 8, 1, 4, 7, 9, None, 2]

        p, q = TreeNode(3), TreeNode(8)
        p1, q1 = TreeNode(3), TreeNode(4)

        root = self.create_bst(root1)
        sol1 = self.lowestCommonAncestor(root, p, q)
        sol2 = self.lowestCommonAncestor(root, p1, q1)

        print(f"The lowest common ancestor for tree1 is: {sol1.val}")  # output: 5
        print(f"The lowest common ancestor for tree2 is: {sol2.val}")  # output: 3


solution = Solution()

solution.sol()
