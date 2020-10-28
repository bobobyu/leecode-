class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        length1 = len(nums1)
        [nums1.pop(-1) for _ in range(length1-m)]
        length2 = len(nums2)
        [nums2.pop(-1) for _ in range(length2-n)]
        if not nums1:
            [nums1.append(i) for i in nums2]
        else:
            index_point: int = 0
            while nums2:
                num2 = nums2.pop(0)
                while index_point < len(nums1)-1 and nums1[index_point] <= num2:
                    index_point += 1
                if num2 >= nums1[index_point]:
                    if index_point < len(nums1) - 1:
                        nums1.insert(index_point + 1, num2)
                    else:
                        nums1.append(num2)
                else:
                    nums1.insert(index_point, num2)
            print(nums1)
s = Solution()
a = [0]
b = [1]
s.merge(a,0,b,1)
print(a)