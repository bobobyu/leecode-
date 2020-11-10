class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        minlen = min(nums1, nums2, key=len)
        min_length:int = len(minlen)
        self.nums1_sub_dict:dict = {}
        self.nums2_sub_dict:dict = {}
        def sub_continue_set(n:int, nums:list, dict_id:dict):
            for j in range(1, n+1):
                for i in range(0, len(nums), j):
                    interval = [0, j]
                    while interval[-1] <= len(nums):
                        dict_id[tuple(nums[interval[0]: interval[1]])] = 1
                        interval = [i+1 for i in interval]
        sub_continue_set(n=min_length, nums=nums1, dict_id=self.nums1_sub_dict)
        sub_continue_set(n=min_length, nums=nums2, dict_id=self.nums2_sub_dict)

        flag = len(nums2) == min_length
        res = []
        for i in self.nums2_sub_dict if flag else self.nums1_sub_dict:
            if len(i) > len(res) and i in self.nums1_sub_dict if flag else self.nums2_sub_dict:
                res = i
        return list(res)


s = Solution()
s.intersection([1,2,2,1]
,[2,2])