class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        point:int = 0
        length:int = len(nums)
        while point < length:
            if nums[point] == val:
                nums.remove(val)
                length -= 1
            else:
                point += 1
        return length

a = []
s = Solution()
print(s.removeElement(a, 1))
print(a)