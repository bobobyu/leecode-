class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dim_dict: dict = {i:1 for i in J}
        count: int = 0
        for i in S:
            if dim_dict.get(i):
                count += 1
        return count
s = Solution()
print(s.numJewelsInStones(J = "a", S = "aAAbbbb"))
