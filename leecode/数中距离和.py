class Solution:
    def sumOfDistancesInTree(self, N: int, edges: list) -> list:
        layer_dict: dict = {N_: 0 for N_ in range(N)}
        layer_child_count: dict = {N_: [] for N_ in range(N)}
        layer_number_count: dict = {}
        for i in edges:
            layer_dict[i[1]] = layer_dict[i[0]] + 1
            layer_child_count[i[0]] = layer_child_count[i[0]] + [i[1]]
        for i in range(N):
            for j in layer_child_count[i]:
                layer_child_count[i] += layer_child_count[j]
        res = []
        for i, j in layer_dict.items():
            layer_number_count[j] = layer_dict.get(j, 0) + 1
        max_deep = max(layer_number_count.keys())
        sum_ = 0
        print(layer_dict, layer_child_count, layer_number_count)
        for i in range(N):
            for j in range(max_deep + 1):
                sum_ += (layer_dict[i] + j) * layer_number_count[j]


a = Solution()
print(a.sumOfDistancesInTree(N=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
