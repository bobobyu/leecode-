class Solution:
    def numWays(self, n: int, relation: list, k: int) -> int:
        relation_dic = {i: [] for i in range(n)}
        for i in relation:
            relation_dic[i[0]].append(i[1])
        # print(relation_dic)
        next_list = relation_dic[0]
        # print(next_list)
        next_list_ = []
        for i in range(k -1):
            for j in next_list:
                next_list_ += relation_dic[j]
            # print(next_list_)
            next_list = next_list_
            next_list_ = []
            # print()
        # print(next_list)
        return next_list.count(n - 1)



s = Solution()
print(s.numWays(3,
                [[0, 2], [0, 1], [1, 2], [2, 1], [2, 0], [1, 0]],
                1))
