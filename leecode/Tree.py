class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self, list_: list):
        stack: list = [TreeNode(list_.pop(0))]
        self.root_node: TreeNode = stack[0]
        while list_:
            root: TreeNode = stack.pop(0)
            left_child: TreeNode = TreeNode(list_.pop(0))
            right_child: TreeNode = TreeNode(list_.pop(0))
            root.left = left_child
            root.right = right_child
            stack.append(left_child)
            stack.append(right_child)

    def pre_order(self, root: TreeNode):
        if root:
            print(root.val)
            if root.left:
                self.pre_order(root.left)
            if root.right:
                self.pre_order(root.right)
    def middle_order(self, root:TreeNode):
        if root:
            if root.left:
                self.middle_order(root.left)
            print(root.val)
            if root.right:
                self.middle_order(root.right)

