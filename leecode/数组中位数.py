class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        if nums2 or nums1:
            merge_nums: list = []
            while nums1 and nums2:
                if nums1 <= nums2:
                    merge_nums.append(nums1.pop(0))
                else:
                    merge_nums.append(nums2.pop(0))
            if nums1:
                merge_nums += nums1
            if nums2:
                merge_nums += nums2
            length: int = len(merge_nums)
            print(merge_nums, length)
            return merge_nums[length // 2] if  length % 2 else (merge_nums[length // 2] + merge_nums[
                length // 2 - 1]) / 2
        return False
s = Solution()
print(s.findMedianSortedArrays([],[]))