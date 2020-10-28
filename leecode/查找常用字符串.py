class Solution:
    def commonChars(self, A: list) -> list:
        a = [[j for j in i] for i in A]
        [i.sort() for i in a]
        a_total = [['' for i in range(26)] for j in range(len(a))]
        result = []
        for i in range(len(a)):
            for j in a[i]:
                a_total[i][ord(j)-97] += j
        for i in zip(*a_total):
            if '' not in i:
                min_string = i[0]
                for j in i[1:]:
                    if len(j) < len(min_string):
                        min_string = j
                [result.append(min_string[0]) for s in range(len(min_string))]
        return result

s = Solution()
print(s.commonChars(["cool","lock","cook"]))
