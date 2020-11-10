class Solution:
    def findLUSlength(self, strs: list) -> int:
        def judge_sub(i, j):
            index_i = 0
            index_j = 0
            while index_j < len(j) and index_i < len(i):
                if i[index_i] == j[index_j]:
                    index_i += 1
                index_j += 1
            # print(i, index_i)
            return index_i == len(i)

        size = len(strs)
        strs.sort(key=len, reverse=True)
        for i in range(size):
            flag = True
            for j in range(size):
                # print(strs[i], strs[j])
                if len(strs[i]) > len(strs[j]) or i == j:
                    continue
                # print(strs[i], strs[j], 'i')
                if judge_sub(strs[i], strs[j]):
                    flag = False
                    # print(flag)
                    break
            # print(flag)
            if flag:
                return len(strs[i])
        return -1