from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        remain_count: dict = {}
        end_dict: dict = {}
        for i in nums:
            remain_count[i] = remain_count.get(i, 0) + 1
            end_dict[i] = end_dict.get(i, 0)
        for i in nums:
            # print(remain_count, end_dict, i)
            if remain_count[i]:
                if end_dict.get(i - 1):
                    end_dict[i - 1] -= 1
                    end_dict[i] += 1
                    remain_count[i] -= 1

                else:
                    f = True
                    for offset in range(3):
                        if not remain_count.get(i + offset):
                            f = False
                            break
                    if f:
                        for offset in range(3):
                            remain_count[i+offset] -= 1

                        end_dict[i+2] += 1
        return True if not any(remain_count.values()) else False


s = Solution()
print(s.isPossible([1,2,3,4,4,5]))
