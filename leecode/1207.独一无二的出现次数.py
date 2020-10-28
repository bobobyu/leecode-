class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        d: dict = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        l = d.values()
        return len(set(l)) == len(l)


s = Solution()
print(s.uniqueOccurrences([1, 2,1]))
