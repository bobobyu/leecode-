from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length: int = len(gas)
        start_point: int = 0
        invalid_set: set = set()
        while start_point < length:
            pre_point = start_point
            next_node = (start_point + 1) % length
            sum_gas: int = gas[start_point]
            flag = True
            print(start_point, next_node)
            while next_node != start_point:
                sum_gas -= cost[pre_point]
                if sum_gas < 0:
                    flag = False
                    break
                sum_gas += next_node
                pre_point = next_node
                next_node = (next_node + 1) % length
            if flag:
                return start_point
            else:
                if next_node in invalid_set:
                    break
                tmp = start_point
                while tmp !=
                start_point = next_node
        return -1


s = Solution()
s.canCompleteCircuit([1, 2, 3, 4, 5],
                     [3, 4, 5, 1, 2])
