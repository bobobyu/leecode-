class CDNode:
    def __init__(self, value: str, pre_node=None, next_node=None):
        self.value: str = value
        self.pre_node: CDNode = pre_node
        self.next_node: CDNode = next_node


class CDLink:
    def __init__(self, values_list):
        self.nodes_list: list = [CDNode(i) for i in values_list]
        for i in range(len(self.nodes_list) - 1):
            self.nodes_list[i].next_node = self.nodes_list[i + 1]
            self.nodes_list[i + 1].pre_node = self.nodes_list[i]
        self.nodes_list[0].pre_node = self.nodes_list[-1]
        self.nodes_list[-1].next_node = self.nodes_list[0]

    def delete_node(self, node: CDNode) -> CDNode:
        pre_node = node.pre_node
        next_node = node.next_node
        pre_node.next_node = next_node
        next_node.pre_node = pre_node
        return next_node


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        length = len(ring)
        Ring: CDLink = CDLink(values_list=range(length))
        max_step: int = len(ring) // 2
        min_dis: dict = {i: {j: float('inf') for j in range(length)} for i in range(length)}
        index_dic: dict = {}
        for i, j in enumerate(ring):
            index_dic[j] = index_dic.get(j, []) + [i]
        for i in Ring.nodes_list:
            center_node: CDNode = i
            update_dict: dict = min_dis[center_node.value]
            pre_node: CDNode = center_node.pre_node
            next_node: CDNode = center_node.next_node
            step_count: int = 1
            update_dict[center_node.value] = 0
            while step_count <= max_step:
                update_dict[pre_node.value] = min(update_dict[pre_node.value], step_count)
                update_dict[next_node.value] = min(update_dict[next_node.value], step_count)
                pre_node = pre_node.pre_node
                next_node = next_node.next_node
                step_count += 1
        current_pos:int = 0
        op_count:int = 0
        # [print(i) for i in min_dis.items()]
        # [print(i) for i in index_dic.items()]
        for letter in key:
            next_pos: int = min(index_dic[letter], key=lambda x: min_dis[current_pos][x])
            print(current_pos,next_pos, index_dic[letter])
            op_count += min_dis[current_pos][next_pos] + 1
            current_pos = next_pos
        return op_count


s = Solution()
print(s.findRotateSteps(
"caotmcaataijjxi",
"oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"))
