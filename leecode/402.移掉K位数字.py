class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        point = 1
        num = list(num)
        while point < len(num) and k:
            # print(num, point)
            if num[point - 1] > num[point]:
                # print(num[point - 1], num[point])
                num.pop(point - 1)
                point = max(1, point - 1)
                k -= 1
            else:
                point += 1
        # print(point, k)
        if k and num:
            num = num[:len(num) - k]
        while num and num[0] == '0':
            num.pop(0)
        return string if (string := ''.join(num)) else '0'


s = Solution()
print(s.removeKdigits('10020', 2))
