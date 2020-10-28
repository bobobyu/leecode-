class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        if nums:
            nums = [i for i in nums if i > 0]
            if nums:
                max_ = max(nums)
                list_ = [-1 for _ in range(max_)]
                for i in nums:
                    list_[i-1] = 1
                for i in range(len(list_)):
                    if list_[i] < 0:
                        return i+1
                return max_ + 1
            return 1
        return 1



s = Solution()
print(s.firstMissingPositive([1,2,3,4,5,6,7,8,9,11,12]))
