from Tree import *


class Solution:
    def findMode(self, root: TreeNode) -> list:
        if root:

            self.list_: list = []

            def middle_order(root: TreeNode):
                if root.left:
                    middle_order(root.left)
                if root.val or str(root.val) == '0':
                    self.list_.append(root.val)
                if root.right:
                    middle_order(root.right)

            middle_order(root)
            count_dict: dict = {}
            [count_dict.update({i: count_dict.get(i, 0) + 1}) for i in self.list_]
            max_frequency = max(count_dict, key=lambda x:count_dict[x])

            return [i for i in count_dict.keys() if count_dict[i]==count_dict[max_frequency]]

s = Tree([1, 0, 2, -1, 0, 2, None])
S = Solution()
print(S.findMode(s.root_node))
