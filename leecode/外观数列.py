class Solution:
    def countAndSay(self, n: int) -> str:
        pre_string: str = ''
        next_string: str = ''

        for i in range(1, n + 1):
            if not pre_string:
                pre_string = str(i)
                continue
            start_point = 0
            end_point = 1
            while end_point < len(pre_string):
                if pre_string[start_point] != pre_string[end_point]:
                    next_string += str(end_point-start_point)+str(pre_string[start_point])
                    start_point = end_point
                    end_point += 1
                else:
                    end_point += 1
            # print(i,'s', start_point, end_point, pre_string)
            next_string += str(end_point-start_point)+str(pre_string[start_point])
            pre_string = next_string
            next_string =''

            # print(pre_string, next_string)
            # print()
        return pre_string
s = Solution()
print(s.countAndSay(5))
