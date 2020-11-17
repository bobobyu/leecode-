from Tree import *
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        layer_list = [root]
        while any(layer_list):
            values_list = [i.val if i else None for i in layer_list]
            start_point:int = 0
            end_point:int = len(values_list) - 1
            while start_point < end_point:
                if values_list[start_point] != values_list[end_point]:
                    return False
                start_point += 1
                end_point -= 1
            next_values_list:list = []
            for i in layer_list:
                if not  i:
                    next_values_list += [None, None]
                else:
                    if i.left:
                        next_values_list.append(i.left)
                    else:
                        next_values_list.append(None)
                    if i.right:
                        next_values_list.append(i.right)
                    else:
                        next_values_list.append(None)
            layer_list = next_values_list.copy()
        return True