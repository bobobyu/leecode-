from Tree import *


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        if root:
            res: list = []
            stack: list = [root]
            while stack:
                curr_root: TreeNode = stack.pop(0)
                res.append(curr_root.val)
                curr_root.right and stack.insert(0, curr_root.right)
                curr_root.left and stack.insert(0, curr_root.left)
            return res
        return []


t = Tree([1, 2, 3, 4, 5, 6, 7])
s = Solution()
print(s.preorderTraversal(t.root_node))
'''

    1
   2 3
4 5  6 7
'''
