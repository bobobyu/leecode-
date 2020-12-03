from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger.pop(0))
            return ans

        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]


        max_ = 0
        for i in range(0, len(nums1) + 1):
            for j in range(0, len(nums2) + 1):
                if i + j == k:
                    print(i, j)
                    if (e_max := sum(sol := merge(nums1[:i], nums2[:j]))) > max_:
                        max_ = e_max
                        res = sol
        return max(merge(pick_max(nums1, i), pick_max(nums2, k - i)) for i in range(k + 1) if
                   i <= len(nums1) and k - i <= len(nums2))


