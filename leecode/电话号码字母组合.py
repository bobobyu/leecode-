class Solution:

    def letterCombinations(self, digits: str) -> list:
        self.dict_: dict = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        def dfs(nums: str) -> list:
            if len(nums) == 1:
                return [i for i in self.dict_.get(int(nums), ''*4)]
            elif len(nums) == 0:
                return []
            else:
                return [j + i for i in dfs(nums=nums[1:]) for j in self.dict_.get(int(nums[0]), ''*4)]

        return dfs(nums=digits)


s = Solution()
print(s.letterCombinations('2'))
