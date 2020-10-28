class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hams: dict = {}
        for i, num in enumerate(nums):
            first = hams.get(num)
            second = hams.get(target - num)
            if not first:
                hams[num] = [i]
            else:
                hams[num].append(i)
            if second:
                first_index = hams[num][0]
                hams.get(num).pop(0)
                second_index = hams[target - num][0]
                hams.get(target - num).pop(0)
                return [first_index, second_index]


a = [3, 3]
s = Solution()
print(s.twoSum(a, target=6))
