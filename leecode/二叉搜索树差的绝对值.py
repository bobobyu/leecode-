from Tree import *

a = [12, 5, 18, 2, 9, 15, 19]
t = Tree(a)


# t.middle_order(t.root_node)

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min_abs: float = float('inf')
        self.pre_val: float = float('inf')

        def middle_order(root: TreeNode = root):
            if root:
                if root.left:
                    middle_order(root.left)
                print(self.pre_val, root.val)
                if self.pre_val < float('inf'):
                    self.min_abs = min(abs(self.pre_val - root.val), self.min_abs)
                    self.pre_val = root.val
                else:
                    self.pre_val = root.val
                if root.right:
                    middle_order(root.right)

        middle_order()
        return int(self.min_abs)


s = Solution()
print(s.getMinimumDifference(t.root_node))
