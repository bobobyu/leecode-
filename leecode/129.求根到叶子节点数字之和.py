from Tree import *
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root:
            def search_path(root: TreeNode) -> list:
                left = []
                right = []
                if root.left:
                    left = [[str(root.val)] + i for i in search_path(root.left)]
                if root.right:
                    right = [[str(root.val)] + i for i in search_path(root.right)]
                search_ = left + right
                return left + right if search_ else [[str(root.val)]]
            res_path = search_path(root=root)
            for i in range(len(res_path)):
                while res_path[i][0] == '0' and len(res_path[i]) > 1:
                    res_path[i].pop(0)
                res_path[i] = eval(''.join(res_path[i]))
            return sum(res_path)
        return 0



s = Solution()
t = Tree([0,1,None])
print(s.sumNumbers(t.root_node))
