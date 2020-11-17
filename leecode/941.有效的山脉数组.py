class Solution:
    def validMountainArray(self, arr: list) -> bool:
        summit:int = arr.index(max(arr))
        left = arr[:summit]
        right = arr[summit+1:]
        if not left or not right:
            return False
        if right[-1] == arr[summit]:

            return False
        for i in range(len(left)-1):
            if left[i] >= left[i+1]:
                return False
        for i in range(len(right) - 1):
            if right[i] <= right[i + 1]:
                return False
        return True


s = Solution()
print(s.validMountainArray([3,5,5]))