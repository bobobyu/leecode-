from typing import *


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_count: int = 0
        ten_count: int = 0
        for i in bills:
            print(five_count, ten_count, i)

            if five_count < 0 or ten_count < 0:
                return False
            if i == 5:
                five_count += 1
            elif i == 10:
                if not five_count:
                    return False
                else:
                    five_count -= 1
                ten_count += 1
            else:
                if ten_count and five_count:
                    ten_count -= 1
                    five_count -= 1

                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False
        return True


print(Solution().lemonadeChange([5, 5, 5, 10, 5, 20, 5, 10, 5, 20]))
[5,5,10,5,20]